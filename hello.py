QUERY_STRING = 'a=1&a=2&b=3'

origin = QUERY_STRING
param_list = origin.split('&')
for x in param_list:
	print(x)