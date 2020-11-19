print('終極密碼1~100')
from random import*
win = randint(1,100)

x = 10

while  True:
	number = input('請輸入數字：')
	number = int(number)
	if number == win:
		print('你贏了')
		break
	elif number == win + randint(1,3) :
		print('非常接近')
	elif number == win - randint(1,3) :
		print('非常接近')
	elif x == 1:
		print('你猜太多次了遊戲結束')
		break
	x = x - 1
	print('你剩',x,'次機會了')
print('答案是',win)