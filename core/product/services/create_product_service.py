from core.product.dtos.create_product_dto import CreateProductDto
from core.product.dtos.product_dto import ProductDto
from core.product.repositories.create_product_repo import create_product_repo


async def add_product_service(dto: CreateProductDto) -> ProductDto:
    """
    Service method to create a new product.

    This method receives a `CreateProductDto` object, creates a new product in the database
    using the `create_product_repo` function, and returns the created product as a `ProductDto`
    instance.

    Args:
        dto (CreateProductDto): The DTO containing the product's details to be created.

    Returns:
        ProductDto: The `ProductDto` instance representing the newly created product.

    Example:
        new_product_dto = CreateProductDto(code="P001", name="New Product", price=19.99)
        created_product = await add_product_service(new_product_dto)
        print(f"Created Product: {created_product.name} - Price: {created_product.price}")
    """
    product = await create_product_repo(dto)
    return ProductDto.from_entity(product)
