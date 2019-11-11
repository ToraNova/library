#!/usr/bin/python

# join.py
# join example

import hashlib, datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, DateTime

# additional stuff
from sqlalchemy import join
from sqlalchemy.sql import select

# The following statement is declarative and can be used in the main function
# the vars engine and sample can then be imported by other modules and used
engine = create_engine('sqlite:///test.db', echo = False)
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
j = sample.join(example, sample.c.id == example.c.sample_id )
jc = select([ sample ]).select_from( j )

# open a connection
conn = engine.connect()

res = conn.execute( jc )
for r in res.fetchall():
    print(r)

# close the connection
conn.close()
