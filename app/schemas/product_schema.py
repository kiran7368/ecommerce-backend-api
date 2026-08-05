from marshmallow import Schema, fields, validate


class ProductSchema(Schema):

    name = fields.String(
        required=True,
        validate=validate.Length(min=2, max=200)
    )

    description = fields.String(required=True)

    price = fields.Float(required=True)

    stock = fields.Integer(required=True)

    image_url = fields.String(required=False)

    category_id = fields.Integer(required=True)