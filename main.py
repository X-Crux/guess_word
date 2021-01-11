from random import choice


def start_game():
    words_bank = [
        'дорога', 'мороженое', 'дерево',
        'телефон', 'аккредитация', 'шапка',
        'страна', 'лето', 'пароход'
    ]

    secret_word = choice(words_bank)

    # print(secret_word)

    gamer_word = ['*'] * len(secret_word)
    print(''.join(gamer_word))

    errors_counter = 0
    while True:
        letter = input('Введите ОДНУ русскую букву:\n').lower()
        if len(letter) != 1:
            continue

        if letter in secret_word:  # to contain -> contains
            for idx, symbol in enumerate(secret_word):  # (num, item)
                if symbol == letter:
                    gamer_word[idx] = letter
            if gamer_word.count('*') == 0:
                print('Вы выиграли ;)')
                print('Было загадано слово:', secret_word.upper())
                break
        else:
            errors_counter += 1
            print('Ошибок допущено:', errors_counter)
            if errors_counter == 8:
                print("Вы проиграли ;(")
                break
        print(''.join(gamer_word))

    print('Возвращайтесь!')

if __name__ == '__main__':
    start_game()
