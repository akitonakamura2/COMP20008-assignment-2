import pandas as pd
from scatter import preprocess_crime1, preprocess_house, preprocess_combined

h1 = preprocess_house("1bflat.csv")
c1 = preprocess_crime1("crime1.csv")

one_bf = preprocess_combined(h1, c1)

livabilities = {}
counts = {}
one_bf["Livability"] = 1/(one_bf["Median House Price"] * one_bf["Rate per 100,000 population"])
for i in range(len(one_bf)):
    if one_bf["LGA"][i] in livabilities:
        livabilities[one_bf["LGA"][i]] += one_bf["Livability"][i]
        counts[one_bf["LGA"][i]] += 1
    else:
        livabilities[one_bf["LGA"][i]] = one_bf["Livability"][i]
        counts[one_bf["LGA"][i]] = 1

one_bf.drop("index", inplace=True, axis=1)

for LGA in livabilities:
    livabilities[LGA] = livabilities[LGA]/counts[LGA]
print("count:", len(counts))
print("livabilities: ", len(livabilities))
livabilities = dict(sorted(livabilities.items(), key=lambda item: item[1]))

print(one_bf)
f= open("top10.txt","w+")
f.write("Top 10 Areas Ranked on Crime Rate and Rent price\n\n")
for i in range(10):
    print(list(livabilities.items())[i])
    f.write(str(list(livabilities.items())[i]))
    f.write("\n")

print("\nTop 10 Safest Areas")
for i in range(1, 11):
    print(list(livabilities.items())[-i])
    f.write(str(list(livabilities.items())[i]))
    f.write("\n")
     
f.close() 
