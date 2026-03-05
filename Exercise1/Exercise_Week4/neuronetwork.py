import pickle
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization
from tensorflow.keras.utils import to_categorical

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

    x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 784).astype("float32") / 255.0


    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    print()


    model = Sequential()
    model.add(Dense(128, input_dim=784,activation="relu"))  # piilokerros (voit muuttaa neuronien määrää)
    model.add(BatchNormalization())  # normalisointi (parantaa oppimista)
    model.add(Dense(10, activation="softmax"))  # ulostulo, 10 luokkaa

    model.compile(optimizer="adam", loss="categorical_crossentropy",
                  metrics=["accuracy"])


    history = model.fit(x_train, y_train, epochs=20, batch_size=32,
                        validation_data=(x_test, y_test), verbose=2)


    plt.plot(history.history["loss"], label="train loss")
    plt.plot(history.history["val_loss"], label="val loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()


    train_acc = model.evaluate(x_train, y_train, verbose=0)[1]
    test_acc = model.evaluate(x_test, y_test, verbose=0)[1]

    print(f"Harjoitusdatan tarkkuus: {train_acc:.4f}")
    print(f"Testidatan tarkkuus: {test_acc:.4f}")


    y_pred = model.predict(x_test)
    pred_classes = np.argmax(y_pred, axis=1)


    np.savetxt("PRED_mlp.dat", pred_classes, fmt="%d")

    print()





if __name__ == "__main__":
    main()