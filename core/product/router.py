from fastapi import APIRouter

from infrastructure.auto_import import auto_import_endpoints

product_router = APIRouter(prefix="/product", tags=["Product"])

auto_import_endpoints("core.product.endpoints")
