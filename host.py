import database

def upload_new_property():
    hostID = -1
    while hostID < 1:
        print('Please enter your host assimilation number:')
        try:
            hostID = int(input())
        except:
            print('Invalid input format')
    print('Welcome to the borg collective, host {}'.format(hostID))

    addressID = insert_into_address()
    propertyID = insert_into_property(addressID)
    rentalID = insert_into_rental(propertyID, hostID)
    insert_into_has_address(addressID, propertyID)
    insert_into_has_agreement(rentalID, propertyID)
    insert_into_signedby(hostID, rentalID)
    return None

def insert_into_address():
    line1 = input('Enter first line of address: ')
    city = input('Enter city: ')
    province = input('Enter province code: ')
    country = input('Enter Country: ')
    postal_code = input('Enter postal code')
    query_string = f"insert into address(addressl1,addressl2,city,province,country,postalcode)\
        values ('{line1}',null,'{city}','{province}','{country}','{postal_code}')\
        RETURNING addressID"
    result = database.execute_query(query_string)
    return result[0][0]
    
def insert_into_property(addressID):
    query_string = f"insert into property(addressID,buildingType,roomtype,accomodates,amenities,bathrooms,availability,beds,price)\
        values ({addressID},'house','double',3,'WIFI, Pets, Laundry',1,'available','{{Double,Single}}',144.00)\
        returning propertyID"
    result = database.execute_query(query_string)
    return result[0][0]

def insert_into_rental(propertyID, hostID):
    query_string = f"insert into rentalagreement(propertyID,hostID,signingdate,startdate,enddate)\
        values ({propertyID},{hostID},'2020-01-22','2020-02-29','2021-02-28')\
        returning rentalID;"
    result = database.execute_query(query_string)
    return result[0][0]

def insert_into_has_address(addressID, propertyID):
    query_string = f"insert into hasAddress(addressId,propertyID)\
        values ({addressID},{propertyID});"
    database.execute_query(query_string)

def insert_into_has_agreement(rentalID, propertyID):
    query_string = f"insert into hasagreement(rentalID,propertyID)\
        values ({rentalID},{propertyID});"
    database.execute_query(query_string)

def insert_into_signedby(hostID, rentalID):
    query_string = f"insert into signedby(hostID,rentalID)\
        values ({hostID},{rentalID});"
    database.execute_query(query_string)

def list_my_properties():
    hostID = -1
    while hostID < 1:
        print('Please enter your host assimilation number:')
        try:
            hostID = int(input())
        except:
            print('Invalid input format')
    print('Welcome to the borg collective, host {}'.format(hostID))

    query_string = f"select host.hostid, property.* from property\
        inner join rentalagreement\
        on rentalagreement.propertyid = property.propertyid\
        inner join host\
        on host.hostid = rentalagreement.hostid\
        where host.hostid = {hostID};"

    result = database.execute_query(query_string)
    print('Your listed properties are:')
    for row in result:
        print(row)

def exit_program():
    exit()

if __name__ == "__main__":

    while True:
        print('\n\n\nPlease select one of the following options: \n\
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