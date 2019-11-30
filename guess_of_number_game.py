import random


low_digit = 10
high_digit = 50
digit = 0
# count_input = 0
x= ''
play_game = True
win = False
start_score = 100
max_score = 0
# score = 0


while(play_game):
    digit = random.randint(low_digit, high_digit)
    print(('-'*50))
    count_input = 0
    score = start_score
    print('Компьютер загадал число - попробуй его отгадать!!')
    # print(f'Guess computer number is: {digit}')
    while (not win and score>0):
        print('-'*50)
        print(f'Заработано очков: {score}')
        print(f'Рекорд: {max_score}')

        x = ''
        while (not x.isdigit()):
            x = input(f'Введите число от {low_digit} до {high_digit}: ')
            if (not x.isdigit()):
                print('.' * 22 + 'Вы ввели какую-то ересь. Введите пожалуйста число!!' + '.' * 22)
        x = int(x)

        if (x == digit):
            win = True
        else:
            length = abs(x-digit)
            if(length<3):
                print('Очень горячо!!!')
            elif(length<5):
                print('Горячо!!')
            elif(length<10):
                print('Тепло!')
            elif(length<15):
                print('Прохладно')
            elif(length<20):
                print('Холодно')
            else:
                print('Просто жуткий мороз')

            if(count_input == 7):
                score -= 10
                if(digit%2 ==0):
                    print('Число четное')
                else:
                    print('Число нечетное')
            elif(count_input == 6):
                score -= 8
                if(digit%3==0):
                    print('Число делится на три')
                else:
                    print('Число не делится на три')
            elif (count_input == 5):
                score -= 4
                if (digit % 4 == 0):
                    print('Число делится на четыре')
                else:
                    print('Число не делится на четыре')
            elif (count_input >2 and count_input<5):
                score -= 2
                if (x>digit):
                    print('Загаданное число МЕНЬШЕ вашего')
                else:
                    print('Загаданное число БОЛЬШЕ вашего')
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
print('*'*50)
print('''Спасибо что сыграли в эту великолепную чудо-игру!! 
Возвращайтесь скорее - вы хорошо держались.
P.S. Это лучше чем играть в лохотрон!!''')








































