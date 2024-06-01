# Tutorial to build python api with Poetry
Here’s a step-by-step tutorial to build a Python API using Poetry for dependency management and packaging:

### Step 1: Install Poetry

First, ensure Poetry is installed. You can install it by running the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your PATH by following the instructions provided after installation, then verify the installation:

```sh
poetry --version
```

### Step 2: Create a New Project

Create a new directory for your project and navigate to it:

```sh
mkdir my_api_project
cd my_api_project
```

Initialize a new Poetry project:

```sh
poetry init --no-interaction
```

This command will create a `pyproject.toml` file in your project directory.

### Step 3: Add Dependencies

You will need a web framework to build your API. FastAPI is a popular choice for building APIs in Python.

Add FastAPI and Uvicorn (an ASGI server) as dependencies:

```sh
poetry add fastapi uvicorn
```

### Step 4: Create the API

Create a new directory for your API code and navigate to it:

```sh
mkdir app
cd app
```

Create a file named `main.py` and add the following code to define a simple FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/status")
def read_status():
    return {"status": "ok"}
```

### Step 5: Configure the Entry Point

In the root directory of your project, create a file named `run.sh` to run your FastAPI application with Uvicorn:

```sh
#!/bin/bash

poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Make this script executable:

```sh
chmod +x run.sh
```

### Step 6: Install Dependencies and Run the Application

Install your project's dependencies:

```sh
poetry install
```

Run your API:

```sh
./run.sh
```

Your API will be accessible at `http://localhost:8000`. You can check the status endpoint by navigating to `http://localhost:8000/status`.

### Step 7: Project Structure

Your project directory should now look like this:

```
my_api_project/
│
├── app/
│   └── main.py
│
├── poetry.lock
├── pyproject.toml
├── run.sh
```

### Step 8: Testing Your API

You can test your API using `curl` or any API client like Postman. For example, to check the root endpoint, run:

```sh
curl http://localhost:8000/
```

You should receive a response:

```json
{"message": "Hello World"}
```

To check the status endpoint:

```sh
curl http://localhost:8000/status
```

You should receive a response:

```json
{"status": "ok"}
```

### Conclusion

You've successfully set up a Python API using FastAPI and Poetry. This structure allows you to manage dependencies easily and ensures your project is well-organized. You can extend this API by adding more endpoints and functionalities as needed.


## Test
```
curl -i -X GET http://localhost:8001/items
curl -i -X GET http://localhost:8001/items/665971fbdc93f9cea526ee2c
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009", "description": "Item Description"}' http://localhost:8001/items
// other
curl -i -X DELETE http://localhost:8001/items/5069b47aa892630aae059584
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://localhost:8001/items
curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://localhost:8001/items/5069b47aa892630aae059584
```