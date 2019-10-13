from requests import get
from bottle import Bottle, request, response
from json import dumps
from app.core import search_all_artists , insert_artist, insert_album, search_albums
api = Bottle()


@api.get('/')
def index_map():
    """
    :return: um mapa completo da api;
    """
    return dumps({'artistas': 'url/artistas', 'albuns': 'url/albuns'})


@api.get('/artistas')
def artistas_map():
    """
    :return: todos os artistas;
    """
    return search_all_artists()

@api.post('/artista')
def post_artist():
    """
    Insere dados na API
    Formato do input:
        Content-Type: application/json
        payload: {"nome":"A7x"}
    """
    artista = request.json
    print(artista)
    response.headers['Content-Type'] = 'application/json'
    if not artista:
        response.status = 400
        return {response.status:artista}
    if insert_artist(artista['nome'].lower()):
        response.status = 201   # created
        return {response.status:artista}
    else:
        response.status = 400   # not found
    return dumps({response.status: artista})


@api.post('/album')
def post_albums():
    """
    {
        "nome": "dear god",
        "artista": "Avenged",
        "ano": 2019
    }
    """
    disc = request.json
    response.headers['Content-Type'] = 'application/json'
    if not disc:
        response.status = 400
        return {response.status:disc}
    if insert_album(disc['nome'], disc['ano'], disc['artista']):
        response.status = 201   # created
        return {response.status:disc}
    else:
        response.status = 400   # not found
    return dumps({response.status: disc})


@api.get('/albums/<artist>')
def albums_map(artist):
    return search_albums(artist)


if __name__=='__main__':
    api.run(debug=False, reload=True)

