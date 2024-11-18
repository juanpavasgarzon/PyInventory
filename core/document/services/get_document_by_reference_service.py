from typing import Optional

from core.document.dtos.document_dto import DocumentDto
from core.document.repositories.get_document_by_reference_repo import get_document_by_reference_repo


async def get_document_by_reference_service(reference: str) -> Optional[DocumentDto]:
    document = await get_document_by_reference_repo(reference)
    if document is None:
        return None
    return DocumentDto.from_entity(document)
