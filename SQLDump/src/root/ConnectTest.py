'''
Created on Mar 31, 2017

@author: Keeyan
'''
import ConfigParser
import MySQLdb as mdb
import sys

##
##Function definition for config parsing

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1            

try:
    Config = ConfigParser.ConfigParser()
    Config.read("config.ini")
    password = ConfigSectionMap('Info')['password']
    database = ConfigSectionMap('Info')['db']
    con = mdb.connect('localhost', 'root', password, database);

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    
    print "Database version : %s " % ver
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()

