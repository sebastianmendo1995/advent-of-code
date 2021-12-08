my_file = open("instructions.txt", "r")
content = my_file.read()
instructions = content.split("\n")

my_file.close()

x = 0
y = 0

i = 0

while i < len(instructions):
  [dir, amount] = instructions[i].split(" ")
  if(dir == "forward"): x += int(amount)
  if(dir == "down"): y += int(amount)
  if(dir == "up"): y -= int(amount)

  i += 1

print(x*y)

# part 2

x = 0 
y = 0
aim = 0

i=0

while i < len(instructions):
  [dir, amount] = instructions[i].split(" ")

  if dir == "forward": 
    x += int(amount)
    y += aim * int(amount)

  if dir == "down": 
    aim += int(amount)

  if dir == "up": 
    aim -= int(amount)

  i += 1

print(x*y) 