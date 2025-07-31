
import matplotlib.pyplot as plt

def plot_indicators(df, signal):
    fig, ax = plt.subplots(figsize=(10, 5))
    df['Close'].plot(label='Close Price', ax=ax)
    df['EMA_20'].plot(label='EMA 20', ax=ax)
    df['SMA_50'].plot(label='SMA 50', ax=ax)
    ax.set_title(f"Indicators with Signal: {signal}")
    ax.legend()
    return fig
