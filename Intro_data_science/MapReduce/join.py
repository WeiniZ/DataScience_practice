import MapReduce
import sys

"""
Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: join variable identifier (order_id)
    # value: table row contents 
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: join variable identifier (order_id)
    # value: table content
    result = []
    for record in list_of_values:
        if (record[0] == "order"):
          for lineItem in list_of_values: 
            if (lineItem[0] != "order"):
               mr.emit(record+lineItem)
             
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
