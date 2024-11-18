from fastapi import HTTPException

from core.product.dtos.product_dto import ProductDto
from core.product.router import product_router
from core.product.services.get_product_by_id_service import get_product_by_id_service


@product_router.get("/{product_id}", response_model=ProductDto)
async def get_product_by_id_endpoint(product_id: str):
    """
    Endpoint to retrieve a product by its ID.

    This endpoint receives a `product_id`, fetches the corresponding product from the database
    using the `get_product_by_id_service` service method, and returns the product as a
    `ProductDto`. If no product with the given ID is found, it raises a 404 HTTPException
    with the message "Product not found".

    Args:
        product_id (str): The ID of the product to retrieve.

    Raises:
        HTTPException: If the product with the given ID does not exist, raises a 404 HTTP
        exception with the message "Product not found".

    Returns:
        ProductDto: The `ProductDto` instance representing the retrieved product.

    Example:
        Get a product by its ID:
        GET /products/{product_id}

        Response:
        {
            "id": "60b91b5e64e2a9f024f5b04f",
            "code": "P001",
            "name": "Sample Product",
            "price": 19.99,
            "description": "A sample product description"
        }
    """
    product = await get_product_by_id_service(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
