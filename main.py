import requests
import bs4
 

url = input("enter your url ")
response = requests.get(url)

print(type(response))
print(response.text)
filename = "temp.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()
print(formatted_text)

with open(filename, "w+") as f:
    f.write(formatted_text)

list_imgs = bs.find_all('img')
print(list_imgs)

no_of_imgs = len(list_imgs)

list_as = bs.find_all('a')
no_of_as = len(list_as)

print("no of img tags", no_of_imgs)
print("no of anchor tags", no_of_as)