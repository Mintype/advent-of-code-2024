raw_input = open("input.txt", "r")

is_reading_rules = True
rules = []
updates = []
sum = 0

for line in raw_input:
    if is_reading_rules:
        if line == "\n":
            is_reading_rules = False
            continue
        rule = line.split("|")
        for i in range(len(rule)):
            rule[i] = int(rule[i])
        rules.append(rule)
    else:
        update = line.split(",")
        for i in range(len(update)):
            update[i] = int(update[i])
        updates.append(update)

for update in updates:
    in_order = True
    for rule in rules:
        if update.__contains__(rule[0]) and update.__contains__(rule[1]):
            if update.index(rule[0]) > update.index(rule[1]):
                in_order = False
                break
    if in_order:
        sum += update[int(len(update)/2)]
        
print(sum)