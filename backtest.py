
import matplotlib.pyplot as plt

def run_backtest(df):
    df['Return'] = df['Close'].pct_change()
    df['Strategy'] = df['Signal'].shift(1) * df['Return']
    df[['Return', 'Strategy']].cumsum().plot(figsize=(10, 5))
    plt.title("📈 Backtest: Strategy vs Market")
    return plt
