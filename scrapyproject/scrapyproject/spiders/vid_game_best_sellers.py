import scrapy
from scrapyproject.items import ScrapyprojectItem


class VidGameBestSellersSpider(scrapy.Spider):
    name = "vid-game-best-sellers"
    allowed_domains = ["amazon.co.za"]

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
        start_urls = ["https://www.amazon.co.za/gp/bestsellers/videogames?ref_=Oct_d_obs_S"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_list = []
        price_list = []

        for best_seller in response.css("div.a-row.a-size-small"):
            # Extract product_name
            product_name = best_seller.css('div._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text').get()
            test_product = best_seller.xpath('//*[contains(@id,"")]/div/div/a/span/div/text()').getall()
            
            
            # Extract price (assuming you have the correct selector for price)
            price = best_seller.css('span.p13n-sc-price::text').getall()
            test_price = best_seller.xpath('//span[@class="p13n-sc-price"]/text()').getall()
            for i in test_price:
                price_list.append(i)
            
            # Remove '.a-size-small' CSS class
            if best_seller.css('.a-size-small'):
                if best_seller.css('span.a-color-secondary'):
                    return None
                best_seller = best_seller.get().replace('a-size-small', '')

            
            for i in test_product:
                product_list.append(i)

            print(f'Product: {product_list}')
            print(f'Price: {price_list}')
            # print(f"Product: {test_product}, Price: {price}")

            for product, price in zip(product_list, price_list):
                yield {
                    'product_name': product,
                    'price': price
                }


    # def parse(self, response):
    #     # The `parse()` method takes raw contents in the `response`
    #     # variable and yields/returns the parsed data after applying
    #     # the relevant parsing.
        
    #     # response.xpath("//div/span[contains(@class, 'p13n-sc-price')]").getall()
    #     # ☝🏾 The query above returns all the product prices for
    #     # best sellers in the video games category.

    #     # Create instance of an item as test, initially
    #     item = ScrapyprojectItem()

    #     # manufacturer = []
    #     for best_seller in response.css("div.a-row"): # This is the <div> class wrapping all best-sellers
    #         # We want to extract:
    #         # (1) product_name,
    #         # (2) price

    #         # Extract product_name
            
    #         product_name = best_seller.css('div._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text').get()
            
    #         # print(f"Product name: {product_name}")
    #         # Extract price
    #         price = best_seller.css("span.p13n-sc-price::text").get()
        
    #         # Store in item dictionary
    #         item['product_name'] = product_name
    #         # item['price'] = price
        
    #         # print(f"Manufacturer: {manufacturer}")

    #         # misc = response.css('.a-size-small::text').get()
    #         # for i in response.css('.a-size-small::text').getall():
    #         #     print(f"Misc: {i.replace(i, "")}")
    #         yield item

    # TO-DO: 
    # 19/06/2024
    # - Got the data to be cleaner and precise with product name
    # selection.
    # - Use Item Loaders to process the data yielded by the Spider.
    # - Must still clean up script so that it makes use of items
    # and item loaders.
    # - Lastly, look into the strange behavior of the output in 
    # Test.csv. Currently, the product names don't always match 
    # the prices.