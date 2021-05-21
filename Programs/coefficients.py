import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from sklearn import metrics
from scatter import preprocess_house, preprocess_crime1

def price_discretise(df, low, high):
    price_category = []
    for price in df["Median House Price"].to_list():
        if price < low:
            price_category.append("low")
        elif price < high:
            price_category.append("mid")
        else:
            price_category.append("high")
    df.insert(len(df.columns), "Price Category", price_category)
    return df
 
def crime_discretise(df, low, high, low100k, high100k):
    crime_category = []
    crime_category_100k = []
    for c in df["Incidents Recorded"].to_list():
        if c < low:
            crime_category.append("low")
        elif c < high:
            crime_category.append("mid")
        else:
            crime_category.append("high")
    df.insert(len(df.columns), "Crime Category", crime_category)
    for c in df["Rate per 100,000 population"].to_list():
        if c < low100k:
            crime_category_100k.append("low")
        elif c < high100k:
            crime_category_100k.append("mid")
        else:
            crime_category_100k.append("high")
    df.insert(len(df.columns), "Crime Category (per 100k)", crime_category_100k)
    return df

#Calculating coefficients
one_bf = preprocess_house("1bflat.csv") # contains count and median price
one_bf = price_discretise(one_bf, 150, 250)
two_bf = preprocess_house("2bflat.csv")
two_bf = price_discretise(two_bf, 250, 350)
two_bh = preprocess_house("2bhouse.csv")
two_bh = price_discretise(two_bh, 250, 320)
three_bf = preprocess_house("3bflat.csv") 
three_bf = price_discretise(three_bf, 300, 400)
three_bh = preprocess_house("3bhouse.csv")
three_bh = price_discretise(three_bh, 300, 400)
four_bh = preprocess_house("4bhouse.csv") 
four_bh = price_discretise(four_bh, 350, 420)
all = preprocess_house("all.csv")
all = price_discretise(all, 250, 350)


c1 = preprocess_crime1("crime1.csv") # contains incidents and rate/100k
c1 = crime_discretise(c1, 4000, 8000, 5000, 7000)
print("1bf:", pearsonr(one_bf["Median House Price"], c1["Incidents Recorded"]))
print("1bf:", metrics.normalized_mutual_info_score(one_bf["Price Category"], c1["Crime Category"]))
print("1bf100k:", pearsonr(one_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("1bf100k:", metrics.normalized_mutual_info_score(one_bf["Price Category"], c1["Crime Category (per 100k)"]))

print("2bf:", pearsonr(two_bf["Median House Price"], c1["Incidents Recorded"]))
print("2bf:", metrics.normalized_mutual_info_score(two_bf["Price Category"], c1["Crime Category"]))
print("2bf100k:", pearsonr(two_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("2bf100k:", metrics.normalized_mutual_info_score(two_bf["Price Category"], c1["Crime Category (per 100k)"]))

print("2bh:", pearsonr(two_bh["Median House Price"], c1["Incidents Recorded"]))
print("2bh:", metrics.normalized_mutual_info_score(two_bh["Price Category"], c1["Crime Category"]))
print("2bh100k:", pearsonr(two_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("2bh100k:", metrics.normalized_mutual_info_score(two_bh["Price Category"], c1["Crime Category (per 100k)"]))

print("3bf:", pearsonr(three_bf["Median House Price"], c1["Incidents Recorded"]))
print("3bf:", metrics.normalized_mutual_info_score(three_bf["Price Category"], c1["Crime Category"]))
print("3bf100k:", pearsonr(three_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("3bf100k:", metrics.normalized_mutual_info_score(three_bf["Price Category"], c1["Crime Category (per 100k)"]))

print("3bh:", pearsonr(three_bh["Median House Price"], c1["Incidents Recorded"]))
print("3bh:", metrics.normalized_mutual_info_score(three_bh["Price Category"], c1["Crime Category"]))
print("3bh100k:", pearsonr(three_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("3bh100k:", metrics.normalized_mutual_info_score(three_bh["Price Category"], c1["Crime Category (per 100k)"]))

print("4bh:", pearsonr(four_bh["Median House Price"], c1["Incidents Recorded"]))
print("4bh:", metrics.normalized_mutual_info_score(four_bh["Price Category"], c1["Crime Category"]))
print("4bh100k:", pearsonr(four_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("4bh100k:", metrics.normalized_mutual_info_score(four_bh["Price Category"], c1["Crime Category (per 100k)"]))