import pandas as pd
from scatter import preprocess_crime1, preprocess_house, preprocess_combined
from coefficients import price_discretise
h1 = preprocess_house("1bflat.csv")
c1 = preprocess_crime1("crime1.csv")

one_bf = preprocess_combined(h1, c1) #Remove 0's and merge dataframes

livabilities = {}
counts = {}
one_bf["Livability"] = 1/(one_bf["Median House Price"] * one_bf["Rate per 100,000 population"]) #Calculate livability column

#Store total livabilities in dictionary
for i in range(len(one_bf)):
    if one_bf["LGA"][i] in livabilities:
        livabilities[one_bf["LGA"][i]] += one_bf["Livability"][i]
        counts[one_bf["LGA"][i]] += 1
    else:
        livabilities[one_bf["LGA"][i]] = one_bf["Livability"][i]
        counts[one_bf["LGA"][i]] = 1

one_bf.drop("index", inplace=True, axis=1) 

#Calculate average livability
for LGA in livabilities:
    livabilities[LGA] = livabilities[LGA]/counts[LGA]

livabilities = dict(sorted(livabilities.items(), key=lambda item: item[1])) #Sort by livability

f = open("top10.txt","w+")
f.write("Top 10 (Unsafe) Areas Ranked on Crime Rate and Rent price\n")

#Write first 10 areas to text file "top10.txt"
for i in range(10):
    f.write(str(list(livabilities.items())[i]))
    f.write("\n")
     
f.close() 

avg_price = {}
count = {}
#Accumulate total rent price for each LGA from 2011-2020
for i in range(len(one_bf)):
    if one_bf["LGA"][i] in avg_price:
        avg_price[one_bf["LGA"][i]] += one_bf["Median House Price"][i]
        count[one_bf["LGA"][i]] += 1
    else:
        avg_price[one_bf["LGA"][i]] = one_bf["Median House Price"][i]
        count[one_bf["LGA"][i]] = 1

#Calculate average rent price for each LGA from 2011-2020
for LGA in avg_price:
    avg_price[LGA] = avg_price[LGA]/count[LGA]

avg_df = pd.DataFrame(list(avg_price.items()), columns = ["LGA", "Median House Price"])
avg_df = price_discretise(avg_df, 190, 290) #Sort rent prices into discrete groups

livabilities_low ={}
livabilities_mid ={}
livabilities_high ={}
#Sort into separate ditionaries by rent price group
for i in range(len(avg_df)):
    if avg_df["Price Category"][i] == "low":
        livabilities_low[avg_df["LGA"][i]] = livabilities[avg_df["LGA"][i]]
    elif avg_df["Price Category"][i] == 'mid':
        livabilities_mid[avg_df["LGA"][i]] = livabilities[avg_df["LGA"][i]]
    else:
        livabilities_high[avg_df["LGA"][i]] = livabilities[avg_df["LGA"][i]]

top10 = open("top10-groups.txt","w+")
top10.write("Top 10 (Unsafe) Areas Ranked on Crime and Rent Price\n")
group_titles = ["Low Rent Price", "Mid Rent Price", "High Rent Price"]
i = 0
#For each price group write to the same file under their respective categories
for group in livabilities_low, livabilities_mid, livabilities_high:
    group = dict(sorted(group.items(), key=lambda item: item[1]))
    top10.write(group_titles[i])
    top10.write("\n")
    for LGA in list(group.items())[0:10]:
        print(LGA)
        top10.write(str(LGA))
        top10.write("\n")
    print("\n")
    top10.write("\n")
    i += 1