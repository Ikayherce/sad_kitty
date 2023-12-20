import random
from words import word_list

class Level:
    """
    Level class
    """
    def __init__(self, level):
        self.level = level

    def decide_level(self):
        """
        Decides level based on user input
        """
        if self.level == "1":
            print(Easy)
            return "Easy"
        elif self.level == "2":
            print(Medium)
            return "Medium"
        elif self.level == "3":
            print(hard)
            return "Hard"


def validate_level(value):
    """
    Checks if user input for level choice equals only 1, 2 or 3
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed {value}"
            )
    except ValueError as e:
        print(f"Invalid data:{e}, please try again\n")
        return False
    return True


def get_level():
    """
    Gets level value from user and creates word list accordingly
    """
    while True:
        chosen_level = input(
            "Choose your level:\n\n 1. Easy\n 2. Medium\n 3. Hard\n")
        level = Level(chosen_level).decide_level()

        if validate_level(chosen_level):
            filter_words(words, level)
            break
    word_list = filter_words(words, level)

    return word_list


def filter_words(words, level):
    """
    Filters words by length into seperate lists
    depending on chosen level
    """
    if level == "Easy":
        easy = [word for word in words if len(word) < 5]
        return easy
    elif level == "Medium":
        Medium = [word for word in words if len(word) < 10]
        return Medium
    elif level == "Hard":
        hard = [word for word in words if len(word) >= 10]
        return hard


def get_word():
    """This is the get word function. It gets a random word for the user to guess from the word list in words.py"""
    word = random.choice(word_list)
    return word.upper()

def play(word):
    """ 
    this is the play function. It checks and stores data provided by the user and gives feedback accordingly
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = [] #stores guessed letters
    guessed_words = [] #stores guessed words
    tries = 6 #number of tries before the whole sad kitty is on display
    print("Welcome to Hangman. Let's play!")# show welcome message
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter, or the whole word: ").upper()
        # check that user data is one letter or a word of the riht length
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters: #warns user letter has been already guessed
                print("You already guessed this letter!", guess)
            elif guess not in word:
                print("Oh no!", guess, "is not in the word.")  
                tries -= 1  #substract tries by 1 when guess is wrong
                guessed_letters.append(guess)
            else:
                print("Well done,", guess, "is in the word.")#print feedback to user when guess is correct
                guessed_letters.append(guess)
                #displays right guesses to user by replacing underscore by correctly guessed letter
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                #if all underscores are replaced by correctly guessed letters, word is guessed
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            #conditional block checks if word is guessed, if letter is already guessed 
            #and whether letter is or is not in the word. 
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            #if user has not provided a letter or word of correct length they get feedback that guess is invalid
            word_length = len(word)
            print("Your guess is not valid.")
            print(f"It needs to be a letter or a word of {word_length} length")
        #print display of hangman and of word completion
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    #check if user guessed or ran out of tries,print right feedback to user that they have won or lost the game
    if guessed:
        print("Congratulations, you guessed the word! You can be proud!")
    else:
        print("Oh no! You ran out of tries.")
        print(f"The word was {word}. Better luck next time!")


def display_hangman(tries):
    """
    This is the display function. 
    It displays the different stages of display of the disappointed cat, one stage for each failed try. 
    """
    stages = [  # final state: head, torso, paws, tail
                """
                          ／＞　 フ
                         | 　_　_| 
                       ／` ミ＿xノ 
                      /　　　　 |
                     /　 ヽ　　 ﾉ
                    │　　|　|　|
                ／￣|　　 |　|　|
                 (￣ヽ＿_ヽ_)__)
                  ＼二)

                               
                """,
                # head, torso and paws
                """
                  
                                         ／＞　 フ  
                                        | 　_　_| 
                                      ／` ミ＿xノ 
                                     /　　　　 |
                                    /　 ヽ　　 ﾉ
                                   │　　|　|　|

                """,
                # head and full torso
                """
                                         ／＞　 フ
                                        | 　_　_| 
                                      ／` ミ＿xノ 
                                     /　　　　 |
                                    /　 ヽ　　 ﾉ
                                   
                """,
                # head and some torso
                """
                           ／＞　 フ
                          | 　_　_| 
                        ／` ミ＿xノ 
                       /　　　　 |
                      
                """,
                # head
                """
                        ／＞　 フ
                       | 　_　_| 
                     ／` ミ＿xノ 
                      
                """,
                # ears and eyes
                """
                 ／＞　 フ
                | 　_　_| 
               
                """,
                # ears
                """
                  ／＞　 フ
                """,
                      # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]        

def main():
    """
    This function runs the game and asks user if they want to play again when game is over
    """
    decide_level()
    validate_level()
    filter_words()
    word = get_word() 
    play(word)
   
    
    while input("Do you want to play again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)

#code fragment so game runs by running the script on the command line
if __name__ == "__main__":
    main()
 











