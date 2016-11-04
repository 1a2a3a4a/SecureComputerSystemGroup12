import sys
import random
import math

WORDS_PATH = "../../../usr/share/lib/dict/words" #directory of dictionary, you have to execute this program from /home/user1337/SecureComputerSystemsGroup12 
NUMBER_OF_WORDS = 4 #number of words in the password



def main():
    password = "" #initalize password

    with open(WORDS_PATH) as file: #put all words from the dictionary in a list called words
        words = file.read().splitlines()

    for _ in range(NUMBER_OF_WORDS): #loop NUMBER_OF_WORDS times
        password = password +  random.choice(words) + " " #take a random word from the dictionary and use it in the password

    print(password)
    print str(NUMBER_OF_WORDS) + " RANDOM words from word list of " + str(len(words)) + " words"
    #TODO calculate entropy
    #print "Entropy:" + str(round(math.log(math.pow(len(words),NUMBER_OF_WORDS), 
        
    
        

    



if __name__ == "__main__":
    main()
