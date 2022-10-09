#importing libraries
import random
import colorama
colorama.init()

#opening a downloaded dictionary 
wordlist = open("a.txt", "r")
a = []

#checking each if a word has 5 letters and if it does, stores it in a variable, takes a random word from the variable and makes it into a list.
for line in wordlist:
  if len(line.strip()) == 5:
    a.append(line.strip())
word = random.choice(a)
word = list(word)
print(word)

#checks if the user's guess is the correct word
for i in range(5) :
    guess = input("Please enter a 5 letter word of your choice: ")
    guess = list(guess)
    if guess == word:
        print("good job!")
        break

    string = ""
    map = {}

#For example: check if the first letter of guess is the same as the first letter of word, if it is, then mark it green,
#if it's not but it exists within the word mark it yellow(also checks if a guess has more of the same letters than in the word and if it does it only marks those that are below 
# or equal to the number of the same letters in word), if it doesn't exist within a word, mark it black
    for j in range(5):
        colour = colorama.Fore.BLACK
        if guess[j] == word[j]:
            colour = colorama.Fore.GREEN
            if guess[j] in map:
                map[guess[j]] += 1
            else:
                map[guess[j]] = 1   
        elif guess[j] != word[j] and guess[j] in word:

            if guess[j] in map:
                map[guess[j]] += 1
            else:
                map[guess[j]] = 1   

            if word.count(guess[j]) >= map[guess[j]]:
                colour = colorama.Fore.YELLOW

        string += colour + guess[j] + colorama.Fore.RESET
    print(string)

#telling the user that they ran out of attempts and the game is lost
else: 
    print("you lose")