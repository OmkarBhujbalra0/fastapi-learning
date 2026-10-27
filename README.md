# FastAPI Learning 

FastAPI Learning is basically my Github Repository containing multiple folders of projects which dealing with building REST APIs using FastAPI.

## Folders:

### FastAPI Concepts

| Folder Name | Concepts |
|:-----------:|:--------:|
| [basic_one](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/basic_one) and [replica_api](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/replica_api) | CRUD API using list, HTTP Methods |
| [pydanticplusapi](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/pydanticplusapi) | Data Validation using Pydantic Model |
| [responsemodel](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/responsemodel) | Response Model |
| [httpexception](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/httpexception) | HTTP Exception and Status codes |
| [customerrors](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/customerrors) | Custom Errors |
| [dependencyinjection](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/dependencyinjection) | Dependency Injection using Header() and Depends() |
| [middleware](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/middleware) | Basic Request Logging Middleware |
| [async_api](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/async_api) | Difference between synchronous and asynchronous tasks |
| [file_uploads](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/file_uploads) | File Upload + Static Files |
| [cors_middleware](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/cors_middleware) | CORS Implementation |
| [env_files](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/env_files) | Environment Variables |
| [testing](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/fastapi_concepts/testing) | Testing |

### Database Operations

| Folder Name | Concepts |
|:-----------:|:--------:|
| [basic_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/basic_db) | Connect with Database |
| [sqla_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/sqla_db) and [sqla_db2](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/sqla_db2) | SQLAlchemy Setup |
| [insert_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/insert_db) | Create Data in SQLAlchemy |
| [read_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/read_db) | Read Data in SQLAlchemy |
| [update_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/update_db) | Update Data in SQLAlchemy |
| [delete_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/insert_db) and [crud_db](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/database_operations/crud_db) | Delete Data in SQLAlchemy / Basic CRUD API |

### Authentication

| Folder Name | Concepts |
|:-----------:|:--------:|
| [jwt_auth_intro](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/authentication_concepts/jwt_auth_intro) |  Creating and Verifying JSON Web Tokens using PyJWT |
| [jose_auth](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/authentication_concepts/jose_auth) | JWT Authentication using python-jose |
| [oauth2](https://github.com/OmkarBhujbalra0/fastapi-learning/tree/main/authentication_concepts/oauth2) | JWT + Oauth2 Authentication |

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

