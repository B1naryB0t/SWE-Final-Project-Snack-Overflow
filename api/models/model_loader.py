from . import customer

from ..dependencies.database import engine


def index():
    customer.Base.metadata.create_all(engine)
