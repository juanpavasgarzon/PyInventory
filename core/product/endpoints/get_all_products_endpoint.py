from typing import List

from core.product.dtos.product_dto import ProductDto
from core.product.router import product_router
from core.product.services.get_all_products_service import get_all_products_service


@product_router.get("/", response_model=List[ProductDto])
async def list_products_endpoint() -> List[ProductDto]:
    """
    Endpoint to retrieve a list of all products.

    This endpoint fetches all products from the database using the `get_all_products_service`
    service method and returns them as a list of `ProductDto` objects. If there are no products,
    it returns an empty list.

    Returns:
        List[ProductDto]: A list of `ProductDto` instances representing all products.

    Example:
        List all products:
        GET /products

        Response:
        [
            {
                "id": "60b91b5e64e2a9f024f5b04f",
                "code": "P001",
                "name": "Sample Product 1",
                "price": 19.99,
                "description": "Description of product 1"
            },
            {
                "id": "60b91b5e64e2a9f024f5b050",
                "code": "P002",
                "name": "Sample Product 2",
                "price": 29.99,
                "description": "Description of product 2"
            }
        ]
    """
    return await get_all_products_service()
