## BrainfuckInterpreter

A Brainfuck interpreter written in Python.

---

### Table Of Contents

* [Table of Contents](#table-of-contents)
* [Requirements](#requirements)
* [How To Run](#how-to-run)
* [Executable Release](#executable-release)
* [Debug Character](#debug-character)

---

### Requirements

The module **readchar** is required to get keyboard input.
This can be installed by running: `pip install readchar`

---

### How To Run

To run the interpreter you double-click `Interpreter.py` or call it from the command-line.

You can copy-paste code directly into the console, or you can load a file by typing `file:some_filename.bf` (supports any file extension).

Any character other than `+-` `<>` `[]` `,.` `!` will be ignored.

---

### Executable Release

A Windows executable file for the Brainfuck interpreter can be found and downloaded here: **[Releases](https://github.com/BenTearzz/BrainfuckInterpreter/releases)**

---

### Debug Character

The interpreter allows for an extra character to show the value of all cells and show what cell is currently selected (the default character is `!` ).

**Example 1:**  

```brainfuck
+++>!
```

This will output:

```
[3, 0]
    ^
```

**Example 2:**  

```brainfuck
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

---
