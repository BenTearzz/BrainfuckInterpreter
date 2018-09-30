# BrainfuckInterpreter
A Brainfuck interpreter made with Python.

Requires the module **readchar** to get keyboard input.
Install by running: `pip install readchar`

Load a file containing Brainfuck code. (Parsed as an argument) `Interpreter.py myfile.ext` (All file extensions supported).
Copy-pasting code is also possible, simply double-click Interpreter.py or run it without any arguments: `Interpreter.py`

Every character except for `+-<>[],.` will be ignored.

----
  
The interpreter uses a simple matching system for handling brackets which can be seen in function `cell_loop`. If there's no matching opening bracket `[` or closing bracket `]` it goes to the next character.
