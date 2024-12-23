from app import create_app, db
from app.models import User, Restaurant, MenuItem
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Add sample users
    user1 = User(username="john_doe", email="john@example.com", password="password", allergies="peanuts", preferences="vegan")
    user2 = User(username="jane_doe", email="jane@example.com", password="password", allergies="gluten", preferences="vegetarian")

    # Add sample restaurants
    restaurant1 = Restaurant(name="The Vegan Spot", address="123 Greenway Blvd", latitude=40.7128, longitude=-74.0060)
    restaurant2 = Restaurant(name="Burger Bliss", address="456 Meat St", latitude=40.7130, longitude=-74.0070)

    # Add sample menu items
    menu_item1 = MenuItem(name="Vegan Burger", description="A delicious plant-based burger.", price=12.99, allergens="", restaurant=restaurant1)
    menu_item2 = MenuItem(name="Gluten-Free Salad", description="Fresh greens with a gluten-free dressing.", price=9.99, allergens="nuts", restaurant=restaurant1)
    menu_item3 = MenuItem(name="Cheeseburger", description="Classic beef burger with cheese.", price=11.99, allergens="dairy,gluten", restaurant=restaurant2)

    # Commit to database
    db.session.add_all([user1, user2, restaurant1, restaurant2, menu_item1, menu_item2, menu_item3])
    db.session.commit()

    print("Database seeded!")
