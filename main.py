import random

def show_menu(choices):
    
    okay = False
    while not okay:
        print('=' * 20)
        for i in choices:
            print(f'{i}: {choices[i]}')
        print('=' * 20)
        choice = input('Choice: ').upper()
        if choice in choices:
            okay = True
        else:
            print('\nError: Please type a single letter to choose one of the options\n')
    return choice

def practice():
    times = int(input("How many times do you want to practice? "))

    with open('words.txt', "r") as the_file:
        the_text = the_file.read()

    raw = the_text.strip().split('----')

    words = []
    meanings = []

    for w in raw:
        word, meaning = w.strip().split('\n')
        words.append(word)
        meanings.append(meaning)

    types = ["words", "meanings"]

    for i in range(0, int(times)):
        word_or_meaning = random.choice(types)
        if word_or_meaning == 'words':
            the_word = random.choice(words)
            guess = input(f"What does the word {the_word} mean? ")
            index = words.index(the_word)
            if guess == meanings[index]:
                print(f"You got it, the word means: {meanings[index]}")
            else:
                print(f"The wording is not exact, maybe you got it right anyway, check your answer. The word means: {meanings[index]}. You answered {guess}")
        else:
            the_meaning = random.choice(meanings)
            guess = input(f"What does '{the_meaning}' mean? ")
            index = meanings.index(the_meaning)
            if guess == words[index]:
                print(f'Thats right, the word was: {words[index]}!')
            else:
                print(f'did you get it correct, check your answer. The word was: {words[index]}. You answered: {guess}')

    print("Well done you have completed your practice!")
    

def add_words():
    print('Adding words...')

def edit_words():
    print('Editing words...')


sections = {
        'A': 'Practice',
        'B': 'Add words',
        'C': 'Edit words',
        'Q': 'Quit'
    }
finished = False
while not finished:
    section = show_menu(sections)

    if section == 'A':
        practice()
    elif section == 'B':
        add_words()
    elif section == 'C':
        edit_words()
    elif section == 'Q':
        finished = True
    else:
        print('Unknown selection - error!')

quit()



