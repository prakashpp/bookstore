from trytond.model import ModelSQL, ModelView, fields

class Product(ModelSQL, ModelView):
    "Product"
    _name = "product.product"
    _description = __doc__

    book = fields.Many2One('bookstore.book', 'Book')

Product()
