from mongoengine import Document as MongoDocument, StringField, DateTimeField, EmbeddedDocumentListField, IntField

from core.document.entities.document_item import DocumentItem


class Document(MongoDocument):
    """
    Represents a document in the inventory system.

    This class defines a document entity in the MongoDB database, which contains details such as the
    document's reference, consecutive number, datetime, concept, description, and a list of items.

    Attributes:
        reference (str): The unique reference of the document.
        consecutive (int): The consecutive number of the document.
        datetime (datetime): The date and time when the document was created.
        concept (str): The concept or purpose of the document.
        description (str, optional): A description of the document (optional).
        items (List[DocumentItem]): A list of items associated with the document.

    Methods:
        to_dict: Converts the Document instance to a dictionary representation.

    Example:
        document = Document(reference="DOC-001", consecutive=1, datetime=datetime.now(), concept="Purchase", items=[...])
        document_dict = document.to_dict()

    """
    meta = {
        'collection': 'documents',
        'db_alias': 'inventory'
    }

    reference = StringField(required=True)
    consecutive = IntField(required=True)
    datetime = DateTimeField(required=True)
    concept = StringField(required=True)
    description = StringField(required=False)
    items = EmbeddedDocumentListField(DocumentItem, required=True)

    def to_dict(self) -> dict:
        """
        Converts the Document instance to a dictionary representation.

        This method is used to convert the document object to a dictionary format, which can be used
        for serialization, e.g., returning the document data in an API response.

        Returns:
            dict: A dictionary containing the document's data.

        Example:
            {
                "id": "60c72b2f9b1d8f7c6d0f1a2d",
                "reference": "DOC-001",
                "consecutive": 1,
                "datetime": "2024-11-20T10:00:00",
                "concept": "Purchase",
                "description": "Order for office supplies",
                "items": [...]
            }

        """
        return {
            "id": str(self.id),
            "reference": self.reference,
            "consecutive": self.consecutive,
            "datetime": self.datetime,
            "concept": self.concept,
            "description": self.description,
            "items": [item.to_dict() for item in self.items],
        }
