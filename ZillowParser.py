import json
import pandas as pds
from bs4 import BeautifulSoup as soup
from Scraper import scrape_zillow
from EstateFactory import House, Lot, Location, Geo

class ZillowListParser():
    def __init__(self, ScrapedData:list):
        self.scrapedData = ScrapedData
        self.res = self.parseData()

    def __repr__(self):
        return f'ZillowListParser: \nObjects Stored: {len(self.res)}'

    def parseData(self):
        '''Iterates through rows in the raw scraped data and parses "Estate" types
            removes the 'loading' value'''
        res = [None] * len(self.scrapedData)
        for index, dct in enumerate(self.scrapedData):
            if dct['text'] == 'Loading':
                continue
            floorSize, loc = self.metaToObj(dct['data'])
            res[index] = self.textToObj(dct['text'], floorSize, loc)
        if res[2] is not None:
            raise ValueError(f'Expected a None value, got: \n{res[2]}')
        del res[2]
        return res

    def textToObj(self, data, floorSize, loc):
        '''Parses the text part between types, returns "Estate" Object'''

        data = [line for line in data.split('\n')]
        estateType = data[1]
        if estateType in ('House for sale','New construction','Coming soon'):
            return House(_type = estateType,
                        price = data[2],
                        rooms = data[3],
                        availability = data[4],
                        agency = data[5],
                        location= loc,
                        size= floorSize)
        if estateType == 'Lot / Land for sale':
            return Lot(_type = estateType,
                        price = data[2],
                        size= data[3].split(' ')[0],
                        availability = data[4],
                        agency = data[5],
                        location= loc)
        if estateType == 'For sale by owner':
            return House(_type = estateType,
                        price = data[2],
                        rooms = data[3],
                        availability = data[4],
                        agency = 'owner',
                        location= loc,
                        size= floorSize)
        if estateType == 'Auction':
            return House(_type = estateType,
                        price = None,
                        rooms = data[3],
                        availability = data[4],
                        agency = data[5],
                        location= loc,
                        size= floorSize)
        raise ValueError(f'Unknown Sale Type: {estateType}')
        
    def metaToObj(self, metadata):
        '''From the metaData it returns the floorSize:int and the Location:Object '''
        try: jsonContents = self.scrapedData.find(type="application/ld+json").text
        except: 
            ScrapedSoup = soup(metadata, 'html.parser')
            jsonContents = ScrapedSoup.find(type="application/ld+json").text

        Metadicts = json.loads(jsonContents)
        Geoloc = Geo(latitude=Metadicts['geo']['latitude'],
                    longitude=Metadicts['geo']['longitude'])

        loc = Location(streetAddress=Metadicts['address']['streetAddress'],
                    city=Metadicts['address']['addressLocality'],
                    state=Metadicts['address']['addressRegion'],
                    postalCode=Metadicts['address']['postalCode'],
                    geo=Geoloc)

        try: floorSize = Metadicts['floorSize']['value']
        except: floorSize = None
        return floorSize, loc

    def getParsed(self):
        return self.res

def dfToList(data):
    '''Temporary function to convert the Cached DF to a List the ZillowParser Interprets'''
    lst = [None] * len(data)
    for index, row in data.iterrows():
        lst[index] = row
    return lst

# try: ScrapedData = pds.read_csv('RealEstate/ZillowData23.csv')
# except: ScrapedData = pds.read_csv('ZillowData23.csv')  
# ScrapedData = dfToList(ScrapedData)
# ZData = ZillowListParser(ScrapedData)
# print(ZData)

if __name__ == "__main__":
    ZData = scrape_zillow('//*[@id="grid-search-results"]/ul/li')
    ZParser = ZillowListParser(ZData)
    data = ZParser.getParsed()
    ZDF = pds.DataFrame(data)
    ZDF.to_csv('ZillowParsed.csv')