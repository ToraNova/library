# dumps the dataset provided in sklearn
from sklearn import datasets
import dist_matrix as dmat
import csv
import numpy
		
if __name__ == "__main__":

	split_point = 3
	md = datasets.load_boston()
	
	xc = md.data
	yc = md.target
	
	xda, xdb = dmat.vsplit_mat( xc, split_point)
	
	
	delim = ';'
	quotechar ='"'

	with open('xda.csv','w') as outfile:
			csv_writer = csv.writer(outfile,
					delimiter=delim,quotechar=quotechar,
					quoting=csv.QUOTE_MINIMAL)
			for i,rows in enumerate(xda):
				rows = numpy.append(rows,yc[i])
				csv_writer.writerow( rows)

	with open('xdb.csv','w') as outfile:
			csv_writer = csv.writer(outfile,
					delimiter=delim,quotechar=quotechar,
					quoting=csv.QUOTE_MINIMAL)
			for i,rows in enumerate(xdb):
				rows = numpy.append(rows,yc[i])
				csv_writer.writerow( rows)
	
	
