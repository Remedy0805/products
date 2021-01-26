products = []
print('如果想結束的話請輸入q')
while True :
	name = input('請輸入商品的名稱：')
	if name == 'q':
		break
	price = input ('請輸入商品的價格：')
	price = int(price)
	products.append([name,price])	
print(products)
with open ('products.csv','w',encoding = 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(str(p[0]) + ',' + str(p[1]) + '\n')
