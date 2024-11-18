from mongoengine import Document, StringField, IntField


class Counter(Document):
    """
    Represents a counter for generating sequential values, typically used for document numbering.

    This class is used to store and manage counters in the database, with each counter having a unique
    name and a value. The value can be incremented to generate sequential values for various purposes
    (e.g., generating unique document references or invoice numbers).

    Attributes:
        name (str): The name of the counter, which must be unique.
        value (int): The current value of the counter, starting from 0 by default.

    Meta:
        collection (str): The name of the MongoDB collection where the counter is stored.
        db_alias (str): The alias of the database where the counter collection resides.

    Example:
        counter = Counter.objects(name="invoice_number").first()
        if counter:
            print(counter.value)  # Output: current counter value
    """

    meta = {
        'collection': 'counters',
        'db_alias': 'inventory'
    }

    name = StringField(required=True, unique=True)
    value = IntField(default=0)
