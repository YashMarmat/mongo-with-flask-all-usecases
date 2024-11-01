from marshmallow import Schema, fields


class AuthorSchema(Schema):
    name = fields.Str(required=True)
    books_written = fields.Integer(default=0)

class BookSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    published_date = fields.Date()
    author = fields.Nested(AuthorSchema)