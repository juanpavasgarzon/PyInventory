from fastapi import HTTPException

from core.document.dtos.document_dto import DocumentDto
from core.document.router import document_router
from core.document.services.get_document_by_reference_service import get_document_by_reference_service


@document_router.get("/{reference}", response_model=DocumentDto)
async def get_document_by_reference_endpoint(reference: str):
    """
    Endpoint for retrieving a document by its reference.

    This endpoint allows for fetching a document by its unique reference. If the document with the provided
    reference exists, it will return the document details. Otherwise, a 404 error is raised.

    Args:
        reference (str): The reference of the document to be retrieved.

    Returns:
        DocumentDto: The DTO representing the document found with the provided reference.

    Raises:
        HTTPException: If the document with the provided reference is not found, a 404 error is raised.

    Example:
        GET /documents/DOC-001
        Response:
        {
            "id": "60c72b2f9b1d8f7c6d0f1a2d",
            "reference": "DOC-001",
            "consecutive": "001",
            "datetime": "2024-11-20T10:00:00",
            "concept": "Purchase Order",
            "description": "Order for office supplies",
            "items": [
                {"product_id": "123", "product_code": "P001", "product_name": "Product 1", "product_description": "Description of Product 1", "quantity": 10, "price": 15.0, "total": 150.0}
            ]
        }

    """
    product = await get_document_by_reference_service(reference)
    if product is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return product
