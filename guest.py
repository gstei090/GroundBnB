import database

def list_available_properties():
    query_string = "select property.* from property\
        where availability = 'available'"
    result = database.execute_query(query_string)
    for row in result:
        print(row)

def exit_program():
    exit()

if __name__ == "__main__":
    guestID = -1
    while guestID < 1:
        print('Please enter your non-valued guest number:')
        try:
            guestID = int(input())
        except:
            print('Invalid input format')
    
    print('Welcome to GroundBnB, guest {}!'.format(guestID))
    
    while True:
        print('\n\n\nPlease select one of the following options: \n\
            1: List available properties.\n\
            2: Exit program.')

        switcher = {
            1: list_available_properties,
            2: exit_program,
        }
        chosen_option = -1
        while chosen_option < 1 or chosen_option > 11:
            print('Please enter numerical value for desired option:')
            try:
                chosen_option = int(input())
            except:
                chosen_option = -1
        chosen_func = switcher.get(chosen_option)
        chosen_func()