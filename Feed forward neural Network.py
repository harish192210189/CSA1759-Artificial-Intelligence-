import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]

y = [[0], [1], [1], [0]]

input_layer_size = 3
hidden_layer_size = 4
output_layer_size = 1
W1 = [[random.uniform(0, 1) for _ in range(hidden_layer_size)] for _ in range(input_layer_size)]
W2 = [[random.uniform(0, 1) for _ in range(output_layer_size)] for _ in range(hidden_layer_size)]
alpha = 0.1

for epoch in range(10000):
    A1 = [[0] * hidden_layer_size for _ in range(len(X))]
    A2 = [[0] * output_layer_size for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(hidden_layer_size):
            A1[i][j] = sigmoid(sum(X[i][k] * W1[k][j] for k in range(input_layer_size)))
        
    for i in range(len(X)):
        for j in range(output_layer_size):
            A2[i][j] = sigmoid(sum(A1[i][k] * W2[k][j] for k in range(hidden_layer_size)))

    output_error = [[A2[i][j] - y[i][j] for j in range(output_layer_size)] for i in range(len(X))]
    output_delta = [[output_error[i][j] * sigmoid_derivative(A2[i][j]) for j in range(output_layer_size)] for i in range(len(X))]

    hidden_error = [[0] * hidden_layer_size for _ in range(len(X))]
    hidden_delta = [[0] * hidden_layer_size for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(hidden_layer_size):
            hidden_error[i][j] = sum(output_delta[i][k] * W2[j][k] for k in range(output_layer_size))
            hidden_delta[i][j] = hidden_error[i][j] * sigmoid_derivative(A1[i][j])

    for i in range(hidden_layer_size):
        for j in range(output_layer_size):
            W2[i][j] -= alpha * sum(A1[k][i] * output_delta[k][j] for k in range(len(X)))

    for i in range(input_layer_size):
        for j in range(hidden_layer_size):
            W1[i][j] -= alpha * sum(X[k][i] * hidden_delta[k][j] for k in range(len(X)))

print("Final outputs after training:")
for output in A2:
    print(output)
