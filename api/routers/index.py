from . import customer, ingredient, menu_item, menu_item_ingredient, order, order_item, payment, promotion, review


def load_routes(app):
    app.include_router(customer.router)
    app.include_router(ingredient.router)
    app.include_router(menu_item.router)
    app.include_router(menu_item_ingredient.router)
    app.include_router(order.router)
    app.include_router(order_item.router)
    app.include_router(payment.router)
    app.include_router(promotion.router)
    app.include_router(review.router)
