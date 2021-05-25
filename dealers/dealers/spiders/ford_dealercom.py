import scrapy
import js2py
import json
import logging
from urllib.parse import urlparse

from . import util

INVENTORY_PATH = '/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_NEW:inventory-data-bus1/getInventory'


# spider for dealer.com templated websites
class FordDealercomSpider(scrapy.Spider):
    name = 'ford_dealercom'

    dealers = [
        {
            "name": 'Frontier Ford',
            "url": 'https://www.frontierford.com/new-inventory/index.htm?model=Mustang%20Mach-E&sortBy=internetPrice+desc&',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Sunnyvale Ford',
            "url": 'https://www.sunnyvaleford.com/new-inventory/index.htm?model=Mustang%20Mach-E&sortBy=internetPrice+desc&',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Putnam Ford of San Mateo',
            "url": 'https://www.putnamfordsanmateo.com/all-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Serramonte Ford (SF)',
            "url": 'https://www.serramonteford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Fremont Ford',
            "url": 'https://www.fremontford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'The Ford Store of San Leandro',
            "url": 'https://www.fordsanleandro.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Livermore Ford',
            "url": 'https://www.livermoreford.net/new-inventory/ford-sale-livermore-ca.htm?make=Ford&model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Tracy Ford',
            "url": 'https://www.tracyford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Walnut Creek Ford',
            "url": 'https://www.walnutcreekford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Hilltop Ford (Richmond)',
            "url": 'https://www.hilltopford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Allstar Ford (Pittsburg)',
            "url": 'https://allstarford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Bill Brandt Ford (Brentwood)',
            "url": 'https://www.billbrandtford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Manteca Ford',
            "url": 'https://www.mantecafm.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Big Valley Ford (Stockton)',
            "url": 'https://www.bigvalleyford.biz/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Rio Vista Ford',
            "url": 'https://www.riovistaford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Henry Curtis Ford (Petaluma)',
            "url": 'https://www.henrycurtisford.com/new-inventory/index.htm?reset=InventoryListing&make=Ford&model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Marin County Ford (Novato)',
            "url": 'https://www.marincountyford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Cypress Coast Ford (Seaside)',
            "url": 'https://www.cypresscoastford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Razzari Ford (Merced)',
            "url": 'https://www.fordrazzari.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'McAuley Ford (Patterson)',
            "url": 'https://www.mcauleyford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Hansel Ford (Santa Rosa)',
            "url": 'https://www.hanselford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Zumwalt Ford (Saint Helena)',
            "url": 'https://www.zumwaltford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Santa Maria Ford',
            "url": 'https://www.santamariaford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Mullahey Ford (Arroyo Grande)',
            "url": 'https://www.mullaheyford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Perry Ford (San Luis Obispo)',
            "url": 'https://www.perryfordofsanluis.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Paso Robles Ford',
            "url": 'https://www.pasoford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Ken Garff Ford (American Fork)',
            "url": 'https://www.kengarfffordaf.com/new-inventory/index.htm?year=2021&make=Ford&model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Wilson Motor Ford (Logan)',
            "url": 'https://www.wilsonmotorford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Tim Dahle Ford (Spanish Fork)',
            "url": 'https://www.timdahleford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Young Automotive Group (Brigham City)',
            "url": 'https://www.youngfordbrigham.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Crandall Ford (Park City)',
            "url": 'https://www.crandallford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Young Automotive Group (Morgan)',
            "url": 'https://www.youngfordmorgan.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Larry H Miller Ford (Provo)',
            "url": 'https://www.larryhmillerfordprovo.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Labrum Ford (Heber City)',
            "url": 'https://www.labrumford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Larry H Miller Ford (Salt Lake City)',
            "url": 'https://www.lhmford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Tooele Ford',
            "url": 'https://www.tooeleford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Ken Garff Ford (American Fork)',
            "url": 'https://www.kengarfffordaf.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Larry H Miller Ford (Draper)',
            "url": 'https://www.lhmforddraper.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Ed Kenley Ford (Layton)',
            "url": 'https://www.edkenleyford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Young Automotive Group (Ogden)',
            "url": 'https://www.youngfordogden.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Ken Garff Ford (West Valley)',
            "url": 'https://www.kengarffwestvalleyford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'St George Ford',
            "url": 'https://www.stgeorgeford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Auburn Ford',
            "url": 'https://www.auburnford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Harrold Ford (Sacramento)',
            "url": 'https://www.harroldford.net/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Folsom Lake Ford',
            "url": 'https://www.folsomlakeford.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
        {
            "name": 'Downtown Ford (Sacramento)',
            "url": 'https://www.dtfords.com/new-inventory/index.htm?model=Mustang%20Mach-E',
            "settings": {
                "inventory_query": True,
            }
        },
    ]

    def start_requests(self):
        for dealer in self.dealers:
            name, url, settings = dealer['name'], dealer['url'], dealer['settings']
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(dealer_name=name, settings=settings))

    def __parse_ddc(self, response, settings):
        logging.info("DDC parsing.")

        # this one is default because it's more reliable
        DL_XPATH = '//div[@class=" ddc-content tracking-ddc-data-layer"]/script/text()'
        javascript = response.xpath(DL_XPATH)[0].get()
        prep = "window={DDC: {siteSettings:{proximityAccount:\'\'}}};\n"

        context = js2py.EvalJs()
        context.execute(prep+javascript)

        for vehicle in context.window.DDC.dataLayer.vehicles:
            options = (vehicle['optionCodes'] or []) + (vehicle['optionCodesOther'] or [])
            title = "%s %s %s %s" % (vehicle['modelYear'], vehicle['make'], vehicle['model'], vehicle['trim'])

            yield {
                'dealer': vehicle['accountName'],
                'title': title,
                'msrp': vehicle['msrp'],
                'odometer': vehicle['odometer'],
                'vin': vehicle['vin'],
                'options': options
            }

    def __parse_inventory_query(self, response, dealer_name, settings):
        jsonResponse = json.loads(response.text)

        if 'inventory' not in jsonResponse:
            logging.warn(f"Warning: no 'inventory' field found for dealer {dealer_name}")

        dealer_parsed_url = urlparse(response.url)

        for vehicle in jsonResponse['pageInfo']['trackingData']:
            # logging.info(f"Inventory response (from cb): {json.dumps(vehicle, indent=3)}")
            pricingBlock = vehicle.get('pricing', {})
            msrp = pricingBlock.get('finalPrice', pricingBlock.get('msrp', ''))
            yield {
                'dealer': dealer_name,
                'title': f"{vehicle['make']} {vehicle['model']} {vehicle['trim']}",
                'driveLine': vehicle.get('driveLine', ''),
                'engine': vehicle.get('engine', ''),
                'trim': vehicle.get('trim', ''),
                'msrp': msrp,
                'vin': vehicle['vin'],
                'exteriorColor': vehicle.get('exteriorColor', ''),
                'interiorColor': vehicle.get('interiorColor', ''),
                'link': f"{dealer_parsed_url.scheme}://{dealer_parsed_url.netloc}{vehicle['link']}"
            }

    def __parse_no_ddc(self, response, dealer_name, settings):
        logging.info("No DDC parsing.")

        # this one is less preferable as it uses the dom elements and not the DDC json
        LI_XPATH = "//ul[contains(@class, 'gv-inventory-list')]/li"

        for li in response.xpath(LI_XPATH):
            MSRP_XPATH = '*//li[contains(@class, "finalPrice")]//span[@class="value"]//text()'

            yield {
                'dealer': dealer_name,
                'title': "%s %s %s %s" % (li.xpath('@data-year').get(), li.xpath('@data-make').get(), li.xpath('@data-model').get(), li.xpath('@data-trim').get()),  # noqa
                'msrp': util.parse_msrp(li.xpath(MSRP_XPATH).get()),
                'vin': li.xpath('@data-vin').get(),
                'ext_color': li.xpath('@data-exteriorcolor').get(),
                'int_color': li.xpath('@data-interiorcolor').get(),
                'odometer': li.xpath('@data-odometer').get(),
                'options': []
            }

    def parse(self, response, dealer_name, settings):
        if ('inventory_query' in settings) and settings['inventory_query']:
            parsed_url = urlparse(response.url)
            inventory_url = parsed_url._replace(path=INVENTORY_PATH)
            yield scrapy.Request(url=inventory_url.geturl(), callback=self.__parse_inventory_query,
                                 cb_kwargs=dict(dealer_name=dealer_name, settings=settings))
        elif ('no_ddc' in settings) and settings['no_ddc']:
            for vehicle in self.__parse_no_ddc(response, dealer_name, settings):
                yield vehicle
        else:
            for vehicle in self.__parse_ddc(response, settings):
                yield vehicle

        next_page = response.xpath('(//a[@rel="next" and not(contains(@class, "disabled"))])[1]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, cb_kwargs=dict(dealer_name=dealer_name, settings=settings))


'''
UL_XPATH = "//ul[contains(@class, 'gv-inventory-list')]"
li[data-year]

'''
