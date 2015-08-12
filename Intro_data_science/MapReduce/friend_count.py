
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
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key,1)


#Part3
def reducer(key, list_of_value):
    #key: Person A
    #value: list of friend count
    total = 0
    for v in list_of_value:
        total += v
    mr.emit((key,total))

#Part4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

    
