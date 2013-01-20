from trytond.model import ModelSQL, ModelView, fields

class Author(ModelSQL, ModelView):
    "Author"
    _name = "party.author"
    _description = __doc__
    _inherits = {'party.party': 'party'}

    party = fields.Many2One(
        'party.party', 'Party', required=True, ondelete='CASCADE',
    )
    books = fields.One2Many('product.book', 'author', 'Books')

Author()


class Publisher(ModelSQL, ModelView):
    "Publisher"
    _name = "party.publisher"
    _description = __doc__
    _inherits = {'party.party': 'party'}

    party = fields.Many2One(
        'party.party', 'Party', required=True, ondelete='CASCADE',
    )
    books = fields.One2Many('product.book', 'publisher', 'Books')

Publisher()
