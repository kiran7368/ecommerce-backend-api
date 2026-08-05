from marshmallow import Schema, fields


class CartSchema(Schema):

    product_id = fields.Integer(required=True)

    quantity = fields.Integer(required=True)