import numpy as np
  
def dEMA(df, base, short, long):
    df['EMA '+str(short)] = df[base].ewm(span=short, adjust=False).mean()
    df['EMA '+str(long)] = df[base].ewm(span=long, adjust=False).mean()

    def buy_sell(df):
        sigPriceBuy = []
        sigPriceSell = []
        flag = -1

        for i in range(len(df)):
            if df['EMA '+str(short)][i] > df['EMA '+str(long)][i]:
                if flag !=1:
                    sigPriceBuy.append(df['Close'][i])
                    sigPriceSell.append(np.nan)
                    flag = 1
                else:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(np.nan)
            elif df['EMA '+str(short)][i] < df['EMA '+str(long)][i]:
                if flag != 0:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(df['Close'][i])
                    flag = 0
                else:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(np.nan)
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)

        return (sigPriceBuy, sigPriceSell)

    buy_sell = buy_sell(df)
    df['Buy'] = buy_sell[0]
    df['Sell'] = buy_sell[1]
    return df

def bband(df, base, period, std):
    df['SMA'] = df[base].rolling(window=period).mean()
    df['STD'] = df[base].rolling(window=period).std()
    df['Upper'] = df['SMA'] + (df['STD'] * std)
    df['Lower'] = df['SMA'] - (df['STD'] * std)

    def get_signal(df):
        buy_signal = []
        sell_signal = []

        for i in range(len(df[base])):
            if df[base][i] > df['Upper'][i]:
                buy_signal.append(np.nan)
                sell_signal.append(df['Close'][i])
            elif df[base][i] < df['Lower'][i]:
                buy_signal.append(df[base][i])
                sell_signal.append(np.nan)
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        return (buy_signal, sell_signal)

    df['Buy'] = get_signal(df)[0]
    df['Sell'] = get_signal(df)[1]
    return df

def rsi(df, base, EMA, MA, RSI):
    if len(df) < MA:
        df['MA'+str(MA)] = df[base].rolling(window=(len(df)-1)).mean()
    else:
        df['MA'+str(MA)] = df[base].rolling(window=MA).mean()
    df['Price Change'] = df[base].pct_change()
    df['Upmove'] = df['Price Change'].apply(lambda x: x if x > 0 else 0)
    df['Downmove'] = df['Price Change'].apply(lambda x: abs(x) if x < 0 else 0)
    df['Avg Up'] = df['Upmove'].ewm(span=EMA).mean()
    df['Avg Down'] = df['Downmove'].ewm(span=EMA).mean()
    df['RS'] = df['Avg Up']/df['Avg Down']
    df['RSI'] = df['RS'].apply(lambda x: 100-(100/(x+1)))
    df.loc[(df[base] > df['MA'+str(MA)]) & (df['RSI'] < RSI), 'Buy'] = df[base]
    df['Sell'] = np.nan
    return df

def stoch(df, period, period2, high, low):
    df[str(period)+'-high'] = df['High'].rolling(period).max()
    df[str(period)+'-low'] = df['Low'].rolling(period).min()
    df['%K'] = (df['Close'] - df[str(period)+'-low'])*100/(df[str(period)+'-high'] - df[str(period)+'-low'])
    df['%D'] = df['%K'].rolling(period2).mean()

    def stoch(prices, k, d):    
        buy_price = []
        sell_price = []
        stoch_signal = []
        signal = 0

        for i in range(len(prices)):
            if k[i] < low and d[i] < low and k[i] < d[i]:
                if signal != 1:
                    buy_price.append(prices[i])
                    sell_price.append(np.nan)
                    signal = 1
                    stoch_signal.append(signal)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    stoch_signal.append(0)
            elif k[i] > high and d[i] > high and k[i] > d[i]:
                if signal != -1:
                    buy_price.append(np.nan)
                    sell_price.append(prices[i])
                    signal = -1
                    stoch_signal.append(signal)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    stoch_signal.append(0)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                stoch_signal.append(0)
        return buy_price, sell_price, stoch_signal            

    x = stoch(df['Close'], df['%K'], df['%D'])
    df['Buy'] = x[0]
    df['Sell'] = x[1]
    df['Stoch Signal'] = x[2]
    return df