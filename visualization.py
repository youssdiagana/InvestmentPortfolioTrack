import plotly.express as px
import streamlit as st


def visualize_portfolio_plotly(portfolio):
    tickers = [stock["ticker"] for stock in portfolio]
    values = [stock["value"] for stock in portfolio]

    # Create the Plotly Pie Chart
    fig = px.pie(values=values, names=tickers, title="Portfolio Allocation")

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)