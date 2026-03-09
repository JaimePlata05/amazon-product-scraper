import pandas as pd


class ExcelExportPipeline:

    def open_spider(self, spider):

        self.items = []

    def process_item(self, item, spider):

        self.items.append(dict(item))

        return item

    def close_spider(self, spider):

        if not self.items:
            spider.logger.warning("No se recolectaron datos")
            return

        df = pd.DataFrame(self.items)

        df.to_excel("amazon_products.xlsx", index=False)

        spider.logger.info("Archivo Excel exportado correctamente")