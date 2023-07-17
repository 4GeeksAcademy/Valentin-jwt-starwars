import os
from flask_admin import Admin
from models import db, User, Address, Planet, Character, Vehicle, FavoriteList
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
 # Add Address model to the admin
    admin.add_view(ModelView(Address, db.session))

     # Add Planet model to the admin
    admin.add_view(ModelView(Planet, db.session))

    # Add Character model to the admin
    admin.add_view(ModelView(Character, db.session))

    # Add Vehicle model to the admin
    admin.add_view(ModelView(Vehicle, db.session))

    # Add Character_Favorite_List model to the admin
    admin.add_view(ModelView(FavoriteList, db.session))
