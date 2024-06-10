import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#если посчитать следующий к предыдущему году
years = [1913, 1937, 1956]
dyn_USA = [100, 99.04, 104.23]
dyn_USSR = [100, 253.84, 115.21]
dyn_Eng = [100, 95.05, 76.53]
dyn_Fra = [100, 83.34, 61.82]
dyn_FRG = [100, 79.29, 89.29]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(years, dyn_USA, color='blue')
ax.plot(years, dyn_USSR, color='red')
ax.plot(years, dyn_Eng, color='plum')
ax.plot(years, dyn_Fra, color='seagreen')
ax.plot(years, dyn_FRG, color='sienna')


ax.set_title("Industry dynamics", fontsize=24)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("rates", fontsize=14)

ax.tick_params(axis='both', labelsize=14)
plt.legend()


plt.show()