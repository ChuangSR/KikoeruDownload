# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Item
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline

from Kikoeru import settings
from Kikoeru.items import WorkInfoItem


class WorkInfoPipeline:
    def process_item(self, item, spider):
        if spider.name == 'kikoeru_info' and type(item) == WorkInfoItem:
            dict_item = dict(item)
            with open(f"{settings.IMAGES_STORE}/info.json",mode="w",encoding="utf-8") as info:
                info.write(json.dumps(dict_item,ensure_ascii=False))
        return item


class KikoeruImagesPipeline(ImagesPipeline):

    def get_images(self, response, request, info, *, item=None):
        return super().get_images(response, request, info, item=item)
    # #构建文件的路径
    def file_path(self, request, response=None, info=None, *, item=None):
        self.store = self._get_store(settings.IMAGES_STORE)
        images_path_name:dict = dict(item).get("images_path_name")
        return images_path_name.get(request.url)

class SaveFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        self.store = self._get_store(settings.IMAGES_STORE)
        path = item.get("path")
        return path.get(request.url)
