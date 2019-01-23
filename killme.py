import traceback, sys, re, socket, collections
from functools import reduce

index_html = '<!DOCTYPE html><html><head><title>Killme</title></head><body><H1>killme</h1><form action="/" method="post"><input type="text" name="title"><br><textarea rows="4" cols="50" name="content"></textarea><br><input type="submit" value="Submit"></form>'
def thread_html(t): return '<!DOCTYPE html><html><head><title>Killme</title></head><body><H1>killme</h1><form action="/" method="post"><br><textarea rows="4" cols="50" name="content"></textarea><br><input type="submit" value="Submit"></form>'
def apply_head(body): return 'HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/html\r\nConnection: Closed\r\n\r\n'.format(len(body.encode()))+body
def index(): return apply_head(reduce(lambda a, b: a+'<a href="/'+ b +'">'+ b +'</a><br>', t, index_html)+'</body></html>')
def thread(t): return apply_head(reduce(lambda a, b: a+b+'<br>', t, thread_html(t))+'</body></html>')

def get(p, t): return thread(t[p]) if p in t else index()


reply_pattern = re.compile(r"reply=(?P<content>.*))", re.DOTALL)
def reply_parse(b):
    m = thread_pattern.match(b)
    return m.group('reply')
def make_reply(b, t, p):
    title, content = reply_parse(b)
    t[title].append(content)
    return index()

thread_pattern = re.compile(r"title=(?P<title>.*)&content=(?P<content>.*))", re.DOTALL)
def thread_parse(b):
    m = thread_pattern.match(b)
    return (m.group('title'), m.group('content'))
def make_thread(b, t):
    title, content = thread_parse(b)
    t[title] = [content]
    return index()
def post(p, b, t): return make_thread(b, t) if p == '' else make_reply(b, t, p)


request_pattern = re.compile(r"(?P<method>.*) /(?P<path>.*) HTTP.*\r\n\r\n(?P<body>.*)", re.DOTALL)
def request_parse(d):
    m = request_pattern.match(data)
    return (m.group("method"), m.group("path"), m.group("body"))

t = {'xd':['haha','gg','ez'], 'wow':['lol','lmao']}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3000))
server.listen(5)
print("starting server")
while True:
    client, address = server.accept()
    try:
        data = client.recv(1024).decode()
        method, path, body = request_parse(data)
        res = post(path, body, t) if method == 'POST' else get(path, t)
        client.send(res.encode())
    except:
        traceback.print_exc(file=sys.stdout)
        client.send('error'.encode())
    client.close()