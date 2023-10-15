import random
def play():
    user = input(">>>>>>>>'r'for Rock, 'p' for paper, 's' for sissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 0
    elif user == 'r' and computer == 'p':
        return -1
    elif user == 'r' and computer == 's':
        return 1
    elif user == 'p' and computer == 's':
        return -1
    elif user == 'p' and computer == 'r':
        return 1
    elif user == 's' and computer == 'r':
        return -1
    else:
        return 1
    
result = play()

if result==1:
    print('WON')
elif result==-1:
    print('LOSE')
else:
    print('TIE')