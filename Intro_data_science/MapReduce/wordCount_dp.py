
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
   key = record[0]
   value = record[1]
   word = value.split()
   for w in word:
       mr.emit_intermediate(w, 1)



def reducer(key, list_of_values):
   count = 0
   for v in list_of_values:
       count += v
   mr.emit((key, count))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
