print('Please select your local temperature rule')
temp_r = input('C for Celsius, F for Fahrenheit: ')
if temp_r == 'C':
	temp_c = input('How is the weather in Celsius? ')
	temp_c = int(temp_c)
	temp_f = temp_c*(9/5)+32
	print('The weather in Fahrenheit is: ', temp_f)
elif temp_r == 'F':
	temp_f = input('How is the weather in Fahrenheit? ')
	temp_f = float(temp_f)
	temp_c = (temp_f-32)/1.8
	print('The weather in Celsius is: ', temp_c)
else:
	print('Please type again')
	