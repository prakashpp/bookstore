from trytond.model import ModelSQL, ModelView, fields

LANGUAGES = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
]

class Book(ModelSQL, ModelView):
    "Book"
    _name = "product.book"
    _description = __doc__

    products = fields.One2Many('product.product', 'book', 'Products')
    title = fields.Char('Title', required=True)
    author = fields.Many2One('party.author', 'Author', required=True)
    publisher = fields.Many2One('party.publisher', 'Publisher', required=True)
    isbn10 = fields.Integer('ISBN-10')
    isbn13 = fields.Integer('ISBN-13')
    publishing_year = fields.Integer('Publishing Year')
    number_of_pages = fields.Integer('Number of Pages')

    #TODO: many2one on ir.lang.
    language = fields.Selection(LANGUAGES, 'Language', required=True)
    description = fields.Text('Desciption')

Book()


class Product(ModelSQL, ModelView):
    "Product"
    _name = "product.product"
    _description = __doc__

    book = fields.Many2One('product.book', 'Book')

Product()
