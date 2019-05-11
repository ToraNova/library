# Highly specialized lib file, do not use for other dataset.
# This file is meant for lookup tables for categorical value quantisation.
import csv, numpy

# This function is used to read
def read_csvfile(filename,compd=numpy.double,limiter=10000,skips=0):
    # dataset preparation
    with open(filename) as dataset:
        reader = csv.reader(dataset,delimiter=';', quotechar='"')
        for index in range(skips):
            next(reader)
        rin_list = list(reader) #read in the csv file, skipping the first
        rowcount = len( rin_list ) if len( rin_list ) <= limiter else limiter
        x_mat = []
        y_vct = []
        #x_mat = numpy.zeros(dtype=compd,shape=(rowcount,f_size)) #specifically choose 13 vectors only
        #y_vct = numpy.zeros(dtype=numpy.bool,shape=(rowcount,1))

        for index,row in enumerate(rin_list):
            #print("Registering row",index,row)
            if(index>=limiter):
                break

            x_mat.append([float(i) for i in row[:-1]])
            y_vct.append(float(row[-1]))

        x_mat = numpy.array(x_mat)
        y_vct = numpy.array(y_vct)

    return x_mat,y_vct,rowcount
