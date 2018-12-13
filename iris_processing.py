from sklearn.datasets import load_iris
import numpy as np
from sklearn.tree import DecisionTreeClassifier

iris_dataset = load_iris()
delete_data_idx = [0, 50, 100] #Based on data distribution

# removing data at specific indices to prepare for training and predicting
# using numpy to delete data at specific indices provided as array of indices.
# I am a python noob
# training data
train_data = np.delete(iris_dataset.data, delete_data_idx, axis = 0)
train_target = np.delete(iris_dataset.target, delete_data_idx)

print ("train data")
for i in range(len(train_target)) :
    print ("Count %d : label %s, features %s" % (i, train_target[i], train_data[i]))

# test data
test_data = iris_dataset.data[delete_data_idx]
test_target = iris_dataset.target[delete_data_idx]

print ("test data")
for i in range(len(test_target)) :
    print ("Count %d : label %s, features %s" % (i, test_target[i], test_data[i]))

clf = DecisionTreeClassifier()
clf.fit(train_data, train_target)
clf = clf.predict(test_data)

print (clf)

# splitting internal datasets for train and test
# method 2

from sklearn.cross_validation import train_test_split
X = iris_dataset.data
Y = iris_dataset.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5)
m2_split_train = list(zip(X_train, Y_train))
m2_split_test = list(zip(X_test, Y_test))

print ("train")
for i in range(len(m2_split_train)) :
    print ("idx %d value %s" % (i, m2_split_train[i]))
print ("test")
for i in range(len(m2_split_test)) :
    print ("idx %d value %s" % (i, m2_split_test[i]))