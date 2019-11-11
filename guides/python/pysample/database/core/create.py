#!/usr/bin/python

# connect.py
# connects to the database engine

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, DateTime

# sqlite is the minimalist sql engine used here
# creates and connects to a database 'test.db'
engine = create_engine('sqlite:///test.db', echo = True)

# The following is for mysql
# engine = create_engine("mysql://user:pwd@localhost/college",echo = True)

# creates metadata class
meta = MetaData()

sample = Table(
   'samples', meta,
   Column('id', Integer, primary_key = True),
   Column('variable_A', String),
   Column('time_B', DateTime, nullable = False),
)

example = Table(
   'example', meta,
   Column('id', Integer, primary_key = True),
   Column('sample_id', Integer, nullable = True),
)

# the following method creates the tables in the database
meta.create_all( engine )
