
def list_all_branch_properties():
    return None

def exit_program():
    exit()


if __name__ == "__main__":
    employeeID = -1
    while employeeID < 1:
        print('Please enter your useless employee number:')
        try:
            employeeID = int(input())
        except:
            print('Invalid input format')
    
    print('Welcome back number {}, you\'re late'.format(employeeID))
    
    while True:
        print('Please select one of the following options: \n\
            1: List available properties.\n\
            2: Exit program.')

        switcher = {
            1: list_all_branch_properties,
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