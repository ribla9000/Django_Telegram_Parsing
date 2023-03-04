async def text_validator(param):
	for i in range(len(param)-1):
		if param[i].islower() and param[i+1].isupper():
			param = f"{param[:i+1]}. {param[i+1:]}"
	return param
