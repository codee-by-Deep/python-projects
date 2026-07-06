with open("expenses.txt","r") as f:
    lines = f.readlines()
total = 0

for line in lines:
    part = line.strip().split(",")
    total = total + int(part[1])
    print(total) 