from typing import Optional

from core.product.dtos.product_dto import ProductDto
from core.product.repositories.get_product_by_id_repo import get_product_by_id_repo


async def get_product_by_id_service(product_id: str) -> Optional[ProductDto]:
    """
    Service method to retrieve a product by its ID.

    This method fetches a product from the database using its unique product ID
    and returns it as a `ProductDto`. If the product is not found, it returns `None`.

    Args:
        product_id (str): The unique identifier of the product to retrieve.

    Returns:
        Optional[ProductDto]: A `ProductDto` instance containing the product details
                               if found, or `None` if the product does not exist.

    Example:
        product_dto = await get_product_by_id_service("12345")
        if product_dto:
            print(f"Product found: {product_dto.name}")
        else:
            print("Product not found.")
    """
    product = await get_product_by_id_repo(product_id)
    if not product:
        return None
    return ProductDto.from_entity(product)
