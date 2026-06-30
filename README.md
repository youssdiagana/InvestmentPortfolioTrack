# 💼 Investment Portfolio Tracker
  An interactive web application built with Python and Streamlit that allows users to track the real-time value of their investment portfolios by       inputting stock tickers, purchase prices, and quantities. The tool validates tickers, fetches live market data, calculates gains/losses, and          visualizes portfolio allocation using interactive charts.

**Note:** This app is hosted on Streamlit's cloud platform and may take a few seconds to load if inactive.

🔗 **Live Demo:** https://investmentportfoliotrackerbyyouss.streamlit.app

---

## Features

- **Ticker Validation** - Validates stock tickers against Yahoo Finance before adding them to the portfolio
- **Real-Time Pricing** - Fetches live stock prices using the `yfinance` API and displays the current price as you type a ticker
- **Multi-Stock Portfolio** - Add multiple stocks to your portfolio within a single session using Streamlit session state
- **Gain/Loss Calculation** - Calculates current portfolio value and unrealized gains/losses per stock based on purchase price and quantity
- **Interactive Pie Chart** - Visualizes portfolio allocation by value using an interactive Plotly pie chart rendered inside the Streamlit app
- **Simple, Responsive Interface** - Clean UI built with Streamlit, accessible from any browser

---

## How It Works
         
- Step 1: Enter a stock ticker symbol (e.g. `AAPL`, `TSLA`, `MSFT`) in the input field.
         
- Step 2: The app fetches and displays the current market price for that ticker.
         
- Step 3: Enter the quantity of shares you own and the price you originally paid per share.
         
- Step 4: Click **"Add to Portfolio"** to save the stock to your session.
         
- Step 5: Repeat for as many stocks as you like.
         
- Step 6: Click **"Calculate Metrics"** to see a summary of current values and gains/losses, 
      along with a portfolio allocation pie chart.
         
## Project Structure
```
InvestmentPortfolioTrack/
├── main.py             # Streamlit app entry point - UI, session state, user input flow
├── tracker.py          # Core logic - fetches stock data and calculates portfolio metrics
├── visualization.py    # Plotly pie chart rendering inside Streamlit
├── requirements.txt    # Python dependencies
└── .devcontainer/      # Dev Container configuration for VS Code / GitHub Codespaces
```

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application framework and UI |
| yfinance | Real-time stock data retrieval from Yahoo Finance |
| Plotly | Interactive portfolio allocation pie chart |
| Matplotlib | Listed as a dependency (available for future use) |

## Installation and Local Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Steps
1. Clone the repository
```bash
   git clone https://github.com/youssdiagana/InvestmentPortfolioTrack.git
   cd InvestmentPortfolioTrack
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
5. Run the Streamlit app
```bash
   streamlit run main.py
```
The app will open in your browser at `http://localhost:8501`.
---
### Dev Container (Optional)
This project includes a `.devcontainer` configuration for use with VS Code Dev Containers or GitHub Codespaces. 
Open the repository in either environment and it will automatically set up the development environment.

## Dependencies
```
    streamlit
    yfinance
    matplotlib
    plotly
```
---

## Author
**youssdiagana** – [GitHub Profile](https://github.com/youssdiagana)

---


