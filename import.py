import random   #standard library標準函數庫   
#package（套件）裏面有很多module 模組
r = random.randint(1,100) #包括1跟100
while True:
	answer = input("請寫入數字:")
	answer = int(answer)
	if answer == r :
		print("你猜對了")
		break
	elif answer > r :
		print("比答案大")
	elif answer < r :
		print("比答案小")


