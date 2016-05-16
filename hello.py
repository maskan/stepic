from cgi import parse_qs                                                        


def application(environ, start_response):

    query_string = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = ''
    print(query_string)
    for key, value in query_string.items():
        for element in value:
            body += key + '='
            body += element + '\r\n'

    print(body)

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, response_headers)

    return [body]