# FastAPI Learning 

FastAPI Learning is basically my Github Repository containing multiple folders of projects which dealing with building REST APIs using FastAPI.

## Folders:

- basic_one and replica_api folders consists of Python scripts using which you can learn how to build CRUD API.
- pydantic_api folder deals with building CRUD API but using Pydantic library for data validation.

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
