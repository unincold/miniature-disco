def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		print(f"printing model:{current_design}")
		completed_models.append(current_design)
		"""模拟打印设计"""
def show_completed_models(completed_models):
	"""显示完成模型"""
	print("\nthe following models have been painted")
	for completed_model in completed_models:
		print(completed_model)




		
unprinted_designs=['phone case','robot','dode']
completed_models=[]
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

