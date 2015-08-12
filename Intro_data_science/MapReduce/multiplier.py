import MapReduce
import sys



mr = MapReduce.MapReduce()

def mapper(record):
    matrix_length = 5
    matrix_name = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
     
    for k in range(0,matrix_length):
       if (matrix_name == "a"):
           mr.emit_intermediate((row, k), (matrix_name, col, val))
       else:
           mr.emit_intermediate((k,col), (matrix_name, row, val))


def reducer(key, list_of_values):
   matrix_length = 5
   result = 0

   #Fix for missing values
   val_fix =  {0:{"a":0, "b":0},
               1:{"a":0, "b":0},
               2:{"a":0, "b":0},
               3:{"a":0, "b":0},
               4:{"a":0, "b":0}} 
   
   for v in list_of_values:
      val_fix[v[1]][v[0]] = v[2]

   for k in val_fix.keys():
       result += val_fix[k]["a"]*val_fix[k]["b"]
       
   mr.emit((key[0],key[1],result))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
