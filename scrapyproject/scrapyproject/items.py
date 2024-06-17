# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join


# Define a function to filter nested CSS classes
value = "div._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"
def filter_nested_css_class(value):
    if ".a-size-small" in value:
        # Temporarily print value variable for debugging purposes
        print(value.replace(".a-size-small", ","))
    

class ScrapyprojectItem(scrapy.Item):
    # define the fields for item here:
    # This creates a template for our ScrapyprojectItem()
    product_name = scrapy.Field(
        input_processor=MapCompose(filter_nested_css_class),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(filter_nested_css_class),
        output_processor=Join(),
    )

# TO DO (17-06-2024):
# 1. Further work the `filter_nested_css_class()` function
# so that the `.a-size-small` CSS class is effectively
# removed from the scraped data. 
# 2. Fine-tune items and item loaders for cleaner data.