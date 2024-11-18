from typing import Optional

from pydantic import BaseModel


class UpdateProductDto(BaseModel):
    """
    Data Transfer Object (DTO) for updating product details.

    This class is used to transfer updated product data. It is a Pydantic model
    that provides automatic data validation and conversion. This DTO is typically
    used when updating an existing product in the database.

    Attributes:
        code (str): The unique code of the product.
        name (str): The name of the product.
        price (float): The price of the product.
        description (Optional[str], optional): A brief description of the product.
                                              Defaults to None if not provided.

    Example:
        update_product_dto = UpdateProductDto(code="P123", name="Updated Product", price=29.99, description="Updated description.")
    """

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
