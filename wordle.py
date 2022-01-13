words_dict = []
with open("dictionary.txt") as file:
    words_dict = file.readlines()
    
known_letters = [[],[],[],[],[]]
missed_letters = []
for i in range(1,6):
    if (len(words_dict)) > 1:
        word_guess = words_dict[0] #input("Guess #" + str(i) + ":")
        print("Guess #" + str(i) + ": "  + word_guess)
        guess_result = input("Result:")
        for char in range(5):
            if guess_result[char] == "X" and word_guess[char] not in known_letters:
                missed_letters.append(word_guess[char])
            elif guess_result[char] == "G":
                known_letters[char] = word_guess[char]
                if word_guess[char] in missed_letters:
                    missed_letters.remove(word_guess[char]) # make sure a repeat letter doesn't get put in the missed letters list
            elif guess_result[char] == "Y":
                known_letters[char].append(word_guess[char])
                if word_guess[char] in missed_letters:
                    missed_letters.remove(word_guess[char]) # make sure a repeat letter doesn't get put in the missed letters list

        next_guess = []
        for word in words_dict:
            candidate = True
            for l in missed_letters:
                if l in word:
                    candidate = False
                    break
            if candidate:
                for j in range(5):
                    if type(known_letters[j]) is list:
                        if word[j] in known_letters[j]:
                            candidate = False
                            break
                        for l in known_letters[j]:
                            if l not in word:
                                candidate = False
                                break
                    else:
                        if known_letters[j] != word[j]:
                            candidate = False
                            break
            if candidate:
                next_guess.append(word)

        if len(next_guess) < 25:
            print("Possible guesses:")
            print(*next_guess, sep='\n')
        words_dict = next_guess
    else:
        print("Solution: " + words_dict[0])
