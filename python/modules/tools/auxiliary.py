#--------------------------------------------------
# auxtools.py
# this file acts like the swiss army knife of my python
# library, it will contain powerful and useful python functions
# which do not really match to any classes of operation
# created 01/09/2019 11:45pm
#--------------------------------------------------

def getAttrList(in_obj):
	'''returns a list of attributes of an object, not
	including methods and intrinsic attributes'''
	out = []
	for a in dir(in_obj):
		if not a.startswith('__') and not callable(getattr(in_obj,a)):
			out.append(a)
	return out

def getSpecAttrList(in_obj,start_keyword=''):
	'''returns the specific attribute of an object.
	it returns a dictionary with the attribute name striped of the
	start_keyword as the key and value of the actual attribute'''
	out = {}
	for a in dir(in_obj):
		if a.startswith(start_keyword):
			out[a[len(start_keyword):]]=in_obj.__getattribute__(a)
	return out
