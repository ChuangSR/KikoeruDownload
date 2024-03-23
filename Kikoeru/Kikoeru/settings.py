# Scrapy settings for Kikoeru project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Kikoeru"

SPIDER_MODULES = ["Kikoeru.spiders"]
NEWSPIDER_MODULE = "Kikoeru.spiders"

#页面详细信息的api接口
WORK_INFO_API = "https://api.asmr-200.com/api/workInfo/"
#页面数据下载的api接口
TRACKS_API = "https://api.asmr-200.com/api/tracks/"
#下载的文件被保存的路径
SAVE_PATH = ""
#默认下载的语言
LANGUAGE = "JZ"

PROXYS = [
    # {"ip_port":"xxx.xxx.xxx:xxx","user":"xxx","password":"xxx"}
]

"""
    此属性对应WORK_INFO_API中的language_editions
    数组中的对象的label属性，在其api属性未修改的情况下
    请不要修改此字段的数据
"""
LANGUAGES = {
    "EG":"英語",
    "JP":"日本語",
    "JZ":"簡体中文",
    "FJ":"繁体中文"
}

#仅仅会存储WORK_INFO的URL作为起始
INFO_START_URLS =[]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#爬虫下载文件的存储路径
#这行并没有什么软用，删除会导致图片管道无法加载
IMAGES_STORE="./血压值100"
FILES_STORE="./血压值100"


# IMAGES_URLS_FIELD = 'image_urls'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Kikoeru.middlewares.KikoeruSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "Kikoeru.middlewares.KikoeruDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
ITEM_PIPELINES = {
    # "scrapy.pipelines.images.ImagesPipeline": 1,
   "Kikoeru.pipelines.WorkInfoPipeline": 300,
   "Kikoeru.pipelines.KikoeruImagesPipeline": 301,
   "Kikoeru.pipelines.SaveFilesPipeline": 302,

}
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"