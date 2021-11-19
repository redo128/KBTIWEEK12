import numpy as np
import matplotlib.pyplot as plt
msg = "Hellow World"
print(msg)
x = np.linspace(0, 20, 100)  # membuat list angka berjarak sama dala
#m range yang ditentukan
plt.plot(x, np.sin(x))  # Plot sinusoida dari tiap nilai
plt.show()  # tampilkan plot
#