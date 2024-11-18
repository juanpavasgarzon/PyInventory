from pydantic import BaseModel

from core.document.entities.document_item import DocumentItem


class DocumentItemDto(BaseModel):
    """
    Data Transfer Object (DTO) for representing a document item.

    This DTO is used to transfer data for an individual item in a document. Each item contains information about
    a product, its quantity, price, and total value.

    Attributes:
        product_id (str): The unique identifier for the product.
        product_code (str): The code of the product.
        product_name (str): The name of the product.
        product_description (str): A description of the product.
        quantity (int): The quantity of the product in the document item.
        price (float): The price of a single unit of the product.
        total (float): The total cost for the quantity of the product in this item (quantity * price).

    Methods:
        from_entity: Converts a `DocumentItem` entity into a `DocumentItemDto` instance.

    Example:
        document_item_dto = DocumentItemDto.from_entity(document_item)

    Configuration:
        - The `from_orm` configuration in the `Config` class allows the model to be created from ORM data
          (i.e., MongoDB documents).
    """
    product_id: str
    product_code: str
    product_name: str
    product_description: str
    quantity: int
    price: float
    total: float

    @classmethod
    def from_entity(cls, document_item: DocumentItem) -> "DocumentItemDto":
        """
        Converts a DocumentItem entity into a DocumentItemDto instance.

        Args:
            document_item (DocumentItem): The document item entity to convert.

        Returns:
            DocumentItemDto: The corresponding DTO instance.
        """
        return cls(
            product_id=document_item.product.id,
            product_code=document_item.product.code,
            product_name=document_item.product.name,
            product_description=document_item.product.description,
            quantity=document_item.quantity,
            price=document_item.price,
            total=document_item.quantity * document_item.price,
        )

    class Config:
        from_orm = True
