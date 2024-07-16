import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the standard normal distribution
mu = 0  # mean
sigma = 1  # standard deviation

# Generating points on the x-axis
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)

plt.figure(figsize=(7, 5))
plt.plot(x, norm.pdf(x, mu, sigma), label='Standard Normal (μ)')
plt.plot(x, norm.pdf(x, mu + 2*sigma, sigma), label='Shifted Normal (μ + 2σ)')
plt.title('Grade Average Distribution')
plt.ylabel('Probability Density')
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
