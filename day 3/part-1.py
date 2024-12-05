memory_input = open("memory.txt", "r")
sum = 0
for line in memory_input:
    memory = line.split("mul")
    for item in memory:
        if item.startswith("(") and ")" in item:
            item = item.split(")")[0]
            item = item[1:]
            try:
                numbers = item.split(",")
                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])
                sum += numbers[0] * numbers[1]
            except ValueError:
                continue
            
print("Sum of all memory values: " + str(sum))