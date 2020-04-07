import database

def get_all_the_corona_spreaders():
    '''
    Question 1
    Give the details of all the ​guests who rented properties. 
    Display the columns as ​guest name, rentaltype, rentalprice​, ​signingdate​,​ branch, payment type and ​payment status​.
    Sort by the ​payment type in ascending order and signing date in descending order​.
    '''
    query_string = "SELECT guest.firstname, guest.middleinitial, guest.lastname, property.buildingtype,property.price, booking.startdate, operatingin.branchid, payment.typeofpayment, payment.status from guest\
        inner join hasbooking\
        on hasbooking.guestid = guest.guestid\
        inner join booking\
        on hasbooking.bookingid = booking.bookingid\
        inner join property\
        on property.propertyid = booking.propertyid\
        inner join operatingin\
        on operatingin.propertyid = property.propertyid\
        inner join payedfor\
        on payedfor.bookingid = booking.bookingid\
        inner join payment\
        on payment.paymentid = payedfor.paymentid\
        ORDER by payment.typeofpayment asc, booking.startdate desc;"
        
    result = database.execute_query(query_string)
    for row in result:
        print(row)

def get_guest_list_view():
    '''
    Question 2
    Create a view named ​GuestListView that gives the details of all the guests.
    Sort the guests by the ​branch id ​and then by ​guest id​.
    '''
    query_string = ("select * from GuestListView")
    result = database.execute_query(query_string)
    print("This is the Guest List View")
    for row in result:
        print(row)

def get_cheapest_rental():
    '''
    Question 3
    Display the details of the cheapest (completed) rental. 
    '''
    query_string = ("select min(price) from property\
        inner join booking\
        on booking.propertyid = property.propertyid\
        where booking.startdate <= '2020-04-06'")
    result = database.execute_query(query_string)
    print(f"The lowest rental price is {result}")

def get_all_rented_properties():
    '''
    Question 4
    List all the properties rented and sort based on the ​branch ​​id​ and ​review rating​.
    '''
    #not sure if working
    query_string = ("SELECT Booking.propertyID,reviews.rating,operatingin.branchid FROM booking\
        INNER JOIN hasreview\
        ON booking.propertyID = hasreview.propertyID\
        INNER JOIN reviews\
        ON hasreview.reviewID = reviews.reviewID\
        INNER JOIN OperatingIn\
        ON booking.propertyID = OperatingIn.PropertyID\
        WHERE booking.enddate <= '2020-04-06'\
        ORDER BY branchID, rating")
    result = database.execute_query(query_string)
    print('The following properties are rented:')
    for row in result:
        print('Property ID {}, rating {}, branch ID {}'.format( row[0], row[1], row[2]))

def get_all_available_properties():
    '''
    Question 5
    Find the properties that are already listed but not yet rented. Please, avoid duplications.
    '''
    query_string = "SELECT propertyid\
        FROM booking\
        where (startdate >= '2020-04-06') and propertyID not in (select propertyID\
        from booking\
        where startdate < '2020-04-06')"
    result = database.execute_query(query_string)
    print('The following properties are available:')
    for row in result:
        print('Property ID {}'.format( row[0]))

def get_the_tenth_legion():
    '''
    Question 6
    List all the details of all properties rented on the 10​th day of any month. 
    Ensure to insert dates in your table that correspond in order to run your query
    '''
    
    query_string = "SELECT property.* , booking.startdate FROM property\
        inner join booking\
        on booking.propertyid = property.propertyid\
        where (extract (day from startdate)) = '10'"
    
    result = database.execute_query(query_string)
    for row in result:
        print(row)
    return None

def get_all_rich_people():
    '''
    Question 7
    List all the managers and the employees with salary greater than or equal to $​15000 
    by their​: ids, names, branch ids​, ​branch names and salary​. 
    Sort by ​manager id​ and then by ​employee id​.
    '''

    query_string = "select employee.employeeid, employee.firstname, employee.middleinitial, employee.lastname, worksat.branchid,branches.country, employee.salary, employee.eposition from employee\
        inner join worksat\
        on worksat.employeeid = employee.employeeid\
        inner join branches\
        on branches.branchid = worksat.branchid\
        where employee.salary >= 50000\
        order by employee.eposition desc, employee.employeeid;"
    
    result = database.execute_query(query_string)
    for row in result:
        print(row)

def create_bill():
    '''
    Question 8
    Consider creating a simple bill for a guest stating the ​property type​, ​host, address, amount paid and ​payment type​.
    '''
    print('Enter the guestID for the bill: ')
    guestID = -1
    while guestID < 1:
        print('Please enter numerical value for desired option:')
        try:
            guestID = int(input())
        except:
            print('Invalid input format')

    query_string = f"select property.buildingtype, host.firstname,host.middleinitial,host.lastname, address.addressl1,address.addressl2, address.city,address.province,address.country,address.postalcode, payment.amount, payment.typeofpayment from payment\
        inner join payedfor\
        on payment.paymentID = payedfor.paymentID\
        inner join booking\
        on payedfor.bookingid = booking.bookingid\
        inner join property\
        on booking.propertyid = property.propertyid\
        inner join hasaddress\
        on property.propertyid = hasaddress.propertyID\
        inner join address\
        on hasaddress.addressid = address.addressId\
        inner join host\
        on payment.receiverID = host.hostID\
        where booking.guestID = {guestID};"
    result = database.execute_query(query_string)
    print('This is the output of the create bill')
    for row in result:
        print(row)

def new_phone_who_dis():
    '''
    Question 9
    Update the phone number of a guest.
    '''
    guestID = int(input('Please enter guest ID'))
    new_number = input('please enter new phone number: ')
    s = "{" + new_number + "}"
    query_string = f"update guest\
        set phonenum = '{s}'\
        where guestid = {guestID};"
    database.execute_query(query_string)
    return None

def firstNameFirst():
    '''
    Create and test a user-defined function named ​FirstNameFirst that combines two attributes of the 
    guest named ​firstName and ​lastName into a concatenated value named ​fullName [e.g.,​ James and ​Brown​ will be combined to read ​James Brown​].
    '''
    query_string = "select firstnamefirst(guest.firstname, guest.lastname) from guest"
    result = database.execute_query(query_string)
    print('This is the output of the function First Name First')
    for row in result:
        print(row)


def exit_program():
    exit()

if __name__ == "__main__":
    print("\nWelcome administrator, we've been expecting you.\n")
    
    while True:
        print('\n\nPlease select one of the following options: \n\
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
            11: Exit Program\n\n')

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



