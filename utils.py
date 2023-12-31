from database import Database, Note

def extract_route(request):
    route = request.split(" ")[1][1:]
    return route

def read_file(path):
    file = open(path, mode='r+b')
    lines = file.read()
    return lines

def load_data():
    db = Database('banco')
    return db.get_all()

def load_template(path):
    filepath = 'templates/' + path
    file = open(filepath, mode="r", encoding="utf-8")
    return file.read()

def add_anotacao(params):
    db = Database('banco')
    db.add(Note('',params['titulo'],params['detalhes']))

def build_response(body='', code=200, reason='OK', headers=''):
    if len(headers) > 0:
        return ("HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body).encode()
    else:
        return ("HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body).encode()
    