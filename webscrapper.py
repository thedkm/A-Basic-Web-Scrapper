import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&ignorear=0&N=-1&isNodeId=1"
uClient = uReq(url)
page_html = uClient.read()
#print(page_html)
uClient.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.find_all("div", {"class":"item-container"})


filename = "product.csv"
f = open(filename,"w")

headers = "Brand, Product Name, Shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	
	
	title_container = container.find_all("a",{"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.find_all("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	
	

	print("Brand:"+brand)
	print("Product Name:"+product_name)
	
	print("Shipping:"+shipping)
	f.write(brand +" ,"+product_name.replace(",","|")+","+shipping+"\n")

f.close()