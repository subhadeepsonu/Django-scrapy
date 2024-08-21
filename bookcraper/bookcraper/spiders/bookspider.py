import scrapy
class NoberospiderSpider(scrapy.Spider):
    name = "Noberospider"
    allowed_domains = ["nobero.com"]
    start_urls = ["https://nobero.com/pages/men"]
    def parse(self, response):
        categories = response.css("div.custom-page-season-grid div.custom-page-season-grid-item")
        for category in categories:
            href = category.css("a::attr(href)").get()
            yield response.follow(href, self.parse_category)
    def parse_category(self, response):
        products = response.css("article.product-on-page section.product-card-container")
        category =  response.css("h1.list-title::text").get()
        for product in products:
            relativeurl = product.css("a::attr(href)").get()
            absoluteurl = "https://nobero.com" + relativeurl
            yield response.follow(absoluteurl, self.parse_product, meta={"category": category})
    def parse_product(self, response, **kwargs):
        category = response.meta["category"]
        title = response.css("h1::text").get()
        url = response.url
        price = response.css("#variant-price spanclass::text").get()
        mrp = response.css("#variant-compare-at-price spanclass::text").get()
        description = response.css("div.product-description *::text").getall()
        feilds = response.css("div.product-metafields div.product-metafields-values p::text ").getall()
        name = title
        yield {
            "category": category,
            "name": name.strip(),
            "url": url,
            "price": price,
            "mrp": mrp,
            "description": description,
            "Fit": feilds[0],
            "Fabric": feilds[1],
            "Neck": feilds[2],
            "Sleeve": feilds[3],
            "Pattern": feilds[4],
            "Length": feilds[5]
        }
        
