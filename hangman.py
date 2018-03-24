import requests
from urllib.request import urlopen

r = requests.get('http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=false&minCorpusCount=0&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=10&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5')

secret_word = r.json()[0]['word'].lower()

def hangman(random_word):
    guess = input("Guess: ").lower()
    num_guesses = 10
    guess_word = ["-"]*(len(random_word))
    while num_guesses > 1:
        i = 0
        if guess in random_word:
            while i < len(random_word):
                if random_word[i] == guess:
                    guess_word[i] = guess
                    print ("".join(guess_word))
                i += 1
            if "-" in guess_word:
                print ("Guesses remaining: " + str(num_guesses))
                print ("".join(guess_word))

            else:
                print("Congratulations! You guessed correctly! The secret word is: " + random_word)
        else:
            num_guesses -= 1
            print ("Guesses remaining: " + str(num_guesses))
            print ("".join(guess_word))
        guess = input("Guess: ").lower()
    print ("Sorry, you lost. The secret word was: " + random_word)

hangman(secret_word)
