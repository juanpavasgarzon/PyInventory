from fastapi import APIRouter

from infrastructure.auto_import import auto_import_endpoints

document_router = APIRouter(prefix="/document", tags=["Document"])

auto_import_endpoints("core.document.endpoints")
