from sklearn.datasets import load_iris

iris_dataset = load_iris()
print (iris_dataset.feature_names)
print (iris_dataset.target_names)
print (iris_dataset.data[10])
print (iris_dataset.target[2])

for i in range(len(iris_dataset.target)):
    print ("Example %d : label %s, features %s" % (i, iris_dataset.target[i], iris_dataset.data[i]))