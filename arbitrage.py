import os
import requests
import ccxt
from dotenv import load_dotenv

load_dotenv()

def run_arbitrage_bot():
    print("🔁 فحص فرصة أربيتراج بين MEXC و Uniswap...")

    # الإعدادات
    symbol = "ETH/USDT"
    amount = 0.01

    mexc = ccxt.mexc({
        'apiKey': os.getenv("MEXC_API_KEY"),
        'secret': os.getenv("MEXC_API_SECRET"),
    })

    # قراءة السعر من MEXC
    ticker_mexc = mexc.fetch_ticker(symbol)
    mexc_price = ticker_mexc['bid']

    # قراءة السعر من Uniswap باستخدام The Graph
    uniswap_url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    query = """
    {
      pair(id: "0x06da0fd433C1A5d7a4faa01111c044910A184553") {
        token0Price
      }
    }
    """
    response = requests.post(uniswap_url, json={'query': query})
    data = response.json()
    uniswap_price = float(data["data"]["pair"]["token0Price"])

    print(f"MEXC: {mexc_price} | Uniswap: {uniswap_price}")

    # حساب الفارق
    spread = uniswap_price - mexc_price
    if spread > 5:  # فارق 5 دولار كمثال
        print("✅ فرصة أربيتراج مؤكدة!")
        # تنفيذ الشراء من MEXC (افتراضي)
        order = mexc.create_market_buy_order(symbol, amount)
        print("✅ تم الشراء من MEXC!")

        # نفترض التحويل اليدوي إلى Uniswap + البيع لاحقًا
    else:
        print("❌ لا توجد فرصة مناسبة حالياً.")
