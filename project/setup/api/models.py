from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название фильма'),
    'description': fields.String(required=True, max_length=100, example='Описание фильма'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер'),
    'year': fields.Integer(required=True, example=2020),
    'rating': fields.Float(required=True, example=20.2),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)

})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='email'),
    'password': fields.String(required=True, max_length=300, example='qwerty'),
    'name': fields.String(required=True, max_length=100, example='имя'),
    'surname': fields.String(required=True, max_length=100, example='фамилия'),
    'favorite_genre': fields.Nested(genre)
})
