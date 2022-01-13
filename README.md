# wordle-solver

(Requires Python 3)  

To play:
1. Run wordle.py (`python3 /path/to/wordle.py`).  The solver will make an initial guess (first word in the dictionary.txt file)
2. The user is prompted to provide feedback on the result of the guess.  The expected format is a 5 letter string consisting only of 'X' (indicates a letter that doesn't exist in the word), 'Y' (indicates a letter that exists in the word but is misplaced), and 'G' (indicates a letter that is correctly placed in the word)
3. The solver continues to guess and prompt for feedback until a solution is determined

The solver's guess ranking is currently very dumb-- it just ranks in order of the words in the dictionary file.  Next step is to determine a way to score/rank guesses based on the currently-known information from previous guesses
