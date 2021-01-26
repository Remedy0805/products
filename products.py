products = []
print('如果想結束的話請輸入q')
while True :
	name = input('請輸入商品的名稱：')
	if name == 'q':
		break
	price = input ('請輸入商品的價格：')
	products.append([name,price])
	
print(products)

for p in products:
	print(p[0],'的價格是',p[1])