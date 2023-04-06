import random
attempts = 8
win_count = 0
lose_count = 0

print("H A N G M A N")

while True:
    user_answer = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    list_of_words = "python", "java", "swift", "javascript"
    rand_num = random.randint(0, len(list_of_words) - 1)
    word_to_guess = str(list_of_words[rand_num])
    printed_word = "-" * len(word_to_guess)
    guessed_letter = []
    if user_answer == "play":
        while True:
            print(" ")

            if attempts != 0 and printed_word != word_to_guess:
                print(printed_word)
                user_input = input("Input a letter:")

                if len(user_input) > 1 or len(user_input) < 1:
                    print("Please, input a single letter.")
                    continue

                elif not user_input.isalpha() or user_input.isupper():
                    print("Please, enter a lowercase letter from the English alphabet.")
                    continue

                elif user_input in word_to_guess and user_input not in printed_word:
                    word_so_far = ""

                    for i in range(len(word_to_guess)):
                        if user_input == str(word_to_guess[i]):
                            word_so_far += user_input

                        else:
                            word_so_far += printed_word[i]
                    guessed_letter.append(user_input)
                    printed_word = word_so_far
                    continue

                elif user_input in guessed_letter:
                    print("You've already guessed this letter.")
                    continue

                elif user_input not in word_to_guess:
                    print("That letter doesn't appear in the word.")
                    guessed_letter.append(user_input)
                    attempts -= 1
                    continue

            elif printed_word == word_to_guess:
                print("You guessed the word " + word_to_guess + "!")
                print("You survived!")
                win_count += 1
                break

            else:
                print("You lost!")
                lose_count += 1
                break

    elif user_answer == "results":
        print("You won: " + str(win_count) + " times.")
        print("You lost: " + str(lose_count) + " times.")
        continue

    elif user_answer == "exit":
        break

    elif len(user_answer) < 4:
        continue
