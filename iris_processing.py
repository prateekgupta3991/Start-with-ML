from sklearn.datasets import load_iris
import numpy as np

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