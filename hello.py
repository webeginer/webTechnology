QUERY_STRING = 'a=1&a=2&b=3'

origin = QUERY_STRING
param_list = origin.split('&')
for x in param_list:
	print(x)

def hello(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = 'Hello, world!'
	start_response(status, headers)
	return [ body ]