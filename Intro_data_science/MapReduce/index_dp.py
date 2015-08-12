import sys
import MapReduce


mr = MapReduce.MapReduce()


def mapper(record):
    content = record[1]
    book = record[0]
    words = content.split()
    for w in words:
        mr.emit_intermediate(w, book)



def reducer(key, list_of_values):
    book_list = []
    for v in list_of_values:
        book_list.append(v)

    mr.emit((key, book_list))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


    
