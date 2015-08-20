import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import csv as csv

def main():
    # create the training & test sets
    dataset = pd.read_csv('train.csv')

    target = dataset.Cover_Type.values
    train = dataset.drop(['Cover_Type', 'Id'],axis=1).values 
	
    testset = pd.read_csv('test.csv')
    ids = testset.Id.values
    test = testset.drop('Id',axis=1).values

    # create and train the random forest
    # n_jobs set to -1 will use the number of cores present on your system.
    print 'Training...'
    rf = RandomForestClassifier(n_estimators=90, n_jobs = -1)
    rf.fit(train, target)
	
    print 'Predicting...'
    #output = rf.predict(test).astype(int)
    #predictions_file = open("myfirstforest.csv", "wb")
    #open_file_object = csv.writer(predictions_file)
    #open_file_object.writerow(["Id","Cover_Type"])
    #open_file_object.writerows(zip(ids, output))
    #predictions_file.close()
	
    loc_submission = "sub.csv"
    with open(loc_submission, "wb") as outfile:
        outfile.write("Id,Cover_Type\n")
        for e, val in enumerate(list(rf.predict(test))):
            outfile.write("%s,%s\n"%(ids[e],val))
	
if __name__ == "__main__":
    main()