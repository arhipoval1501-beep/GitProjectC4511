import requests


res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_pars = response_text.split("<span>")
for pars_elem_1 in response_pars:
    if pars_elem_1.startswith("$"):
        for pars_elem_2 in pars_elem_1.split("</span>"):
            if pars_elem_2.startswith("$") and pars_elem_2[1].isdigit():
                res_parse_list.append(pars_elem_2)

print(f"Bitcoin - {res_parse_list[8]}")
#print(response.parse)