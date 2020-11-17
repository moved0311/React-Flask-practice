import pandas as pd
import random

df = pd.read_json("./constants/dict.json")
wordSeries = df["Word"]
pickWord = random.choice(wordSeries)
print(pickWord)

#======
