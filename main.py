import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

basketData = pd.read_csv('/Users/amalalsamara/development/datasets/Market_Basket_Optimisation.csv', header = None)

baskets =[]
for i in range(0,basketData.shape[0]):
    baskets.append([str(basketData.values[i,j]) for j in range(0,basketData.shape[1])])

# The shape[0] function gives the number of rows in the array, shape[1] gives the number of columns in the array


# Train the apriori algorithm
associationRule = apriori(transactions=baskets, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2, max_length=2)

#min_support = numbers of trasnactions we want item to be appearing in/ total transactions = 3 * 7 / 7501 = 0.003
#min_confidence = 0.2; trial and error start with 0.8, keep dividing by two until there is an appropriate number of rules
#min_length and max_length = how many items we want in each rule


associationResult= list(associationRule)
associationResult


# Using a Panda DataFrame to arrange and display the results of the association rules
def inspect(associationResult):
    left = [tuple(result[2][0][0])[0] for result in associationResult]
    right = [tuple(result[2][0][1])[0] for result in associationResult]
    supports = [result[1] for result in associationResult]
    confidences = [result[2][0][2] for result in associationResult]
    lifts = [result[2][0][3] for result in associationResult]
    return list(zip(left, right, supports, confidences, lifts))
resultsDataFrame = pd.DataFrame(inspect(associationResult), columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
resultsDataFrame

print(resultsDataFrame)

def getIndex(word):
    for row in resultsDataFrame.row:
        if row.contains(word):
            return row


# Recommendations
question1 = input("What item are you buying today? ")
for row in resultsDataFrame.itertuples():
    if question1 in row[1]:
        print("We recommend: ", row[2])
else: print("Enjoy your shopping :)")

