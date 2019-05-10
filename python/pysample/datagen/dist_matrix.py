# Custom matrix library used for distributed ML
# static functions to reduce driver program code size
import numpy

# BY CONVENTION, THE ROWS WILL INDICATE DATA AND COLUMNS WILL INDICATE FEATURES
# PLEASE DO NOT MODIFY ANY CODE HERE AND EDIT IT ON THE DRIVER PROGRAMS.

def hsplit_mat(target,s_point):
    # slice the target matrix at s_point (horizontal line segregation)
    # | 1 2 3 |
    # | 4 5 6 |
    # | 7 8 9 |
    # s_point 1 will move first row onto first return array
    # row 2,3 will be onto second return array.
    # returns 2 arrays
    # TODO: No input sanitization
    ret0 = target[:s_point,:]
    ret1 = target[s_point:,:]
    return (ret0,ret1)

def vsplit_mat(target,s_point):
    # slice the target matrix at s_point (vertical line segregation)
    # | 1 2 3 |
    # | 4 5 6 |
    # | 7 8 9 |
    # s_point 1 will move first col onto first return array
    # col 2,3 will be onto second return array.
    # returns 2 arrays
    # TODO: No input sanitization
    ret0 = target[:,:s_point] #begin till s_point
    ret1 = target[:,s_point:] #s_point till end
    return (ret0,ret1)

def compute_S(x_mat):
    #Compute x_mat dot x_mat transpose
    return x_mat.dot(x_mat.T)

def compute_K(x_mat):
    #Compute x_mat tranpose dot x_mat
    return x_mat.T.dot(x_mat)

# Singular functions
def cov_w_nos(x_mat,y_vct,lambd=0.99,compd=numpy.intc):
    # Compute W without S. takes only x_mat and y_vct
    # compute S first
    S_nos = compute_S(x_mat)
    # inverse the S+ lambd I
    pre_w = numpy.linalg.inv(S_nos + lambd * numpy.identity(S_nos.shape[0],dtype=compd))
    w = pre_w.dot(x_mat).dot(y_vct)
    return w

def ker_w_nos(x_mat,y_vct,lambd=0.99,compd=numpy.intc):
    # Compute W without K.
    K_nos = compute_K(x_mat)
    # inverse the K + lambd I
    pre_w = numpy.linalg.inv(K_nos + lambd * numpy.identity(K_nos.shape[0],dtype=compd))
    w = x_mat.dot(pre_w).dot(y_vct)
    return w

def ker_a_mul( klist, y_vct , lambd=0.99,compd = numpy.intc ):
    # Compute a from multiple K's via the kernel matrix
    K_mul = numpy.zeros( klist[0].shape,dtype=compd )
    for k in klist:
        K_mul += k

    pre_a = numpy.linalg.inv(K_mul + lambd * numpy.identity(K_mul.shape[0],dtype=compd))
    a = (lambd * pre_a).dot(y_vct)
    return a

def recompute_W( x , a , lambd=0.99):
    # Recopmute w with the alpha value
    return x.dot( (1/lambd) * a )

def batch_split(target, test_batch_size):
    # split the target into 2 batches, one for testing and one for training
    train = target[:-test_batch_size]
    test = target[-test_batch_size:]

    return train,test

def check_all_close(a,b,etolr,imsg="check_all_close"):
    print("[{}] all close with tolerance {} : {}".format(
        imsg,
        etolr,
        numpy.allclose(a,b,
        atol=etolr,equal_nan=True)
    ))

# lib TODO:
# sanitize inputs
# include try: except blocks to prevent misuse

def check_symmetric(a, tol=1e-8):
    #credits to original author @
    #stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
    return numpy.allclose(a, a.T, atol=tol)
