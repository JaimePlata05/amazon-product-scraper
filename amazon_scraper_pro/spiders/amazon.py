import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]

    def __init__(self, search="mechanical keyboard", pages=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search = search
        self.pages = int(pages)

    custom_settings = {
        "FEEDS": {
            "amazon_products.csv": {
                "format": "csv",
                "encoding": "utf-8-sig",
                "fields": [
                    "title",
                    "price",
                    "original_price",
                    "rating",
                    "reviews",
                    "stock",
                    "asin",
                    "link",
                ],
                "delimiter": ";",
            },
            "amazon_products.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
            },
        }
    }

    def start_requests(self):

        for page in range(1, self.pages + 1):

            url = f"https://www.amazon.com/s?k={self.search.replace(' ','+')}&page={page}"

            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):

        if "captcha" in response.text.lower():
            self.logger.warning("CAPTCHA detectado en Amazon")
            return

        products = response.css("div[data-component-type='s-search-result']")

        for product in products:

            asin = product.attrib.get("data-asin")

            if not asin:
                continue

            title = product.css("h2 span::text").get()

            price = product.css(".a-price .a-offscreen::text").get()

            original_price = product.css(
                "span.a-text-price span.a-offscreen::text"
            ).get()

            rating = product.css(
                "span.a-icon-alt::text"
            ).re_first(r"[\d\.]+")

            reviews = product.css(
                "a[href*='customerReviews'] span::text"
            ).get()

            if reviews:
                reviews = reviews.replace(",", "").strip()
            else:
                reviews = "N/A"

            link = f"https://www.amazon.com/dp/{asin}"

            item = {
                "title": title,
                "price": price,
                "original_price": original_price or price,
                "rating": rating,
                "reviews": reviews,
                "stock": "N/A",
                "asin": asin,
                "link": link,
            }

            yield scrapy.Request(
                url=link,
                callback=self.parse_product_detail,
                meta={"item": item},
            )

    def parse_product_detail(self, response):

        item = response.meta["item"]

        stock = response.css("div#availability span::text").get()

        if stock:
            stock = stock.strip()
        else:
            stock = "N/A"

        item["stock"] = stock

        yield item