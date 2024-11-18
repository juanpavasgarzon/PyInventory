from fastapi import HTTPException

from core.product.dtos.create_product_dto import CreateProductDto
from core.product.dtos.product_dto import ProductDto
from core.product.router import product_router
from core.product.services.create_product_service import add_product_service


@product_router.post("/", response_model=ProductDto)
async def create_product(product: CreateProductDto):
    """
    Endpoint to create a new product.

    This endpoint accepts a `CreateProductDto` containing the product details and creates a new
    product in the database using the `add_product_service` service method. If the creation is
    successful, it returns the created product as a `ProductDto`. If an error occurs during the
    creation process, a `400` status code with the error message is returned.

    Args:
        product (CreateProductDto): The product data transfer object containing the details
        required to create a new product.

    Returns:
        ProductDto: A data transfer object representing the created product.

    Raises:
        HTTPException: If an error occurs during product creation, an HTTPException with status
        code 400 and the error message will be raised.

    Example:
        Create a new product:
        POST /products

        Request Body:
        {
            "code": "P003",
            "name": "New Product",
            "price": 49.99,
            "description": "Description of the new product"
        }

        Response:
        {
            "id": "60b91b5e64e2a9f024f5b051",
            "code": "P003",
            "name": "New Product",
            "price": 49.99,
            "description": "Description of the new product"
        }
    """
    try:
        return await add_product_service(product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
