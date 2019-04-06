# Brainfuck Interpreter
from readchar import readchar

import platform, os

if platform.system() == "Windows":
	import ctypes
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


#######'''#######
# - MAIN LOOP - #
#######'''#######

def main():
	os.system("clear || cls") # Clear Console

	debug_character = "!"
	character = 0

	global cells
	cells = [0]
	index = 0

	code = input("Brainfuck code: ")

	if "file:" in code:
		with open(code[code.index("file:") + 5:].strip()) as f:
			code = f.read()

	while character < len(code):
		char = code[character]

		# INDEX
		if char == "<":
			if index != 0:
				index -= 1

		elif char == ">":
			index += 1

			if index > len(cells) - 1:
				cells.append(0)

		# VALUES
		elif char == "+":
			cells[index] += 1

			if cells[index] > 255:
				cells[index] = 0

		elif char == "-":
			cells[index] -= 1

			if cells[index] < 0:
				cells[index] = 255

		# LOOPING
		elif char == "[":
			if cells[index] != 0:
				pass
			else:
				character += loop(char, code[character:])

		elif char == "]":
			if cells[index] == 0:
				pass
			else:
				character += loop(char, code[:character])

		# I/O
		elif char == ",":
			cells[index] = ord(readchar())
			print(chr(cells[index]))

		elif char == ".":
			print(chr(cells[index]), end="") # to print on one-line (default: "\n")

		# DEBUG
		elif char == debug_character:
			
			print("[", end="")
			i = 0

			for cell in cells:

				if i == index:
					print(f"\033[1;32;40m{cell}\033[0m", end="")
				else:
					print(f"{cell}", end="")

				if i < len(cells) - 1:
					print(", ", end="")

				i += 1

			print("]")

		character += 1

	input("\033[33;1m\n\n------\n Done\n------\033[0m")
	main()


#####''#####
# - LOOP - #
#####''#####

def loop(char, code):
	match = 0
	index = 0

	add = 1 if char == "[" else -1

	while match != 1:
		if index == len(code) * add:
			return 0

		if code[index] == "[":
			match -= add

		if code[index] == "]":
			match += add

		index += add

	if char == "[":
		return index
	else:
		return index + 1

main()