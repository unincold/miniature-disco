class Dog:

	def __init__(self,name,age):
		"""self 这里是形参"""
		self.name=name
		self.age=age
	def sit(self):
		"""模拟小狗动作"""
		print(f"{self.name} now is sitting")

	def roll_over(self):
		print(f"{self.name} rolled over")

my_dog=Dog('amy',5)
print(f"{my_dog.name.title()} is my dog")
print(f"she is {my_dog.age} years old now")

my_dog.sit()
my_dog.roll_over()