import pandas as pd

# contains count, median price for each quarter as cols, LGA in 2nd entry of 
# each row.

def preprocess_house(fname):
    # reorganises the house price csv files into a more standard format
    # columns: Quarter, LGA, Count, Median

    h = pd.read_csv(fname)

    # creates a sorted list of LGAs 
    LGAs = h["Unnamed: 1"].to_list()
    LGAs = sorted(LGAs[2:-6])
    LGAs = LGAs[0:28] + LGAs[35:] # removing "group total" rows

    # creates a sorted list of quarters
    quarters = h.values.tolist()[0]
    quarters = quarters[2::2]

    # duplicates list values to store 1 row per quarter per LGA
    quarters_new = [""] * (len(quarters)*len(LGAs))
    for i in range(len(quarters)):
        for j in range(len(LGAs)):
            quarters_new[i * len(LGAs) + j] = quarters[i]

    LGAs_new = [""] * (len(quarters)*len(LGAs))
    for i in range(len(quarters)):
        for j in range(len(LGAs)):
            LGAs_new[i * len(LGAs) + j] = LGAs[j]

    # creates lists for count and median price
    dict = {} # stores counts and median house prices as list of tuples
    row_count = len(h.index)
    for r in [i + 2 for i in range(row_count - 7)]:
        row = h.values.tolist()[r]
        if row[1] != "Group Total":
            dict[row[1]] = []
            for j in range(len(quarters)):
                dict[row[1]].append((row[2*j+2], row[2*j+3]))
    
    print(sorted(dict.keys()))
    print(LGAs)
    
    counts = [""] * len(quarters_new)
    prices = [""] * len(quarters_new)

    for i in range(len(quarters)):
        j = 0
        for LGA in sorted(dict.keys()):
            counts[i * len(LGAs) + j] = dict[LGA][i][0]
            prices[i * len(LGAs) + j] = dict[LGA][i][1]
            j += 1

    df = pd.DataFrame.from_dict({"Quarter": quarters_new, "LGA": LGAs_new, "Count": counts, "Median House Price": prices})

    return df

# reading in csv files
c1 = pd.read_csv("crime1.csv") # contains incidents and rate/100k
df = preprocess_house("1bflat.csv")
print(df)