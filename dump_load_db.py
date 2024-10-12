# MODULE:  dump_load_db.py                  used by PROJECT:  RobertDU12Dict.py
# AUTHOR:  Robert Depweg                                         DESIGNER: C Claussen
# DESCRIPTION:  Does pickling/unpickling of DB (dictionary) to/from
#       MovieDB.bin.  Needs load and dump functions.
#
#       Exits program if IO or other exception occurs
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pickle
import sys

def load_backup():  
    ''' loads .bin file into dictionary and returns dictionary '''
    try:
        infile = open('MovieDB.bin', 'rb')
        movie_db = pickle.load(infile) # loads .bin file used before
        print('\nMovie database is loaded from backup and ready to query.')
        infile.close()
        return movie_db
    except IOError as err: # exits system if issue with file
        sys.exit(err)
    except Exception:
        sys.exit()

def dump_backup(movie_db):  
    ''' stores dictionary into pickled binary file '''
    try:
        infile = open('MovieDB.bin', 'wb')
        pickle.dump(movie_db, infile) # places dict into .bin file
        print('\nMovie database saved to backup.')
        infile.close()
    except IOError as err:
        sys.exit(err)
    except Exception:
        sys.exit()