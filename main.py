from fastapi import FastAPI, Query
from typing import Optional
import pandas as pd

app = FastAPI()

# Cargar datos desde CSV
securities_df = pd.read_csv('securities.csv')
market_data_df = pd.read_csv('market_data.csv')
historical_prices_df = pd.read_csv('historical_prices.csv')

# Endpoint para Security
@app.get("/securities/")
def get_securities(
    symbol: Optional[str] = None,
    name: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: int = 1,
    size: int = 10
):
    df = securities_df.copy()
    if symbol:
        df = df[df['symbol'].str.contains(symbol, case=False)]
    if name:
        df = df[df['name'].str.contains(name, case=False)]
    if sort_by:
        df = df.sort_values(by=sort_by)
    total = len(df)
    start = (page - 1) * size
    end = start + size
    data = df.iloc[start:end].to_dict(orient='records')
    return {"total": total, "page": page, "size": size, "data": data}

# Endpoint para MarketData
@app.get("/market_data/")
def get_market_data(
    security_id: Optional[int] = None,
    date: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: int = 1,
    size: int = 10
):
    df = market_data_df.copy()
    if security_id:
        df = df[df['security_id'] == security_id]
    if date:
        df = df[df['date'] == date]
    if sort_by:
        df = df.sort_values(by=sort_by)
    total = len(df)
    start = (page - 1) * size
    end = start + size
    data = df.iloc[start:end].to_dict(orient='records')
    return {"total": total, "page": page, "size": size, "data": data}

# Endpoint para HistoricalPrices
@app.get("/historical_prices/")
def get_historical_prices(
    security_id: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: int = 1,
    size: int = 10
):
    df = historical_prices_df.copy()
    if security_id:
        df = df[df['security_id'] == security_id]
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    if sort_by:
        df = df.sort_values(by=sort_by)
    total = len(df)
    start = (page - 1) * size
    end = start + size
    data = df.iloc[start:end].to_dict(orient='records')
    return {"total": total, "page": page, "size": size, "data": data}

