from scrapy import cmdline

from Kikoeru.util import util


if "__main__" == __name__:
    #需要爬取的url
    url = "";
    util.insert_info_start_url(url)
    cmdline.execute("scrapy crawl kikoeru".split())
    # code = os.system("scrapy crawl kikoeru_info")
    # print(code)



