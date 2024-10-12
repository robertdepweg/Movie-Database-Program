# MODULE:  create_db.py                       used by PROJECT:  RobertDU12Dict.py
# AUTHOR:  Robert Depweg                      DESIGNER: Dr. Kaminski
# DESCRIPTION:  Creates DB (dictionary) using data from MovieData.csv file.
#       (NOTE:  There are 2 header records to skip).  The DB contains:
#               KEY:  movie name (convert to all caps)
#               VALUE:  tuple of (genre, studio, rt_rate, gross, year)
#                       stored as str, str, int, str, str
#        Exits program if IO or other exception occurs
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import sys 

def load_initial_data():  
    ''' reads in data from .csv file, creates + returns 
    dictionary of tuples '''
    try:
        movie_db = {}
        with open('MovieData.csv', 'r') as infile:
            for i in range(2): # skips two header lines
                infile.readline()
            for line in infile: 
                line: str = line.strip('\n')
                fields: list = line.split(',')
                film, genre, studio, rt_rate, gross, year = get_conv_fields(fields)
                # entry tuple added to dict
                movie_db[film] = genre, studio, rt_rate, gross, year
            print('\nMovie database is ready to query.')
            return movie_db
    except IOError as err: # exits system if issue with file
        sys.exit(err)
    except Exception:
        sys.exit()

def get_conv_fields(fields):  
    ''' recieves list of fields, returns each 
    list element as converted variable '''
    try:
        film: str = fields[0]
        film = film.upper()
        genre: str = fields[1]
        studio: str = fields[2]
        rt_rate: int = int(fields[3])
        gross: str = fields[4].strip()
        year: str = fields[5]
        return film, genre, studio, rt_rate, gross, year
    except Exception:
        sys.exit()