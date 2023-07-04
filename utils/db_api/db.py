import tracemalloc

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import sessionmaker, declarative_base

tracemalloc.start()

db_url = "postgresql+psycopg2://postgres:databasepass100%@localhost:5432/evos"
engine = create_engine(url=db_url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Reviewers(Base):
    __tablename__ = 'reviewers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String)
    phone_number = Column(String)
    full_name = Column(String)
    username = Column(String)
    review = Column(Text)

    def __str__(self):
        return f"{self.phone_number}: {self.review}"

    def add_review(self, user_id, phone_number, full_name, username, review):
        session.add(Reviewers(user_id=user_id,
                              phone_number=phone_number,
                              full_name=full_name,
                              username=username,
                              review=review))
        session.commit()


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    price = Column(Integer)
    category = Column(String)

    @staticmethod
    def all_read(category):
        list0 = []
        students = session.query(Products).filter(Products.category == category)
        for i in students:
            list0.append(f'{i.name}')
        return list0

    @staticmethod
    def all_get():
        list0 = []
        students = session.query(Products).all()
        for i in students:
            list0.append(f'{i.name}')
        return list0

    @staticmethod
    def get_one(name):
        list0 = []
        students = session.query(Products).filter(Products.name == name)
        for i in students:
            list0.append(f'{i.name}')
            list0.append(f'{i.price}')
            list0.append(f'{i.id}')
        return list0

    @staticmethod
    def get_one_id(id):
        list0 = []
        students = session.query(Products).filter(Products.id == id)
        for i in students:
            list0.append(f'{i.name}')
            list0.append(f'{i.price}')
            list0.append(f'{i.id}')
        return list0

    @property
    def all_data(self):
        list0 = []
        students = session.query(Products).distinct(Products.category)
        for i in students:
            list0.append(f'{i.category}')
        return list0


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(String)
    product_id = Column(String)
    quantity = Column(Integer)

    def add_to_cart(self, customer_id, product_id, quantity=1):
        session.add(Cart(customer_id=customer_id,
                         product_id=product_id,
                         quantity=quantity))
        session.commit()

    @staticmethod
    def cart_for_user(customer_id):
        list0 = []
        list1 = []
        students = session.query(Cart).filter(Cart.customer_id == customer_id).all()
        for i in students:
            list0.append(f'{i.customer_id}')
            list0.append(f'{i.product_id}')
            list0.append(f'{i.quantity}')
            list1.append(list0)
            list0=[]
        return list1


class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, autoincrement=True, primary_key=True)
    image = Column(BYTEA)

    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    

# Base.metadata.create_all(engine)
