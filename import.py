import random   #standard library標準函數庫   
#package（套件）裏面有很多module 模組
r = random.randint(1,100) #包括1跟100
count = 0
while True:
	count += 1 
	answer = input("請寫入數字:")
	answer = int(answer)
	if answer == r :
		print("你猜對了")
		print("這是你猜的第", count ,"次")
		break
	elif answer > r :
		print("比答案大")
	elif answer < r :
		print("比答案小")
	print("這是你猜的第", count ,"次")

