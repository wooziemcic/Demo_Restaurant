from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    allergies = db.Column(db.Text, nullable=True)  # Store allergies as a comma-separated string
    preferences = db.Column(db.Text, nullable=True)  # Store preferences as a comma-separated string

    def __repr__(self):
        return f"<User {self.username}>"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    menu = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return f"<Restaurant {self.name}>"

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    allergens = db.Column(db.Text, nullable=True)  # Comma-separated allergens
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<MenuItem {self.name} - {self.restaurant.name}>"
