abc = " abcdefghijklmnopqrstuvwxyz"

t = int(input())
while t > 0:
    line = input()
    sum = 0
    if len(line) == 1:
        print('Bob ' + str(abc.index(line)))
    elif len(line) % 2 == 0:
        for i in line:
            sum += abc.index(i)
        print('Alice ' + str(sum))
    else:
        if line[0] > line[len(line) - 1]:
            for i in line[0:len(line) - 1]:
                sum += abc.index(i)
            print("Alice " + str(sum - abc.index(line[len(line) - 1])))
        else:
            for i in line[1:len(line)]:
                sum += abc.index(i)
            print("Alice " + str(sum - abc.index(line[0])))
    t -= 1