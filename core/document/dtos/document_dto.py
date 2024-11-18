from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from core.document.dtos.document_item_dto import DocumentItemDto
from core.document.entities.document import Document


class DocumentDto(BaseModel):
    """
    Data transfer object (DTO) for representing a document.

    This DTO is used to transfer document data, including reference, consecutive, datetime, concept, description,
    and associated document items. It is designed to be used when creating, updating, or transferring document information.

    Attributes:
        id (str): The unique identifier for the document.
        reference (str): The reference code for the document.
        consecutive (str): A consecutive number or identifier for the document.
        datetime (datetime): The date and time when the document was created.
        concept (str): A description or concept of the document.
        description (Optional[str]): An optional description for the document.
        items (List[DocumentItemDto]): A list of items (DocumentItemDto) associated with the document.

    Usage:
        This class is used to represent a document in a format suitable for data transfer. The `from_entity` method
        is used to convert an actual document entity (usually a database model) into an instance of this DTO.

    Example:
        document_dto = DocumentDto.from_entity(document)

    Configuration:
        - The `from_orm` configuration in the `Config` class allows the model to be created from ORM data
          (i.e., MongoDB documents).
    """
    id: str
    reference: str
    consecutive: str
    datetime: datetime
    concept: str
    description: Optional[str] = None
    items: List[DocumentItemDto]

    @classmethod
    def from_entity(cls, document: Document) -> "DocumentDto":
        """
        Converts a document entity into a DocumentDto instance.

        Args:
            document (Document): The document entity to convert.

        Returns:
            DocumentDto: The corresponding DTO instance.
        """
        return cls(
            id=document.id,
            reference=document.reference,
            consecutive=document.consecutive,
            datetime=document.datetime,
            concept=document.concept,
            description=document.description,
            items=[DocumentItemDto.from_entity(item) for item in document.items],
        )

    class Config:
        from_orm = True
