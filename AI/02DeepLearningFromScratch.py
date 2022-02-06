# A simple neural network coded from scratch (no frameworks)
# Sample problem statment: Given a pattern of street lights, figure out whether to walk or stop

# for vector multiplication
import numpy as np

# seed the random number generator
np.random.seed(1)

# activation function
# could be sigmoid, but ReLUs help learn better
# A ReLU is max(0, x)
def relu(x):
    return (x > 0) * x

# the derivative of the ReLU.
# 1 for input > 0
# 0 otherwise
def reluPrime(output):
    return output > 0

# Street light data
# In the real world, this data would come from an external dataset
# Here, it's a simple street light with three lights OOO
# 1 = on, 0 = off
streetLights = np.array( [[1, 0, 1],
                          [0, 1, 1],
                          [0, 0, 1],
                          [1, 1, 1]])

# To walk or to stop, that is the question
# We take the transpose of this vector,
# unlike in 01MachineLearningFromScratch.py
walkOrStop = np.array([1, 1, 0, 0]).T

# Unlike the data in 01MachineLearningFromScratch.py
# There is no direct correlation between one of the lights
# and whether to walk or stop. We need a deep neural network
# to solve this problem. The middle layer is nothing but
# a processed form of the input dataset.

# prevents gradient descent from going out of control and overshooting to actually increasing the error with a huge jump
alpha = 0.1

# our hidden layer has 4 neurons
hiddenLayerSize = 4

# get random weights (values between -1 and 0)...
# ...in a 3 x 4 matrix (input layer of three lights to the hidden layer of four neurons)
weights_01 = 2 * np.random.random((3, hiddenLayerSize)) - 1
# ...in a 4 x 1 matrix (hidden layer of four neurons to one result layer for true/false (= walk/stop) result)
weights_12 = 2 * np.random.random((hiddenLayerSize, 1)) - 1


# iteratively reduce the error
# sometimes, you have hundreds or thousands of iterations in real world scenarios
for iteration in range(100):
    # initialise error to 0
    layer2Error = 0
    # for each element in the streetLights dataset
    for i in range(len(streetLights)):
        # initialise the layers
        layer0 = streetLights[i : i + 1] # a given row of input (street light pattern data)
        layer1 = relu(np.dot(layer0, weights_01)) # take the ReLU of the layer 1 activations times the weights
        layer2 = np.dot(layer1, weights_12) # get the activations in the result layer

        # calculate the training example's error as (value - desiredValue) ^ 2
        # and add it to the total error
        layer2Error += np.sum((layer2 - walkOrStop[i : i + 1]) ** 2)

        # how much the activation differs from the expected result
        layer2Delta = (layer2 - walkOrStop[i : i + 1])

        # Backpropagation
        # layer2Delta is backpropagated to layer1Delta
        # and how much each weight contributed to the error.
        # It shows how much we want the layer1 activations to go up or down
        layer1Delta = layer2Delta.dot(weights_12.T) * reluPrime(layer1)

        # Gradient descent
        # Adjust the weights using the deltas calculated above
        # Alpha is used to prevent gradient descent from overshooting
        # and increasing the error in the next iteration
        weights_12 -= alpha * layer1.T.dot(layer2Delta)
        weights_01 -= alpha * layer0.T.dot(layer1Delta)

    # Display the result every 10 iterations
    if (iteration % 10 == 9):
        print('Error: {}'.format(layer2Error)) # Should approach 0
        print('Weights (1 => 2): {}'.format(weights_12))
        print('Weights (0 => 1): {}\n'.format(weights_01))
