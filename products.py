#讀取檔案
products = []
with open ('products.csv','r',encoding = 'UTF-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name,price = line.strip().split(',')
		products.append([name,price])

#讓消費者輸入
print('目前已經有這些商品~',products)
print('如果想結束的話請輸入q')
while True :
	name = input('請輸入商品的名稱：')
	if name == 'q':
		break
	price = input ('請輸入商品的價格：')
	price = int(price)
	products.append([name,price])	
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'的商品價格是',p[1])

#寫入檔案
with open ('products.csv','w',encoding = 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(str(p[0]) + ',' + str(p[1]) + '\n')
