import random
import os


words = {"game","born","corn","morning","loan","name","monster","lover","lover","nigga","bitch","mover"}
word = random.choice(list(words))

os.system("cls")
def hangman():
    word = random.choice(list(words))
    #get two random unique words 
    hint = random.sample(word,2)
    #get index of the hintwords
    hint_indeces = [word.index(h) for h in hint]

    #populate the word to be displayed
    display_word=""
    for i in range(len(word)):
        if i in hint_indeces:
           display_word += word[i]+" "
        else:
           display_word += " _ "  

    print(display_word) 

    
hangman()