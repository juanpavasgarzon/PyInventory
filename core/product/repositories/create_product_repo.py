from core.product.dtos.create_product_dto import CreateProductDto
from core.product.entities.product import Product


async def create_product_repo(dto: CreateProductDto) -> Product:
    """
    Creates a new product in the database from the provided DTO.

    This asynchronous function takes a `CreateProductDto` object, extracts
    the product details (code, name, price, description), creates a new
    product in the database, and returns the created product.

    Args:
        dto (CreateProductDto): The data transfer object containing the
                                 information needed to create the product.

    Returns:
        Product: The newly created product object.

    Example:
        dto = CreateProductDto(code="P123", name="Product Name", price=19.99, description="Product description")
        new_product = await create_product_repo(dto)
        print(new_product.name)
    """
    product = Product(code=dto.code, name=dto.name, price=dto.price, description=dto.description)
    await product.save()
    return product
