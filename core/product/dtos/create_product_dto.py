from typing import Optional

from pydantic import BaseModel


class CreateProductDto(BaseModel):
    """
    Data Transfer Object (DTO) for creating a product.

    This class defines the data structure used to create a new product. It
    includes attributes for the product's code, name, price, and an optional
    description. This DTO is validated using Pydantic to ensure that the
    provided data conforms to the required types and constraints.

    Attributes:
        code (str): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        description (Optional[str], optional): A brief description of the product.
                                              Defaults to None if not provided.

    Example:
        dto = CreateProductDto(code="P123", name="Sample Product", price=15.99, description="This is a sample product.")
    """

    code: str
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        """
        Pydantic configuration for this model.

        Enables the use of ORM (Object-Relational Mapping) to convert database
        model instances to Pydantic model instances. This is useful when
        interacting with databases directly.

        Attributes:
            from_orm (bool): Enables ORM support for automatic conversion of
                              database models to this DTO.
        """
        from_orm = True
