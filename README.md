# Weather Data Local History Scraper (Python)

A Python script to scrape historical weather data (temperature, precipitation) for a given location.

> [!NOTE]
> This tool scrapes public weather data sites (mock implementation targets `wunderground.com` structure). For reliable historical data, consider using the Visual Crossing Weather API or OpenWeatherMap.

## Features

-   **Historical Data**: Fetches data for past dates.
-   **CSV Export**: Saves daily summaries to a CSV file.
-   **Configurable Location**: Set the specific station ID.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python run_scraper.py
```

## Configuration

Edit `weather_scraper/config.py` to change the `STATION_ID` or date range.

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
