import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from sklearn import metrics
from scatter import preprocess_house
from scatter import preprocess_crime1

# Combines two dataframes and removes rows with 0
def preprocess_combined(df1, df2):
    df1["Incidents Recorded"] = df2["Incidents Recorded"]
    df1["Rate per 100,000 population"] = df2["Rate per 100,000 population"]
    df1 = df1[df1.Count != 0]
    df1.reset_index(inplace=True)
    return df1

#Calculating coefficients
one_bf = preprocess_house("1bflat.csv") # contains count and median price
two_bf = preprocess_house("2bflat.csv") 
two_bh = preprocess_house("2bhouse.csv")
three_bf = preprocess_house("3bflat.csv") 
three_bh = preprocess_house("3bhouse.csv")
four_bh = preprocess_house("4bhouse.csv") 
all = preprocess_house("all.csv")

c1 = preprocess_crime1("crime1.csv") # contains incidents and rate/100k
print("1bf:", pearsonr(one_bf["Median House Price"], c1["Incidents Recorded"]))
print("1bf:", metrics.normalized_mutual_info_score(one_bf["Median House Price"], c1["Incidents Recorded"]))
print("1bf100k:", pearsonr(one_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("1bf100k:", metrics.normalized_mutual_info_score(one_bf["Median House Price"], c1["Rate per 100,000 population"]))

print("2bf:", pearsonr(two_bf["Median House Price"], c1["Incidents Recorded"]))
print("2bf:", metrics.normalized_mutual_info_score(two_bf["Median House Price"], c1["Incidents Recorded"]))
print("2bf100k:", pearsonr(two_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("2bf100k:", metrics.normalized_mutual_info_score(two_bf["Median House Price"], c1["Rate per 100,000 population"]))

print("2bh:", pearsonr(two_bh["Median House Price"], c1["Incidents Recorded"]))
print("2bh:", metrics.normalized_mutual_info_score(two_bh["Median House Price"], c1["Incidents Recorded"]))
print("2bh100k:", pearsonr(two_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("2bh100k:", metrics.normalized_mutual_info_score(two_bh["Median House Price"], c1["Rate per 100,000 population"]))

print("3bf:", pearsonr(three_bf["Median House Price"], c1["Incidents Recorded"]))
print("3bf:", metrics.normalized_mutual_info_score(three_bf["Median House Price"], c1["Incidents Recorded"]))
print("3bf100k:", pearsonr(three_bf["Median House Price"], c1["Rate per 100,000 population"]))
print("3bf100k:", metrics.normalized_mutual_info_score(three_bf["Median House Price"], c1["Rate per 100,000 population"]))

print("3bh:", pearsonr(three_bh["Median House Price"], c1["Incidents Recorded"]))
print("3bh:", metrics.normalized_mutual_info_score(three_bh["Median House Price"], c1["Incidents Recorded"]))
print("3bh100k:", pearsonr(three_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("3bh100k:", metrics.normalized_mutual_info_score(three_bh["Median House Price"], c1["Rate per 100,000 population"]))

print("4bh:", pearsonr(four_bh["Median House Price"], c1["Incidents Recorded"]))
print("4bh:", metrics.normalized_mutual_info_score(four_bh["Median House Price"], c1["Incidents Recorded"]))
print("4bh100k:", pearsonr(four_bh["Median House Price"], c1["Rate per 100,000 population"]))
print("4bh100k:", metrics.normalized_mutual_info_score(four_bh["Median House Price"], c1["Rate per 100,000 population"]))