# Brainfuck Interpreter
from readchar import readchar

class BrainfuckInterpreter():
    def __init__(self):
        self.cells = [0]
        self.index = 0

        self.shifting   = {">": 1, "<":-1}
        self.increment  = {"+": 1, "-":-1}

        self.cell_value_max = 255

        code = input("Brainfuck code: ")
        if code.strip() != "":
            self.interpret(code.strip())

    def interpret(self, code):
        c = 0

        while c < len(code):
            char = code[c]

            if char == ">" or char == "<":
                self.cell_shifting(char)

            if char == "+" or char == "-":
                self.cell_increment(char)


            if char == "[":
                c = c + self.cell_loop(char, code[c:])
            elif char == "]":
                c = c + self.cell_loop(char, code[:c])

            # Input & Output
            if char == ",":
                self.cells[self.index] = ord(readchar())
                print(chr(self.cells[self.index]), end='', flush=True)
            elif char == ".":
                print(chr(self.cells[self.index]), end='')

            c += 1

        #print(self.cells)
        input() # So that it doesn't just close when done

    def cell_shifting(self, char):
        self.index += self.shifting[char]

        if self.index < 0:
            self.index = 0

        if self.index > len(self.cells)-1:
            self.cells.append(0)

    def cell_increment(self, char):
        self.cells[self.index] += self.increment[char]

        if self.cells[self.index] < 0:
            self.cells[self.index] = self.cell_value_max

        if self.cells[self.index] > self.cell_value_max:
            self.cells[self.index] = 0

    def cell_loop(self, char, code):
        match = 0
        i = 0

        if char == "[":

            if self.cells[self.index] != 0:
                return 0

            while match != 1:
                if i == len(code):
                    return 1

                if code[i] == "[":
                    match -= 1

                if code[i] == "]":
                    match += 1

                i += 1

            return i

        if char == "]":

            if self.cells[self.index] == 0:
                return 0

            while match != 1:
                if i == -len(code):
                    return 1

                if code[i] == "]":
                    match -= 1

                if code[i] == "[":
                    match += 1

                i -= 1

            return i+1

bf = BrainfuckInterpreter
bf()
