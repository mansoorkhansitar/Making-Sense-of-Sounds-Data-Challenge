import numpy as np
import pandas as pd
"""A = np.array([5.1, 3.5, 1.4, 0.2, 0], [4.9, 3, 1.4, 0.2, 0], [4.7, 3.2, 1.3, 0.2, 0], [4.6,	3.1, 1.5, 0.2, 0], [5, 3.6, 1.4, 0.2, 1],
             [6.4, 3.2, 4.5, 1.5, 1], [6.9,	3.1, 4.9, 1.5, 1], [
                 5.5, 2.3, 4, 1.3, 1], [6.3,	3.3, 6, 2.5, 2], [5.8, 2.7,	5.1, 1.9, 2],
             [7.1, 3, 5.9, 2.1, 2], [6.3, 2.9, 5.6, 1.8, 2], [5.5, 1.5, 6.2,
                                                              1.9, 3], [5.4, 1.4, 6.4, 1.6, 3], [5.6, 1.6, 6.3, 1.3, 3],
             [5.3, 1.4, 6.0, 1.4, 3], [2.8, 0.9, 2.9, 0.8, 4], [2.7, 0.8, 2.8, 0.7, 4], [2.9, 0.9, 2.7, 0.9, 4], [2.8, 0.7, 2.5, 0.8,	4])
             """
B = np.array([[5.1, 3.5, 1.4, 0.2, 0], [4.9, 3, 1.4, 0.2, 0], [4.7, 3.2, 1.3, 0.2, 0], [4.6,	3.1, 1.5, 0.2, 0], [5, 3.6, 1.4, 0.2, 1],
              [6.4, 3.2, 4.5, 1.5, 1], [6.9,	3.1, 4.9, 1.5, 1], [
    5.5, 2.3, 4, 1.3, 1], [6.3,	3.3, 6, 2.5, 2], [5.8, 2.7,	5.1, 1.9, 2],
    [7.1, 3, 5.9, 2.1, 2], [6.3, 2.9, 5.6, 1.8, 2], [5.5, 1.5, 6.2,
                                                     1.9, 3], [5.4, 1.4, 6.4, 1.6, 3], [5.6, 1.6, 6.3, 1.3, 3],
    [5.3, 1.4, 6.0, 1.4, 3], [2.8, 0.9, 2.9, 0.8, 4], [2.7, 0.8, 2.8, 0.7, 4], [2.9, 0.9, 2.7, 0.9, 4], [2.8, 0.7, 2.5, 0.8,	4]])
print (np.shape(B))
df1 = pd.DataFrame(data=B)
df1.to_csv('test_comparison_code.csv')
print (B)
