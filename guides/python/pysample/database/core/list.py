#!/usr/bin/python

# list.py
# list out 'sample' objects

import hashlib, datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, DateTime

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

# beginning scripts relevant to selection
sel = sample.select().where( sample.c.id > 1 ).where( sample.c.id < 7 )
sel2 = sample.select()

# open a connection
conn = engine.connect()
# execute the statement (we do not need to use try/catch or with block
# since listing doesn't actually change anything in the database
result = conn.execute(sel)
result2 = conn.execute(sel2)

# get one (this actually pops a result from the list)
row = result.fetchone()
print(row)

# print all (the result from conn.execute can be iterated)
for r in result:
    print(r)

print( result2.fetchall() )

# close the connection
conn.close()

