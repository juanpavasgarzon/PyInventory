from typing import Optional

from core.product.entities.product import Product


async def get_product_by_id_repo(product_id: str) -> Optional[Product]:
    """
    Retrieves a product by its unique identifier.

    This asynchronous function queries the database for a product using
    its unique `product_id`. If the product exists, it will return the
    corresponding `Product` entity. If the product is not found, it will
    return None.

    Args:
        product_id (str): The unique identifier of the product to retrieve.

    Returns:
        Optional[Product]: The product object if found, otherwise None
                            if no product with the given id exists.

    Example:
        product = await get_product_by_id_repo("12345")
        if product:
            print(product.name)
        else:
            print("Product not found.")
    """
    return await Product.objects(id=product_id).first()
