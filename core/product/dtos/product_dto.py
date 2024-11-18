from typing import Optional

from pydantic import BaseModel

from core.product.entities.product import Product


class ProductDto(BaseModel):
    """
    Data Transfer Object (DTO) for representing product data.

    This class is used to transfer product data, including attributes such as
    product id, code, name, price, and an optional description. It is a Pydantic
    model that provides automatic data validation and conversion from ORM models
    (such as MongoDB documents) to a Python object.

    Attributes:
        id (str): The unique identifier for the product.
        code (str): The product's unique code.
        name (str): The name of the product.
        price (float): The price of the product.
        description (Optional[str], optional): A brief description of the product.
                                              Defaults to None if not provided.

    Example:
        product_dto = ProductDto(id="123", code="P123", name="Sample Product", price=19.99, description="This is a sample product.")
    """

    id: str
    code: str
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        """
        Pydantic configuration for this model.

        Enables the use of ORM (Object-Relational Mapping) for automatic conversion
        of database model instances (such as MongoDB documents) to Pydantic model
        instances. This configuration makes it easy to work with data returned
        from a database query.

        Attributes:
            from_orm (bool): Allows the automatic conversion of ORM models to Pydantic
                              models using the ORM's data fields.
        """
        from_orm = True

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductDto":
        """
        Class method to convert a Product entity into a ProductDto.

        This method creates an instance of ProductDto from a Product entity,
        typically an ORM model instance, and maps the relevant fields from
        the entity to the DTO.

        Args:
            entity (Product): The Product entity to convert.

        Returns:
            ProductDto: A DTO representation of the Product entity.

        Example:
            product_dto = ProductDto.from_entity(product_entity)
        """
        return cls(
            id=str(entity.id),
            code=entity.code,
            name=entity.name,
            price=entity.price,
            description=entity.description,
        )
