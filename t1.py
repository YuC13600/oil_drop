import csv

with open('no_chart.csv', newline='') as f:
    rows = list(csv.reader(f, delimiter=','))
    del rows[0]

    least = float(rows[0][5])
    for row in rows:
        print(row[5])
        least = float(row[5]) if float(row[5]) < least else least

    print('smallest:' + str(least))
        
