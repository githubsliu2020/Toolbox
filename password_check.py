x = 0
y = 1
while x < 3 and y < 3:
 	pass_word=input('請輸入密碼') 
 	if str(pass_word) == 'a123456':
		 print ('login successfully')
		 break
 	else:
  		x = x + 1 
  		y = 3 - x 
  		
  		print ('還有',y,'次機會')
print ('已錯誤超過三次,登入失敗')