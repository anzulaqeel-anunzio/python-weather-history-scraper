# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import pandas as pd
from datetime import datetime, timedelta
from weather_scraper.scraper import scrape_weather_history
from weather_scraper.config import START_DATE, END_DATE
import time

def main():
    print("Starting Weather History Scraper...")

    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    end = datetime.strptime(END_DATE, "%Y-%m-%d")
    
    current = start
    weather_data = []

    while current <= end:
        date_str = current.strftime("%Y-%m-%d")
        data = scrape_weather_history(date_str)
        
        if data:
            weather_data.append(data)
        
        current += timedelta(days=1)
        time.sleep(0.5) # Nice delay

    if weather_data:
        df = pd.DataFrame(weather_data)
        filename = "weather_history.csv"
        df.to_csv(filename, index=False)
        print(f"\nSaved {len(weather_data)} daily records to {filename}")
    else:
        print("No data collected.")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
