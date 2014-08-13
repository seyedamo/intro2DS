import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    id = record[1]
    mr.emit_intermediate(id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    list = []
    order_list = []
    line_list = []
    for v in list_of_values:
        if v[0] == 'order':
            order_list.append(v)
        if v[0] == 'line_item':
            line_list.append(v)
    for order in order_list:
        for line in line_list:
            list = order + line
            mr.emit((list))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
