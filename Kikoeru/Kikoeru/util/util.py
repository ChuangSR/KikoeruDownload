import re,os

from Kikoeru import settings


"""
    一个工具包
"""

def insert_info_start_url(url):
    RJ = get_RJ(url)
    work_info_api = settings.WORK_INFO_API + RJ
    # tracks_api = settings.TRACKS_API + RJ
    # self.start_urls.append(tracks_api)
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

"""
    构建文件的根目录
    会对于settings.IMAGES_STORE进行修改
"""
def create_root_path(item):
    dict_item = dict(item)
    save_path = settings.SAVE_PATH
    if save_path[-1] != "/" or save_path[-1] != "\\":
        save_path += "/"
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\']
    root_path = f"{dict_item.get('RJ')}{dict_item.get('title')}"
    for i in char_list:
        if i in root_path:
            root_path = root_path.replace(i, "_")
    root_path = save_path + root_path

    if not os.path.exists(root_path):
        os.makedirs(root_path)

    settings.IMAGES_STORE = root_path
