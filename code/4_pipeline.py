from sklearn import datasets

iris = datasets.load_iris()


# X input, Y output, f(X) = Y
X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

from sklearn import tree 
# or from sklearn.neighbors import KNeighborsClassifier
# everything else is same
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)