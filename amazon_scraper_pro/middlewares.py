import random


class RandomProxyMiddleware:

    def __init__(self, proxies):
        self.proxies = proxies or []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("PROXY_LIST"))

    def process_request(self, request, spider):

        if self.proxies:
            proxy = random.choice(self.proxies)
            request.meta["proxy"] = proxy


class RandomUserAgentMiddleware:

    def __init__(self, user_agents):
        self.user_agents = user_agents or []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("USER_AGENT_LIST"))

    def process_request(self, request, spider):

        if self.user_agents:

            ua = random.choice(self.user_agents)

            request.headers["User-Agent"] = ua

            request.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            })

            referers = [
                "https://www.google.com/",
                "https://www.bing.com/",
                "https://duckduckgo.com/",
            ]

            request.headers["Referer"] = random.choice(referers)