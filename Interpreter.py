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

	# ---------------- #
	global cells
	cells = [0]
	index = 0
	character = 0
	# ---------------- #

	code = input("Brainfuck code: ")

	# File Load
	if "file:" in code:
		with open(code[code.index("file:") + 5:].strip()) as f:
			code = f.read()

	# Interpret
	while character < len(code):
		char = code[character]

		# INDEX
		if char == "<":
			if index != 0:			# Decrement cell index
				index -= 1

		elif char == ">":			# Increment cell index
			index += 1

			if index > len(cells) - 1:
				cells.append(0)

		# VALUES
		elif char == "+":			# Increment cell value
			cells[index] += 1

			if cells[index] > 255:
				cells[index] = 0

		elif char == "-":			# Decrement cell value
			cells[index] -= 1

			if cells[index] < 0:
				cells[index] = 255

		# LOOPING
		elif char == "[":
			if cells[index] != 0: # If current cell is NOT 0 -> pass
				pass
			else:
				character += loop(char, code[character:])

		elif char == "]":
			if cells[index] == 0: # If current cell IS 0 -> pass
				pass
			else:
				character += loop(char, code[:character])

		# I/O
		elif char == ",":
			cells[index] = ord(readchar())	 # Get keyboard character
			print(chr(cells[index]))		 # Print keyboard input character

		elif char == ".":
			print(chr(cells[index]), end="") # Print current cell value

		# DEBUG
		elif char == debug_character:
			print("[", end="")
			i = 0

			for cell in cells:

				if i == index:
					print(f"\033[1;32;40m{cell}\033[0m", end="") # Highlight current cell
				else:
					print(f"{cell}", end="")

				if i < len(cells) - 1:
					print(", ", end="")	# Add comma seperator when at the last cell

				i += 1

			print("]")

		character += 1

	# End
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