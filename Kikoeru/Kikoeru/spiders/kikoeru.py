import json

import scrapy

from Kikoeru import settings
from Kikoeru.items import WorkInfoItem, ImagesItem, FileItem
from Kikoeru.util import util


class KikoeruSpider(scrapy.Spider):
    handle_httpstatus_list = [200,404]
    name = "kikoeru"
    allowed_domains = ["asmr-200.com"]
    start_urls = settings.INFO_START_URLS

    def parse(self, response):
        if response.status == 404:
            yield self.after_404(response)
        else:
            response_json = json.loads(response.text)
            language_editions = response_json["language_editions"]
            RJ = self.get_language_version(language_editions)

            if RJ and RJ != response.url.split("/")[-1] and response.meta.get("url", None) is None:
                work_info = settings.WORK_INFO_API + RJ
                yield scrapy.Request(url=work_info, callback=self.parse, meta={"url": response.url})
            else:
                reply = self.parse_info(response)
                yield reply["images_item"]
                yield reply["work_info_item"]
                yield scrapy.Request(url=reply["tracks_api"], callback=self.parse_track)



    #获取配置的语言版本
    def get_language_version(self,language_editions:list):
        if language_editions is not None and len(language_editions) > 0:
            for language_edition in language_editions:
                if language_edition["label"] == settings.LANGUAGES.get(settings.LANGUAGE):
                    return util.get_RJ(language_edition["workno"])

    def after_404(self, response):
        url = response.meta["url"]
        if url is not None:
            return scrapy.Request(url=url, callback=self.parse, meta={"url": response.url})

    def parse_info(self,response):
        response_json = json.loads(response.text)
        RJ = response.url.split("/")[-1]
        work_info_item = WorkInfoItem()
        work_info_item["language_editions"] = response_json["language_editions"]
        work_info_item["title"] = response_json["title"]
        work_info_item["age_category_string"] = response_json["age_category_string"]
        work_info_item["circle_name"] = response_json["circle"]["name"]
        work_info_item["create_date"] = response_json["create_date"]
        work_info_item["dl_count"] = response_json["dl_count"]
        work_info_item["duration"] = util.to_hour(response_json["duration"])
        work_info_item["has_subtitle"] = response_json["has_subtitle"]
        work_info_item["RJ"] = f"RJ{RJ}"
        work_info_item["nsfw"] = response_json["nsfw"]
        work_info_item["original_workno"] = response_json["original_workno"]
        work_info_item["price"] = response_json["price"]
        work_info_item["rate_average_2dp"] = response_json["rate_average_2dp"]
        work_info_item["rate_count"] = response_json["rate_count"]
        work_info_item["tags"] = response_json["tags"]
        work_info_item["vas"] = response_json["vas"]

        #构造下载封面图片
        images_item = ImagesItem()
        images_item["image_urls"] = [response_json["mainCoverUrl"]]
        images_path_name = {}
        images_path_name[response_json["mainCoverUrl"]] = "cover.jpg"
        images_item["images_path_name"] = images_path_name

        reply = {}

        reply["work_info_item"] = work_info_item

        #构造文件路径请求链接
        tracks_api = settings.TRACKS_API + RJ
        reply["tracks_api"] = tracks_api
        reply["images_item"] = images_item

        #构造项目根路径
        util.create_root_path(work_info_item)
        return reply

    def parse_track(self, response):
        response_jsons = json.loads(response.text)
        file_urls= []
        path_dict = {}
        response.meta["cache"] = []
        for response_json in response_jsons:
            dir_title = response_json["title"]
            self.get_children(dir_title,response_json,response_json.get("children",None),response)
        for i in response.meta.get("cache"):
            i = i.split("|")
            file_urls.append(i[1])
            path_dict[i[1]] = i[0]
        file_item = FileItem()
        file_item["file_urls"] = file_urls
        file_item["path"] = path_dict
        yield file_item
    def get_children(self,path,node,children,response):
        if children:
            for child in children:
                mediaDownloadUrl = child.get("mediaDownloadUrl",None)
                if mediaDownloadUrl:
                    temp = path
                    temp += "/"+child["title"]
                    temp += "|" + mediaDownloadUrl
                    response.meta.get("cache").append(temp)
                else:
                    path += "/"+child["title"]
                    self.get_children(path,child, child.get("children", None),response)
        else:
            path += "|" + node["mediaDownloadUrl"]
            response.meta.get("cache").append(path)



