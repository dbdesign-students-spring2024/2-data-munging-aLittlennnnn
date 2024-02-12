# Place code below to do the analysis part of the assignment.
f = open('./data/clean_data.csv', 'r')
lines = f.readlines()

last = int(lines[-1].strip().split(',')[0])
sums = 0
average = 0
count = 1880
firstc = 0
lastc = 0
dic = {}
dic1 = {}

for i in range(len(lines)-1):
    values = lines[i+1].strip().split(',')
    for j in range(12):
        sums += float(values[j+1])
    average = format(sums/12, ".1f")
    sums = 0
    dic[values[0]] = average
# print(last)

for j in range(len(dic)//10):
    firstc = count
    for i in range(10):
        sums += float(dic[str(count)])
        count += 1
    lastc = count - 1
    average = format(sums/10, ".1f")
    sums = 0
    dic1[str(firstc) + " to " + str(lastc)] = average
    average = 0

if count != last:
    firstc = count
    lastc = last
    c = 0
    while count != last:
        sums += float(dic[str(count)])
        count += 1
        c += 1

    average = format(sums/c, ".1f")
    dic1[str(firstc) + " to " + str(lastc)] = average

for key, value in dic1.items():
    print("The average temperature from " + key + " is " + value + ".")
