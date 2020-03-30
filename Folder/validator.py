import random
def gen_password(F_name,L_name,li):
    string = ''
    cuantos = random.sample(li,5)
    for i in cuantos:
        string +=i

    
    password = F_name[:2] + L_name[-2:] + string
    return password

container = dict()
def save(F_name,L_name,Email,password, container):
    temp = {}
    temp['first_name'] = F_name
    temp['last_name'] = L_name
    temp['Mail'] = Email
    temp['password'] = password
    container[Email] = temp
    return container

onboarding = True
while onboarding:
    
    F_name = input('enter your first name:')
    L_name = input('enter your last name:')
    Email = input('enter your mail address:')
    li = 'abcdefghijklmnopqrstuvwxyz0123456789'


    user_password = gen_password(F_name,L_name,li)
    response = input(f'your password is {user_password.capitalize()}, if you want to continue with it press enter,else enter a new password of choice:')
    if len(response)>=1 and len(response)<7:
        bouncer = True
        while bouncer:
            password = input('please enter a password with atleast 7 characters...')
            if len(password) < 7:
                bouncer = True
            else:
                bouncer = False
                user_password = password
    save(F_name,L_name,Email,user_password, container)
    
    registral = input('press any key to add another user, hit enter to quit:')
    if registral == '':
        onboarding = False
    else:
        continue
    for i in container:
        print()
        print('-----------------------------------------------------------------')
        print(f"FULL NAME: {container[i]['first_name'] +' ' +  container[i]['last_name']}")
        print(f"EMAIL ADDRESS: {container[i]['Mail']}")
        print('------------------------------------------------------------------')
    

        

