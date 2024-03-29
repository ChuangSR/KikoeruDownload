import re,os

from Kikoeru import settings


"""
    一个工具包
"""

def insert_info_start_url(url):
    RJ = get_RJ(url)
    work_info_api = settings.WORK_INFO_API + RJ
    settings.INFO_START_URLS.append(work_info_api)

def get_RJ(url):
    groups = re.match(".*RJ(\d*).*", url.strip())
    if groups is None:
        return None
    return groups.group(1)
def to_hour(duration) -> str:
    duration = int(duration)
    second = duration%60
    minute = int(duration/60)%60
    hour = int(duration/60/60)
    return f"{hour}:{minute}:{second}"

def replace(file_name):
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\', "："]
    for i in char_list:
        if i in file_name:
            file_name = file_name.replace(i, "_")
    return file_name