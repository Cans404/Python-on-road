// created by Cans, 20180320

package main 

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func ip_encrypt(ip string) {
	ip_decs := strings.Split(ip, ".")
	ip_bins := []string{}
	ip_code_zip := ""

	for _, ip_dec := range ip_decs {
		tmp, _ := strconv.Atoi(ip_dec)
		ip_bin := strconv.FormatInt(int64(tmp), 2)
		ip_bins = append(ip_bins, fmt.Sprintf("%08s", ip_bin))
	}

	ip_code_bin := strings.Join(ip_bins, "")
	fmt.Printf("1. %-45s ------> %45s\n", ip, ip_code_bin)

	ip_code_str := strings.Replace(ip_code_bin, "0", "a", -1)
	ip_code_str = strings.Replace(ip_code_str, "1", "b", -1)
	fmt.Printf("2. %-45s ------> %45s\n", ip_code_bin, ip_code_str)

	var x = make([](map[string]int), 0)
	mp_names := make(map[string](map[string]int))
	mp_name := ""
	counter := 0
	flg := false
	crt_chr := ""

	for i, s := range strings.Split(ip_code_str, "") {
		if i == 0 {
			flg = true
			crt_chr = s
		}

		if s != crt_chr {
			crt_chr = s
			flg = true
			counter += 1
		}

		if flg == true {
			mp_name = "mp" + strconv.Itoa(counter)
			mp_names[mp_name] = make(map[string]int)
			flg = false
			x = append(x, mp_names[mp_name])
		}

		mp_names[mp_name][s] += 1
	}

	for _, mp := range x {
		for k, v := range mp {
			ip_code_zip += strconv.Itoa(v) + k
		}
	}

	fmt.Printf("3. %-45s ------> %45s\n", ip_code_str, ip_code_zip)

	ip_code := strings.Replace(ip_code_zip, "1", "", -1)
	fmt.Printf("4. %-45s ------> %45s\n", ip_code_zip, ip_code)
}

func ip_decrypt(ip_code string) {
	ip_code_zip := ip_code
	ip_code_str := ""
	ip_bins := []string{}
	ip_decs := []string{}

	if strings.HasPrefix(ip_code, "a") || strings.HasPrefix(ip_code, "b") {
		ip_code_zip = "1" + ip_code
	}

	ip_code_zip = strings.Replace(ip_code_zip, "ab", "a1b", -1)
	ip_code_zip = strings.Replace(ip_code_zip, "ba", "b1a", -1)

	fmt.Printf("1. %-45s ------> %45s\n", ip_code, ip_code_zip)

	reg := regexp.MustCompile(`\d*`)
	rep := "${1}"
	ab_str := reg.ReplaceAllString(ip_code_zip, rep)
	ab_str_arr := strings.Split(ab_str, "")

	num_str_arr := strings.FieldsFunc(ip_code_zip, Split)

	for i := 0; i < len(ab_str_arr); i++ {
		num, _ := strconv.Atoi(num_str_arr[i])
		ip_code_str += strings.Repeat(ab_str_arr[i], num)
	}

	fmt.Printf("2. %-45s ------> %45s\n", ip_code_zip, ip_code_str)

	ip_code_bin := strings.Replace(ip_code_str, "a", "0", -1)
	ip_code_bin = strings.Replace(ip_code_bin, "b", "1", -1)
	fmt.Printf("3. %-45s ------> %45s\n", ip_code_str, ip_code_bin)

	for i := 0; i <= 8 * 3; i += 8 {
		tmp := strings.TrimLeft(string(ip_code_bin[i:i+8]), "0")
		ip_bins = append(ip_bins, tmp)
	}

	for _, x := range ip_bins {
		i, _ := strconv.ParseInt(x, 2, 0)
		ip_decs = append(ip_decs, strconv.Itoa(int(i)))
	}

	ip := strings.Join(ip_decs, ".")
	fmt.Printf("3. %-45s ------> %45s\n", ip_code_bin, ip)
}

func Split(r rune) bool {
	return r == 'a' || r == 'b'
}

func main() {
	ip_encrypt("1.1.1.129")
	fmt.Printf("\n<<%98s>>\n\n", strings.Repeat("#", 98))
	ip_decrypt("7ab7ab7a2b6ab")
}
