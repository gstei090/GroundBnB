import database

def upload_new_property(hostID):
    return None

def list_my_properties(hostID):
    return None

def exit_program():
    exit()

if __name__ == "__main__":
    hostID = -1
    while hostID < 1:
        print('Please enter your host assimilation number:')
        try:
            hostID = int(input())
        except:
            print('Invalid input format')
    
    print('Welcome to the borg collective, host {}'.format(hostID))

    while True:
        print('Please select one of the following options: \n\
            1: Upload a new property to your listings.\n\
            2: List all of your properties.\n\
            3: Exit Program')

        switcher = {
            1: upload_new_property,
            2: list_my_properties,
            3: exit_program,
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