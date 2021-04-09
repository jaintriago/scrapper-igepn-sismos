from scrapperIgen import scrapperIgen
from twitterscrapper import twitterscrapper
startDate = "01/01/2013"
endDate = "30/05/2019"
scrapper = scrapperIgen(startDate, endDate)
scrapperTwitter = twitterscrapper()
dftwiter = scrapperTwitter.scrape()

results = scrapper.scrape();
scrapper.procesarDataFrame()
scrapper.joinFile(dftwiter)
scrapper.writeFile()