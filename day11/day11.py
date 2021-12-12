example = open("example.txt", "r").read()
puzzle = open("puzzle.txt", "r").read()

example = [int(i) for i in example.split(",")]
puzzle = [int(i) for i in puzzle.split(",")]