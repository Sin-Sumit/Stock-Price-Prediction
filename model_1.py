import numpy as np,pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import date
from yahoo_fin.stock_info import get_data
import datetime
from pandas import DataFrame


def sarimax_model(ticker):
        # Dataset Building##
    today = date.today()
    end_d = str(str(today.day)+"/"+str(today.month)+"/"+str(today.year))
    df = get_data(ticker, end_date = end_d, index_as_date = True, interval ='1mo')
    ds = df[['close']]
        ##Model Fitting##
    model = SARIMAX(ds,  order = (2,0,1),  seasonal_order = (2, 1, 0, 12)) 
    result = model.fit() 
        ##Model Forecasting and creating frequency##
    dti = pd.date_range(str(ds.index[-1]), periods=12, freq="M")
    forecast = result.predict(start = str(ds.index[-1]), end = (len(ds)-1)+11, typ='levels') 
    forecast.index=dti
    l=[]
    da=str(ds.index[-1].year)+str(ds.index[-1].month)+str(ds.index[-1].day)
    for i in range(len(ds)):
        l.append([ds.index[i],ds['close'][i]])
    for i in range(len(dti)):
        l.append([dti[i],forecast.get(key=dti[i])])
    dff = DataFrame (l,columns=['Date','Forecast']) 
    year=dff['Date'].dt.year
    month=dff['Date'].dt.month
    day=dff['Date'].dt.day
    ldates=[]
    for i in range(len(year)):
        sr=str(year[i])+str(month[i])+str(day[i])
        ldates.append(int(sr))
    dff_forecast=dff['Forecast'].tolist()
    return [ldates,dff_forecast,da]


