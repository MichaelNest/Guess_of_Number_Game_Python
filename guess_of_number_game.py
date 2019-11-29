import random


low_digit = 10
high_digit = 50
digit = 0

count_input = 0
x= ''
play_game = True
win = False
start_score = 100
max_score = 0
score = 0


while(play_game):
    digit = random.randint(low_digit, high_digit)
    print('Компьютер загадал число - попробуй его отгадать!!')
    print(f'Guess computer number is: {digit}')
    while (not win):
        x = ''
        while (not x.isdigit()):
            x = input(f'Введите число от {low_digit} до {high_digit}: ')
            if (not x.isdigit()):
                print('.' * 22 + 'Вы ввели какую-то ересь. Введите пожалуйста число!!' + '.' * 22)
        x = int(x)

        if (x == digit):
            print('Победа!! Поздравляем!!')
            win = True
    if (input('Enter - сыграть еще; 0 - выход') == '0'):
        play_game = False
    else:
        win = False











