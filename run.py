from flask import Flask
import urllib.request as scraper
app = Flask(__name__)

@app.route('/<country>/<city>')
def getTime(country , city):

    url = F'https://www.timeanddate.com/time/zone/{country}/{city}'

    try:
        with scraper.urlopen(url) as res:
            format = res.read()

        scraped_data = str(format)
        
        # finding time from data  before and after
        sanitized_before_time = scraped_data.find("<span id=ct class=h1>")
        sanitized_after_time = scraped_data.find("</span> <span i")

        sanitized_time_zone_before = scraped_data.find("Offset: </th>")
        sanitized_time_zone_after = scraped_data.find("hours</")

        #sanitized_date_before = scraped_data.find("<p><span id=ctdat>")
        #sanitized_date_after = scraped_data.find("2020</span>")
        
        # sanitized_date = scraped_data.find("")
        actual_time = scraped_data[sanitized_before_time+21:sanitized_after_time]
        actual_time_zone = scraped_data[sanitized_time_zone_before+25:sanitized_time_zone_after]
        #actual_date = scraped_data[sanitized_date_before+18:sanitized_date_after]

        # print(F"LALALALA {actual_date.encode('utf-8')}")

    except Exception as e:
        print(e)

    final_data = {}
    final_data["country"] = country
    final_data["cuty"] = city
    final_data["offset"] = actual_time_zone.strip()
    final_data["time"] = actual_time

    return (final_data)
    