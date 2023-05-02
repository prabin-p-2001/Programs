import numpy as np

# define a function to predict the output of a simple linear model
def predict(X, weights):
  return X @ weights

# define a function to calculate the mean squared error
def mean_squared_error(predictions, targets):
  return np.mean((predictions - targets)**2)

# define a function to perform gradient descent
def gradient_descent(X, y, learning_rate=0.01, num_iterations=100):
  # initialize the weights
  weights = np.zeros(X.shape[1])

  # loop over the number of iterations
  for i in range(num_iterations):
    # make predictions using the current weights
    predictions = predict(X, weights)

    # calculate the error
    error = mean_squared_error(predictions, y)

    # calculate the gradient of the error with respect to the weights
    gradients = 2 * X.T @ (predictions - y) / len(y)

    # update the weights using the gradient and learning rate
    weights -= learning_rate * gradients

  return weights

# define some training data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 3, 5, 7])

# train the model
weights = gradient_descent(X, y)

# print the trained weights
print(weights)
