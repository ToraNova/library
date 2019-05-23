#!/usr/bin/python3

'''sample of opening a file for writing'''
import time

if __name__ == "__main__":

    '''
    opens a file 'file_write.txt' in some modes:
    w - write
    r - read
    b - binary
    t - text
    a - append
    + - r/w

    an optional 3rd arg 0 at the end is to disable bufferring 
    (this causes the file to be written instantly
    alternatively, a flush can be used outfile.flush() to force
    the buffer to be written into the file
    '''
    with open("file_write.txt",'w') as outfile:
        for i in range(10):
            outfile.write('1')
            outfile.flush()
            time.sleep(0.5)
        outfile.write('\n')

