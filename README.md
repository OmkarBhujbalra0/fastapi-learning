# FastAPI Learning 

FastAPI Learning is basically my Github Repository containing multiple folders of projects which dealing with building REST APIs using FastAPI.

## Folders:

- `basic_one` and `replica_api` folders consists of Python scripts using which you can learn how to build CRUD API.
- `pydantic_api` folder deals with building CRUD API but using Pydantic library for data validation.
- `responsemodel` folder deals with use of Response Model which helps in displaying only required content.
- `httpexception` folder introduces you to use raising HTTP Exceptions and understand how to use status code

## Setup 

1. Python 3.13 or newer
2. Create a Virtual Environment

```
python -m venv .venv
```
3. Install the required dependencies
```
pip install fastapi uvicorn
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

