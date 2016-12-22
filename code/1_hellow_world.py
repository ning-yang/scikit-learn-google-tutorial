from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # input, (weight, texture)
labels = [0, 0, 1, 1]  # output, 0 => apple, 1 => orange

classifier = tree.DecisionTreeClassifier()
classifier.fit(features, labels) # Train the classifier

print(classifier.predict([160, 0]))