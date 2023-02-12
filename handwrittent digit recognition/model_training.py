import numpy as np
from sklearn.metrics import accuracy_score


def calculate_centroid(train_X, train_y):
    centroids = []
    for i in range(len(set(train_y))):
        data = train_X[train_y == i, :]
        centroid = np.mean(data, axis=0)
        centroids.append(centroid)
    return np.array(centroids)


def distances(x_test, centroids):
    centroids = centroids.reshape(centroids.shape[0], centroids.shape[1] * centroids.shape[2])
    x_test = x_test.reshape(x_test.shape[0] * x_test.shape[1])
    X2 = np.sum(centroids * centroids, 1)
    z2 = np.sum(x_test * x_test)
    D = X2 + z2 - 2 * centroids.dot(x_test)
    return np.argmin(D)


def get_labels(test_X, centroids):
    labels = []
    for i in range(test_X.shape[0]):
        labels.append(distances(test_X[i], centroids))
    return np.array(labels)


if __name__ == "__main__":
    from keras.datasets import mnist
    (train_X, train_y), (test_X, test_y) = mnist.load_data()
    centroids = calculate_centroid(train_X, train_y)
    y_pred = get_labels(test_X, centroids)

    # testing with a image from train set.
    test_point = np.array([train_X[20]])
    test_point_pred = get_labels(test_point, centroids)
    print("real label is: ")
    print(train_y[20])

    # print result:
    print("test point pred is: ")
    print(test_point_pred[0])

    print("accuracy is: ")
    print(accuracy_score(test_y, y_pred)*100, " %")
