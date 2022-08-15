
import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
 Print()
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word =random.choice(word_list)  # random.choice to pick up random words from the list
        self.list_letters= []
        self.word_guessed = list(len(self.word) * '_')  # 
        self.word_list = word_list
        self.num_lives = num_lives 
        self.num_letters = len(self.word)

        

        print(f"The mystery word has {len(self.word)} characters")
        print (self.word_guessed)
        pass

    def check_letter(self, letter):
        letter = letter.lower()
       
        if letter in self.word:
        
            for index,character in  enumerate(self.word): 
                if character == letter: 
               
                    self.word_guessed[index] = letter
        #if letter in self.word:
                    print(f"{letter} in the word ")
                    print (self.word_guessed) 
        else:

            self.num_lives  -= 1         
             
            print(f"number of live let {self.num_lives}")         
            #self.list_letters.append(letter)   
             #for i in self.num_lives:
              #  i == self.num_lives 
               # i -=1
                #if i == 4:
                 #print ("\|\||")
                #elif i == 3                    
                            

                                                        
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        
        while True:      
            letter = input("pick a letter: ")
            if len(letter) > 1:
              print("Please, enter just one character" )
            elif letter in self.list_letters:
                 print (f" {letter}  was already tried" )
            else :
                #self.list_letters.append(letter)
                print(self.list_letters)
                self.check_letter(letter)

            
        
        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives ==0:
            print(f"You ran out of lives. The word was {game.word}") 
            break        
        elif game.num_letters > 0:
            game.ask_letter()
    
    
        else:
            print ("Congratulations, you won!")
            break 
       
    
     
        pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
