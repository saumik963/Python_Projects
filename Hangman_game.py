import random
from termcolor import colored

wordlist=[line.strip() for line in open("hangman_list.txt")]
    

def choose_letter():
    word=random.choice(wordlist)

    cl=[]
    result=['_' for ch in word]
    l=len(word)*3
    for life in range(l):
        if "_" not in result:
            break
        print(colored( f"___You Have {l-life} life___",'cyan'))
        c=input("Choose a letter: ")

        if c=='exit':
            break
        cl.append(c)
        print(colored(f"Letters you have choosen: {cl}",'cyan'))
        
        for i in range(len(result)):
            if word[i]==c:
                result[i]=c
            print(result[i],end=' ')
        
        print()
    
    if "_" not in result:
        print(colored(f"WOW! You guess it: {word}","green"))
    else:
        print(colored(f"You Loose! The Word is: {word}",'red'))
        


print("\t______Welcome to Hangman______\n \tIt's a simple word gussing game. (Quit by typing exit)")

choose_letter()