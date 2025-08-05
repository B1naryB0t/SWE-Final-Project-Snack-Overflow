from .dependencies.database import SessionLocal
from .models.customer import Customer
from .models.ingredient import Ingredient
from .models.menu_item import MenuItem
from .models.menu_item_ingredient import MenuItemIngredient
from .models.order import Order
from .models.payment import Payment
from .models.promotion import Promotion
from .models.review import Review
from datetime import datetime

def seed_if_needed():
    db = SessionLocal()
    if db.query(Customer).count() == 0:
        alice = Customer(name="Alice", email="alice@example.com", phone="1234567890")
        bob = Customer(name="Bob", email="bob@example.com", phone="9876543210")
        carol = Customer(name="Carol", email="carol@example.com", phone="5551234567")
        dave = Customer(name="Dave", email="dave@example.com", phone="5559876543")
        db.add_all([alice, bob, carol, dave])
        db.commit()
        db.refresh(alice)
        db.refresh(bob)
        db.refresh(carol)
        db.refresh(dave)

        lettuce = Ingredient(name="Lettuce", quantity=100.0, unit="grams")
        tomato = Ingredient(name="Tomato", quantity=80.0, unit="grams")
        chicken = Ingredient(name="Chicken", quantity=200.0, unit="grams")
        cheese = Ingredient(name="Cheese", quantity=150.0, unit="grams")
        db.add_all([lettuce, tomato, chicken, cheese])
        db.commit()
        db.refresh(lettuce)
        db.refresh(tomato)
        db.refresh(chicken)
        db.refresh(cheese)

        caesar = MenuItem(name="Caesar Salad", category="Appetizer", price=7.50, calories=250)
        blt = MenuItem(name="BLT Sandwich", category="Main", price=10.00, calories=500)
        chicken_wrap = MenuItem(name="Chicken Wrap", category="Main", price=9.00, calories=400)
        cheese_plate = MenuItem(name="Cheese Plate", category="Appetizer", price=6.00, calories=300)
        db.add_all([caesar, blt, chicken_wrap, cheese_plate])
        db.commit()
        db.refresh(caesar)
        db.refresh(blt)
        db.refresh(chicken_wrap)
        db.refresh(cheese_plate)

        db.add_all([
            MenuItemIngredient(menu_item_id=caesar.id, ingredient_id=lettuce.id, quantity=10.0),
            MenuItemIngredient(menu_item_id=caesar.id, ingredient_id=chicken.id, quantity=20.0),
            MenuItemIngredient(menu_item_id=blt.id, ingredient_id=lettuce.id, quantity=5.0),
            MenuItemIngredient(menu_item_id=blt.id, ingredient_id=tomato.id, quantity=10.0),
            MenuItemIngredient(menu_item_id=chicken_wrap.id, ingredient_id=chicken.id, quantity=30.0),
            MenuItemIngredient(menu_item_id=chicken_wrap.id, ingredient_id=lettuce.id, quantity=8.0),
            MenuItemIngredient(menu_item_id=cheese_plate.id, ingredient_id=cheese.id, quantity=25.0),
            MenuItemIngredient(menu_item_id=cheese_plate.id, ingredient_id=tomato.id, quantity=5.0),
        ])
        db.commit()

        order1 = Order(
            date=datetime.now(),
            status="pending",
            total=17.50,
            order_type="takeout",
            tracking_number=123456,
            customer_id=alice.id
        )
        order2 = Order(
            date=datetime.now(),
            status="completed",
            total=10.00,
            order_type="dine-in",
            tracking_number=654321,
            customer_id=bob.id
        )
        order3 = Order(
            date=datetime.now(),
            status="completed",
            total=9.00,
            order_type="delivery",
            tracking_number=789012,
            customer_id=carol.id
        )
        order4 = Order(
            date=datetime.now(),
            status="pending",
            total=6.00,
            order_type="takeout",
            tracking_number=210987,
            customer_id=dave.id
        )
        db.add_all([order1, order2, order3, order4])
        db.commit()
        db.refresh(order1)
        db.refresh(order2)
        db.refresh(order3)
        db.refresh(order4)

        payment1 = Payment(order_id=order1.id, status="paid", type="credit_card", total=17.50, transaction_id="txn_001")
        payment2 = Payment(order_id=order2.id, status="paid", type="cash", total=10.00, transaction_id="txn_002")
        payment3 = Payment(order_id=order3.id, status="paid", type="credit_card", total=9.00, transaction_id="txn_003")
        payment4 = Payment(order_id=order4.id, status="pending", type="cash", total=6.00, transaction_id="txn_004")
        db.add_all([payment1, payment2, payment3, payment4])
        db.commit()

        promo = Promotion(code="WELCOME25", discount_amount=25.0, expiration_date=datetime(2025, 12, 31))
        db.add(promo)
        db.commit()

        review1 = Review(customer_id=alice.id, menu_item_id=caesar.id, rating=4, comment="Great salad!")
        review2 = Review(customer_id=bob.id, menu_item_id=blt.id, rating=5, comment="Best sandwich ever!")
        review3 = Review(customer_id=carol.id, menu_item_id=chicken_wrap.id, rating=3, comment="Pretty good wrap.")
        review4 = Review(customer_id=dave.id, menu_item_id=cheese_plate.id, rating=5, comment="Loved the cheese plate!")
        db.add_all([review1, review2, review3, review4])
        db.commit()
    db.close()