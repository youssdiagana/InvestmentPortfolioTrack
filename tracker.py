import yfinance as yf


def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period = "1d")
    return {
        "current_price": history["Close"].iloc[-1],
        "ticker": ticker
    }

def get_portfolio():
    portfolio = []
    print("Enter your portfolio (type 'end' to quit): ")
    while True:
        ticker = input("Enter stock ticker: ")
        if ticker.lower() == "end":
            break
        quantity = float(input(f"Enter quantity for {ticker}: "))
        purchase_price = float(input(f"Enter purchase price for {ticker}: "))
        portfolio.append({"ticker": ticker, "quantity": quantity, "purchase_price": purchase_price})
    return portfolio

def calculate_metrics(portfolio):
    results = []
    total_portfolio_value = 0

    for stock in portfolio:
        data = fetch_stock_data(stock["ticker"])
        current_price = data["current_price"]
        stock_value = current_price * stock["quantity"]
        gain_loss = (current_price - stock["purchase_price"]) * stock["quantity"]

        results.append({
            "ticker": stock["ticker"],
            "current_price": current_price,
            "quantity": stock["quantity"],
            "purchase_price": stock["purchase_price"],
            "value": stock_value,
            "gain_loss": gain_loss,
        })
        total_portfolio_value += stock_value

    return results, total_portfolio_value

