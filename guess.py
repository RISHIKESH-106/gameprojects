'''
Number Guessing Game
-------------------------------------------------------------
'''

import random


def show_score(attempts_list):
    if not attempts_list:
        print('There is currently no best score,'
              ' it\'s yours for the taking!')

    else:
        print(f'The current best score is'
              f' {min(attempts_list)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    attempts_list = []

    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name?: ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score(attempts_list)

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1

            if guess == rand_num:
                attempts_list.append(attempts)
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score(attempts_list)
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()




# '''
# Chat Bot
# -------------------------------------------------------------
# 1) pip install ChatterBot chatterbot-corpus spacy
# 2) python3 -m spacy download en_core_web_sm
#    Or... choose the language you prefer
# 3) Navigate to your Python3 directory
# 4) Modify Lib/site-packages/chatterbot/tagging.py
#   to properly load 'en_core_web_sm'
# '''


# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# def create_chat_bot():
#    chatbot = ChatBot('Chattering Bot')
#    trainer = ChatterBotCorpusTrainer(chatbot)
#    trainer.train('chatterbot.corpus.english')

#    while True:
#        try:
#            bot_input = chatbot.get_response(input())
#            print(bot_input)

#        except (KeyboardInterrupt, EOFError, SystemExit):
#            break


# if __name__ == '__main__':
#    create_chat_bot()