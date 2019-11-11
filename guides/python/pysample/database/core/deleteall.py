#!/usr/bin/python

# deleteall.py
# deletes everything from the database (not the schema)

import hashlib, datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, DateTime

# The following statement is declarative and can be used in the main function
# the vars engine and sample can then be imported by other modules and used
engine = create_engine('sqlite:///test.db', echo = True)
meta = MetaData()

sample = Table(
   'samples', meta,
   Column('id', Integer, primary_key = True),
   Column('variable_A', String),
   Column('time_B', DateTime),
)

example = Table(
   'example', meta,
   Column('id', Integer, primary_key = True),
   Column('sample_id', Integer, nullable = True),
)

# beginning scripts relevant to deletion
delall = sample.delete().where( sample.c.id > 0 )
delall2 = example.delete().where( example.c.id > 0 )

# open a connection
conn = engine.connect()
with conn.begin() as trans:
    # execute the statement
    conn.execute(delall)
    conn.execute(delall2)
# close the connection
conn.close()
