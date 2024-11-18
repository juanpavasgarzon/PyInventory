from mongoengine import Document, StringField, FloatField


class Product(Document):
    """
    Class for managing product entities in the inventory system.

    This class represents a product with attributes such as its unique
    code, name, price, and an optional description. The `Product` class
    allows you to interact with product data stored in the MongoDB database
    under the 'products' collection.

    Attributes:
        code (str): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        description (str, optional): A description of the product (default is None).
    """

    meta = {
        'collection': 'products',
        'db_alias': 'inventory'
    }

    code = StringField(required=True)
    name = StringField(required=True)
    price = FloatField(required=True)
    description = StringField(required=False)

    def to_dict(self) -> dict:
        """
        Converts the Product object to a dictionary representation.

        This method returns a dictionary that contains the product's
        information, such as its ID, name, price, and description,
        for easier use in other parts of the application (e.g., serialization).

        Returns:
            dict: A dictionary containing the product's id, name, price,
                  and description.

        Example:
            {
                "id": "60b8d2950d5b5b6f1015fd4a",
                "name": "Laptop",
                "price": 1200.99,
                "description": "A high-performance laptop."
            }
        """
        return {
            "id": str(self.id),
            "name": self.name,
            "price": self.price,
            "description": self.description
        }
