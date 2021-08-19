# cuansignal: Signal Indicator to Buy / Sell Stock

Bismillaahirrahmaanirrahiim.

cuansignal is a library that contains several functions to predict and provide signals to buy and sell stocks. There are several indicators included in this library. In the initial version, there are four functions, namely Double Exponential Moving Average, Bollinger Band, Stochastics and Relative Strength Index.
More functions will be added in the next edition. We welcome input and critics.

### Double Exponential Moving Average (dEMA)

cuansignal.dEMA(df, base, short, long)

>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.dEMA(data, base='Close', short=10, long=100)

### Bollinger Band (bband)

cuansignal.bband(df, base, period, std)

>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.bband(data, base='Close', period=30, std=2)

### Relative Strength Index

cuansignal.rsi(df, base, EMA, MA, RSI)

>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')
>>> result = cs.rsi(data, base='Close', EMA=11, MA=200, RSI=30)

### Stochastics

cuansignal.stoch(df, period, period2, high, low)

>>> import yfinance as yf
>>> from cuansignal import signals as cs
>>> data = yf.download('AAPL', start='2018-01-01', end='2020-08-01')