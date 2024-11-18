import mongoengine as me


def connect_to_mongo():
    """
    Establishes a connection to the MongoDB database.

    This function connects to a MongoDB instance using the provided connection string and connects to the
    `inventory` database with the alias `inventory`. The connection uses MongoDB Atlas as the host for the
    database.

    Args: None

    Returns: None

    Raises:
        mongoengine.errors.ConnectionError: If the connection to the MongoDB database fails.

    Example:
        connect_to_mongo()  # Establishes a connection to the 'inventory' database.
    """
    me.connect(db="inventory", alias='inventory', host="mongodb+srv://root:root@cluster0.mbcxo.mongodb.net/")
