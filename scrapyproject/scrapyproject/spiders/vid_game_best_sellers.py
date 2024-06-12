import scrapy


class VidGameBestSellersSpider(scrapy.Spider):
    name = "vid-game-best-sellers"
    allowed_domains = ["tinyurl.com"]

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
    start_urls = ["https://tinyurl.com/4swm2a8b"]

    def parse(self, response):
        pass
    
    # TO-DO: 
    # 13/06/2024
    # Modify Spider to suit project's craping needs. 

    