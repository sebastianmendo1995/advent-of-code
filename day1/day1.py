my_file = open("numbers.txt", "r")
content = my_file.read()
numbers = content.split("\n")

my_file.close()

count=0
secondCount=0

i = 1

print(numbers)

while i < len(numbers):
  if int(numbers[i]) > int(numbers[i-1]) : count += 1
  i += 1

print(count)

j=0
while  j < len(numbers)-3:
    prev = int(numbers[j]) + int(numbers[j+1]) + int(numbers[j+2])
    next = int(numbers[j+1]) + int(numbers[j+2]) + int(numbers[j+3])
    if(prev < next): secondCount+=1
    j+=1

print(secondCount)