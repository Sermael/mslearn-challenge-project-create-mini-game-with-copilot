#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option. The computer will then randomly generate a choice. After that, the winner of the game will be outputted.

import random

def start():
    choose = input('Enter one of the three options rock, paper or scissors:')

    if choose == 'rock' or choose == 'paper' or choose == 'scissors':
        print('You chose:', choose)
        #use the random function to choose between rock, paper, or scissors
        computer = random.randint(1, 3)

        score = 0

        if computer == 1:
            computer = 'rock'
        elif computer == 2:
            computer = 'paper'
        else:   
            computer = 'scissors'

        print('Computer chose:', computer)

        if choose == computer:
            print('It is a tie')

        elif choose == 'rock':
            if computer == 'paper':
                print('Computer wins')
                score = score -1
            else:
                print('You win')
                score = score +1

        elif choose == 'paper':
            if computer == 'scissors':
                print('Computer wins')
                score = score -1
            else:
                print('You win')
                score = score +1

        elif choose == 'scissors':
            if computer == 'rock':
                print('Computer wins')
                score = score -1
            else:
                print('You win')
                score = score +1
        
        play = input('Do you want to play again? Y/N:')

        if play == 'Y' or play == 'y':
            print('Score:', score)
            start()
        elif play == 'N' or play == 'n':
            print('Score:', score)
            print('Thanks for playing')
        else:
            print('Invalid option')
    else:
        print('Invalid option')





start()