from fastapi import FastAPI

from core.document.router import document_router
from core.product.router import product_router
from infrastructure.lifespan import lifespan

"""
FastAPI application that includes product and document routers.

This FastAPI application instance includes two routers for handling product and document-related
endpoints. The application is configured with a custom lifespan, which manages the startup and
shutdown events. The `product_router` is responsible for product-related API operations, while
the `document_router` handles document-related functionalities.

The application serves as the entry point to expose APIs for product management and document
handling within the system.

Attributes:
    app (FastAPI): The main FastAPI application instance, configured with a custom lifespan
                   and two included routers (product_router and document_router).

Usage:
    To run the application, use the following command in the terminal:

    `uvicorn main:app --reload`

    This will start the FastAPI application with automatic reloading enabled.

Routers Included:
    - `product_router`: Handles endpoints related to product management, including creating,
      retrieving, and updating products.
    - `document_router`: Manages document-related endpoints, including operations for handling
      and manipulating documents.

Lifespan:
    - The `lifespan` parameter manages startup and shutdown events for the FastAPI application,
      ensuring that necessary tasks are performed before the app starts and after it shuts down.
"""

app = FastAPI(lifespan=lifespan)

app.include_router(product_router)
app.include_router(document_router)

for route in app.routes:
    print(f"Route: {route.path}, Methods: {route.methods}")