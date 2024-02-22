import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
        
    array = np.reshape(list, (3, 3))
    print(array)

    min = [np.min(array, axis=0), np.min(array, axis=1), np.min(array)]
    max = [np.max(array, axis=0), np.max(array, axis=1), np.max(array)]
    sum = [np.sum(array, axis=0), np.sum(array, axis=1), np.sum(array)]
    mean = [np.mean(array, axis=0), np.mean(array, axis=1), np.mean(array)]
    variance = [np.var(array, axis=0), np.var(array, axis=1), np.var(array)]
    stddev = [np.std(array, axis=0), np.std(array, axis=1), np.std(array)]
        
    calculations = dict([
         ('mean', mean), 
         ('variance', variance), 
         ('standard deviation', stddev), 
         ('max', max),
         ('min', min), 
         ('sum',sum)
        ])
    print(calculations)

    return calculations

calculate([0,1,2,3,4,5,6,7,8])