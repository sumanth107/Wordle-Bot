# @uthor: $um@nth Nethi
# @date: 05-08-2022
import random
from collections import Counter

with open('wordset.txt', 'r') as f:
    lines = f.readlines()

words = [word.strip() for word in lines]


def word_result(word, guess):
    word_re = [''] * 5
    temp = []
    for i, x, y in zip(range(5), word, guess):
        if y == x:
            word_re[i] = 'c'
        elif y not in word:
            temp.append(x)
        else:
            temp.append(x)
    for i, y in enumerate(guess):
        if word_re[i] == 'c':
            continue
        elif y in temp:
            word_re[i] = 'x'
            temp.remove(y)
        else:
            word_re[i] = 'w'
    word_re = ''.join(word_re)
    return word_re


def update_wordset(current_wordset, guess, result):
    l = []
    for word in current_wordset:
        word_res = word_result(word, guess)
        if word_res == result:
            l.append(word)
    return l


def guesstimate(current_wordset):
    guess = ''
    if len(current_wordset) > 3300:
        freq = Counter()
        for word in current_wordset:
            freq.update(word)
        best = 0
        for word in current_wordset:
            curr = sum([freq[x] for x in set(word)])
            if curr > best:
                best = curr
                guess = word
        return guess
    w_avg = 3560 ** 2
    w_worst = 3560
    for x in current_wordset:
        avg, worst = 0, 0
        for y in current_wordset:
            temp = len(update_wordset(current_wordset, x, word_result(y, x)))
            avg += temp
            worst = max(worst, temp)
        if avg > w_avg:
            continue
        if avg < w_avg:
            w_avg = avg
            w_worst = worst
            guess = x
        elif worst < w_worst:
            w_worst = worst
            w_avg = avg
            guess = x
    return guess


def wordle():
    global words
    done = False
    current_wordset = words
    print("Hey there! Welcome to Wordle!")

    while not done:
        guess = guesstimate(current_wordset)
        print("Guess: " + guess.upper())
        result = input('Result: ')
        if not any(x in 'wxc' for x in result) or len(result) != len(guess):
            print("Invalid input. Try again.")
            continue
        if result == 'ccccc':
            done = True
            break
        current_wordset = update_wordset(current_wordset, guess, result)

    print("Done!!")


wordle()
