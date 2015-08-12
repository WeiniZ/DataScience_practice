import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    dim = 5

    mat = record[0]
    row = record[1]
    col = record[2]
    val = record[3]

    for k in range(0, dim):
        if mat == 'a':
            mr.emit_intermediate((row, k), (mat, col, val))
        if mat == 'b':
            mr.emit_intermediate((k, col), (mat, row, val))

def reducer(key, list_of_values):
    dim = 5

    val_dict = {0:{'a':0, 'b':0},
                1:{'a':0, 'b':0},
                2:{'a':0, 'b':0},
                3:{'a':0, 'b':0},
                4:{'a':0, 'b':0}}
    result = 0
    
    for v in list_of_values:
        val_dict[v[1]][v[0]] = v[2]
       
    for k in range(0, dim):
        result += val_dict[k]['a']*val_dict[k]['b']

    mr.emit((key[0], key[1], result))
            

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)





