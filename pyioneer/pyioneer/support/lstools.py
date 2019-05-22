################################################################################
# lstool.py
# lstool is the tools for lists. Some direct supports include slicing,
# batching, joining etc. that aids listing operations
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
################################################################################

################################################################################
# 1dimensional lists
################################################################################
def splitls(target, cutpoint):
    '''split the target into 2 batches, one for testing and one for training
    b1 is from index 0 until cutpoint while b2 is from cutpoint until the last 
    element. set cutpoint < 0 to start cutting from the back, 
    @example : 
    if cutpoint = 1, then 0 will be b1 and 1...end will be b2
    if cutpoint = -1, then 0...end - 1 will be b1 and end will be b2'''
    b1 = target[:cutpoint]
    b2 = target[cutpoint:]
    return b1,b2

################################################################################
# 2dimensional lists
################################################################################
def hsplit_2dlist(target,cutpoint):
    ''' slice the target matrix at s_point (horizontal)
     | 1 2 3 |
     | 4 5 6 |
     | 7 8 9 |
     s_point 1 will move first row onto first return array
     row 2,3 will be onto second return array.
     returns 2 arrays'''
    # TODO: No input sanitization
    ret0 = target[:cutpoint][:]
    ret1 = target[cutpoint:][:]
    return (ret0,ret1)

def vsplit_2dlist(target,cutpoint):
    '''slice the target matrix at s_point (vertical)
     | 1 2 3 |
     | 4 5 6 |
     | 7 8 9 |
     s_point 1 will move first col onto first return array
     col 2,3 will be onto second return array.
     returns 2 arrays'''
    # TODO: No input sanitization

    # transpose the 2Dlist
    target = list( map( list, zip(*target)))
    ret0 = target[:][:cutpoint] #begin till s_point
    ret1 = target[:][cutpoint:] #s_point till end
    return (ret0,ret1)

def transpose_2dlist(target):
    '''perform transpose on a 2D list. assumes target has the form
    of a matrix (i.e, with positive rowcount and all column lenght in
    the rows are the same'''
    # PLEASE CALL pyioneer.variable.sanitize.isMatrix before launching
    # this function. PLEASE!
    return list( map(list, zip(*target)))


# Test script
if __name__ == "__main__":

    sample = [1,2,3,'4',True]
    sb0, sb1 = splitls(sample,2)
    print(sb0,sb1)
    testmat = [ [1,2,3],[4,5,6],[7,8,9] ]
    hm0, hm1 = hsplit_2dlist( testmat, 2) 
    print(hm0,'//',hm1)
    hm0, hm1 = vsplit_2dlist( testmat, 1) 
    print(hm0,'//',hm1)

