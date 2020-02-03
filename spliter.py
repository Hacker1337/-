out = open("Данные1таблица.txt", 'w')
src = open("Данные1.txt", 'r')
while (src.readable()):
    a = src.readline().strip().split()
    b = src.readline().strip().split()
    if (len(a) == 0 or len(b) == 0):
        break

    out.write(a[-1] + "\t" + b[-1] + "\n")
