
def get_all_the_corona_spreaders():
    '''
    Give the details of all the ​guests who rented properties. 
    Display the columns as ​guest name, rentaltype, rentalprice​, ​signingdate​,​ branch, payment type and ​payment status​.
    Sort by the ​payment type in ascending order and signing date in descending order​.
    '''
    return None

def get_guest_list_view():
    '''
    Create a view named ​GuestListView that gives the details of all the guests.
    Sort the guests by the ​branch id ​and then by ​guest id​.
    '''
    return None

def get_cheapest_rental():
    '''
    Display the details of the cheapest (completed) rental. 
    //TEMP Not sure what they mean by completed
    '''
    return None

def get_all_rented_properties():
    '''
    List all the properties rented and sort based on the ​branch ​​id​ and ​review rating​.
    '''
    return None

def get_all_available_properties():
    '''
    Find the properties that are already listed but not yet rented. Please, avoid duplications.
    '''
    return None

def get_the_tenth_legion():
    '''
    List all the details of all properties rented on the 10​th day of any month. 
    Ensure to insert dates in your table that correspond in order to run your query
    '''
    return None

def get_all_rich_people():
    '''
    List all the managers and the employees with salary greater than or equal to $​15000 
    by their​: ids, names, branch ids​, ​branch names and salary​. 
    Sort by ​manager id​ and then by ​employee id​.
    '''
    return None

def create_bill():
    '''
    Consider creating a simple bill for a guest stating the ​property type​, ​host, address, amount paid and ​payment type​.
    '''
    return None

def new_phone_who_dis():
    '''
    Update the phone number of a guest.
    '''
    return None

def firstNameFirst():
    '''
    Create and test a user-defined function named ​FirstNameFirst that combines two attributes of the 
    guest named ​firstName and ​lastName into a concatenated value named ​fullName [e.g.,​ James and ​Brown​ will be combined to read ​James Brown​].
    '''
    return None

def exit_program():
    exit()

if __name__ == "__main__":
    print("\nWelcome administrator, we've been expecting you.\n")
    
    while True:
        print('Please select one of the following options: \n\
            1: Give the details of all the ​guests who rented properties.\n\
            2: Create a view named ​GuestListView that gives the details of all the guests.\n\
            3: Display the details of the cheapest (completed) rental.\n\
            4: List all the properties rented and sort based on the ​branch​​ id​ and ​review rating​.\n\
            5: Find the properties that are already listed but not yet rented.\n\
            6: List all the details of all properties rented on the 10​th day of any month.\n\
            7: List all the managers and the employees with salary greater than or equal to $​15000.\n\
            8: Create a simple bill for a guest.\n\
            9: Update the phone number of a guest.\n\
            10: Create and test a user-defined function named ​FirstNameFirst.\n\
            11: Exit Program')

        switcher = {
            1: get_all_the_corona_spreaders,
            2: get_guest_list_view,
            3: get_cheapest_rental,
            4: get_all_rented_properties,
            5: get_all_available_properties,
            6: get_the_tenth_legion,
            7: get_all_rich_people,
            8: create_bill,
            9: new_phone_who_dis,
            10: firstNameFirst,
            11: exit_program
        }
        chosen_option = -1
        while chosen_option < 1 or chosen_option > 11:
            print('Please enter numerical value for desired option:')
            try:
                chosen_option = int(input())
            except:
                print('Invalid input format')
        chosen_func = switcher.get(chosen_option)
        chosen_func()



