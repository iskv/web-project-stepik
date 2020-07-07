# Application
def app(environ, start_response):	
	url_param = environ['QUERY_STRING'].split('&')
	url_param = [param + '\n' for param in url_param]
	
	status = '200 OK'
	response_headers = [
		('Content-type', 'text/plain')
	]	
	start_response(status, response_headers)
	return map(str.encode, url_param)
