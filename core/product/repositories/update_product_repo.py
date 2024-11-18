from typing import Optional

from core.product.dtos.update_product_dto import UpdateProductDto
from core.product.entities.product import Product


async def update_product_repo(product_id: str, dto: UpdateProductDto) -> Optional[Product]:
    """
    Updates an existing product in the database using the provided data.

    This function retrieves a product by its ID and updates its attributes
    (code, name, price, description) with the data provided in the
    `UpdateProductDto`. If the product is found, it will be saved with
    the updated values. If the product does not exist, it will return None.

    Args:
        product_id (str): The unique identifier of the product to update.
        dto (UpdateProductDto): A DTO (Data Transfer Object) containing the
                                 updated product information.

    Returns:
        Optional[Product]: The updated product object if the product was found
                            and updated, otherwise None if the product was not
                            found in the database.

    Example:
        If the product with ID '123' exists and the dto contains the updated
        information, the method will update the product and return the updated
        product entity.

        updated_product = update_product_repo('123', UpdateProductDto(code="ABC123", name="New Product", price=15.99))
        print(updated_product.name)
    """
    product = await Product.objects(id=product_id).first()
    if product:
        product.code = dto.code
        product.name = dto.name
        product.price = dto.price
        product.description = dto.description
        product.save()

    return product
