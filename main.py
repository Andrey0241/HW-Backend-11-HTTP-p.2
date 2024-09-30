import json

def get_request():
    request = "GET /index HTTP/1.0\r\n\r\n"
    print(request)

def post_request():
    body = "username=Alice&password=secret"
    content_length = len(body)
    request = f"POST /api/login HTTP/1.0\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n{body}"
    print(request)

def get_request_1_1():
    request = "GET http://example.com/home HTTP/1.1\r\nHost: example.com\r\n\r\n"
    print(request)

def get_request_accept():
    request = "GET http://example.com/data HTTP/1.1\r\nHost: example.com\r\nAccept: application/json\r\n\r\n"
    print(request)

def post_request_json():
    data = {"username": "Alice", "msg": "Hello"}
    body = json.dumps(data)
    content_length = len(body)
    request = f"POST http://example.com/api/messages HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: {content_length}\r\n\r\n{body}"
    print(request)

def put_request():
    body = "Updated message"
    content_length = len(body)
    request = f"PUT http://example.com/api/messages/42 HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n\r\n{body}"
    print(request)

def delete_request():
    request = "DELETE http://example.com/api/messages/42 HTTP/1.1\r\nHost: example.com\r\n\r\n"
    print(request)

def post_form_request():
    body = "username=admin&password=secret"
    content_length = len(body)
    request = f"POST www.example.com/login HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n{body}"
    print(request)

def post_json_request():
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    body = json.dumps(data)
    content_length = len(body)
    request = f"POST www.example.com/api/users HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: {content_length}\r\n\r\n{body}"
    print(request)

def get_query_request():
    request = "GET www.example.com/search?query=blue%20shoes HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
    print(request)

def post_chunked_request():
    chunked_body = "7\r\nHello, \r\n6\r\nworld!\r\n0\r\n\r\n"
    request = f"POST www.example.com/api/chunked HTTP/1.1\r\nTransfer-Encoding: chunked\r\n\r\n{chunked_body}"
    print(request)

def main():
    get_request()
    post_request()
    get_request_1_1()
    get_request_accept()
    post_request_json()
    put_request()
    delete_request()
    post_form_request()
    post_json_request()
    get_query_request()
    post_chunked_request()

if __name__ == "__main__":
    main()