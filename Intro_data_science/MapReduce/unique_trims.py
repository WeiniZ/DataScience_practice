
import MapReduce
import sys

"""
Friends count in the Simple Python MapReduce Framework
"""
#Part1

mr = MapReduce.MapReduce()


#Part2

def mapper(record):
    #key: DNA nucleotides
    nucleotides = record[1] 
    mr.emit_intermediate(nucleotides[:-10], 1)


#Part3
    
def reducer(key, list_of_value):
    #key: DNA nucleotides 
    mr.emit(key)


#Part4
    
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

