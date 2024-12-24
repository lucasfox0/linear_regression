import yfinance as yf # fetches historical financial data (stock price)
import plotly.graph_objects as go # creates interactive visualizations

# Fetch data for ExxonMobil (XOM)
ticker_xom = yf.Ticker("XOM")
data_xom = ticker_xom.history(period="max")

# Fetch data for Brent Crude Oil Futures (BZ=F)
ticker_bz = yf.Ticker("BZ=F")
data_bz = ticker_bz.history(period="max")

# Get the earliest date in BZ=F data (this will be the cut-off date). This is so the graph starts where both stocks data starts.
bz_start_date = data_bz.index.min()

# Filter the XOM data to start from the same date as BZ=F (aka rremoves XOM data that predates the BZ=F data)
data_xom_filtered = data_xom[data_xom.index >= bz_start_date]

# Create the Plotly graph
fig = go.Figure()

# Add ExxonMobil data (XOM) - Stock price (filtered)
fig.add_trace(go.Scatter(x=data_xom_filtered.index, y=data_xom_filtered['Close'], mode='lines', name='XOM Stock Price', line=dict(color='blue')))

# Add Brent Crude Oil Futures data (BZ=F)
fig.add_trace(go.Scatter(x=data_bz.index, y=data_bz['Close'], mode='lines', name='Brent Crude Oil', line=dict(color='orange')))

# Add title and labels
fig.update_layout(
    title="ExxonMobil Stock Price vs Brent Crude Oil Price (All Time)",
    xaxis_title="Date",
    yaxis_title="Price ($)",
    legend_title="Legend",
    template="plotly_dark"  # Optional: Set a dark theme
)

# Convert Plotly graph to HTML
graph_html = fig.to_html(full_html=False)

# Save the graph HTML to a file
with open("stock_and_oil_graph.html", "w") as file:
    file.write(graph_html)
