safe_reports = 0
reports = open("reports.txt", "r")

for line in reports:
    safe = True
    split_line = line.split()
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
            
    if safe:
        safe_reports += 1
        
    # print(split_line, safe)
    
reports.close()

print("Total safe reports: " + str(safe_reports))