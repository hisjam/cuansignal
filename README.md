# cuansignal: Signal Indicator to Buy / Sell Stock

Bismillaahirrahmaanirrahiim.
cuansignal is a library that contains several functions to predict and provide signals to buy and sell stocks. There are several indicators included in this library. In the initial version, there are four functions, namely Double Exponential Moving Average, Bollinger Band, Stochastics and Relative Strength Index.
More functions will be added in the next edition. We welcome input and critics.


## Function

### Double Exponential Moving Average (dEMA)
```python
cuansignal.dEMA(df, base, short, long)
df = data to be analyzed, with format ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
base = parameter on which the EMA calculation is based, for example 'Close', or 'Adj Close', or something else
short = the first EMA period used in the model (which is shorter)
long = the second EMA period used in the model (which is longer)
The resulting output is a DataFrame
```

```python
>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.dEMA(data, base='Close', short=10, long=100)
>>> print(result)

#                   Open        High         Low       Close   Adj Close     Volume     EMA 10    EMA 100      Buy       Sell
# Date
# 2018-01-02   42.540001   43.075001   42.314999   43.064999   41.248272  102223600  43.064999  43.064999      NaN        NaN
# 2018-01-03   43.132500   43.637501   42.990002   43.057499   41.241089  118071600  43.063635  43.064850      NaN  43.057499
# 2018-01-04   43.134998   43.367500   43.020000   43.257500   41.432659   89738400  43.098883  43.068665  43.2575        NaN
# 2018-01-05   43.360001   43.842499   43.262501   43.750000   41.904385   94640000  43.217268  43.082157      NaN        NaN
# 2018-01-08   43.587502   43.902500   43.482498   43.587502   41.748737   82271200  43.284583  43.092164      NaN        NaN
# ...                ...         ...         ...         ...         ...        ...        ...        ...      ...        ...
# 2020-07-27   93.709999   94.904999   93.480003   94.809998   94.034538  121214000  95.069989  82.520419      NaN        NaN
# 2020-07-28   94.367500   94.550003   93.247498   93.252502   92.489784  103625600  94.739537  82.732936      NaN        NaN
# 2020-07-29   93.750000   95.230003   93.712502   95.040001   94.262657   90329200  94.794167  82.976640      NaN        NaN
# 2020-07-30   94.187500   96.297501   93.767502   96.190002   95.403267  158130000  95.047955  83.238291      NaN        NaN
# 2020-07-31  102.885002  106.415001  100.824997  106.260002  105.390907  374336800  97.086509  83.694166      NaN        NaN

```

### Bollinger Band (bband)
```python
cuansignal.bband(df, base, period, std)
df = data to be analyzed, with format ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
base = parameter that is the basis for calculating Simple MA, for example 'Close', or 'Adj Close', or others
period = length of the period to be used in calculating the value of Simple MA and Standard Deviation
std = standard deviation multiplier
The resulting output is a DataFrame
```

```python
>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.bband(data, base='Close', period=30, std=2)
>>> print(result)

#                   Open        High         Low       Close   Adj Close     Volume        SMA       STD       Upper      Lower  Buy        Sell
# Date
# 2018-01-02   42.540001   43.075001   42.314999   43.064999   41.248272  102223600        NaN       NaN         NaN        NaN  NaN         NaN
# 2018-01-03   43.132500   43.637501   42.990002   43.057499   41.241089  118071600        NaN       NaN         NaN        NaN  NaN         NaN
# 2018-01-04   43.134998   43.367500   43.020000   43.257500   41.432659   89738400        NaN       NaN         NaN        NaN  NaN         NaN
# 2018-01-05   43.360001   43.842499   43.262501   43.750000   41.904385   94640000        NaN       NaN         NaN        NaN  NaN         NaN
# 2018-01-08   43.587502   43.902500   43.482498   43.587502   41.748737   82271200        NaN       NaN         NaN        NaN  NaN         NaN
# ...                ...         ...         ...         ...         ...        ...        ...       ...         ...        ...  ...         ...
# 2020-07-27   93.709999   94.904999   93.480003   94.809998   94.034538  121214000  92.712333  3.608910   99.930152  85.494514  NaN         NaN
# 2020-07-28   94.367500   94.550003   93.247498   93.252502   92.489784  103625600  92.962499  3.361075   99.684650  86.240349  NaN         NaN
# 2020-07-29   93.750000   95.230003   93.712502   95.040001   94.262657   90329200  93.196500  3.247561   99.691622  86.701377  NaN         NaN
# 2020-07-30   94.187500   96.297501   93.767502   96.190002   95.403267  158130000  93.472916  3.131830   99.736577  87.209256  NaN         NaN
# 2020-07-31  102.885002  106.415001  100.824997  106.260002  105.390907  374336800  94.083833  3.741930  101.567694  86.599972  NaN  106.260002

```

### Relative Strength Index
```python
cuansignal.rsi(df, base, EMA, MA, RSI)
df = data to be analyzed, with format ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
base = parameter on which the RSI calculation is based, for example 'Close', or 'Adj Close', or something else
EMA = the length of the period to be used in calculating the EMA value for the Average Up and Down periods
MA = the length of the MA period which is the cut-of buying signal
RSI = RSI value which is the reference for buying signal
The resulting output is a DataFrame
```

