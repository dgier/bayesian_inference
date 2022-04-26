import numpy as np

def gaussian_random_sampler(mean, variance):

    x = np.random.normal(mean, variance)

    return x