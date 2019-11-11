#!/usr/bin/python

# update.py
# update the database and insert 'example' objects

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

# beginning scripts relevant to update
# get current time
now = datetime.datetime.now()
upd = sample.update().where( sample.c.id > 1 ).values( time_B = now )

# get the number of sample objects
hwm = sample.select()

# open a connection
conn = engine.connect()
with conn.begin() as trans:
    # execute the statement
    conn.execute(upd)

    res = conn.execute(hwm)
    for r in res:
        # for every sample, insert an 'example' object (for testing only)
        conn.execute( example.insert().values( sample_id = r.id ) )

# close the connection
conn.close()
