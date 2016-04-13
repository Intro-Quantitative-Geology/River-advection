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
y3 = np.sin(x**2)
y4 = np.cos(x**2)

# Create subplot 1
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'ro-')
plt.xlabel('angle [rad.]')
plt.ylabel('sin(x)')
plt.axis([0.0, 2 * np.pi, -1.1, 1.1])
plt.title('Example of four subplots')

# Create subplot 2
plt.subplot(2, 2, 2)
plt.plot(x, y2, 'ko-')
plt.xlabel('angle [rad.]')
plt.ylabel('cos(x)')
plt.axis([0.0, 2 * np.pi, -1.1, 1.1])

# Create subplot 3
plt.subplot(2, 2, 3)
plt.plot(x, y3, 'bo-')
plt.xlabel('angle [rad.]')
plt.ylabel('sin(x^2)')
plt.axis([0.0, 2 * np.pi, -1.1, 1.1])

# Create subplot 4
plt.subplot(2, 2, 4)
plt.plot(x, y4, 'go-')
plt.xlabel('angle [rad.]')
plt.ylabel('cos(x^2)')
plt.axis([0.0, 2 * np.pi, -1.1, 1.1])

# Display plot
plt.show()
