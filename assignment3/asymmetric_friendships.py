import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0]
    friend = record[1]
    list = [person, friend]
    list.sort()
    mr.emit_intermediate(str(list), list)

def reducer(key, list_of_values):
    list = []
    count = len(list_of_values)
    if count == 1:
        mr.emit((list_of_values[0][0], list_of_values[0][1]))
        mr.emit((list_of_values[0][1], list_of_values[0][0]))

if __name__== '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

