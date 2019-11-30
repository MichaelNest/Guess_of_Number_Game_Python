import random


def get_digit(low_digit, high_digit):
    digit = random.randint(low_digit, high_digit)
    print(('-' * 50))
    print('Компьютер загадал число - попробуй его отгадать!!')
    return digit

def podskazki_1(x, digit):
    length = abs(x - digit)
    if (length < 3):
        print('Очень горячо!!!')
    elif (length < 5):
        print('Горячо!!')
    elif (length < 10):
        print('Тепло!')
    elif (length < 15):
        print('Прохладно')
    elif (length < 20):
        print('Холодно')
    else:
        print('Просто жуткий мороз')


def podskazky_2(score, count_input, x, digit):
    if (count_input == 7):
        score -= 10
        if (digit % 2 == 0):
            print('Число четное')
        else:
            print('Число нечетное')
    elif (count_input == 6):
        score -= 8
        if (digit % 3 == 0):
            print('Число делится на три')
        else:
            print('Число не делится на три')
    elif (count_input == 5):
        score -= 4
        if (digit % 4 == 0):
            print('Число делится на четыре')
        else:
            print('Число не делится на четыре')
    elif (count_input > 2 and count_input < 5):
        score -= 2
        if (x > digit):
            print('Загаданное число МЕНЬШЕ вашего')
        else:
            print('Загаданное число БОЛЬШЕ вашего')

def include_loop_text(score, max_score):
    print('-' * 50)
    print(f'Заработано очков: {score}')
    print(f'Рекорд: {max_score}')

def finish_text():
    print('*'*50)
    print('''Спасибо что сыграли в эту великолепную чудо-игру!! 
    Возвращайтесь скорее - вы хорошо держались.
    P.S. Это лучше чем играть в лохотрон!!''')


def main():
    low_digit = 10
    high_digit = 50
    digit = 0
    x = ''
    play_game = True
    win = False
    start_score = 100
    score = start_score
    max_score = 0
    count_input = 0

    while(play_game):
        digit = get_digit(low_digit, high_digit)

        while (not win and score>0):
            include_loop_text(score, max_score)
            x = ''
            while (not x.isdigit()):
                x = input(f'Введите число от {low_digit} до {high_digit}: ')
                if (not x.isdigit()):
                    print('.' * 22 + 'Вы ввели какую-то ересь. Введите пожалуйста число!!' + '.' * 22)
            x = int(x)
            if (x == digit):
                win = True
            else:
                podskazki_1(x, digit)
                podskazky_2(score, count_input, x, digit)
                score -=5
            count_input +=1

        print('*'*50)
        if(x==digit):
            print('Победа!! Поздравляем!!')
        else:
            print('У вас закончились очки - вы проиграли.(")')
        if (input('Enter - сыграть еще; 0 - выход') == '0'):
            play_game = False
        else:
            win = False
        if(score>max_score):
            max_score = score

    finish_text()

if __name__ == '__main__':
    main()


