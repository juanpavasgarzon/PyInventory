from pydantic import BaseModel


class CreateDocumentItemDto(BaseModel):
    """
    Data transfer object (DTO) for creating a new document item.

    This DTO is used to represent a single item in a document, including the product ID and quantity.
    It is designed to be used when creating or updating document items.

    Attributes:
        product_id (str): The unique identifier for the product in the document item.
        quantity (int): The quantity of the product in the document item.

    Usage:
        To create a document item, an instance of `CreateDocumentItemDto` is used to encapsulate the data.
        The `product_id` field refers to the unique ID of the product, while the `quantity` represents how
        many of that product are included in the document item.

    Example:
        document_item_dto = CreateDocumentItemDto(product_id="prod_001", quantity=5)

    Configuration:
        - The `from_orm` configuration in the `Config` class allows the model to be created from ORM data
          (i.e., MongoDB documents).
    """
    product_id: str
    quantity: int

    class Config:
        from_orm = True
