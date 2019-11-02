import csv

def read(path):
    csv_reader = csv.reader(open(path,'r'), delimiter=",")
    next(csv_reader)
    my_list = list()
    for row in csv_reader:
        my_list.append(row)
    return my_list