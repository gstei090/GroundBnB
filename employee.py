import database

def list_all_branch_properties():
    employeeID = -1
    while employeeID < 1:
        print('Please enter your employee number:')
        try:
            employeeID = int(input())
        except:
            print('Invalid input format')
    
    query_string = f"select property.propertyID, address.city, property.accomodates, property.availability, address.city,address.country, operatingIn.branchID\
        from property\
        inner join hasAddress\
        on hasAddress.propertyID = property.propertyID\
        inner join address\
        on address.addressID = hasaddress.addressID\
        inner join operatingIN\
        on property.propertyID = operatingIn.propertyID\
        inner join worksat\
        on operatingin.branchID = worksat.branchID\
        where worksat.employeeId = {employeeID};"
    result = database.execute_query(query_string)
    for row in result:
        print(row)

def exit_program():
    exit()


if __name__ == "__main__":

    
    while True:

        switcher = {
            1: list_all_branch_properties,
            2: exit_program
        }
        chosen_option = -1
        while chosen_option < 1 or chosen_option > 11:
            print('\n\n\nPlease select one of the following options: \n\
                1: List available properties.\n\
                2: Exit program.')
            print('Please enter numerical value for desired option:')
            try:
                chosen_option = int(input())
            except:
                chosen_option = -1
        chosen_func = switcher.get(chosen_option)
        chosen_func()