from sklearn.datasets import load_iris

iris_dataset = load_iris()
print (iris_dataset.feature_names)
print (iris_dataset.target_names)
print (iris_dataset.data[10])