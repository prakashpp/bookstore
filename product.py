from trytond.model import ModelSQL, ModelView, fields

LANGUAGES = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
]

class Author(ModelSQL, ModelView):
    "Author"
    _name = "party.author"
    _description = __doc__

    books = fields.One2Many('product.book', 'author', 'Books')

Author()


class Publisher(ModelSQL, ModelView):
    "Publisher"
    _name = "party.publisher"
    _descriptiom = __doc__

    books = fields.One2Many('product.book', 'publisher', 'Books')
    party = fields.Many2One('party.party', 'Party')

Publisher()


class Book(ModelSQL, ModelView):
    "Book"
    _name = "product.book"
    _description = __doc__

    products = fields.One2Many('product.product', 'book', 'Products')
    title = fields.Char('Title', required=True)
    author = fields.Many2One('party.author', 'Author', required=True)
    isbn10 = fields.Integer('ISBN-10')
    isbn13 = fields.Integer('ISBN-13')
    publishing_year = fields.Integer('Publishing Year')
    number_of_pages = fields.Integer('Number of Pages')
    language = fields.Selection(LANGUAGES, 'Language', required=True)
    description = fields.Text('Desciption')

Book()


class Product(ModelSQL, ModelView):
    "Product"
    _name = "product.product"
    _description = __doc__

    book = fields.Many2One('product.book', 'Book')

Product()
