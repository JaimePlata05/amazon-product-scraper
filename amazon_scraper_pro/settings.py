BOT_NAME = "amazon_scraper_pro"

SPIDER_MODULES = ["amazon_scraper_pro.spiders"]
NEWSPIDER_MODULE = "amazon_scraper_pro.spiders"


# USER AGENTS
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120",
]

# proxies opcionales
PROXY_LIST = []


DOWNLOADER_MIDDLEWARES = {
    "amazon_scraper_pro.middlewares.RandomProxyMiddleware": 100,
    "amazon_scraper_pro.middlewares.RandomUserAgentMiddleware": 200,
}


ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 4

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0

COOKIES_ENABLED = True

RETRY_ENABLED = True
RETRY_TIMES = 5

DOWNLOAD_TIMEOUT = 60


ITEM_PIPELINES = {
    "amazon_scraper_pro.pipelines.ExcelExportPipeline": 300,
}


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"