
from scrapy.item import Item, Field

class DeSpiderItem(Item):
    # define the fields for your item here like:
    price = Field()
    location = Field()
    num_bed_rooms = Field()
    num_bath_rooms = Field()
    area = Field()
    building_type = Field()
