import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler
from telegram import Bot

# إعدادات البوت
TELEGRAM_TOKEN = "PUT-YOUR-TELEGRAM-TOKEN-HERE"
CHAT_ID = "PUT-YOUR-CHAT-ID-HERE"

bot = Bot(token=TELEGRAM_TOKEN)

# قائمة الأسهم للمراقبة
STOCKS = ["AAPL", "TSLA", "MSFT"]

def check_stocks():
    message = "📊 Stock Updates:\n"
    for ticker in STOCKS:
        data = yf.Ticker(ticker).history(period="1d")
        price = round(data["Close"].iloc[-1], 2)
        message += f"{ticker}: ${price}\n"
    bot.send_message(chat_id=CHAT_ID, text=message)

# جدولة كل ساعة
scheduler = BlockingScheduler()
scheduler.add_job(check_stocks, "interval", minutes=60)

print("✅ Trading Bot is running...")
scheduler.start()
