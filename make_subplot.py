'''
make_subplot.py - A simple demonstration of using subplots

Dave Whipp - 13.04.2016
'''

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Create plot arrays
x = np.linspace(0,2*np.pi,101)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplot 1
plt.subplot(2, 1, 1)
plt.plot(x, y1, 'ro-')
plt.xlabel('angle [rad.]')
plt.ylabel('sin(x)')
plt.title('Example of two subplots')

# Create subplot 2
plt.subplot(2, 1, 2)
plt.plot(x, y2, 'ko-')
plt.xlabel('angle [rad.]')
plt.ylabel('cos(x)')

# Display plot
plt.show()
