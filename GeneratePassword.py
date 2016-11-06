import sys
import random
import math

NUMBER_OF_WORDS_IN_PASSWORD = 4 #number of words in the password

#directory of dictionary, you have to execute this program from /home/user1337/SecureComputerSystemsGroup12 
DICTIONARY_PATH = "../../../usr/share/lib/dict/words" 

# The dictionary file is formatted as 'word1/n', 'word2\n' etc. so it looks like 
# apple
# cat
# Michigan
# ...

def main():
    password = "" #initalize password
    
    #put all dictionary words from the dictionary in a list called dictionaryWords
    with open(DICTIONARY_PATH) as file: 
        dictionaryWords = file.read().splitlines()

    #loop NUMBER_OF_WORDS_IN_PASSWORD times. In this case 4 times to generate a password with 4 words
    for _ in range(NUMBER_OF_WORDS_IN_PASSWORD): 
        #take a random word from the dictionary and use it in the password
        password = password +  random.choice(dictionaryWords) + " " 
        
    print(password)
    print str(NUMBER_OF_WORDS_IN_PASSWORD) + " RANDOM words from word list of " + str(len(dictionaryWords)) + " words"

   
    entropyOld = round(math.log(math.pow(len(dictionaryWords),NUMBER_OF_WORDS_IN_PASSWORD),2),2)
    entropyNew = entropyOld / math.log(62,2)
    print "Entropy:" + str(entropyOld) + " bits"
    print "You need "  + str(round(entropyNew)) + " RANDOM characters in [a-zA-Z0-9] to get the same entropy."
        
if __name__ == "__main__":
    main()
