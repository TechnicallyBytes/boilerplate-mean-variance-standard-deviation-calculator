import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
        
    array = np.reshape(list, (3, 3))
 
    min = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()]
    max = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()]
    sum = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    mean = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()]
    variance = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()]
    stddev = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()]
        
    calculations = dict([
         ('mean', mean), 
         ('variance', variance), 
         ('standard deviation', stddev), 
         ('max', max),
         ('min', min), 
         ('sum',sum)
        ])
    

    return calculations