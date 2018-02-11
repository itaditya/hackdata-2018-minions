# DATASET = 'https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=9999999999&period=14400'

import json
import numpy as np
import os
import pandas as pd
import urllib.request
import matplotlib.pyplot as mpl
from TFANN import ANNR
 
def JSONDictToDF(d):
    '''
    Converts a dictionary created from json.loads to a pandas dataframe
    d:      The dictionary
    '''
    n = len(d)
    cols = []
    if n > 0:   #Place the column in sorted order
        cols = sorted(list(d[0].keys()))
    df = pd.DataFrame(columns = cols, index = range(n))
    for i in range(n):
        for coli in cols:
            df.set_value(i, coli, d[i][coli])
    return df
     
def GetAPIUrl(cur):
    u = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC' + cur + '&start=1420070400&end=9999999999&period=7200'
    return u
 
def GetCurDF(cur, fp):
    '''
    cur:    3 letter abbreviation for cryptocurrency (BTC, LTC, etc)
    fp:     File path (to save price data to CSV)
    '''
    openUrl = urllib.request.urlopen(GetAPIUrl(cur))
    r = openUrl.read()
    openUrl.close()
    d = json.loads(r.decode())
    df = JSONDictToDF(d)
    df.to_csv(fp, sep = ',')
    return df
 
def generator():
    #%%Path to store cached currency data
    datPath = 'CurDat/'
    if not os.path.exists(datPath):
        os.mkdir(datPath)
    cl = ['BTC', 'LTC', 'ETH', 'XMR']
    #Columns of price data to use
    CN = ['close', 'high', 'low', 'open', 'volume']
    #Store data frames for each of above types
    D = []
    for ci in cl:
        dfp = os.path.join(datPath, ci + '.csv')
        try:
            df = pd.read_csv(dfp, sep = ',')
        except FileNotFoundError:
            df = GetCurDF(ci, dfp)
        D.append(df)
    #%%Only keep range of data that is common to all currency types
    cr = min(Di.shape[0] for Di in D)
    for i in range(len(cl)):
        D[i] = D[i][(D[i].shape[0] - cr):]

        NC = B.shape[2]
        #2 1-D conv layers with relu followed by 1-d conv output layer
        ns = [('C1d', [8, NC, NC * 2], 4), ('AF', 'relu'), 
              ('C1d', [8, NC * 2, NC * 2], 2), ('AF', 'relu'), 
              ('C1d', [8, NC * 2, NC], 2)]
        #Create the neural network in TensorFlow
        cnnr = ANNR(B[0].shape, ns, batchSize = 32, learnRate = 2e-5, 
                    maxIter = 64, reg = 1e-5, tol = 1e-2, verbose = True)
        cnnr.fit(B, Y)

        CI = list(range(C.shape[0]))
        AI = list(range(C.shape[0] + PTS.shape[0] - HP))
        NDP = PTS.shape[0] #Number of days predicted
        for i, cli in enumerate(cl):
            fig, ax = mpl.subplots(figsize = (16 / 1.5, 10 / 1.5))
            hind = i * len(CN) + CN.index('high')
            ax.plot(CI[-4 * HP:], C[-4 * HP:, hind], label = 'Actual')
            ax.plot(AI[-(NDP + 1):], A[-(NDP + 1):, hind], '--', label = 'Prediction')
            ax.legend(loc = 'upper left')
            ax.set_title(cli + ' (High)')
            ax.set_ylabel('USD')
            ax.set_xlabel('Time')
            ax.axes.xaxis.set_ticklabels([])
            mpl.show()
