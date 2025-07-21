from . import customer , ingredient , menuItem , menuItemIngredient , order , orderItem , payment , promotion , review


def load_routes(app):
    app.include_router(customer.router)
    app.include_router(ingredient.router)
    app.include_router(menuItem.router)
    app.include_router(menuItemIngredient.router)
    app.include_router(order.router)
    app.include_router(orderItem.router)
    app.include_router(payment.router)
    app.include_router(promotion.router)
    app.include_router(review.router)

