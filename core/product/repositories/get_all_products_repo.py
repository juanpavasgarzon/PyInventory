from typing import List

from core.product.entities.product import Product


async def get_all_products_repo() -> List[Product]:
    """
    Retrieves all products from the database.

    This asynchronous function queries the database and returns a list of
    all the products in the 'products' collection. If no products are
    found, it returns an empty list.

    Returns:
        List[Product]: A list of all products stored in the database.
                        If no products are found, an empty list is returned.

    Example:
        products = await get_all_products_repo()
        for product in products:
            print(product.name)
    """
    return await Product.objects.all()
