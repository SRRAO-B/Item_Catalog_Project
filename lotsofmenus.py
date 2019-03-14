from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Category, Base, Item

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


iuser =User(name="sundar b", email="sundar.semafor@gmail.com", picture="https://lh6.googleusercontent.com/-m3_SJRuvcL4/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rfviWiC5j1S09MmMqAXR-D8dUeRiQ/mo/photo.jpg")
session.add(iuser)
session.commit()

# ItemCatalog for Categorys
icategory = Category(name="PEDEGO", user=iuser)
session.add(icategory)
session.commit()


iItem = Item(name="PEDEGO INTERCEPTOR", description="The most comfortable and user-friendly electric bikes on Earth", price="$1399.00", category=icategory)
session.add(iItem)
session.commit()





user1 =User(name="Sundar Rao", email="srraob@gmail.com", picture="https://lh6.googleusercontent.com/-eE6haWan9Rk/AAAAAAAAAAI/AAAAAAAAAAA/TUaBrQ5aMEo/photo.jpg")
session.add(user1)
session.commit()

# ItemCatalog for Categorys
category1 = Category(name="E-MOJO", user=user1)

session.add(category1)
session.commit()

Item1 = Item(name="E-MOJO WILDCAT", description="Pavement, dirt, parks or trails, the lightweight alloy rigid frame paired with a torquey 48-volt 500-watt Bafang electric motor that provides the boost you need to push your limits", price="$1299.00", category=category1)

session.add(Item1)
session.commit()


Item11 = Item(name="E-MOJO Hurricane Item", description="The E-MOJO Hurricane Item has the classic beach cruiser look but packs a punch.", price="$1499.00", category=category1)

session.add(Item11)
session.commit()





print "added menu items!"
