import csv

with open('no_chart.csv', newline='') as f:
    
    rows = list(csv.reader(f, delimiter=','));

    del rows[0]

    # print smallest Q
    smallest = float(rows[0][5])
    for row in rows:
        smallest = float(row[5]) if float(row[5]) < smallest else smallest

    print('smallest Q: {:.2e}'.format(smallest))

    # use +-4% as error
    error = 0.04
    print('error = +-' + str(error))

    for row in rows:
        Q = float(row[5])
        row.append(Q * (1 - error))
        row.append(Q * (1 + error))

    # since the smallest Q is 7.1771e-19
    # we can suppose that e is less than or equal to it
    # thus we use loop that take 120% of smallest Q as initial_value
    # and to find the answer with three digits fraction part
    # it decrement 0.001E-18 each time
    e = float(smallest) * (1 + error)
    flag = True
    while(flag):
        flag = False

        for row in rows:
            times = 1
            while times < 100 and e * times < row[-2]:
                times += 1
            if e * times > row[-1]:
                flag = True

        if flag:
            e -= 0.001E-19

    print('e = ' + str(e))


