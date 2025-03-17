#input_id = input('id: ')
#id1 = 'Hebu'
#id2 = 'admin'
#
#if input_id == id1:
#    print('Hello Hebu!')
#elif input_id == id2:
#    print('Hello admin!')
#else:
#    print('Who are you?')


input_id = input('id: ')
id = 'Hebu'
input_password = input('password: ')
password = '1234'

if input_id == id:
    if input_password == password:
        print('Welcome!')
    else:
        print('Wrong Password!')
else: 
    print('wrong id')