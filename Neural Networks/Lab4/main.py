import numpy as np
import pandas as pd
import os
from PIL import Image

print("Files in this directory:", os.listdir("."))

train = np.load("C:/Users/colin/Desktop/Repos/Python Repo/Neural Networks/Lab4/train.npz",allow_pickle=True)
test = np.load("C:/Users/colin/Desktop/Repos/Python Repo/Neural Networks/Lab4/test.npz",allow_pickle=True)

train_data = train["data"] / 255.0
train_data = np.array(train_data)

train_labels = train["labels"]
train_labels = np.array(train_labels)

test_data = test["data"] / 255.0
test_data = np.array(test_data)

print("Full train data:", train_data.shape)
print("Full train labels:", train_labels.shape)
print("Test data:", test_data.shape)

X_train = train_data.T
Y_train = train_labels
X_test = test_data.T

print("Training split:", X_train.shape)
print("Validation split:", Y_train.shape)


def init_params():
    W1 = np.random.randn(256, 784) * np.sqrt(2.0 / 784)
    b1 = np.random.randn(256, 1)
    W2 = np.random.randn(10, 256) * np.sqrt(2.0 / 256)
    b2 = np.random.randn(10, 1)
    return W1, b1, W2, b2


def ReLU(Z):
    return np.maximum(0, Z)


def deriv_ReLU(Z):
    return Z > 0


def softmax(Z):
    Z_shift = Z - np.max(Z, axis=0, keepdims=True)
    exp_Z = np.exp(Z_shift)
    return exp_Z / np.sum(exp_Z, axis=0, keepdims=True)


def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2


def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, 10))
    one_hot_Y[np.arange(Y.size, ), Y] = 1
    return one_hot_Y.T


def back_prop(Z1, A1, Z2, A2, W2, X, Y):
    m = Y.size

    one_hot_Y = one_hot(Y)

    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)

    dZ1 = W2.T.dot(dZ2) * deriv_ReLU(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)

    return dW1, db1, dW2, db2


def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    return W1, b1, W2, b2


def get_prediction(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size


def gradient_descent(X, Y, iterations, alpha):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = back_prop(Z1, A1, Z2, A2, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            print("Accuracy: ", get_accuracy(get_prediction(A2), Y))
    return W1, b1, W2, b2


def gradient_descent_experimental(X, Y, iterations, alpha, batch_size):
    W1, b1, W2, b2 = init_params()
    m = X.shape[1]
    for i in range(iterations):
        perm = np.random.permutation(m)
        X_shuffled = X[:, perm]
        Y_shuffled = Y[perm]
        for j in range(0, m, batch_size):
            X_batch = X_shuffled[:, j:j + batch_size]
            Y_batch = Y_shuffled[j:j + batch_size]

            Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X_batch)
            dW1, db1, dW2, db2 = back_prop(Z1, A1, Z2, A2, W2, X_batch, Y_batch)
            W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)

        if i % 10 == 0 or i == iterations - 1:
            _, _, _, A2a = forward_prop(W1, b1, W2, b2, X)
            print("Iteration: ", i)
            print("Accuracy: ", get_accuracy(get_prediction(A2a), Y))
    return W1, b1, W2, b2


# W1, b1, W2, b2 = gradient_descent_experimental(X_train, Y_train, 100, 0.1,64)
# W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 100, 0.1)
W1, b1, W2, b2 = gradient_descent_experimental(X_train, Y_train, 20, 0.1, 64)

def make_prediction(X,W1,b1,W2,b2):
    _,_,_, A2 = forward_prop(W1,b1,W2,b2,X)
    return get_prediction(A2)

test_predictions = make_prediction(X_test,W1,b1,W2,b2)

submission = pd.DataFrame({
    "ID": range(len(test_predictions)),
    "target": test_predictions,
})

submission.to_csv("submission.csv", index=False)
print("Created submission.csv")

def predict_image(file_path, W1,b1,W2,b2):
    img = Image.open(file_path).convert('L').resize((28,28))
    img_array = np.array(img) / 255.0
    reshaped_img = img_array.reshape(784,1)
    _,_,_, A2 = forward_prop(W1,b1,W2,b2,reshaped_img)
    prediction = np.argmax(A2)
    confidence = np.max(A2) * 100

    print("Prediction: ", prediction)
    print("Confidence: ", confidence)
    return prediction

image_path = "C:/Users/colin/Desktop/Repos/Python Repo/Neural Networks/Lab4/image.png"
predict_image(image_path, W1,b1,W2,b2)

