import random  # imports random library


def randWord(word, i=None):  # defines function randWord which takes 2 parameters
    try:  # try this following code and see if it has an exception
        for string in '-,_/*+?><;:[]{}`~"!@#$%^&*()|.=0123456789':  # checks if the string has any special characters
            word = word.replace(string, '')  # removes special characters
        random.seed(i)  # sets the random seed from the second parameter
        a = random.choice(word.split())  # split the words up in the string and randomly choice one
        return a  # return the answer to line 9
    except:  # try this following code and see if it has an exception
        print('input is not a string or word')  # print statement that tells the user the issue
        quit(True)  # exit the program


def strMixer(word, i=None):  # defines function strMixer which takes 2 parameters
    try:  # try this following code and see if it has an exception
        for string in '-,_/*+?><;:[]{}`~"!@#$%^&*()|.=0123456789':  # checks if the string has any special characters
            word = word.replace(string, '')  # removes special characters
        random.seed(i)  # sets the random seed from the second parameter
        if len(word.split()) > 1:  # checks if there is more than one word
            word = word.split()  # splits up the word
            random.shuffle(word)  # shuffle the position of the word
            result = ' '.join(word)  # joins the shuffled words back together with spaces
            return result  # returns the answer in line 24
        else:  # if there is only 1 word then it shuffles the letters
            word = list(word)  # puts the string into a list where each letter is its own element
            random.shuffle(word)  # shuffles the position of the letters
            result = ''.join(word)  # joins the letters together without spaces
            return result  # returns line 29
    except:  # try this following code and see if it has an exception
        print('input is not a string or word')  # print statement that tells the user the issue
        quit(True)  # exit the program


def randIntForWord(word, i=None):  # defines function randIntForWord which takes 2 parameters
    try:  # try this following code and see if it has an exception
        if len(word.split()) > 1:  # checks if there is more than one word
            return 'Only accepts 1 word with no spaces'  # print statement that tells the user the issue
        else:  # if there is only 1 word proceed
            for string in '-,_/*+?><;:[]{}`~"!@#$%^&*()|.=0123456789':  # checks if the string has any special character
                word = word.replace(string, '')  # removes special characters
            if i is not None:  # checks if i is not None
                random.seed(str(i) + word)  # adds the str of i to word
                return random.randint(0, 100000)  # returns a value from 0 to 100k using the random seed
            else:
                random.seed(word)  # the seed is word which is the first parameter
                return random.randint(0, 100000)  # returns a value from 0 to 100k using the random seed
    except:  # try this following code and see if it has an exception
        print('input was not a string')  # print statement that tells the user the issue
        quit(True)  # exit the program


if __name__ == "__main__":  # checks if this is being called directly or is imported
    print("Sorry, but this module can only be imported!")  # prints this if it is being called directly
