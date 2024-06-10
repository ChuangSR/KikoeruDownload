import argparse

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from Kikoeru import settings
from Kikoeru.util import util
from configparser import ConfigParser

def init():
    conf = ConfigParser()
    conf.read('config.ini',encoding="utf-8")
    api = conf['api']
    settings.WORK_INFO_API = api["WORK_INFO_API"]
    settings.TRACKS_API = api["TRACKS_API"]
    ip = conf["proxy"]["IP"]

    settings.LANGUAGE = conf["language"]["LANGUAGE"]
    settings.SAVE_PATH = conf["path"]["SAVE_PATH"]
    settings.USER_AGENT = conf["user_agent"]["USER_AGENT"]
    settings.URL = conf["url"]["URL"]
    settings.DOMAIN = list(conf["domain"].values())
    if ip is not None and len(ip) > 0:
        settings.PROXYS = []
        settings.PROXYS.append(ip)



def run(url, path, language: str):
    if url is None or util.get_RJ(url) == None:
        print("url值为空，或者无法解析！")
        return
    if path is not None:
        settings.SAVE_PATH = path

    if language is not None:
        if language.upper() not in settings.LANGUAGES.keys():
            print("输入语言类型异常，使用settings文件默认配置")
        else:
            settings.LANGUAGE = language.upper()
    if "http" not in url:
        url = settings.URL+url
    util.insert_info_start_url(url)
    process = CrawlerProcess(get_project_settings())
    process.crawl("kikoeru")
    process.start()

def main():
    parser = argparse.ArgumentParser(description="www.asmr.one网站的下载器")
    parser.add_argument("-u", "--url",help="指定下载的url 也可以是一个RJ号")
    parser.add_argument("-p", "--path", help="指定下载文件的保存路径 如果没有指定那么使用config.ini文件中配置")
    parser.add_argument("-l", "--language", help="指定下载的语言类型 参数为:JZ简中 FZ繁中 JP日语 EG英语 你可以在config.ini中配置默认偏好"
                                                 "如果未配置，那么根据链接直接下载")

    args = parser.parse_args()
    url = args.url
    # 需要爬取的url
    path = args.path
    language = args.language
    run(url, path, language)
init()
# main()