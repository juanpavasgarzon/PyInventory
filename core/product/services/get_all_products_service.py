from typing import List

from core.product.dtos.product_dto import ProductDto
from core.product.repositories.get_all_products_repo import get_all_products_repo


async def get_all_products_service() -> List[ProductDto]:
    """
    Service method to retrieve all products.

    This method fetches all products from the database and returns a list of `ProductDto`
    instances representing the products.

    Returns:
        List[ProductDto]: A list of `ProductDto` instances, each containing the details
                           of a product.

    Example:
        products_dto = await get_all_products_service()
        for product in products_dto:
            print(f"Product: {product.name} - Price: {product.price}")
    """
    products = await get_all_products_repo()
    return [ProductDto.from_entity(entity) for entity in products]
