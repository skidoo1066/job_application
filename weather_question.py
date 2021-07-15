import pandas as pd
import numpy as np
from io import StringIO

f = open('w_data.dat')
text = ''
count = 0
for line in f:
    if count > 1:
        text = text + '\n' + line
    count += 1
f.close()
text = text.replace('*', '')
weather = pd.read_csv(StringIO(text), skipfooter=1,
                      delimiter=r"\s+", engine='python',
                      comment='MMU')
weather['tdiff'] = abs(np.array(weather.MxT.astype(int)) -
                       np.array(weather.MnT.astype(int)))
print('Day', weather.sort_values('tdiff', ascending=True).Dy.iloc[0],
      'has the lowest difference between max and min')

