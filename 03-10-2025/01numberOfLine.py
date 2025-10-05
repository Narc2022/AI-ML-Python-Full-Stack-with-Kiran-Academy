def count_line(file):
    f = open(file, 'r')
    count = 0
    for i in f:
        count = count + 1
    print(count)


count_line('demo.txt')
