USER_TYPES = {'admin', 'employee', 'user'}

def welcome():
    current_user_type = ''
    print('Welcome to GroundBnB, your one stop shop for corona free rentals!')
    print('Please enter your user type: admin, employee, or user:')
    while current_user_type not in USER_TYPES:
        current_user_type = str(input())
        if current_user_type not in USER_TYPES:
            print('Please type in lowercase your user type:')
    return current_user_type

def launch_app(user_type):
    if user_type == 'admin':
        execfile('admin.py')
    if user_type == 'employee':
        execfile('employee.py')
    if user_type == 'user':
        execfile('user.py')

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        '__file__': filepath,
        '__name__': '__main__',
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

if __name__ == '__main__':
    current_user_type = welcome()
    launch_app(current_user_type)
