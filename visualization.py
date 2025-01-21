import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

def visualize_portfolio_matplotlib(portfolio):
    tickers = [stock["ticker"] for stock in portfolio]
    values = [stock["value"] for stock in portfolio]

    # Create the Matplotlib Pie Chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(values, labels=tickers, autopct='%1.1f%%')
    ax.set_title("Portfolio Allocation")

    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)

def visualize_portfolio_plotly(portfolio):
    tickers = [stock["ticker"] for stock in portfolio]
    values = [stock["value"] for stock in portfolio]

    # Create the Plotly Pie Chart
    fig = px.pie(values=values, names=tickers, title="Portfolio Allocation")

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)