import scrapy
from scrapy import Selector


class VidGameBestSellersSpider(scrapy.Spider):
    name = "vid-game-best-sellers"
    allowed_domains = ["tinyurl.com", "amazon.co.za"]

    # The original start_url for this project points to the
    # Amazon.co.za Best Seller section for
    # video games.

    """
    Original URL:
    https://www.amazon.co.za/gp/bestsellers/videogames?
    ref_=Oct_d_obs_S&pd_rd_w=vgpmN&content-id=amzn1.sym.2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_p=
    2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_r=KFRAEDFEKSNVJ9S0P1WR&pd_rd_wg=TZhI0&pd_rd_r=
    d64b8cfe-9067-42e9-ba9d-4b1e800d8e20
    """
    
    # https://www.amazon.co.za/gp/bestsellers/videogames?ref_=Oct_d_obs_S&pd_rd_w=vgpmN&content-id=amzn1.sym.2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_p=2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_r=KFRAEDFEKSNVJ9S0P1WR&pd_rd_wg=TZhI0&pd_rd_r=d64b8cfe-9067-42e9-ba9d-4b1e800d8e20
    def start_requests(self):
        # `start_requests()` is a response method that retrieves raw contents 
        # from the target URL and then passes the response to the `parse()`
        # method.
        start_urls = ["https://tinyurl.com/4swm2a8b"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # The `parse()` method takes raw contents in the `response`
        # variable and yields/returns the parsed data after applying
        # the relevant parsing.
        divs = response.xpath("//div")

        for best_seller in response.xpath("//div").getall(): # This is the <div> class wrapping all best-sellers
            # We want to extract:
            # (1) product_name,
            # (2) price
            yield {
                "product_name": best_seller.css("._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y ::text").get(),
                "price": best_seller.css("//span[@class='_cDEzb_p13n-sc-price_3mJ9Z']/text()").get(),
            }
    
    # TO-DO: 
    # 14/06/2024
    # Debug script to get it to recognize `.get()`, `xpath()`, and `.css()`

    