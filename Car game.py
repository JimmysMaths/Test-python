import random

name_right = False
while name_right == False:
    name = input('What is your name(3-15)? ')
    name_number = len(name)
    if name_number < 3:
        print('name is too short just like your....')
    elif name_number > 15:
        print('one long name you have shorten it down')
    else:
        name_right = True


print('say -----> help')
in_car = True
in_jail = False
started = False
stopped = True
driving = False
object_middle = False
object_left = False
object_right = False
object_back = False
object_human = False
while in_car == True:
    car_command = input('> ')
    if car_command == 'start':
        if started == True:
            print(f'Car is already started {name}')
            stopped = False
        elif started == False:
            print(f'{name} starts the car')
            started = True
    elif car_command == 'stop':
        if stopped == True:
            print(f'Car is already started {name}')
            started = False
            driving = False
        elif stopped == False:
            print(f'{name} stops the car')
            stopped = True
    elif car_command == 'help':
        print("""
Commands-
start
stop
quit
drive
        """)
    elif car_command == 'drive':
        if started == True:
            print(f'{name} starts driving')
            driving = True
            print('say help to start drive around')
        else:
            print('start your car ' + name)
    elif car_command == 'quit':
        print("nooo don't leave " + name)
        break
    while driving == True:
        car_direction = input('> ')
        if car_direction == 'help':
            print("""
Forward(f)
Left(l)
Right(r)        
Brake(s)        
Backup(b)
quit(q)        
                    """)
        elif car_direction == 'f':
            random_f = random.randint(1, 4)
            if random_f == 1:
                if object_middle == True:
                    print('crash')
                elif object_human == True:
                    in_car = False
                    driving = False
                    in_jail = True
                elif object_middle == False:
                    print('the road end in 200ft choose left or right')
                    object_middle = True
                    object_left = False
                    object_right = False
                    object_human = False
            if random_f == 2:
                if object_middle == True:
                    print('crash')
                elif object_human == True:
                    in_car = False
                    driving = False
                    in_jail = True
                elif object_middle == False:
                    print('There is a Tree to your Left')
                    object_middle = False
                    object_left = True
                    object_right = False
                    object_human = False
            if random_f == 3:
                if object_middle == True:
                    print('crash')
                elif object_human == True:
                    in_car = False
                    driving = False
                    in_jail = True
                elif object_middle == False:
                    print('There is a truck to your right')
                    object_middle = False
                    object_left = False
                    object_right = True
                    object_human = False
            if random_f == 4:
                if object_middle == True:
                    print('crash')
                elif object_human == True:
                    in_car = False
                    driving = False
                    in_jail = True
                    object_human = False
                elif object_middle == False:
                    print('WATCH OUT THERE IS A FAMILY OF 4 IN FRONT OF YOU')
                    object_middle = False
                    object_left = False
                    object_right = False
                    object_human = True
        elif car_direction == 'l':
            random_l = random.randint(1, 4)
            if random_l == 1:
                if object_left == True:
                    print('crash')
                elif object_left == False:
                    print('the road end in 200ft choose left or right')
                    object_middle = True
                    object_left = False
                    object_right = False
                    object_human = False
            if random_l == 2:
                if object_left == True:
                    print('crash')
                elif object_left == False:
                    print('There is a Tree to your Left')
                    object_middle = False
                    object_left = True
                    object_right = False
                    object_human = False
            if random_l == 3:
                if object_left == True:
                    print('crash')
                elif object_left == False:
                    print('There is a truck to your right')
                    object_middle = False
                    object_left = False
                    object_right = True
                    object_human = False
            if random_l == 4:
                if object_left == True:
                    print('crash')
                elif object_left == False:
                    print('WATCH OUT THERE IS A FAMILY OF 4 IN FRONT OF YOU')
                    object_middle = False
                    object_left = False
                    object_right = False
                    object_human = True
        elif car_direction == 'r':
            random_r = random.randint(1, 4)
            if random_r == 1:
                if object_right == True:
                    print('crash')
                elif object_right == False:
                    print('the road end in 200ft choose left or right')
                    object_middle = True
                    object_left = False
                    object_right = False
                    object_human = False
            if random_r == 2:
                if object_right == True:
                    print('crash')
                elif object_right == False:
                    print('There is a Tree to your Left')
                    object_middle = False
                    object_left = True
                    object_right = False
                    object_human = False
            if random_r == 3:
                if object_right == True:
                    print('crash')
                elif object_right == False:
                    print('There is a truck to your right')
                    object_middle = False
                    object_left = False
                    object_right = True
                    object_human = False
            if random_r == 4:
                if object_right == True:
                    print('crash')
                elif object_right == False:
                    print('WATCH OUT THERE IS A FAMILY OF 4 IN FRONT OF YOU')
                    object_middle = False
                    object_left = False
                    object_right = False
                    object_human = True
        elif car_direction == 'b':
            random_b = random.randint(1, 3)
            if random_b == 1:
                if object_back == True:
                    print('crash')
                elif object_back == False:
                    print('the road end in 200ft choose left or right')
                    object_middle = True
                    object_left = False
                    object_right = False
                    object_human = False
            if random_b == 2:
                if object_back == True:
                    print('crash')
                elif object_back == False:
                    print('There is a Tree to your Left')
                    object_middle = False
                    object_left = True
                    object_right = False
                    object_human = False
            if random_b == 3:
                if object_back == True:
                    print('crash')
                elif object_back == False:
                    print('There is a truck to your right')
                    object_middle = False
                    object_left = False
                    object_right = True
                    object_human = False
        elif car_direction == 'q':
            print('You can never leave!')

while in_jail == True:
    print(f"{name} You Are Sick ")