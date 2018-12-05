from sklearn import tree
features = [[140, 0], [160, 0], [150, 1], [180, 1]] # updating to real valued functions [0-smooth,1-bumpy]
labels = [0, 0, 1, 1] # updating to real valued functions [0-apple, 1-orange]
print (features, labels)

classifier = tree.DecisionTreeClassifier()
clf = classifier.fit(features, labels)
resultLabel = clf.predict([[150, 1], [160, 0], [190, 0]])
print (resultLabel)