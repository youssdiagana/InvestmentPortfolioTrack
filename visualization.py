import matplotlib.pyplot as plt
import plotly.express as px

def visualize_portfolio(portfolio):
    tickers = [stock["ticker"] for stock in portfolio]
    values = [stock["value"] for stock in portfolio]

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=tickers, autopct='%1.1f%%')
    plt.title("Portfolio Allocation")
    plt.show()

def export_to_html(portfolio):
    tickers = [stock["ticker"] for stock in portfolio]
    values = [stock["value"] for stock in portfolio]

    fig = px.pie(values=values, names=tickers, title = "Portfolio Allocation")
    fig.write_html("portfolio_allocation.html")
    print("Interactive chart saved to portfolio_allocation.html")
