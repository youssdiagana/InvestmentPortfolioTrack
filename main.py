import streamlit as st
from tracker import calculate_metrics
from visualization import visualize_portfolio, export_to_html
import yfinance as yf

def validate_ticker(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        # Check if the 'symbol' or 'longName' field exists, indicating a valid ticker
        if 'symbol' in info and info['symbol'] is not None:
            return True
        return False
    except:
        return False

def main():
    st.title("Investment Portfolio Tracker")
    st.write("Welcome! Use this app to track and visualize your portfolio.")

    # Initialize portfolio in session state
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = []

    # Input Section
    st.header("Enter Your Portfolio")

    # Ticker Input
    ticker = st.text_input("Enter stock ticker (type 'done' to finish):", key="ticker_input")
    if ticker.lower() == "done":
        st.write("Portfolio entry complete!")
    elif ticker:
        # Fetch and display the current stock price
        try:
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")['Close'].iloc[-1]
            st.info(f"Current Price for {ticker}: ${current_price:.2f}")
        except:
            st.error(f"Could not fetch data for ticker '{ticker}'. Please check and try again.")
            return

        # Quantity and Purchase Price Inputs
        quantity = st.number_input(
            f"Enter quantity for {ticker}:",
            min_value=0.0,
            step=1.0,
            key=f"qty_{ticker}"
        )
        purchase_price = st.number_input(
            f"Enter purchase price for {ticker} (Current: ${current_price:.2f}):",
            min_value=0.0,
            step=0.01,
            key=f"price_{ticker}"
        )

        # Add to Portfolio
        if st.button(f"Add {ticker} to Portfolio"):
            st.session_state.portfolio.append(
                {"ticker": ticker, "quantity": quantity, "purchase_price": purchase_price, "current_price": current_price}
            )
            st.success(f"Added {ticker} to your portfolio!")

    # Display Current Portfolio
    if st.session_state.portfolio:
        st.header("Current Portfolio")
        for stock in st.session_state.portfolio:
            st.write(
                f"{stock['ticker']}: Quantity = {stock['quantity']}, "
                f"Purchase Price = ${stock['purchase_price']:.2f}, Current Price = ${stock['current_price']:.2f}"
            )

    # Calculate Metrics
    if st.button("Calculate Metrics"):
        results, total_value = calculate_metrics(st.session_state.portfolio)

        # Display Summary
        st.header("Portfolio Summary")
        for stock in results:
            st.write(
                f"{stock['ticker']}: Current Value = ${stock['value']:.2f}, Gain/Loss = ${stock['gain_loss']:.2f}"
            )
        st.write(f"Total Portfolio Value: ${total_value:.2f}")

        # Visualization
        visualize_portfolio(results)

        # Export to HTML
        export_to_html(results)
        st.success("Portfolio visualization exported to `portfolio_allocation.html`!")

if __name__ == "__main__":
    main()
