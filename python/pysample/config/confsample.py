#
# Sample configparser usage
# ToraNova 2019
# https://docs.python.org/3/library/configparser.html 

#imports the configparser module
import configparser

if __name__ == "__main__":
    #main function sample

    #creates a configparser and writes the configuration
    cp = configparser.ConfigParser()
    #section 'class A'
    cp['class A'] = {'something':1, 'something2':'help'}

    #section 'test'
    cp['test'] = {'test0':True}

    #option
    cp['lonewolf'] = {'0':12.3}

    #saves the configuration to a file
    with open('config_out.ini','w') as configfile:
        cp.write(configfile)

    #reads a configuration file
    cp.read('config_out.ini')

    # get a boolean var
    testbool = cp.getboolean('test','test0')

    #get numerics, they throw exceptions if fail
    testfloat = cp.getfloat('lonewolf','0')
    testint = cp.getint('class A','something')

    #the generic get is also supported. the config is like a dict
    classA = cp['class A']
    testdef = classA.get('nonexist','fallback value')
    teststr = classA.get('something2')
    
    print(testbool,testfloat,testint,testdef,teststr)

    #edits an option
    cp['class A']['something2'] = 'thanks'

    #writes back the changes
    with open('config_out_edited.ini','w') as configfile:
        cp.write(configfile)

    # .ini file or .conf file
    # we can use # or ; to put comments



    
