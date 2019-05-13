################################################################################
# constring.py - constant string declares
# this module stores the constantly used string / string formats that
# can be easily imported
# current submods : dateformt
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 13 May 2019
################################################################################
# shared constants for this module

class Dateformt:
    '''Constant strings for easier date formating
    this are used together with strftime
    i.e : print( datetime.datetime.now().strftime( FORMAT ) )'''

    norm = "[%Y/%m/%d %a %H:%M:%S]"                     # Normal Form
    norm_micros = "[%Y/%m/%d %a %H:%M:%S.%f]"           # Normal Form with micros appended


if __name__ == "__main__":

    import datetime

    print( datetime.datetime.now().strftime( Dateformt.norm ) )
    print( datetime.datetime.now().strftime( Dateformt.norm_micros ) )

