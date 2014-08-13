import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    list = []
    dedup_values = set(list_of_values)
    count = len(dedup_values)
    mr.emit((key, count))

if __name__== '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

