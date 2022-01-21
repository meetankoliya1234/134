import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

df = pd.read_csv("star_with_gravity.csv")

df.head()

X = df.iloc[:,[7,8]].values

star = df[1:]

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append((kmeans.inertia_))
plt.plot(range(1,11),wcss)
plt.title("elbow method")
plt.xlabel('Number of clusters')
plt.show()

print(X)

good_star = []

for i in star[2]:
    if i <= 100:
        good_star.append(i)

print(good_star)

for m in star[9]:
    if m >= 150 or m <= 350:
        good_star.append(i)
        
good_star.to_csv("Edit_star_gravity")