#Напишите функцию, которая, получив URL-адрес в виде строки, извлекает только доменное имя и возвращает
# его в виде строки. Например: url = "http://github.com/carbonfive/raygun" -> domain name = "github"

def domain_name(url):
    url = url.replace('http://', '').replace('https://', '')
    if url.startswith("www."):
        url = url[4:]
    domain = url.split('/')[0].split('?')[0]
    return domain.split('.')[0]

#url = "http://github.com/carbonfive/raygun"
url = "http://www.zombie-bites.com"
#url = "https://www.cnet.com"
print(domain_name(url))