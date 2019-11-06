import sqlalchemy as db

from db.secrets import *

# Init the DB
engine = db.create_engine('postgresql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + '/' + DB_NAME)
conn = engine.connect()
metadata = db.MetaData()

# Create answers table
answers = db.Table('answers', metadata,
                   db.Column('Num', db.Integer(), primary_key=True),
                   db.Column('Ans', db.Integer(), nullable=False))

metadata.create_all(engine)
