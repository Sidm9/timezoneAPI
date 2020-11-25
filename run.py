from flask import Flask
import urllib.request as scraper
from getDate import scrapeDate
app = Flask(__name__)

@app.route('/<country>/<city>')
def getTime(country , city):
    url = F'https://www.timeanddate.com/time/zone/{country}/{city}'
    
    try:

        with scraper.urlopen(url) as res:
            format = res.read()

        scraped_data = str(format)
        
        before_time = scraped_data.find("<span id=ct class=h1>")
        after_time = scraped_data.find("</span> <span i")

        time_zone_before = scraped_data.find("Offset: </th>")
        time_zone_after = scraped_data.find("hours</")
        
        actual_time = scraped_data[before_time+21:after_time]

        actual_time_zone = scraped_data[time_zone_before+25:time_zone_after]

        getDate = scrapeDate(country=country,city=city)

    except Exception as e:
        print(e)

    final_data = {}
    final_data["country"] = country
    final_data["cuty"] = city
    final_data["offset"] = actual_time_zone.strip()
    final_data["time"] = actual_time
    final_data["date"] = getDate

    return (final_data)
    