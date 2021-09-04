#This is for API, where API fetch the data, and it perform some operation on it and it will be ready to predict.
#Pro - It helps by not saving the csv files in the system.

import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import date
from yahoo_fin.stock_info import get_data
import datetime
import pandas as pd
from pandas import DataFrame

def sarimax_model(ticker):
        # Dataset Building#
    df.set_index("Date", inplace = True)
    df.index = pd.to_datetime(df.index)
    ds=df['Close']
    # print(ds)
        ##Model Fitting##
    model = SARIMAX(ds,  order = (2,0,1),  seasonal_order = (2, 1, 0, 12)) 
    result = model.fit() 
        ##Model Forecasting and creating frequency##
    dti = pd.date_range(str(ds.index[-1]), periods=12, freq="M")
    forecast = result.predict(start = str(ds.index[-1]), end = (len(ds)-1)+11, typ='levels') 
    forecast.index=dti
    ss=ds.append(forecast)
    # l=[]
    # da=str(ds.index[-1].year)+str(ds.index[-1].month)+str(ds.index[-1].day)
    # for i in range(len(ds)):
    #     l.append([ds.index[i],ds['Close'][i]])
    # print(l)
    # for i in range(len(dti)):
    #     l.append([dti[i],forecast.get(key=dti[i])])
    # print(l)
    # dff = DataFrame (,columns=['Date','Forecast']) 
    dff = ss.to_frame()
    ldates=[]
    
    print(dff.index[0])
    idx=pd.Index(dff)
    dff_forecast=idx.to_list()
    print(dff_forecast)
    # year=dff.index.dt.year
    # month=dff['Date'].dt.month
    # day=dff['Date'].dt.day
    
    ldates=[]
    for i in range(len(year)):
        sr=str(year[i])+str(month[i])+str(day[i])
        ldates.append(int(sr))
    dff_forecast=dff['Forecast'].tolist()
    return [ldates,dff_forecast]

sarimax_model('a')
