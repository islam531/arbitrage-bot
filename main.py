from arbitrage import run_arbitrage_bot
import time

if __name__ == "__main__":
    print("🚀 بدء تشغيل بوت الأربيتراج...")
    while True:
        try:
            run_arbitrage_bot()
            time.sleep(60)  # انتظر دقيقة قبل المحاولة التالية
        except Exception as e:
            print(f"❌ حدث خطأ: {e}")
            time.sleep(30)
