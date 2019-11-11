#!/usr/bin/python

# insert.py
# insert 'sample' objects into the database

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

# beginning scripts relevant to insertion
# get current time
now = datetime.datetime.now()
ins = sample.insert().values(
        variable_A = hashlib.sha256( str(now).encode()).hexdigest(),\
        time_B = now)

# open a connection
conn = engine.connect()
# execute statement in a transaction (rollback when fail)
with conn.begin() as trans:
    conn.execute(ins)
# close the connection
conn.close()
