uname = 'aakash'
pwd= '12345'
while True:
    username = input("enter username: ")
    password = input('enter password: ')
    if username != uname:
        print('invalid username')
    if password != pwd:
        print('invalid password')
    if username == uname and password == pwd:
        print('login sucessfull')
        break
