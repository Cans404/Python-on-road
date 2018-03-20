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

def func(m) :
	if m.expand(r"\g<dig>") == "" :
		mark = ""
	else:
		mark = "*"
	return m.expand(r"\g<dig>") + mark + r"'" + m.expand(r"\g<chr>") + r"'" + "+"

def ip_decrypt(ip_code) :
	cmd = re.sub(r"(?P<dig>\d*)(?P<chr>[ab])", func, ip_code).strip("+")
	ip_code_str = eval(cmd)
	print "1. %-45s ------> %45s" % (ip_code, ip_code_str)

	ip_code_bin = re.sub(r"\w", lambda m: chr(ord(m.group()) - 49), ip_code_str)
	print "2. %-45s ------> %45s" % (ip_code_str, ip_code_bin)

	ip_decs = []

	for i in range(0, 32, 8) :
		ip_bin = ip_code_bin[i:i+8].lstrip("0")
		ip_dec = int(ip_bin, 2)
		ip_decs.append(str(ip_dec))

	ip = ".".join(ip_decs)
	print "3. %-45s ------> %45s" % (ip_code_bin, ip)

if __name__ == '__main__' :
	ip_encrypt("1.1.1.129")
	print ""
	print "<<" + "#" * 98 + ">>"
	print ""
	ip_decrypt("7ab7ab7a2b6ab")
