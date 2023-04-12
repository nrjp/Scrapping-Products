import requests
from bs4 import BeautifulSoup
import json

url = "https://www.google.com/search?tbm=shop&hl=en-GB&psb=1&ved=2ahUKEwjm6rKDtqL-AhVmBoMDHS7hCmEQu-kFegQIABAL&q=mobile&oq=mobile&gs_lcp=Cgtwcm9kdWN0cy1jYxADUABYAGAAaABwAHgAgAEAiAEAkgEAmAEA&sclient=products-cc"
url = 'https://www.google.com/search?q=bikes&hl=en-GB&tbm=shop&sxsrf=APwXEdfOYwJYrmbRUEZkT2bT4Hf-EyoZmQ%3A1681240683669&psb=1&ei=a7I1ZOiYKMmhseMPhrOE2AY&ved=0ahUKEwio-uzNxaL-AhXJUGwGHYYZAWsQ4dUDCAg&uact=5&oq=bikes&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBwgAEIAEEAoyBQgAEIAEOhAIABCKBRCxAxCDARCwAxBDOg4IABCABBCxAxCDARCwAzoICAAQgAQQsAM6BAgjECc6BwgAEIoFEEM6DQgAEIoFELEDEIMBEENKBAhBGAFQgQpY7BJg6RZoAnAAeACAAekBiAHEBZIBBTAuNC4xmAEAoAEByAEKwAEB&sclient=products-cc'



def google_shop(product):

    url = f"https://www.google.com/search?q={product}&tbm=shop"
    print(url)
    response = requests.get(url)

    soup = BeautifulSoup(response.content)

    # print(soup)
    product_list = []

    for item in soup.select(".P8xhZc"):
        name = item.select_one("a").text.strip()
        price = item.select_one(".HRLxBb").text.strip()
        product_link = item.select_one("a")["href"]   

        product_list.append({
        'Product name': name,
        'price': price,
        'product_link': product_link
        })
    with open('data.json', 'w',encoding='utf-8') as f:
        json.dump(product_list, f,ensure_ascii=False)
    print('done')
    return product_list


google_shop('mobile')