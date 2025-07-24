from . import customer, order, order_item, payment, menu_item, menu_item_ingredient, ingredient, review, promotion

from ..dependencies.database import engine


def index():
	customer.Base.metadata.create_all(engine)
	order.Base.metadata.create_all(engine)
	order_item.Base.metadata.create_all(engine)
	payment.Base.metadata.create_all(engine)
	menu_item.Base.metadata.create_all(engine)
	menu_item_ingredient.Base.metadata.create_all(engine)
	ingredient.Base.metadata.create_all(engine)
	review.Base.metadata.create_all(engine)
	promotion.Base.metadata.create_all(engine)
