def name(first_name,last_name,middle_name):
	full_name=f"{first_name} {middle_name} {last_name}"
	FULL_NAME=full_name.titled()
	return name_list.append(FULL_NAME)
name_list=[]
first_name=input('please type in your first_name:')
last_name=input('please type in your last_name:')
active=True
words="Do you have middle name?Type 'q' to skip"
while active:
	if input(words)=='q':
		active=False
	else:
		output=input(words)
		confirm=f"Are you sure your middle name is {output}? Type a to continue."
		while True 
			input(confirm)
			if input(confirm)!='a':
				break
			elif input(confirm)=='a':
				middle_name=input(words)
				print(f'your middle name is {middle_name}')
				break

#有问题！！！！待定。



