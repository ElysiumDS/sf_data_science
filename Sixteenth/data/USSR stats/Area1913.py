import matplotlib.pyplot as plt

# Other countries' part formula
x = 0
countries = [38.2, 2.6, 12.1, 6.6, x ]
highlighted_countries = sum(countries)
other_countries = 100 - highlighted_countries

shares = [38.2, 2.6, 12.1, 6.6, 40.5 ]
labels = ['The USA', 'The USSR', 'England', 'France', 'Other countries']
explode = (0, 0.1, 0, 0, 0)

fig, ax = plt.subplots()
plt.title('Percentage in total for global industrial production by 1913')
ax.pie(shares, explode=explode, labels=labels, autopct='%1.1f%%', startangle=120,
       shadow={'ox': -0.02, 'edgecolor': 'none', 'shade': 0.9},
       colors=['steelblue', 'tab:red','plum', 'seagreen', 'silver' ])

ax.plot()
ax.legend(bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()