# FastAPI Learning 

FastAPI Learning is basically my Github Repository containing multiple folders of projects which dealing with building REST APIs using FastAPI.

## Folders:

### FastAPI Concepts

- [basic_one](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/basic_one) and [replica_api](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/replica_api) folders consists of Python scripts using which you can learn how to build CRUD API.
- [pydantic_api](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/pydantic_api) folder deals with building CRUD API but using Pydantic library for data validation.
- [responsemodel](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/responsemodel) folder deals with use of Response Model which helps in displaying only required content.
- [httpexception](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/httpexception) folder introduces you to use raising HTTP Exceptions and understand how to use status code
- [customerrors](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/customerrors) folder consist of using customized errors.
- [dependencyinjection](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/dependencyinjection) folder deals with dependency injection.
- [middleware](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/middleware) folder deals with basic request logging middleware.
- [async_api](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/async_api) folder distinguishes between synchronous and asynchronous operations.

### Database Operations

- [basic_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/basic_db) folder will introduce you to connect with database. `(Connection)`
- [sqla_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/sqla_db) and [sqla_db2](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/sqla_db2) folders will help you to setup SQLAlchemy.  `(SQLAlchemy Setup)`
- [insert_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/insert_db) folder deals with inserting elements in database.  `(Create data in SQLAlchemy)`
- [read_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/read_db) folder deals with reading the data stored in the database by reading all the data or by reading specific data. `(Read data in SQLAlchemy)`
- [update_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/update_db) folder deals with updating the specific stored data in the database. `(Update data in SQLAlchemy)`
- [delete_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/insert_db) and [crud_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/crud_db) folder deals with deleting the specified data from the database, completing our basic CRUD Api using Database. `(Delete data in SQLAlchemy) / (Basic CRUD API)`

### Authentication

- [jwt_auth_intro](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/jwt_auth_intro) folder introduces you to how JWT Authentication works along with using it in API for secure routes `(Creating and Verifying JSON Web Tokens)`
- [jose_auth](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/jose_auth) folder deals with JWT Authentication using python-jose library `(JWT Authentication using python-jose)`

## Setup 

1. Python 3.13 or newer
2. Create a Virtual Environment

```
python -m venv .venv
```
3. Install the required dependencies (requirements.txt file is there in almost all the folders)
- If there is no requirement.txt file then install following package- (fastapi,uvicorn,sqlalchemy)
```
pip install -r requirements.txt
```

## Usage

```
uvicorn file_name:app --reload
```

To check whether the API is functioning, use tools like Postman or ThunderClient extension on VSCode.

You can also test the API on Swagger Docs
After running the file, you can visit this link to Swagger Docs of each API.
```
http://127.0.0.1/route_name/docs
```

