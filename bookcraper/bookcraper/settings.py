

BOT_NAME = "bookcraper"

SPIDER_MODULES = ["bookcraper.spiders"]
NEWSPIDER_MODULE = "bookcraper.spiders"

FEEDS ={ 
    "products.json": {
        "format": "json",
    }
}
ITEM_PIPELINES = {
    "bookcraper.pipelines.BookcraperPipeline": 300,
    "bookcraper.pipelines.SaveToMySqlPipeline": 400
}

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
