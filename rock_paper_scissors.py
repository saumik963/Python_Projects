import random
from termcolor import colored

turn = ["rock", 'paper', 'scissors']

u_point = 0
c_point = 0

def update_points(user, computer):
    global u_point, c_point
    if user == computer:
        return
    elif (user == 'r' and computer == 'scissors') or \
         (user == 'p' and computer == 'rock') or \
         (user == 's' and computer == 'paper'):
        u_point += 1
    else:
        c_point += 1

def play():
    global u_point, c_point
    life = 3

    while life > 0:

        for l in range(life):
            print(colored("♥",'light_red'),end=' ')

        print()

        user = input(colored("User > ",'green'))
        if user=='q':
            break
        elif user not in ['r', 'p', 's']:
            print(colored("Invalid input. Try again.",'red') )

            continue
       

        computer = random.choice(turn)
        print(colored(f"Computer > {computer}",'cyan') )

        if user == computer[0]:
            pass
        else:
            life -= 1
            update_points(user, computer)

    print(colored(f"\n User Win (^_^) {u_point}",'green')) if u_point > c_point else print(colored(f"\n Computer Win (^!^) {c_point}",'light_red'))

if __name__ == '__main__':
    print(colored("________Rock Paper Scissors Game________\n   r = rock , p = paper , s = scissors (q to Quit)\n",'light_blue'))
    play()
