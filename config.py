import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FOURSQUARE_API_KEY = os.getenv('fsq3PIeaeuj46viOVT3jFRebvtQfmDoIp6DxIBponhp3xaA=')
