with open('sort.txt') as inf:
    data = []
    for line in inf:
        line = line.split()
        print('here is your lines', line)
        if len(line) == 2:
            data.append(line)

            # if you are cool, you can convert it to tuple

            #data.append(tuple(line))
data.sort()


print(data)



