from . import customer


def load_routes(app):
    app.include_router(customer.router)
