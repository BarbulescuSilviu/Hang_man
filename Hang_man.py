import random

cuvinte = ['python', 'masina', 'apa', 'tastatura', 'paine', 'sunet', 'palindrom', 'nor', 'ploaie', 'vreme', 'fericire',
           'albastru','rosu', 'verde', 'gri', 'calculator', 'laptop', 'medicina', 'aviatie', 'avion', 'planor',
           'ubicuitate']


def print_word(word):
    cuvant_final = ''
    for i in word:
        cuvant_final += i
    return cuvant_final


word = random.choice(cuvinte)
guesses = []
answer = []
for i in range(len(word)):
    answer.append('_')
# print(answer)

while len(guesses) < 5:
    if '_' not in answer:
        print(f'BRAVO, ai ghicit cuvantul {word}')
        break
    print('guess the word:')
    print(print_word(answer))
    guess = input('guess one character at a time:\n> ')
    if guess not in word:
        guesses.append(guess)
        if len(guesses) < 5:
            print(f'you have {5 - len(guesses)} tries left')
        else:
            print('you lost')
    else:
        for i in range(len(word)):
            if word[i] == guess:
                answer[i] = guess