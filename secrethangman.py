import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
print secret 
def initialize(): 
    print secret
    print ("We have a secret word")
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = str(raw_input())
def ifWon():
    if secret == updateWord:
        i = 0
        while i<len(secret):
            if secret[i] == letter:
                pos=secret.find(letter)
                updateWord[pos] = letter
        print updateWord.join()
        print ("you win")
        
    else:
        getLetter()
def main():
    while True:
        initialize ()
        getLetter()
        ifWon()
main()
def test():
    global secret
    print secret
    global updateWord
    letter=int(input("What is letter :"))
    if letter in secret:
        pos=secret.find(letter)
        updateWord[pos] = letter
        print updateWord.join()
        print ("yay")
        ifWon()
    else:
        getLetter()
        print("no")
        






  
    
    
    

