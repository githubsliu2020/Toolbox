# 建立隨機整數1-100
#讓使用者猜測數字
#猜對就可以回答"答對了"
#猜錯就提示答案比猜測的數字大或小

import random
r = random.randint(1,100)

while True:
 num = input('請猜出1~100隨機出碼的數字')
 num = int(num)
 if num == r:
  print ('好厲害!答對了!')
  break
 elif num > r:
  print('您的數字比答案大')
 elif num < r:
  print('您的數字比答案小')
