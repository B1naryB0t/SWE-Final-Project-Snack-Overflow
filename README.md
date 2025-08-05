# ITSC-3155 Final Project: Restaurant Management System API

A RESTful API for managing a restaurant's menu, orders, and customers using FastAPI and an SQL database.

## Setup Instructions
A Python environment is required. 

### Install the necessary packages:
* `pip install -r requirements.txt`

### Configure Database:
By default, the API uses SQLite. You can change the database URL in `api/database.py` to connect to a different SQL database.
Example for MySQL:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/db_name"
```

### Run the server:
`uvicorn api.main:app --reload`

### Test API via built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)