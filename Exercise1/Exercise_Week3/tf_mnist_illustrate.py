from sklearn.neighbors import KNeighborsClassifier
import pickle

import matplotlib.pyplot as plt

from random import random
from random import randint
import numpy as np

def main():
    # 1. tf_mnist_dump_data.py - Loads MNIST data using TF and dumps as pickle
    # 2. tf_mnist_illustrate.py - Loads dump and shows images






    # Read MNIST data from dumped pickle
    data_fname = 'mnist_fashion.pkl'

    with open(data_fname,'rb') as data_file:
        x_train = pickle.load(data_file)
        y_train = pickle.load(data_file)
        x_test = pickle.load(data_file)
        y_test = pickle.load(data_file)


    # Print the size of training and test data
    print(f'x_train shape {x_train.shape}')
    print(f'y_train shape {y_train.shape}')
    print(f'x_test shape {x_test.shape}')
    print(f'y_test shape {y_test.shape}')
    print(y_test.shape[0])


    my_1nn(x_train,y_train, x_test)

    for i in range(x_test.shape[0]):
        # Show some images randomly
        if random() > 0.999:
            plt.figure(1);
            plt.clf()
            plt.imshow(x_test[i], cmap='gray_r')
            plt.title(f"Image {i} label num {y_test[i]} predicted {0}")
            plt.pause(1)
            print()
    pred = [randint(0,9) for _ in range(y_test.shape[0])]
    pred = np.array(pred)
    print()

    ratio = my_cl_acc(pred, y_test)
    print(ratio)


def my_cl_acc(pred, gt):
    value_list = []
    for i, j in zip(pred, gt):
        if i == j:
            value_list.append(True)
        else:
            value_list.append(False)
    ratio = sum(value_list)/len(value_list)
    return ratio

def my_1nn(x_train, y_train,x_test):

    x_train = x_train.reshape(60000,784)
    x_test = x_test.reshape(10000,784)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train, y_train)


    y_pred = knn.predict(x_test)
    np.savetxt('PRED_mnist_fashion.dat',y_pred)
    print()


if __name__ == "__main__":
    main()
