# BrainfuckInterpreter
A Brainfuck interpreter written in Python.

Requires the module **readchar** to get keyboard input.
Install by running: `pip install readchar`

Load a file containing Brainfuck code. (Parsed as an argument) `Interpreter.py myfile.ext` (All file extensions supported).
Copy-pasting code is also possible, simply double-click Interpreter.py or run it without any arguments: `Interpreter.py`

Every character except for `+-` `<>` `[]` `,.` will be ignored.

----

The interpreter allows for an extra character to show current cells. To enable the character, go to line 37 and set the variable "show_cells_enabled" to True. By default the current cells character is an exclamation mark **!**. So when **!** is in your code, it will show a list of current cells and also what cell you're on.  
You can change the character used to show the current cells by changing "show_cells_character" on line 38.  

**Example 1:**  
```
+++>!
```  
This will output
```
[3, 0]
    ^
```  

**Example 2:**  
```
!       # [0]
+++>!   # [3, 0]
+       # [3, 1]
<--!    # [1, 1]
```  
This will output:
```
[0]
 ^
[3, 0]
    ^
[1, 1]
 ^
```  

----

The interpreter uses a simple matching system for handling brackets which can be seen in function `cell_loop`. If there's no matching opening bracket `[` or closing bracket `]` it goes to the next character.
