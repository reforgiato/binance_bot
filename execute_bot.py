from binance.client import Client
import smtplib
from time import sleep

host = "smtp.gmail.com"
port = 587
username = "change with your email"
password = "change with your password"
from_email = username
to_mail = username

client = Client("change with your public API key",
                "change with your secret API key")
                
    
coinA_balance = int(float(client.get_asset_balance("coinA").get("free")))
coinB_balance = float(client.get_asset_balance("coinB").get("free"))



Side = "sell"  # depending on the situation, change this with "sell" or "buy"

while True:
    while Side == "sell":
        coinA_last_price = float(client.get_symbol_ticker(symbol="coinA symbol").get("price"))
        coinB_last_price = float(client.get_symbol_ticker(symbol="coinB symbol").get("price"))
        
        if coinA_last_price > you decide and coinB_last_price > you decide:  # change you decide with a float
            client.create_order(symbol="coinA symbol", side="SELL", type="MARKET",
                                quantity=coinA_balance)  # sell all coinA
            
            coinA_balance = int(float(client.get_asset_balance("coinA").get("free")))
            coinB_balance = float(client.get_asset_balance("coinB").get("free"))

            email_conn = smtplib.SMTP(host, port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(username, password)
            email_conn.sendmail(from_email, to_mail, 
                                "you sold")
            email_conn.quit()
            Side = "buy"
        sleep(30)  # seconds
    
    while Side == "buy":
        coinA_last_price = float(client.get_symbol_ticker(symbol="coinA symbol").get("price"))
        coinB_last_price = float(client.get_symbol_ticker(symbol="coinB symbol").get("price"))
        
        if coinA_last_price < you decide and coinB_last_price < you decide:  # change you decide with a float
            coinA_buy_quantity = int(float((coinB_balance / coinA_last_price) - depending on situation))  # more info in the readme file
            client.create_order(symbol="coinA symbol", side="BUY", type="MARKET",
                                quantity=coinA_balance)
            
            coinA_balance = int(float(client.get_asset_balance("coinA").get("free")))
            coinB_balance = float(client.get_asset_balance("coinB").get("free"))
            coinA_last_price = float(client.get_symbol_ticker(symbol="coinA symbol").get("price"))
            coinA_buy_quantity = int(float(coinB_balance / coinA_last_price))
            
            client.create_order(symbol="MFTETH", side="BUY", type="MARKET",
                                quantity=mft_buy_quantity)  # buy the maximum coinA possible
            
            mft_balance = int(float(client.get_asset_balance("mft").get("free")))
            eth_balance = float(client.get_asset_balance("eth").get("free"))
            
            email_conn = smtplib.SMTP(host, port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(username, password)
            email_conn.sendmail(from_email, to_mail,
                                "you bought")
            email_conn.quit()
            Side = "sell"
        sleep(30)
