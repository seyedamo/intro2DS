import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    d = 5
    table = record[0]
    row_id = record[1]
    col_id = record[2]
    value = record[3]
    if table == 'a':
        for k in range(d):
            mr.emit_intermediate([row_id, k], [col_id, value])
    if table == 'b':
        for k in range(d):
            mr.emit_intermediate([k, col_id], [row_id, value])

def reducer(key, list_of_values):
    for v in list_of_values:
        
    mr.emit((key))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

