
import yfinance as yf
import pandas as pd
import joblib

def load_model():
    return joblib.load("models/random_forest_model.pkl")

def add_technical_indicators(df):
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['RSI'] = compute_rsi(df['Close'])
    df['MACD'], df['MACD_signal'] = compute_macd(df['Close'])
    return df.dropna()

def compute_rsi(series, period=14):
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def compute_macd(series, short=12, long=26, signal=9):
    exp1 = series.ewm(span=short, adjust=False).mean()
    exp2 = series.ewm(span=long, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def predict_signal(ticker, model):
    df = yf.download(ticker, period="6mo", interval="1d")
    df = add_technical_indicators(df)
    features = df[["EMA_20", "SMA_50", "RSI", "MACD", "MACD_signal"]]
    df['Signal'] = model.predict(features)
    return df['Signal'].iloc[-1], df
