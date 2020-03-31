products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': # 逃出迴圈
		break
	price = input ('請輸入商品價格')
	p = []
	p.append(name)
	p.append(price)   #以上三行可簡寫為p = [name, price]
	products.append(p)
print(products)

a = products[1][1] # 大清單中的索引二中的索引二.也就是第二個商品的價格
b = products[1][0] # 大清單中的索引二中的索引一.也就是第二個商品的價格
print(a) 
print(b)