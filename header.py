import numpy as np

def poisson(x, mu):
    '''
    Poisson ditribution function
    '''
    return mu**x * np.exp(-mu) / factorial(x)

def normal_dist(x, mu, sigma):
    '''
    '''
    return np.exp(-((x - mu)**2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))

def stand_normal_dist(x):
    '''
    '''
    return np.exp(-(x**2) / 2) / (np.sqrt(2 * np.pi))

def binomial_dist(k, n, p):
    '''
    '''
    return (factorial(n) / (factorial(k) * factorial(n - k))) * p**k * (1 - p)**(n - k)

def even_dist(x):
    return 1/len(x)

def get_probability(Omega, x):
    '''
    '''
    X = sum(even_dist(x))
    return X

def num_cov_0(Omega, a):
    x = []
    for n in a:
        x.append(Omega[0:n])
    #print(np.array(x))
     
    #xx = [[np.linspace(0, (n+a)/2, (Omega[-1]-Omega[0])/len(Omega)) for n in x[i]] for i in range(len(x))]
    #print(np.array(xx).shape)
    xx = []
    X = max(get_probability(Omega, x))
    return X

def num_cov_ab(Omega, a, b):
    x = Omega[a:b]
    xx = [np.linspace((a+n)/2, (n+b)/2, (Omega[-1]-Omega[0])/len(Omega)) for n in x]
    return max(get_probability(Omega, x))

def num_cov_1(Omega, a):
    x = Omega[a:]
    xx = [np.linspace((a+n)/2, 1, (Omega[-1]-Omega[0])/len(Omega)) for n in x]
    return max(get_probability(Omega, x))

def inversion(Omega, num):
    '''
    '''
    parties = np.zeros((num,))
    N = len(Omega)
    h = (Omega[-1]-Omega[0])/len(Omega)
    
    
    
    '''
    for i, n in enumerate(Omega):
        for o in range(Omega[0], n, h):
            for p in range(Omega[0], o, h):
                
            for p in range(o+h, n, h):

        for o in range(n+h, Omega[-1]+h, h):
            for p in range(n+h, o, h):

            for p in range(o+h, Omega[-1]+h, h):'''
