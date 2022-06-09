commands = {
    "params":{
        "symbol": "",
        "side":"",
        "type":"",
        "quantity": "",
        "price":"",
        "stopPrice":"",
        "leverage":"",

        
        
    }
}


from Supports.Options import options
from API_keys import api_keys
import Supports.Binance

MyBot = TradingBot(EXCHANGE, api_keys, options)
MyBot.switch_exchange(EXCHANGE, optional)
result = MyBot.execute(commands)


class TradingBot():
    def __init__(self, EXCHANGE = None, api_keys = None, options = options):
        
        # API dictionary includes the api key and api secret and other essential information for authentication
        self.api_keys = api_keys 
        
        # Setting the basic URL for api
        if EXCHANGE:
            self.BASE_URL = options[EXCHANGE]["BASE_URL"]
            self.url_path = options[EXCHANGE]["url_path"]
        

    def switch_exchange(self, EXCHANGE, options = options):
        
        self.BASE_URL = options[EXCHANGE]["BASE_URL"]
        self.url_path = options[EXCHANGE]["url_path"]
        
        print(f"Current exchange: {EXCHANGE}")

    
    def execute(commands):
        pass
        
    
    
    