# BrainfuckInterpreter
A Brainfuck interpreter made with Python.

Requires the module **readchar** to get keyboard input.
Install by running: `pip install readchar`

Can be started from a console or by double-clicking the script. File loading will be added later, currently you just copy-paste your code.  

Every character except for `+-<>[],.` will be ignored.

----
  
The interpreter uses a simple matching system for handling brackets which can be seen in function `cell_loop`. If there's no matching opening bracket `[` or closing bracket `]` it goes to the next character.
