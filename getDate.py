import urllib.request as scraper
import datetime
def scrapeDate(country , city) -> str:
    global ss
    url2 =F'https://www.timeanddate.com/worldclock/{country}/{city}'
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    try:
        req = scraper.Request(url2, headers=headers)
        response = scraper.urlopen(req)
        data = response.read()

        scraped_data2 = str(data)
        date_before = scraped_data2.find("<span id=ctdat>")
        date_after = scraped_data2.find("</span></p><a hre")

        actual_date = scraped_data2[date_before+15:date_after]
        actual_date = actual_date.replace(',','')
        final_date = datetime.datetime.strptime(actual_date, "%A %d %B %Y")

        ss = str(final_date.date())
        
        return(ss)


        
    except Exception as e:
        return(e)


    