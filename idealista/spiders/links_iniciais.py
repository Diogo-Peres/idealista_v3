import scrapy
import io
from urllib.parse import urlparse


class SampleQuotesSpider(scrapy.Spider):
    name = "precos_idealista"

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
            "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
        },
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000
        },
        "REQUEST_FINGERPRINTER_CLASS": "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter",
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "ZYTE_API_KEY": "9d29172683b843caa81c9fa7504e1894", # Enter Your API Key kere
        "ZYTE_API_TRANSPARENT_MODE": True
    }

    def start_requests(self):
        yield scrapy.Request(
            url= "https://www.idealista.pt/imovel/32733847/",
            meta={
                "zyte_api": {
                    "httpResponseBody": True,
                    #"requestHeaders": {"referer": "https://www.google.com/"}
                }
            }    
        )

    def parse(self, response):
        print(response.status)
        data = response.body
        with io.open("page.html", "w", encoding="utf-8") as f:
            f.write(str(data))
       
