import pandas as pd
from scatter import preprocess_crime1, preprocess_house, preprocess_combined

h1 = preprocess_house("1bflat.csv")
c1 = preprocess_crime1("crime1.csv")

one_bf = preprocess_combined(h1, c1)

livabilities = {}
for i in range(620):
    one_bf["Livability"] = 1/(one_bf["Median House Price"] * one_bf["Rate per 100,000 population"])
    if one_bf["LGA"][i] in livabilities:
        livabilities[one_bf["LGA"][i]] += one_bf["Livability"][i]
    else:
        livabilities[one_bf["LGA"][i]] = one_bf["Livability"][i]

one_bf.drop("index", inplace=True, axis=1)

for LGA in livabilities:
    livabilities[LGA] = livabilities[LGA]/10
    print(LGA)

livabilities = dict(sorted(livabilities.items(), key=lambda item: item[1]))

print(one_bf)
f= open("top10.txt","w+")
f.write("Top 10 Areas Ranked on Crime Rate and Rent price\n\n")
for i in range(20):
    print(list(livabilities.items())[i])
    f.write(str(list(livabilities.items())[i]))
    f.write("\n")
     
f.close() 
