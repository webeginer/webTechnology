def echo(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	request = environ['QUERY_STRING']
	request_list = request.split('&')
	start_response(status, headers)
	return ["\n".join(request_list)]