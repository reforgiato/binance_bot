# binance_bot
very simple bot written in python 3 that uses the binance python api to make market orders, and when it does, it send you a mail (works with gmail smtp so you need a gmail account, and you need to change the setting to make it possible to access your email from unknown source)

If you want to utilize this bot you have to edit the execute_bot.py file, having installed anaconda and having installed the python binance API library, on your computer.

This simple bot utilize a very simple logic: we want to buy or sell the maximum amount possible of coinA, coinA is traded with coinB,
most of the coin available on binance are tradable in BTC, ETH, and BNB, so choose the one you prefer.

the execute_bot.py file needs to be edited with your information, in order to work:
your email, your email password, your api public and secret keys, coinA (example "xlm"), coinB (example "btc"), coinA symbol (example "XLMBTC"), coinB symbol(example "BTCUSDT"), the number at wich you want to buy or sell (you decide), and depending on the situation or amount of buy order, you may need to subtract some coinA to the first order in the " while side == 'buy' " block, cause you will get an error (really i don't know why, it happens also in the binance site) if you try buy the maximum possible in one order, so in the code i make two market buy orders, the first one contains the 98% of the total amount of coinA and the second contains the remainings.

The code is really simple and ugly, i just wanted to create something fast just for me, in the future, if i'll have time, i'll make a well written OOP version of this, and maybe i'll implement something else.


