ingredients={'onion','cucomber','potato'}
words='please type in the ingredients you want:'
active=True
next_stage=False
while active:
	if input(words) in ingredients:
		output=input(words)
		print('f{output} is added')
		next_stage=True
	if input(words) =='quit':
		active=False
	if input(word) not in ingredients:
		#用else也可以
		print("this ingredient is sold out")
while next_stage:
	print('your pizza is making now!')

