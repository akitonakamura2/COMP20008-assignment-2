import pandas as pd
from scatter import preprocess_crime1, preprocess_house

h1 = preprocess_house("1bflat.csv")
c1 = preprocess_crime1("crime1.csv")

print(h1)
print(c1)

