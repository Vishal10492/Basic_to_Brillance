from ks_api_client import ks_api

# Defining the host is optional and defaults to https://tradeapi.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.

# For using sandbox environment use host as https://sbx.kotaksecurities.com/apim
client = ks_api.KSTradeApi(access_token="", userid="",
                           consumer_key="", ip="127.0.0.1", app_id="", host="https://sbx.kotaksecurities.com/apim")

# Get session for user
client.login(password="")

# Generated session token
client.session_2fa(access_code="")

# Place an order
client.place_order(order_type="N", instrument_token=727, transaction_type="BUY",
                   quantity=1, price=0, disclosed_quantity=0, trigger_price=0,
                   validity="GFD", variety="REGULAR", tag="string")
# Place an MIS order
client.place_order(order_type="MIS", instrument_token=727, transaction_type="BUY",
                   quantity=1, price=0, disclosed_quantity=0, trigger_price=0,
                   validity="GFD", variety="REGULAR", tag="string")

# Modify an order
client.modify_order(order_id="", quantity=1, price=0, disclosed_quantity=0, trigger_price=0, validity="GFD")

# Cancel an order
client.cancel_order(order_id="")

# Get Report Orders
client.order_report()

# Get Report Orders for order id
client.order_report(order_id="")

# Get Margin required
order_info = [
    {"instrument_token": 727, "quantity": 1, "price": 1300, "amount": 0, "trigger_price": 1190},
    {"instrument_token": 1374, "quantity": 1, "price": 1200, "amount": 0, "trigger_price": 1150}
]
client.margin_required(transaction_type="BUY", order_info=order_info)

# Get Positions
client.positions(position_type="TODAYS")

# Get Quote details
client.quote(instrument_token=110)

# Get Historical data
client.history("historicalprices",
               {"exchange": "bse", "cocode": "476", "fromdate": "01-jan-2014", "todate": "08-oct-2015"})
client.history("historicalprices-unadjusted", {"exchange": "bse", "co_code": "476", "date": "16-Jun-2016"})
client.history("NSEFNO_HistoricalContinuousChart", {"symbol": "HDFC", "expiry type": "near"})
client.history("LiveorEODHistorical", {"exchange": "BSE", "co_code": "5400", "period": "Y", "cnt": "3"})

# Terminate user's Session
client.logout()
