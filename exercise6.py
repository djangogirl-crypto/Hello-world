inp1=input('enter your choice:')
inp2=input('enter your choice:')

if inp1==inp2:
    print('tie')
elif inp1== 'rock':
    if inp2 == 'scissors':
        print('congo')
    else:
        print('paper wins')
elif inp1== 'scissors':
    if inp2 == 'paper':
        print('congo')
    else:
        print('rock wins')

elif inp1== 'paper':
    if inp2 == 'rock':
        print('congo')
    else:
        print('scis wins')