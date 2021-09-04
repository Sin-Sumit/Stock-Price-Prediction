import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import date
from yahoo_fin.stock_info import get_data
import datetime
import pandas as pd
from pandas import DataFrame
# import yfinance as yf
def sarimax_model(ticker):
        # Dataset Building##
    if ticker=="msft":
        df=pd.read_csv("<relative pathto respective csv file>/MSFT.csv")
    elif ticker=="qcom":
        df=pd.read_csv("<relative pathto respective csv file>/QCOM.csv")
    elif ticker=="nvda":
        df=pd.read_csv("<relative pathto respective csv file>/NVDA.csv")
    elif ticker=="adbe":
        df=pd.read_csv("<relative pathto respective csv file>/ADBE.csv")
    elif ticker=="amgn":
        df=pd.read_csv("<relative pathto respective csv file>/AMGN.csv")
    elif ticker=="pypl":
        df=pd.read_csv("<relative pathto respective csv file>/PYPL.csv")
    elif ticker=="goog":
        df=pd.read_csv("<relative pathto respective csv file>/GOOG.csv")
    elif ticker=="amzn":
        df=pd.read_csv("<relative pathto respective csv file>/AMZN.csv")
    elif ticker=="aapl":
        df=pd.read_csv("<relative pathto respective csv file>/AAPL.csv")
    elif ticker=="tsla":
        df=pd.read_csv("<relative pathto respective csv file>/TSLA.csv")
    elif ticker=="fb":
        df=pd.read_csv("<relative pathto respective csv file>/FB.csv")
    df.set_index("Date", inplace = True)
    df.index = pd.to_datetime(df.index)
    ds=df['Close']
        ##Model Fitting##
    model = SARIMAX(ds,  order = (2,0,1),  seasonal_order = (2, 1, 0, 12)) 
    result = model.fit() 
        ##Model Forecasting and creating frequency##
    dti = pd.date_range(str(ds.index[-1]), periods=12, freq="M")
    forecast = result.predict(start = str(ds.index[-1]), end = (len(ds)-1)+11, typ='levels') 
    forecast.index=dti
    ss=ds.append(forecast)
    dff = ss.to_frame()
    idx = pd.Index(dff)
    dff_f = idx.to_list()
    dff_forecast = []
    dff_dates = []
    for i in range(len(dff_f)):
        dff_forecast.append(dff_f[i][0])
    for i in range(len(dff)):
        st = str(dff.index[i])
        d = str(st[:4])+str(st[5:7])+str(st[8:10])
        dff_dates.append(int(d))
    da=str(dff_dates[-14])
    return [dff_dates,dff_forecast,da]
