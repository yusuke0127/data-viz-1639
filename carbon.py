# carbon.py
import matplotlib.pyplot as plt
plt.style.use("classic")

years_x = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
total_y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]
coal_y = [823, 1136, 1367, 1547, 1660, 1927, 1983, 1827, 1352]
gas_y = [171, 200, 166, 175, 228, 280, 319, 399, 529]

plt.plot(years_x, total_y, label="Total")
plt.plot(years_x, coal_y, label="Coal")
plt.plot(years_x, gas_y, label="Natural Gas")

plt.title("USA - CO2 emissions from electricity production")
plt.xlabel("Year")
plt.ylabel("CO2 - M of tons")
plt.legend(loc="best")

plt.show() # Will open a graph window.
           # Wait for it to be closed to continue script execution