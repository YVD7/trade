from datetime import datetime
import time
import yfinance as yf
import talib as ta
from logger import CustomeLogging as cl

overbought = 70
oversold = 30

filename='bot'
logger = cl().logger(filename)

while True:

    btc = yf.download("BTC-USD", interval="1m", period="1d")
    btc['RSI'] = ta.RSI(btc['Close'], timeperiod=14)

    current_price = round(btc.iloc[-1]['Close'], 2)
    currnet_rsi = round(btc.iloc[-1]['RSI'], 2)
    
    if currnet_rsi >= overbought:
        logger.info(f"rsi: {currnet_rsi}, price: {round(current_price, 2)}, status: Sell")
    
    elif currnet_rsi <= oversold:
        logger.info(f"rsi: {currnet_rsi}, price: {round(current_price, 2)}, status: Buy")

    else:
        logger.info(f"rsi: {currnet_rsi}, price: {round(current_price, 2)}, status: Hold")

    time.sleep(60)

    if datetime.now().time().strftime('%H:%M') == '23:00':
        break 