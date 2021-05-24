import scrapy


# spider for dealer.com templated websites
class FordDealeronSpider(scrapy.Spider):
    name = 'ford_dealeron'

    dealers = [
        {
            "name": 'North Bay Ford',
            "url": 'https://www.northbayford.com/searchnew.aspx?Type=N&Year=2021&Make=Ford&Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'Watsonville Ford',
            "url": 'https://www.watsonvilleford.com/searchnew.aspx?Type=N&Year=2021&Make=Ford&Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'Ford Store Morgan Hill',
            "url": 'https://www.fordstoremorganhill.com/car-dealer-san-jose-ca.html?Bodystyle=Premium&Model=Mustang+Mach-E&Year=2021',
            "settings": {}
        },
        {
            "name": 'Mission Valley Ford',
            "url": 'https://www.missionvalleyford.com/searchnew.aspx?Type=N&Make=Ford&Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'James Ford (Half Moon Bay)',
            "url": 'https://www.jamesford.com/searchnew.aspx?Type=N&Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'Future Ford (Concord)',
            "url": 'https://www.futurefordofconcord.com/searchnew.aspx?Make=Ford&Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'Napa Ford',
            "url": 'https://www.napaford.com/cars-for-sale-napa-ca.html?Model=Mustang+Mach-E',
            "settings": {}
        },
        {
            "name": 'Santos Ford',
            "url": 'https://www.santosford.net/searchnew.aspx?Model=Mustang%20Mach-E',
            "settings": {}
        },
        {
            "name": 'Greenwood Ford (Hollister)',
            "url": 'https://www.teamgreenwoodford.com/searchnew.aspx?Model=Mustang+Mach-E',
            "settings": {}
        },
        {
            "name": 'Woodland Ford',
            "url": 'https://www.woodlandford.com/searchnew.aspx?Model=Mustang%20Mach-E',
            "settings": {}
        },
    ]

    def start_requests(self):
        for dealer in self.dealers:
            name, url, settings = dealer['name'], dealer['url'], dealer['settings']
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(dealer_name=name, settings=settings))

    def parse(self, response, dealer_name, settings):
        UL_XPATH = '//*[@class="row srpVehicle hasVehicleInfo"]'

        for ul in response.xpath(UL_XPATH):
                yield {
                    'dealer': dealer_name,
                    'url': response.url,
                    'title': "%s %s %s %s" % (ul.xpath('@data-year').get(), ul.xpath('@data-make').get(),ul.xpath('@data-model').get(),ul.xpath('@data-trim').get()),
                    'msrp': ul.xpath('@data-msrp').get(),
                    'price': ul.xpath('@data-price').get(),
                    'vin': ul.xpath('@data-vin').get(),
                    'exteriorColor': ul.xpath('@data-extcolor').get(),
                    'interiorColor': ul.xpath('@data-intcolor').get(),
                    'engine': ul.xpath('@data-engine').get(),
                    'trim': ul.xpath('@data-trim').get(),
                    'options': []
                }

        #NEXT_PAGE = '/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/form/div/div[3]/div/div/div[2]/ul/li[3]/a/@href'
        #next_page = response.xpath(NEXT_PAGE).get()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)



# StratosDealerEngine
#   scraping logic
# curl -XGET -H 'Content-Type: application/json' https://www.flemingtonbmw.com/api/InventoryWidget/Galleria/?vin=5UXTY9C03L9C80441

#  get options:  'https://www.flemingtonbmw.com/vehicleoptionscomments.aspx?id=5214&vin=5UXTY9C03L9C80441'
