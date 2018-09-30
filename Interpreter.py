# Brainfuck Interpreter
from readchar import readchar
from sys import argv

class BrainfuckInterpreter():
    def __init__(self):
        self.cells = [0] # Create a cell
        self.index = 0   # Start at cell 0

        self.shifting   = {">": 1, "<":-1}  # Shortcut for shifting cells
        self.increment  = {"+": 1, "-":-1}  # Shortcut for incrementing & decrementing cells

        self.cell_value_max = 255   #255 is the max ASCII value

        code = None
        if len(argv[1:]) > 0:       # Check if an argument was passed
            file = argv[1].strip()  # Set file to the first argument
            try:
                f = open(file, "r") # Open file for reading
                code = f.read()     # Read file and save the content in variable "code"
            except Exception as err:
                print("Error: ", str(err))
                raise SystemExit

        if code == None:
            code = input("Brainfuck code: ")

        if code.strip() != "":
            self.interpret(code.strip())
        else:
            print("No code")
            raise SystemExit

    def interpret(self, code):
        c = 0   # Start at character 0

        while c < len(code):
            char = code[c]  # Character / Symbol is the currentcharacter in our code

            # Shifting
            if char == ">" or char == "<":
                self.cell_shifting(char)

            # Incrementing & Decrementing
            if char == "+" or char == "-":
                self.cell_increment(char)

            # Looping
            if char == "[":
                c = c + self.cell_loop(char, code[c:])
            elif char == "]":
                c = c + self.cell_loop(char, code[:c])

            # Input & Output
            if char == ",":
                self.cells[self.index] = ord(readchar())
                print(chr(self.cells[self.index]))
            elif char == ".":
                print(chr(self.cells[self.index]), end="") # end="" to print on one-line (default: "\n")

            #print(self.cells, "["+char+"]") # Uncomment if you want to see what happens step-by-step
            c += 1

        #print(self.cells)
        input() # So that it doesn't just close when done

    # Shifting
    def cell_shifting(self, char):
        self.index += self.shifting[char]

        if self.index < 0:                  # If the cell index is below 0
            self.index = 0                  # Make the cell index 0

        if self.index > len(self.cells)-1:  # If the cell index is above the current amount of cells
            self.cells.append(0)            # Create a new cell.

    # Incrementing & Decrementing
    def cell_increment(self, char):
        self.cells[self.index] += self.increment[char]

        if self.cells[self.index] < 0:                      # If the cell value is below 0
            self.cells[self.index] = self.cell_value_max    # Make the cell value "cell_value_max" (Default: 255)

        if self.cells[self.index] > self.cell_value_max:    # If the cell value is above "cell_value_max" (Default: 255)
            self.cells[self.index] = 0                      # Make the cell value 0

    # Looping
    def cell_loop(self, char, code):
        match = 0
        i = 0

        if char == "[":

            if self.cells[self.index] != 0: # If our current cell is NOT 0
                return 0                    # Return 0 (it does c += 1 in the "interpret" function)
                                            # Stays at current cell, "c += 1" will move to the instruction inside [ ]

            while match != 1:
                if i == len(code):
                    return 0

                if code[i] == "[":
                    match -= 1

                if code[i] == "]":
                    match += 1

                i += 1

            return i

        if char == "]":

            if self.cells[self.index] == 0: # If our current cell is 0
                return 0                    # Return 0 (it does c += 1 in the "interpret" function)
                                            # Stays at current cell, "c += 1" will move to the instruction outside of the ]
            while match != 1:
                if i == -len(code):         # If we're at the last cell and there's no match
                    return 0                # Stays at current cell, "c += 1" will move to the instruction outside of the ]

                if code[i] == "]":
                    match -= 1

                if code[i] == "[":
                    match += 1

                i -= 1

            return i

bf = BrainfuckInterpreter
bf()
