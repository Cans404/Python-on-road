#!/usr/bin/env python

# create by Cans, 20180319

import re
import subprocess

def ip_encrypt(ip) :
	ip_bins = []
	ip_decs = ip.split(".")

	for ip_dec in ip_decs :
		tmp = bin(int(ip_dec)).replace("0b", "").zfill(8)
		ip_bins.append(tmp)

	ip_code_bin = "".join(ip_bins)
	print "1. %-45s ------> %45s" % (ip, ip_code_bin)

	ip_code_str = re.sub(r"\d", lambda m: chr(ord(m.group()) + 49), ip_code_bin)
	print "2. %-45s ------> %45s" % (ip_code_bin, ip_code_str)

	# doesn't work in re, why?
	# ip_code_zip = re.sub(r"(\w)+(?=[^\1]|$)", lambda m: len(m.group()), ip_code_str)
	# ip_code_zip = re.sub('''(\w)(\1){0,}''', lambda m: len(m.group()), ip_code_str)
	cmd = r'''echo "%s" | grep -E "(\w)(\1)*" -o''' % ip_code_str
	sub_p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE)
	rte = sub_p.communicate()[0].strip().split("\n")
	length = [ len(x) for x in rte]
	ip_code_zip = "".join([ str(i) + j[0] for i, j in zip(length, rte)])
	print "3. %-45s ------> %45s" % (ip_code_str, ip_code_zip)

	ip_code = ip_code_zip.replace("1", "")
	print "4. %-45s ------> %45s" % (ip_code_zip, ip_code)

if __name__ == '__main__' :
	ip_encrypt("1.1.1.129")
