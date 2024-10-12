# MODULE:  db_operations.py                       used by PROJECT:  RobertDU12Dict.py
# AUTHOR:  Robert Depweg                                         DESIGNER: C Claussen
# DESCRIPTION:  query, add, change, or delete a record from a DOT database
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def look_up(movie_db):  
    ''' get title to look up, status messages to user '''
    film = input('\nEnter a movie title: ').upper()
    if film in movie_db:
        for keys, details in movie_db.items():
            if keys == film:
                print(f'{"":8}{"Genre:":<20}{details[0]:<12}')   
                print(f'{"":8}{"Lead Studio:":<20}{details[1]:<12}')     
                print(f'{"":8}{"Rotten Tomato:":<20}'
                      f'{details[2]}{"%":<12}')
                print(f'{"":8}{"Worldwide Gross:":<20}'
                      f'{details[3]:<12}')    
                print(f'{"":8}{"Year:":<20}{details[4]:<12}')
    else:
        print('\nThe specified movie was not found.')

def add(movie_db): 
    ''' adds movie information to database '''
    film = input('\nEnter a movie title to add: ').upper()
    if film in movie_db:
        print('\nThat title already exists.')
    else:
        genre = input('Enter genre: ')
        studio = input('Enter lead studio: ')
        rt_rate = input("Enter Rotten Tomato % rating: ")
        if rt_rate.count('%') > 0: # if % included in input
            rt_rate = rt_rate.strip('%')
        gross = input("Enter Worldwide gross (ex $540.65): ")
        if gross.count('$') > 0: # if $ included in input
            gross = gross.strip('$')
        year = input("Enter year: ")
        # entry tuple added to dict
        movie_db[film] = genre, studio, rt_rate, gross, year
        print('\nMovie information has been added.')

def change(movie_db): 
    ''' change movie data for particular title '''
    film = input('Enter a movie title: ').upper()
    if film in movie_db:
        genre = input('Enter genre: ')
        studio = input('Enter lead studio: ')
        rt_rate = input("Enter Rotten Tomato % rating: ")
        if rt_rate.count('%') > 0:
            rt_rate = rt_rate.strip('%')
        gross = input("Enter Worldwide gross: ")
        if gross.count('$') > 0:
            gross = gross.strip('$')
        year = input("Enter year: ")
        # entry tuple changed in dict
        movie_db[film] = genre, studio, rt_rate, gross, year
        print('\nInformation updated.')
    else:
        print('\nThe specified movie was not found.')

def delete(movie_db): 
    ''' delete movie and corresponding data if exists in db '''
    film = input('Enter a movie title: ').upper()
    if film in movie_db:
        movie_db.pop(film)
        print('\nThe movie has been deleted.')
    else:
        print('\nThe specified movie was not found.')