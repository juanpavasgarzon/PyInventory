from contextlib import asynccontextmanager

import mongoengine as me
from fastapi import FastAPI

from infrastructure.database import connect_to_mongo


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Context manager that manages the lifecycle of the MongoDB connection in a FastAPI application.

    This function is used as the `lifespan` parameter in the FastAPI application, ensuring that the MongoDB
    connection is established when the application starts and disconnected when the application shuts down.

    Args:
        _app (FastAPI): The FastAPI application instance. This is passed automatically by FastAPI when
                         using the `lifespan` context manager.

    Yields:
        None: The function doesn't return anything but ensures the MongoDB connection is available during
              the lifespan of the FastAPI app.

    Raises:
        mongoengine.errors.ConnectionError: If the connection to MongoDB fails during startup.

    Example:
        app = FastAPI(lifespan=lifespan)
        # This sets up the MongoDB connection at the start and closes it when the app shuts down.
    """
    connect_to_mongo()
    yield
    me.disconnect(alias="inventory")
