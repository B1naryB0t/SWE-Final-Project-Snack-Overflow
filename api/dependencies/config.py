import os


class Config:
	app_host = "localhost"
	app_port = 8000


APP_ENV = os.getenv("APP_ENV", "dev")

if APP_ENV == "test":
	DATABASE_URL = "mysql+pymysql://user:password@host:3306/test_db"
else:
	DATABASE_URL = "mysql+pymysql://user:password@host:3306/app_db"
