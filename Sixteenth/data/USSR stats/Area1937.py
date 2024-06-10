import matplotlib.pyplot as plt

x = 0
countries = [37.8, 9.2, 11.5, 5.5, 8.4, x ]
highlighted_countries = sum(countries)
other_countries = 100 - highlighted_countries

shares = [37.8, 9.2, 11.5, 5.5, 8.4, other_countries ]
labels = ['The USA', 'The USSR', 'England', 'France', 'FRG', 'Other countries']
explode = (0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots()
plt.title('Percentage in total for global industrial production by 1937')
ax.pie(shares, explode=explode, labels=labels, autopct='%1.1f%%', startangle=120,
       shadow={'ox': -0.02, 'edgecolor': 'none', 'shade': 0.9},
       colors=['steelblue', 'tab:red','plum', 'seagreen', 'sienna', 'silver' ])

ax.plot()
ax.legend(bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()