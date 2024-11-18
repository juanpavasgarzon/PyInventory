from mongoengine import EmbeddedDocument, IntField, FloatField, ReferenceField

from core.product.entities.product import Product


class DocumentItem(EmbeddedDocument):
    """
    Represents an item in a document, including a reference to a product and its associated quantity and price.

    This class is embedded within the `Document` class and represents an item in the document,
    storing details about the product, quantity, and price.

    Attributes:
        product (Product): A reference to the `Product` entity associated with this item.
        quantity (int): The quantity of the product in the document item.
        price (float): The price of a single unit of the product.

    Methods:
        to_dict: Converts the DocumentItem instance to a dictionary representation.

    Example:
        document_item = DocumentItem(product=product_instance, quantity=10, price=5.0)
        document_item_dict = document_item.to_dict()

    """
    product = ReferenceField(Product)
    quantity = IntField(required=True)
    price = FloatField(required=True)

    def to_dict(self):
        """
        Converts the DocumentItem instance to a dictionary representation.

        This method is used to convert the document item object to a dictionary format,
        which can be used for serialization, e.g., returning the document item data in an API response.

        Returns:
            dict: A dictionary containing the document item's data, including the product's data.

        Example:
            {
                "product": {...},  # Product data in dictionary format
                "quantity": 10,
                "price": 5.0
            }

        """
        return {
            "product": self.product.to_dict(),
            "quantity": self.quantity,
            "price": self.price,
        }
