import basic

while(True):
	text = input('basic > ')
	result, error = basic.run('<stdin>', text) #call run method from basic 

	if error:
		print(error.as_string())

	else:
		print(result)