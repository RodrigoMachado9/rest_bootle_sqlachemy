from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, ForeignKey, select)
# http://initd.org/psycopg/docs/module.html

engine = create_engine('postgresql://postgres@localhost/dev', echo=False)
#conn  =  engine.connect()

metadata = MetaData(bind=engine)


# todo, repassar a construção das tabelas do
#  schema publioc para schema pertinente as entidades;

artists = Table('artistas', metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('nome', String(40), index=True, nullable=False, unique=True))


discs = Table('discos', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('artista_id', ForeignKey('artistas.id'), nullable=False),
              Column('album', String(40), nullable=False),
              Column('ano', Integer, nullable=False)

              )

metadata.create_all()



def search_all_artists():
    return {_id:artist for _id, artist in select([artists]).execute()}

# print(search_all_artists())
def insert_artist(artist):
    conn = engine.connect()
    # instancia metodo insert
    artist_ins = artists.insert()
    new_artist = artist_ins.values(nome=artist)
    try:
        global status
        conn.execute(new_artist)
        status = True
    except Exception as e:
        print(e)
    finally:
        conn.close()
        return status

"""
conn  =  engine.connect()
dev  = conn.execute("select * from notafiscal.notas")

for query in dev:
    cliente = query[1]
    numero  = query[3]

print(cliente)
print(numero)
"""


def insert_album(disc, year, artist):
    """
    :param args: nome, ano, artista
    :return:
    """
    conn = engine.connect()
    # instancia metodo insert
    disc_ins = discs.insert()
    new_disc = disc_ins.values(artista_id=id_artist(artist),
                               album=disc,
                               ano=year)
    try:
        global status
        conn.execute(new_disc)
        status = True
    except Exception as e:
        print(e)
    finally:
        conn.close()
        return status


def id_artist(artist):
    searched = select([artists]).where(artists.c.nome == artist)
    result = [_id for _id, artist in searched.execute()]
    if result:
        return result[0]
    else:
        insert_artist(artist)
        return id_artist(artist)


def search_albums(artist):
    # todo,  tratart insersão de dados....  for lower_case
    artist_id = [x for x in select([artists.c.id]).where(artists.c.nome == artist).execute()]
    if artist_id:
        query = select([discs.c.id, discs.c.album,
                        discs.c.ano, discs.c.artista_id]).where(
                        discs.c.artista_id == artist_id[0][0]).execute()
        return {_id:{'album': album,
                     'ano': ano,
                     'id_artista': artista_id}
                for _id, album, ano, artista_id in query}
    else:
        return {}
