import random
from urllib.request import urlopen
""" The simplest way to use this module is to call the urlopen function,
which accepts a string containing a URL or a Request object (described
below). It opens the URL and returns the results as file-like
object; the returned object has some extra methods described below """
import sys
""" This module provides access to some variables 
used or maintained by the 
interpreter and to functions that interact 
 strongly with the interpreter."""


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = { 
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with parameters self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True 
else:   
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))
    # strip() removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
    # (space is the default leading character to remove)
    # readlines() reads until EOF using readline() and returns a list containing the lines.
    # The list is empty if the file is empty.

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:    
    print("\nBye")
# This exception is raised when the input() function hits an end-of-file condition (EOF) without reading any data.
# The EOFError is a subclass of the ValueError.

#------------------------------------------------   


