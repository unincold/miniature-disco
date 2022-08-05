def greet_users(names):
	"""想每位用户发出简单问候"""
	for name in names:
		msg=f"Hello, {name.title()}!"
		print(msg)
usernames=['aaa','bbb','ccc']
greet_users(usernames)