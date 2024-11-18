from fastapi import HTTPException

from core.document.dtos.create_document_dto import CreateDocumentDto
from core.document.dtos.document_dto import DocumentDto
from core.document.router import document_router
from core.document.services.create_document_service import create_document_service


@document_router.post("/", response_model=DocumentDto)
async def create_document_endpoint(document: CreateDocumentDto):
    """
    Endpoint for creating a new document.

    This endpoint allows for the creation of a new document by accepting the document's reference, concept,
    description, and items. The items are passed as a list of `CreateDocumentItemDto` instances, each representing
    a product with its quantity.

    Args:
        document (CreateDocumentDto): The DTO containing information about the document and its items.

    Returns:
        DocumentDto: The DTO representing the created document.

    Raises:
        HTTPException: If the document creation fails or if the document is not found, a 404 error is raised.

    Example:
        Create a document:
        POST /documents

        Request Body:
        {
            "reference": "DOC-001",
            "concept": "Purchase Order",
            "description": "Order for office supplies",
            "items": [
                {"product_id": "123", "quantity": 10},
                {"product_id": "456", "quantity": 5}
            ]
        }

        Response:
        {
            "id": "60b91b5e64e2a9f024f5b051",
            "reference": "DOC-001",
            "concept": "Purchase Order",
            "description": "Order for office supplies",
            "items": [
                {"product_id": "123", "quantity": 10},
                {"product_id": "456", "quantity": 5}
            ]
        }
    """
    items = [item.to_dict() for item in document.items]
    product = await create_document_service(document.reference, document.concept, items, document.description)
    if product is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return product
