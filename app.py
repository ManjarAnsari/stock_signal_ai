
import streamlit as st
from ml_utils import load_model, predict_signal
from backtest import run_backtest
from indicator_utils import plot_indicators

st.title("📈 AI Stock Signal Detector - India Only")

ticker = st.text_input("Enter NSE stock ticker (e.g., RELIANCE.NS)", "RELIANCE.NS")

if ticker:
    model = load_model()
    prediction, df = predict_signal(ticker, model)
    st.write(f"📊 Predicted Signal: **{prediction}**")

    st.pyplot(plot_indicators(df, prediction))

    st.write("⚡ Backtesting Results")
    result_plot = run_backtest(df)
    st.pyplot(result_plot)
