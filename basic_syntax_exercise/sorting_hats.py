while True:
    command=str(input())
    if command=="Welcome!":
        print(f'Welcome to Hogwarts.')
        break
    elif command=="Voldemort":
        print(f'You must not speak of that name!')
        exit()
    else:
        if len(command)<5:
            print(f'{command} goes to Gryffindor.')
        elif len(command)==5:
            print(f'{command} goes to Slytherin.')
        elif len(command)==6:
            print(f'{command} goes to Ravenclaw.')
        else:
            print(f'{command} goes to Hufflepuff.')