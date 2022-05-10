import GameClass


def main():
    theme1 = GameClass.Game("Class Subject: ", "4 letters", "Math")
    theme2 = GameClass.Game("BOSS LEVEL (+2), Sports: ", "6 Letters", "Soccer")
    theme3 = GameClass.Game("BOSS LEVEL (+2), Soda: ", "5 letters", "Pepsi")
    theme4 = GameClass.Game("BOSS LEVEL (+2), Coding Language: ", "6 letters", "Python")
    user_question = 'Please enter the word you think the theme answer is: '
    score = 6
    level1 = [theme1]
    level2 = [theme2, theme3, theme4]
    for query in level1:
        print(query.get_question())
        user_input = input(user_question)

        if user_input == query.get_solution():
            score = score + 3
        else:
            score = score
            hint_check = input('Do you want a hint (Y or N)? ')
            if hint_check.upper() == 'Y':
                print(query.get_hint())
                user_input = input(user_question)
                if user_input == query.get_solution():
                    score = score + 3
                else:
                    score = score - 3
            else:
                user_input = input(user_question)
                if user_input == query.get_solution():
                    score = score + 3
                else:
                    score = score
                    print('The provided answer is incorrect. Here is the correct answer: ' + query.get_solution())
                    for query in level1:
                        print(query.get_question())
                        user_input = input(user_question)

                        if user_input == query.get_solution():
                            score = score + 3
                        else:
                            score = score
                            hint_check = input('Do you want a hint (Y or N)? ')
                            if hint_check.upper() == 'Y':
                                print(query.get_hint())
                                user_input = input(user_question)
                                if user_input == query.get_solution():
                                    score = score + 3
                                else:
                                    score = score - 3
                            else:
                                user_input = input(user_question)
                                if user_input == query.get_solution():
                                    score = score + 3
                                else:
                                    score = score
                                    print(
                                        'The provided answer is incorrect. Here is the correct answer: ' + query.get_solution())

    for query in level2:
        print(query.get_question())
        user_input = input(user_question)

        if user_input == query.get_solution():
            score = score + 2
        else:
            score = score
            hint_check = input('Do you want a hint (Y or N)? ')
            if hint_check.upper() == 'Y':
                print(query.get_hint())
                user_input = input(user_question)
                if user_input == query.get_solution():
                    score = score + 2
                else:
                    score = score - 2
            else:
                user_input = input(user_question)
                if user_input == query.get_solution():
                    score = score + 2
                else:
                    score = score
                    print('The provided answer is incorrect. Here is the correct answer: ' + query.get_solution())
                    for query in level2:
                        print(query.get_question())
                        user_input = input(user_question)

                        if user_input == query.get_solution():
                            score = score + 2
                        else:
                            score = score
                            hint_check = input('Do you want a hint (Y or N)? ')
                            if hint_check.upper() == 'Y':
                                print(query.get_hint())
                                user_input = input(user_question)
                                if user_input == query.get_solution():
                                    score = score + 2
                                else:
                                    score = score - 2
                            else:
                                user_input = input(user_question)
                                if user_input == query.get_solution():
                                    score = score + 2
                                else:
                                    score = score
                                    print(
                                        'The provided answer is incorrect. Here is the correct answer: ' + query.get_solution())

    print("Points: ", str(score))


main()
