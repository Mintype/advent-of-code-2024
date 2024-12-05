safe_reports = 0
reports = open("reports.txt", "r")

def is_safe_report(split_line):
    safe = True
    for i in range(len(split_line)):
        split_line[i] = int(split_line[i])
        
    increasing = False
    if split_line[0] < split_line[1]:
        increasing = True
    elif split_line[0] == split_line[1]:
        safe = False
    
    if safe:
        for i in range(len(split_line) - 1):
            if increasing and split_line[i] >= split_line[i + 1] or abs(split_line[i + 1] - split_line[i]) > 3:
                safe = False
                break
            elif not increasing and split_line[i] <= split_line[i + 1] or abs(split_line[i + 1] - split_line[i]) > 3:
                safe = False
                break
    
    return safe
    

for line in reports:
    split_line = line.split()
    safe = is_safe_report(split_line)
            
    if safe:
        safe_reports += 1
    else:
        for i in range(len(split_line)):
            list_copy = split_line.copy()
            list_copy.pop(i)
            safe = is_safe_report(list_copy)
            if safe:
                safe_reports += 1
                break
        
    # print(split_line, safe)
    
reports.close()

print("Total safe reports: " + str(safe_reports))