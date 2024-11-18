from datetime import datetime, timezone
from typing import List

from core.counter.repositories.get_next_sequence_repo import get_next_sequence_repo
from core.document.entities.document import Document
from core.document.entities.document_item import DocumentItem
from core.product.entities.product import Product


async def create_document_repo(reference: str, concept: str, items: List[dict], description: str = None) -> Document:
    """
    Creates a new document with the provided reference, concept, items, and an optional description.

    This function creates a `Document` object by validating the items and associating each item with a
    `Product`. It then generates a consecutive number using a counter sequence, sets the document's
    datetime, and saves it to the database.

    Args:
        reference (str): The reference code for the document.
        concept (str): The concept or category for the document (e.g., sales, purchase).
        items (List[dict]): A list of dictionaries representing the document items. Each item should contain:
            - 'product_id' (str): The ID of the product.
            - 'quantity' (int): The quantity of the product in the document item.
        description (str, optional): A description of the document. Defaults to None.

    Raises:
        ValueError: If any product in the items list cannot be found by its ID.

    Returns:
        Document: The created document instance.

    Example:
        items = [
            {"product_id": "60b8fbd6b6a05a001f3db9d2", "quantity": 5},
            {"product_id": "60b8fbd6b6a05a001f3db9d3", "quantity": 3}
        ]
        document = await create_document_repo("INV-12345", "sale", items)

    """
    document_items = []
    for item in items:
        product = await Product.objects(id=item['product_id']).first()
        if not product:
            raise ValueError(f"Product with ID {item['product_id']} not found")

        document_item = DocumentItem(product=product, quantity=item['quantity'], price=product.price)
        document_items.append(document_item)

    document = Document(
        reference=reference,
        concept=concept,
        description=description,
        items=document_items
    )

    document.consecutive = await get_next_sequence_repo(concept)
    document.datetime = datetime.now(timezone.utc)
    await document.save()

    return document
