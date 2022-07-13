import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("F:\\Data_Projects\\wine-reviews.csv", usecols=['country', 'description', 'designation', 'variety', 'price', 'points'] )

plt.hist(df.points, bins= 20)
plt.show()
