from datetime import datetime

from .dependencies.database import SessionLocal
from .models.customer import Customer
from .models.ingredient import Ingredient
from .models.menu_item import MenuItem
from .models.menu_item_ingredient import MenuItemIngredient
from .models.order import Order
from .models.payment import Payment
from .models.promotion import Promotion
from .models.review import Review


def seed_if_needed():
	db = SessionLocal()
	if db.query(Customer).count() == 0:
		alice = Customer(name="Alice", email="alice@example.com", phone="1234567890")
		bob = Customer(name="Bob", email="bob@example.com", phone="9876543210")
		carol = Customer(name="Carol", email="carol@example.com", phone="5551234567")
		dave = Customer(name="Dave", email="dave@example.com", phone="5559876543")
		eve = Customer(name="Eve", email="eve@example.com", phone="2223334444")
		frank = Customer(name="Frank", email="frank@example.com", phone="3334445555")
		db.add_all([alice, bob, carol, dave, eve, frank])
		db.commit()
		db.refresh(alice)
		db.refresh(bob)
		db.refresh(carol)
		db.refresh(dave)
		db.refresh(eve)
		db.refresh(frank)

		lettuce = Ingredient(name="Lettuce", quantity=100.0, unit="grams")
		tomato = Ingredient(name="Tomato", quantity=80.0, unit="grams")
		chicken = Ingredient(name="Chicken", quantity=200.0, unit="grams")
		cheese = Ingredient(name="Cheese", quantity=150.0, unit="grams")
		bacon = Ingredient(name="Bacon", quantity=120.0, unit="grams")
		tortilla = Ingredient(name="Tortilla", quantity=60.0, unit="grams")
		db.add_all([lettuce, tomato, chicken, cheese, bacon, tortilla])
		db.commit()

		caesar = MenuItem(name="Caesar Salad", category="Appetizer", price=7.50, calories=250, tags="vegetarian")
		blt = MenuItem(name="BLT Sandwich", category="Main", price=10.00, calories=500, tags="spicy")
		chicken_wrap = MenuItem(name="Chicken Wrap", category="Main", price=9.00, calories=400, tags="spicy")
		cheese_plate = MenuItem(name="Cheese Plate", category="Appetizer", price=6.00, calories=300, tags="vegetarian")
		bacon_wrap = MenuItem(name="Bacon Wrap", category="Main", price=8.50, calories=450, tags="spicy,vegetarian")
		veggie_plate = MenuItem(name="Veggie Plate", category="Appetizer", price=5.50, calories=200, tags="vegetarian")
		db.add_all([caesar, blt, chicken_wrap, cheese_plate, bacon_wrap, veggie_plate])
		db.commit()

		db.add_all([
			MenuItemIngredient(menu_item_id=caesar.id, ingredient_id=lettuce.id, quantity=10.0),
			MenuItemIngredient(menu_item_id=caesar.id, ingredient_id=chicken.id, quantity=20.0),
			MenuItemIngredient(menu_item_id=blt.id, ingredient_id=lettuce.id, quantity=5.0),
			MenuItemIngredient(menu_item_id=blt.id, ingredient_id=tomato.id, quantity=10.0),
			MenuItemIngredient(menu_item_id=blt.id, ingredient_id=bacon.id, quantity=15.0),
			MenuItemIngredient(menu_item_id=chicken_wrap.id, ingredient_id=chicken.id, quantity=30.0),
			MenuItemIngredient(menu_item_id=chicken_wrap.id, ingredient_id=tortilla.id, quantity=12.0),
			MenuItemIngredient(menu_item_id=cheese_plate.id, ingredient_id=cheese.id, quantity=25.0),
			MenuItemIngredient(menu_item_id=cheese_plate.id, ingredient_id=tomato.id, quantity=5.0),
			MenuItemIngredient(menu_item_id=bacon_wrap.id, ingredient_id=bacon.id, quantity=20.0),
			MenuItemIngredient(menu_item_id=bacon_wrap.id, ingredient_id=tortilla.id, quantity=10.0),
			MenuItemIngredient(menu_item_id=veggie_plate.id, ingredient_id=lettuce.id, quantity=8.0),
			MenuItemIngredient(menu_item_id=veggie_plate.id, ingredient_id=tomato.id, quantity=8.0),
		])
		db.commit()

		order1 = Order(date=datetime(2025, 8, 1, 12, 0, 0), status="pending", total=17.50, order_type="takeout",
		               tracking_number=123456, customer_id=alice.id)
		order2 = Order(date=datetime(2025, 8, 2, 13, 0, 0), status="completed", total=10.00, order_type="dine-in",
		               tracking_number=654321, customer_id=bob.id)
		order3 = Order(date=datetime(2025, 8, 3, 14, 0, 0), status="completed", total=9.00, order_type="delivery",
		               tracking_number=789012, customer_id=carol.id)
		order4 = Order(date=datetime(2025, 8, 4, 15, 0, 0), status="pending", total=6.00, order_type="takeout",
		               tracking_number=210987, customer_id=dave.id)
		order5 = Order(date=datetime(2025, 8, 5, 16, 0, 0), status="completed", total=8.50, order_type="dine-in",
		               tracking_number=345678, customer_id=eve.id)
		order6 = Order(date=datetime(2025, 8, 6, 17, 0, 0), status="completed", total=12.00, order_type="delivery",
		               tracking_number=456789, customer_id=frank.id)
		db.add_all([order1, order2, order3, order4, order5, order6])
		db.commit()

		payment1 = Payment(order_id=order1.id, status="paid", type="credit_card", total=17.50, transaction_id="txn_001")
		payment2 = Payment(order_id=order2.id, status="paid", type="cash", total=10.00, transaction_id="txn_002")
		payment3 = Payment(order_id=order3.id, status="paid", type="credit_card", total=9.00, transaction_id="txn_003")
		payment4 = Payment(order_id=order4.id, status="pending", type="cash", total=6.00, transaction_id="txn_004")
		payment5 = Payment(order_id=order5.id, status="paid", type="credit_card", total=8.50, transaction_id="txn_005")
		payment6 = Payment(order_id=order6.id, status="paid", type="cash", total=12.00, transaction_id="txn_006")
		db.add_all([payment1, payment2, payment3, payment4, payment5, payment6])
		db.commit()

		review1 = Review(customer_id=alice.id, menu_item_id=caesar.id, rating=4, comment="Great salad!")
		review2 = Review(customer_id=bob.id, menu_item_id=blt.id, rating=5, comment="Best sandwich ever!")
		review3 = Review(customer_id=carol.id, menu_item_id=chicken_wrap.id, rating=3, comment="Pretty good wrap.")
		review4 = Review(customer_id=dave.id, menu_item_id=cheese_plate.id, rating=5, comment="Loved the cheese plate!")
		review5 = Review(customer_id=eve.id, menu_item_id=bacon_wrap.id, rating=4, comment="Bacon wrap was tasty!")
		review6 = Review(customer_id=frank.id, menu_item_id=veggie_plate.id, rating=2, comment="Veggie plate was okay.")
		db.add_all([review1, review2, review3, review4, review5, review6])
		db.commit()

		promo = Promotion(code="WELCOME25", discount_amount=25.0, expiration_date=datetime(2025, 12, 31))
		db.add(promo)
		db.commit()

	db.close()
