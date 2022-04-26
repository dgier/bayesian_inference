import numpy as np
from matplotlib import pyplot as plt

def gaussian_generator(variance):

    x = np.random.normal(0, variance)

    return x

def bayes_probability(a, xs):

    prob = (1/(a * np.sqrt(2 * np.pi)))**(len(xs))

    for x in xs:
        prob = prob * np.exp(-x**2/(2*a**2))

    return prob

def bayes_distribution(variance):

    num_as = 10000
    max_a = 10
    xs = []

    for _ in range(100):
        xs.append(gaussian_generator(variance))

    a_vals = np.linspace(max_a/num_as,max_a,num_as)

    probs = []
    for i in range(len(a_vals)):
        probs.append(bayes_probability(a_vals[i], xs)/len(a_vals))

    print(a_vals)
    print(probs)

    plt.hist(xs)
    plt.show()

    plt.plot(a_vals, probs)
    plt.show()

    return a_vals, probs

def metropolis_hastings(a_vals, posterior_dist):

    x_initial = np.random(-20,20)
    t_max = 100

    for t in np.arange(0,t_max):
        x_prime = gaussian_generator()

    
    return 

bayes_distribution(4)