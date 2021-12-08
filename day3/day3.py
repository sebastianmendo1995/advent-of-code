my_file = open("diagnostic.txt", "r")
content = my_file.read()
binaryNumbers = content.split("\n")
my_file.close()

totalOfNumbers = len(binaryNumbers)

digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in binaryNumbers:
    arr = list(number)
    i = 0
    while i < len(arr):
        digits[i] = digits[i] + int(arr[i])
        i += 1

print(digits)
print(totalOfNumbers)

gamma = ""
epsilon = ""

j = 0
while j < len(digits):
    if(digits[j] > totalOfNumbers/2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    j += 1

gammaDecimal = int(gamma, 2)
epsilonDecimal = int(epsilon, 2)

print(gammaDecimal * epsilonDecimal)

#part 2

