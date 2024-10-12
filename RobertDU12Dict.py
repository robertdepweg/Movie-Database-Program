# PROJECT:  RobertDU12Dict.py                     uses MODULES:  see imports below
# AUTHOR:   Robert Depweg                                     DESIGNER: C Claussen
# DESCRIPTION:  Creates a "database" (DB) of movie information so it can
#       be queried and changed by the user.  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import create_db as create
import dump_load_db as backup
import db_operations as op

def main():

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - CONSTANT DECLARATIONS
    # Constants for menu choices
    LOOK_UP: int = 1
    ADD: int = 2
    CHANGE: int = 3
    DELETE: int = 4
    QUIT: int = 5

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - INPUT
    invalid_flag: bool = True # assumes mode is invalid
    mode: str = ''
    while invalid_flag: # marked True until correct output
        mode = input(f'Enter run mode:  N for' 
                          f' Normal, S for Startup: ').upper()
        invalid_flag = good_data(mode) # checks if mode is S or N

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -CALCULATIONS
    if mode.upper() == 'S':
        # initial data created
        movie_db: dict = create.load_initial_data() 
        
    else: # if mode is startup "N"
        # loads .bin file with dictionary
        movie_db = backup.load_backup() 

    num: str = get_user_choice() # presents menu + asks for input
    # ensures digit is in range of one to five
    num: int = valid_number(num, LOOK_UP, QUIT)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -OUTPUT
    while num != QUIT:
        if num == LOOK_UP: # looks up info for movie
            op.look_up(movie_db)
        elif num == ADD: # adds new entry to db
            op.add(movie_db)
        elif num == CHANGE: # changes existing entry in db
            op.change(movie_db)
        else: # DELETE function
            op.delete(movie_db) # deletes movie entry in db
        num = get_user_choice()
        num = valid_number(num, LOOK_UP, QUIT) 

    backup.dump_backup(movie_db) # after quit is selected

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCTIONS
def good_data(mode):
    ''' returns True or False depending if choice 
    is a valid value of S or N '''
    if mode == 'N' or mode == 'S':
        return False
    else:
        return True
    
def get_user_choice():
    ''' present menu and returns validated user menu choice '''
    print('\nMenu')
    print(f'{"-"*40}')
    print('1. Look up movie information')
    print('2. Add a new movie')
    print('3. Change movie information')
    print('4. Delete movie')
    print('5. Quit the program')
    num = input('\nEnter your choice: ')
    return num

def valid_number(num, LOOK_UP, QUIT):
    ''' ensure string contains all digits in the range of min to max '''
    invalid_number: bool = True
    while invalid_number: # flag stays true until 1-5 is typed
        if num.isdigit() and int(num) >= LOOK_UP and int(num) <= QUIT:
            invalid_number = False
        else:
            num = input('Please enter a valid choice [1-5]: ')
    return int(num)

# Conditional call to main()
if __name__ == '__main__':
    main()