```python
>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.rsi(data, base='Close', EMA=11, MA=200, RSI=30)
>>> print(result)

#                   Open        High         Low       Close   Adj Close     Volume      MA200  ...  Downmove    Avg Up  Avg Down          RS        RSI  Buy  Sell
# Date                                                                                          ...
# 2018-01-02   42.540001   43.075001   42.314999   43.064999   41.248272  102223600        NaN  ...  0.000000  0.000000  0.000000         NaN        NaN  NaN   NaN
# 2018-01-03   43.132500   43.637501   42.990002   43.057499   41.241089  118071600        NaN  ...  0.000174  0.000000  0.000095    0.000000   0.000000  NaN   NaN
# 2018-01-04   43.134998   43.367500   43.020000   43.257500   41.432659   89738400        NaN  ...  0.000000  0.001838  0.000057   32.006998  96.970339  NaN   NaN
# 2018-01-05   43.360001   43.842499   43.262501   43.750000   41.904385   94640000        NaN  ...  0.000000  0.004911  0.000039  126.150084  99.213528  NaN   NaN
# 2018-01-08   43.587502   43.902500   43.482498   43.587502   41.748737   82271200        NaN  ...  0.003714  0.003543  0.001063    3.332459  76.918422  NaN   NaN
# ...                ...         ...         ...         ...         ...        ...        ...  ...       ...       ...       ...         ...        ...  ...   ...
# 2020-07-27   93.709999   94.904999   93.480003   94.809998   94.034538  121214000  74.389675  ...  0.000000  0.007620  0.007816    0.975028  49.367794  NaN   NaN        
# 2020-07-28   94.367500   94.550003   93.247498   93.252502   92.489784  103625600  74.568325  ...  0.016428  0.006350  0.009251    0.686457  40.704080  NaN   NaN        
# 2020-07-29   93.750000   95.230003   93.712502   95.040001   94.262657   90329200  74.748262  ...  0.000000  0.008487  0.007709    1.100866  52.400580  NaN   NaN        
# 2020-07-30   94.187500   96.297501   93.767502   96.190002   95.403267  158130000  74.934375  ...  0.000000  0.009089  0.006424    1.414785  58.588444  NaN   NaN        
# 2020-07-31  102.885002  106.415001  100.824997  106.260002  105.390907  374336800  75.171525  ...  0.000000  0.025022  0.005354    4.673949  82.375592  NaN   NaN        

```
### Stochastics
```python
cuansignal.stoch(df, period, period2, high, low)
df = data to be analyzed, with format ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
period = the length of the period to be used in calculating the value of %K
period2 = the length of the period to be used in calculating the value of %D
high = high limit value which becomes the cut-of buying/selling signal
low = low limit value which becomes the cut-of buying/selling signal
The resulting output is a DataFrame
```

```python
>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.stoch(data, period=50, period2=3, high=70, low=30)
>>> print(result)

#                   Open        High         Low       Close   Adj Close     Volume     50-high     50-low         %K         %D  Buy  Sell  Stoch Signal
# Date
# 2018-01-02   42.540001   43.075001   42.314999   43.064999   41.248272  102223600         NaN        NaN        NaN        NaN  NaN   NaN             0
# 2018-01-03   43.132500   43.637501   42.990002   43.057499   41.241089  118071600         NaN        NaN        NaN        NaN  NaN   NaN             0
# 2018-01-04   43.134998   43.367500   43.020000   43.257500   41.432659   89738400         NaN        NaN        NaN        NaN  NaN   NaN             0
# 2018-01-05   43.360001   43.842499   43.262501   43.750000   41.904385   94640000         NaN        NaN        NaN        NaN  NaN   NaN             0
# 2018-01-08   43.587502   43.902500   43.482498   43.587502   41.748737   82271200         NaN        NaN        NaN        NaN  NaN   NaN             0
# ...                ...         ...         ...         ...         ...        ...         ...        ...        ...        ...  ...   ...           ...
# 2020-07-27   93.709999   94.904999   93.480003   94.809998   94.034538  121214000   99.955002  75.052498  79.339410  73.771033  NaN   NaN             0
# 2020-07-28   94.367500   94.550003   93.247498   93.252502   92.489784  103625600   99.955002  77.580002  70.044695  73.303047  NaN   NaN             0
# 2020-07-29   93.750000   95.230003   93.712502   95.040001   94.262657   90329200   99.955002  78.252502  77.352835  75.578980  NaN   NaN             0
# 2020-07-30   94.187500   96.297501   93.767502   96.190002   95.403267  158130000   99.955002  78.272499  82.635771  76.677767  NaN   NaN             0
# 2020-07-31  102.885002  106.415001  100.824997  106.260002  105.390907  374336800  106.415001  78.272499  99.449236  86.479281  NaN   NaN             0

```

## Changelog

### Version 1.1.2 (2021.08.19)
- Updating Minor Bugs
- Add Github Link

### Version 1.1.1 (2021.08.19)
- Updating Minor Bugs

### Version 1.1.0 (2021.08.19)
- Updating Minor Bugs
- Updating Readme.md

### Version 1.0.0 (2021.08.19)
- Initial release

## License

cuansignal is licensed under the [MIT license](LICENSE).
