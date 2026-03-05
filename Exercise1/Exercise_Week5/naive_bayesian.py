import pickle
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization
from tensorflow.keras.utils import to_categorical
from scipy.stats import multivariate_normal




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

    x_train = (x_train.reshape(-1, 784).astype("float32") / 255.0)

    x_train = x_train + np.random.normal(loc=0.0, scale=0.05, size=x_train.shape)
    x_test = x_test.reshape(-1, 784).astype("float32") / 255.0


    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    print()



    mean_1, var_1, cov_1 = my_calc_meanvar(x_train, y_train)
    #x = x_test[i]

    x_exp = x_test[:, np.newaxis, :]  # (N_test, 1, 784)
    mean_exp = mean_1[np.newaxis, :, :]  # (1, 10, 784)
    var_exp = var_1[np.newaxis, :, :]





    print()
    log =  -0.5 * np.sum(np.log(2*np.pi)+np.log(var_exp)+(x_exp-mean_exp)**2/var_exp, axis=2)


    y_pred = np.argmax(log, axis=1)

    y_pred = np.array(y_pred)

    pred_classes = np.argmax(y_test, axis=1)
    accuracy = np.mean(y_pred == pred_classes)
    print("Classification accuracy is", accuracy)

    np.savetxt("PRED_bayes.dat", pred_classes, fmt="%d")

    #multivariate(mean_1, var_1, cov_1, x_test, pred_classes)



    print()

def my_calc_meanvar(x_train, y_train):
    classes_num = y_train.shape[1]
    param_num = x_train.shape[1]

    mean_1 = []
    var_1 = []
    cov_1 = []


    for k in range(classes_num):
        y_k = y_train[:,k]
        x_k = x_train[y_k == 1]

        mean = np.mean(x_k, axis = 0)
        var = np.var(x_k, axis = 0)
        print()
        mean_1.append(mean)
        var_1.append(var)

        cov = np.cov(x_k, rowvar=False)
        cov_1.append(cov)

    mean_1, var_1, cov_1 = np.array(mean_1), np.array(var_1), np.array(cov_1)

    return mean_1, var_1, cov_1

def multivariate(mean_1,var_1,cov_1, x_test, pred_classes):
    log_probs = []
    for k in range(mean_1.shape[0]):
        rv = multivariate_normal(mean=mean_1[k], cov=cov_1[k], allow_singular=False)
        logp = rv.logpdf(x_test)  # (N_test,)
        log_probs.append(logp)

    log_probs = np.array(log_probs).T  # shape (N_test, 10)
    y_pred = np.argmax(log_probs, axis=1)

    accuracy = np.mean(y_pred == pred_classes)
    print("Classification accuracy is", accuracy)

    np.savetxt("PRED_bayes.dat", pred_classes, fmt="%d")


if __name__ == "__main__":
    main()