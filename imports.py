# Explicit importing the whole module
import datetime
today = datetime.date.today()
print ("Today's date is:", today)

# importing specific functions or classes
from math import sqrt
print("Square root of 64 is:", sqrt(64))

 #Importing with alias 'as'
import numpy as np
array = np.array([1,2,3,4,5])
print("Numpy array:", array)