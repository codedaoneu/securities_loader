import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def distance_point_to_point(test_point, train_point):
    d = test_point - train_point.reshape(test_point.shape)
    return np.sum(d*d)


def distance_test_point_to_all_train_point(test_point, train_point_matrix):
    X2 = np.sum(train_point_matrix*train_point_matrix, 1)
    z2 = np.sum(test_point*test_point)
    return X2 + z2 - 2*train_point_matrix.dot(test_point)


def weight(distances):
    sigma2 = 0.5
    return np.exp(-distances ** 2 / sigma2)


def k_nearest_neighbors(train_set, train_label, test_set, k):
    result = []
    for test_point in test_set:
        distances = distance_test_point_to_all_train_point(test_point, train_set)
        weight_distances = distances
        trained = sorted(list(tuple(zip(weight_distances, train_label))), key=lambda x: x[0])
        k_nearest_point = trained[:k]
        label = list(zip(*k_nearest_point))[1]
        result.append(max(set(label), key = label.count))
    return np.array(result)


if __name__ == "__main__":
    iris = datasets.load_iris()
    iris_x = iris.data
    iris_y = iris.target

    k = 10
    x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=50)

    clf = neighbors.KNeighborsClassifier(n_neighbors=k, p=2)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    # no lib training
    y_pred_no_lib = k_nearest_neighbors(train_set=x_train, train_label=y_train, test_set=x_test, k=k)
    #print result
    print(y_test)
    print("using sklearn")
    print(y_pred)
    print(100 * accuracy_score(y_test, y_pred))
    print("no library calculate")
    print(100 * accuracy_score(y_test, y_pred_no_lib))
    print("compare result")
    print(100 * accuracy_score(y_pred_no_lib, y_pred))

