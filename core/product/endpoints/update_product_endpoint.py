from fastapi import HTTPException

from core.product.dtos.product_dto import ProductDto
from core.product.dtos.update_product_dto import UpdateProductDto
from core.product.router import product_router
from core.product.services.update_product_service import update_product_service


@product_router.put("/{product_id}", response_model=ProductDto)
async def update_product_endpoint(product_id: str, product: UpdateProductDto):
    """
    Endpoint to update an existing product.

    This endpoint accepts a `product_id` and an `UpdateProductDto` containing the updated product
    details. It uses the `update_product_service` method to update the product in the database. If
    the product is updated successfully, it returns the updated product as a `ProductDto`. If the
    product is not found or an error occurs during the update process, a `400` status code with the
    error message is returned.

    Args:
        product_id (str): The unique identifier of the product to be updated.
        product (UpdateProductDto): The data transfer object containing the updated product details.

    Returns:
        ProductDto: A data transfer object representing the updated product.

    Raises:
        HTTPException: If an error occurs during the update process, an HTTPException with status
        code 400 and the error message will be raised.

    Example:
        Update an existing product:
        PUT /products/{product_id}

        Request Body:
        {
            "code": "P003",
            "name": "Updated Product",
            "price": 59.99,
            "description": "Updated description of the product"
        }

        Response:
        {
            "id": "60b91b5e64e2a9f024f5b051",
            "code": "P003",
            "name": "Updated Product",
            "price": 59.99,
            "description": "Updated description of the product"
        }
    """
    try:
        return await update_product_service(product_id, product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
