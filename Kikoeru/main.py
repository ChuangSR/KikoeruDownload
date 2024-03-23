from scrapy import cmdline
import argparse

from Kikoeru import settings
from Kikoeru.util import util


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

    util.insert_info_start_url(url)
    cmdline.execute("scrapy crawl kikoeru".split())

def main():
    parser = argparse.ArgumentParser(description="www.asmr.one网站的下载器")
    parser.add_argument("-u", "--url", required=True ,help="指定下载的url 也可以是一个RJ号")
    parser.add_argument("-p", "--path", help="指定下载文件的保存路径 如果没有指定那么使用settings.py文件中配置")
    parser.add_argument("-l", "--language", help="指定下载的语言类型 参数为:JZ简中 FZ繁中 JP日语 EG英语 你可以在settings.py中配置默认偏好"
                                                 "如果未配置，那么根据链接直接下载")

    args = parser.parse_args()
    url = args.url
    # 需要爬取的url
    path = args.path
    language = args.language
    run(url, path, language)

main()






