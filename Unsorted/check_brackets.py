# python3

import sys
import os


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def brackets_on_stack(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                return i + 1
            bracket = opening_brackets_stack.pop()
            if not bracket.Match(next):
                return i + 1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack.pop().position - len(opening_brackets_stack) + 1


# Function for testing on examples from tests folder
def do_testing():
    test_folder = os.path.join(os.path.dirname(__file__), 'tests/')
    for fn in os.listdir(test_folder):
        file = test_folder + fn
        if os.path.isfile(file) and not file.endswith(".a"):
            text = open(file, 'r').read()
            solution = open(file + '.a', 'r').read().strip()
            print(brackets_on_stack(text))
            assert str(brackets_on_stack(text)) == solution, "{} is not {}".format(brackets_on_stack(text), solution)
    return True

if __name__ == "__main__":
    text = sys.stdin.read()
    print(brackets_on_stack(text))
    #do_testing()
