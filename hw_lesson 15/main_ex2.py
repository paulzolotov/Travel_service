"""
Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию,
которая получает от пользователя название альбома через input и выводит список всех треков в этом альбоме.
"""

from peewee import *

db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Albums(BaseModel):
    title = CharField(column_name='Title', null=False)
    album_id = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'albums'


class Tracks(BaseModel):
    name = CharField(column_name='Name', null=False)
    album_id = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'tracks'


def get_tracks(album_name):
    with db:
        return Tracks.select().\
            where(Tracks.album_id == Albums.select().
                  where(Albums.title == album_name))



user_album = input('Введите название альбома: ')  # A-Sides
all_tracks = get_tracks(user_album)
for track in all_tracks:
    print(track.name)




