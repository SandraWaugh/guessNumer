import random   #standard library標準函數庫   
#package（套件）裏面有很多module 模組

count = 0
start = input("請決定數字隨機範圍開始值：")
start = int(start)
end = input("請決定數字隨機範圍結束值：")
end = int(end)
r = random.randint(start,end) #包括1跟100
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

