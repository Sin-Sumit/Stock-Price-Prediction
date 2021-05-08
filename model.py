import numpy as np,pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima_model import ARIMA
# import plotly.express as px 
from pandas_datareader import data as pdr
from yahoo_fin.stock_info import get_data
from datetime import date
import matplotlib.pyplot as plt

class dataset:
    def build_dataset(self,ticker):
        self.ticker=ticker
        today=date.today()
        end_d=str(str(today.day)+"/"+str(today.month)+"/"+str(today.year))
        df= get_data(self.ticker, end_date=end_d, index_as_date = True, interval='1wk')
        ds=df[['close']]
        self.data=ds.fillna(0,inplace=True)
    def build_model(self):
        model = SARIMAX(self.data['close'],  order = (2,0,1),  seasonal_order =(2, 1, 0, 12)) 
        self.result = model.fit() 
    def predict_result(self):
        self.forecast = self.result.predict(start = len(self.data),  end = (len(self.data)-1) + 12,  typ = 'levels').rename('Forecast') 
        print(self.forecast)
class sarimax_model(dataset):
    def __init__(self,ticker):
        self.ticker=ticker
# Forecast for the next 2 years
model=sarimax_model('amzn')
model_1=model.build_dataset(model.ticker)
# Plot the forecast values 


# ds['close'].plot(figsize = (12, 5), legend = True) 
# forecast.plot(legend = True)


# d=pd.DataFrame(forecast)
# d.rename(columns={'Forecast':'close'})
# dss=ds.append(d)
# dss['close']=dss['close'].fillna(dss['Forecast'])
# dss.drop(columns=['Forecast'])
# px.line(data_frame=dss,x=dss.index,y='close')
