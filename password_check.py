i = 3
while True:
 pass_word=input('請輸入密碼') 
 if str(pass_word) == 'a123456':
  print ('login successfully')
  break
 else:
  i = i -1  
  print ('還有',i,'次機會')
  if i == 0:
   print ('已錯誤超過三次,登入失敗')
   break