#add this class to completly different  file
class Game:
    def __init__(self, question, hint, solution):
        self.__question = question
        self.__hint = hint
        self.__solution = solution

    # add set method for each variable defined in init
    def set_question(self, question):
        self.__question = question


    def set_hint(self, hint):
        self.__hint = hint

    def set_solution(self, solution):
        self.__solution = solution


    #add get method for each variable
    def get_question(self):
        return self.__question

    def get_hint(self):
        return self.__hint

    def get_solution(self):
        return self.__solution

