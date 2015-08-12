import MapReduce
import sys

"""
Friends count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


#Part2
def mapper(record):
    #key: Person A
    #value: Person A's friend
    if record[0] > record[1]:
       key = (record[0], record[1])
    else:
       key = (record[1], record[0])
    mr.emit_intermediate(key,1)


#Part3
def reducer(key, list_of_value):
    #key: Person A
    #value: list of friend count 
      mr.emit((key[0],key[1]))
      mr.emit((key[1],key[0]))

#Part4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
