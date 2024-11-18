from typing import Optional

from core.document.entities.document import Document


async def get_document_by_reference_repo(reference: str) -> Optional[Document]:
    """
    Retrieves a document from the database by its reference.

    This function queries the `Document` collection using the provided reference to fetch the first
    document that matches the reference. If no matching document is found, it returns None.

    Args:
        reference (str): The reference code of the document to be fetched.

    Returns:
        Optional[Document]: The document matching the provided reference, or None if no such document is found.

    Example:
        document = get_document_by_reference_repo("INV-12345")
        if document is not None:
            print(document.reference)
        else:
            print("Document not found.")
    """
    return await Document.objects(reference=reference).first()
