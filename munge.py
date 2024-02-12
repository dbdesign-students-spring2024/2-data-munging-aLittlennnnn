# Place code below to do the munging part of this assignment.
f = open('./data/raw.txt','r')
lines = f.readlines()
newline = []
count = 0

for i in range(len(lines)):
    if count == 0 and lines[i].startswith("Year"):
        newline.append(lines[i])
        count += 1
    elif lines[i].startswith("1") or lines[i].startswith("2"):
        newline.append(lines[i])

cleanline = []
cleandata = ""
for i in range(len(newline)):
    for j in range(len(newline[i])):
        if newline[i][j] != " ":
            cleandata += newline[i][j]
        else:
            if newline[i][j+1] != " ":
                cleandata += ","
    cleanline.append(cleandata)
    cleandata = ""

cleanline1 = []
cleandata1 = ""
cleanline1.append(cleanline[0])

for i in range(len(cleanline)-1):
    values = cleanline[i+1].strip().split(',')
    cleandata1 += values[0] + ","
    for j in range(len(values)-2):
        if values[j+1] != '***' and values[j+1] != '****':
            newvalue = format(float(values[j+1])/100*1.8,".1f")
            cleandata1 += newvalue + ","
        else:
            cleandata1 += values[j+1] + ","
    cleandata1 += values[-1] + "\n"
    cleanline1.append(cleandata1)
    cleandata1 = ""

# print(cleanline1)
newf = open('./data/clean_data.csv', 'w')

for i in range(len(cleanline1)):
    newf.write(cleanline1[i])






    
