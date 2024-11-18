from typing import Optional, List

from pydantic import BaseModel

from core.document.dtos.create_document_item_dto import CreateDocumentItemDto


class CreateDocumentDto(BaseModel):
    """
    Data transfer object (DTO) for creating a new document.

    This DTO is used for creating a new document. It includes the reference, concept, an optional
    description, and a list of document items. The `CreateDocumentDto` class ensures that all necessary
    data is provided to create a new document in the system.

    Attributes:
        reference (str): The unique reference identifier for the document.
        concept (str): The concept or purpose of the document.
        description (Optional[str]): An optional description providing more details about the document.
        items (List[CreateDocumentItemDto]): A list of items that are part of the document.

    Usage:
        To create a document, an instance of `CreateDocumentDto` is used to encapsulate the data.
        The `items` field must be populated with instances of `CreateDocumentItemDto` that describe the
        individual items of the document.

    Example:
        document_dto = CreateDocumentDto(
            reference="DOC123",
            concept="Invoice",
            description="Invoice for purchase",
            items=[CreateDocumentItemDto(product_id="prod_001", quantity=2, price=100.0)]
        )

    Configuration:
        - The `from_orm` configuration in the `Config` class allows the model to be created from
          ORM data (i.e., MongoDB documents).
    """
    reference: str
    concept: str
    description: Optional[str] = None
    items: List[CreateDocumentItemDto]

    class Config:
        from_orm = True
