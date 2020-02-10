out = open("Данные2таблица.txt", 'w')
src = open("Данные2.txt", 'r')
i = 0
while (src.readable()):
    a = src.readline().strip().split()
    b = src.readline().strip().split()
    if (len(a) == 0 or len(b) == 0):
        break
    if (int(a[-1]) < i):
        out.write(str(int(a[-1]) + 45323) + "\t" + b[-1] + "\n")
    else:
        out.write(a[-1] + "\t" + b[-1] + "\n")
    i+=1

