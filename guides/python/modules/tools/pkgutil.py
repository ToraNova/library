# pkgutil py allows lessening of code size on other packages

# use the following import line
# from pkg.pkgutil import PKGClass

class PKGClass():
    #moduename and a pkgprint define
    def pkgprint(self,*args,**kwargs):
        print("[{}]".format(self.moduname),*args)

    def __init__(self,moduname,verbose=False):
        self.moduname = moduname
        self.verboseprint = self.pkgprint if verbose else lambda *a, **k: None
    # you may inherit this class with PKGClass arg in class define
    # use PKGClass.__init__(self, <PACKAGE NAME> ) to allow verboseprinting
