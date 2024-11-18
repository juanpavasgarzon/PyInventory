
Overview:
---------
PyInventory is a FastAPI-based application designed to manage inventory, including product and document handling.
It includes features for creating, retrieving, and updating products and documents, and integrates with MongoDB for data persistence.

Key Features:
-------------
- Product Management: APIs for managing product information.
- Document Management: APIs for handling inventory documents with items.
- MongoDB Integration: Uses MongoDB as the database for persistence.
- Scalable Design: Modular and scalable design for easy feature expansion.

Project Structure:
------------------
- core: Contains the main business logic, services, and data transfer objects (DTOs).
- infrastructure: Includes configurations for database connections and lifespan management.
- main.py: Entry point for the FastAPI application.
- Makefile: Includes commands to set up and manage the project (e.g., creating a virtual environment).

Setup Instructions:
-------------------
1. Clone the repository:
   ```
   git clone <repository_url>
   cd PyInventory
   ```

2. Create and activate a virtual environment:
   ```
   make create_venv
   source .venv/bin/activate
   ```

3. Install project dependencies:
   ```
   make install
   ```

4. Start the application:
   ```
   make start
   ```

5. Access the application:
   - API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc Documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Key Commands:
-------------
- `make create_venv`: Creates a virtual environment for the project.
- `make install`: Installs dependencies from requirements.txt.
- `make start`: Starts the FastAPI application with Uvicorn.
- `make clean`: Removes the virtual environment.

Technologies Used:
------------------
- Python 3.10+
- FastAPI
- MongoDB
- Pydantic
- MongoEngine

Contributing:
-------------
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/<feature_name>`.
3. Commit your changes: `git commit -m 'Add feature <feature_name>'`.
4. Push to the branch: `git push origin feature/<feature_name>`.
5. Open a pull request.

License:
--------
This project is licensed under the MIT License. See the LICENSE file for details.

Support:
--------
For any issues or queries, please contact [your_email@example.com].
