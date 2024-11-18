from typing import Optional

from core.product.dtos.product_dto import ProductDto
from core.product.dtos.update_product_dto import UpdateProductDto
from core.product.repositories.update_product_repo import update_product_repo


async def update_product_service(product_id: str, dto: UpdateProductDto) -> Optional[ProductDto]:
    """
    Service method to update an existing product.

    This method receives a `product_id` and an `UpdateProductDto` containing the new product
    details, updates the corresponding product in the database using the `update_product_repo`
    function, and returns the updated product as a `ProductDto` instance.

    Args:
        product_id (str): The ID of the product to be updated.
        dto (UpdateProductDto): The DTO containing the updated product's details.

    Returns:
        Optional[ProductDto]: The `ProductDto` instance representing the updated product,
        or `None` if no product with the given ID was found.

    Example:
        updated_product_dto = UpdateProductDto(code="P001", name="Updated Product", price=29.99)
        updated_product = await update_product_service("60b91b5e64e2a9f024f5b04f", updated_product_dto)
        if updated_product:
            print(f"Updated Product: {updated_product.name} - Price: {updated_product.price}")
        else:
            print("Product not found.")
    """
    product = await update_product_repo(product_id, dto)
    if product is None:
        return None
    return ProductDto.from_entity(product)
