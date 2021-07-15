import pandas as pd
import numpy as np
from io import StringIO

# in order to deal with dashes in the data file,
# I read in the text first for easy editing
f = open('soccer.dat')
text = ''
count = 0
for line in f:
    if count > 1:
        text = text + '\n' + line
    count += 1
f.close()
text = text.replace('-', '')

# turn text to dataframe
soccer = pd.read_csv(StringIO(text), skipfooter=1,
                     delimiter=r"\s+", engine='python').dropna()

# create difference variable and find team with smallest difference
soccer['diff'] = abs(np.array(soccer.F - soccer.A))
soccer = soccer.sort_values('diff', ascending=True)
print(soccer.Team.iloc[0], 'has the smallest difference')

