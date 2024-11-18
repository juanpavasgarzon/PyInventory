from typing import List

from core.document.dtos.document_dto import DocumentDto
from core.document.repositories.create_document_repo import create_document_repo


async def create_document_service(ref: str, concept: str, items: List[dict], description: str = None) -> DocumentDto:
    """
    Creates a new document in the database with the provided reference, concept, items, and optional description.

    This function calls the repository method to create a document and then returns a `DocumentDto` object
    containing the details of the newly created document.

    Args:
        ref (str): The reference code for the new document.
        concept (str): The concept for the document, such as "sale" or "purchase."
        items (List[dict]): A list of items to include in the document, where each item is a dictionary
                            containing product information and quantity.
        description (str, optional): An optional description of the document.

    Returns:
        DocumentDto: A Data Transfer Object (DTO) representing the created document.

    Example:
        items = [
            {"product_id": "12345", "quantity": 2},
            {"product_id": "67890", "quantity": 3}
        ]
        document = await create_document_service("INV-12345", "sale", items, "Sale of office supplies")
        print(document.reference)  # Output: "INV-12345"
    """
    document = await create_document_repo(ref, concept, items, description)
    return DocumentDto.from_entity(document)
