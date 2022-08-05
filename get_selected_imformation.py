def get_name(first_name,middle_name='',last_name):
	if middle_name:
		full_name=f"{first_name} {middle_name} {last_name}"
	else:
		full_name=f"{first_name} {last_name}"