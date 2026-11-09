import pyreadr
import random

# Load the R data file
data = pyreadr.read_r("data/italian_vocab_list.rda")

# Extract the data frame
vocab = next(iter(data.values()))

# Define main function with greetings message
def main():
    print("Welcome to The Italian Word Generator")
    print("You may translate one of two ways:")
    print("English -> Italian or Italian -> English")
    print()
    translator_method()

# Define translator method, whether Italian to English or vise versa
def translator_method():
    language = input("\'eng\' for E -> I, \'ita\' for I -> E, or anything else to quit: ")
    print()
    generator(language)

# Define random generator based on translator method
def generator(ie):
    # Random Word Generator for Italian to English
    if ie == "ita":
        play = True

        while play == True:
            word = random.choice(vocab.index)
            
            print("Italian:", vocab.loc[word, "Italian"])
            input("When ready for English, type \'r\': ")
            print("English:", vocab.loc[word, "English"])
            quest = input("'r' for next word: ")

            if quest == "r":
                print()
                print("Next word:")
            else:
                play = False

        else:
            print("Good job studying!")

    # Random Word Generator for English to Italian            
    elif ie == "eng":
        play = True

        while play == True:
            word = random.choice(vocab.index)
            
            print("English:", vocab.loc[word, "English"])
            input("When ready for Italian, type \'r\': ")
            print("Italian:", vocab.loc[word, "Italian"])
            quest = input("'r' for next word: ")
            if quest == "r":
                print()
                print("Next word")
            else:
                play = False
        else:
            print("Good job studying!")

    # Ends program if user does not put in a valid translator method          
    else:
        print("See you next time!")


main()
