"""
Utilities for calculating distances and finding nearest neighbors.
(These are intended to be completed as numpy exercises.)

Author:
Date:
"""

import numpy as np


def distance_loop(x1, x2):
    """ Returns the Euclidean distance between the 1-d numpy arrays x1 and x2"""
    return -1


def nearest_loop(X, target):
    """ Return the index of the nearest point in X to target.
         Arguments:
          X      - An m x d numpy array storing m points of dimension d
         target - a length-d numpy array
    """
    return -1


def distance(x1, x2):
    """ Returns the Euclidean distance between the 1-d numpy arrays x1 and x2"""
    return -1


def nearest(X, target):
    """ Return the index of the nearest point in X to target.
         Arguments:
          X      - An m x d numpy array storing m points of dimension d
         target - a length-d numpy array
    """

    return -1


def digit_demo():
    """Create a data set containing only 1's and 7's"""
    from sklearn.datasets import load_digits
    import matplotlib.pyplot as plt
    digits, labels = load_digits(return_X_y=True)

    digits_subset = None  # Suppress warnings...
    labels_subset = None

    # YOUR CODE HERE!

    print(digits_subset.shape)  # should be (361, 64)
    print(labels_subset.shape)  # should be (361,)
    plt.gray()
    plt.matshow(digits_subset[0, :].reshape(8, 8))  # should be a "1"
    plt.figure()
    plt.matshow(digits_subset[180, :].reshape(8, 8))  # should be "7"
    plt.show()


if __name__ == "__main__":
    digit_demo()
