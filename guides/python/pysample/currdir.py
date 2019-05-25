import os


if __name__ == "__main__":

    filedir = os.path.dirname(os.path.realpath(__name__))
    print(filedir)

    onlyfiles = [f for f in os.listdir( filedir ) if \
            os.path.isfile( os.path.join(filedir, f) )]
    print(onlyfiles)
