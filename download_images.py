import httplib
import urllib

MAIN_URL = "www.xxx.com" #域名
DATA_FILE = '/Users/apple/Downloads' #本地文件
IMAGE_FILE_PATH = '/Users/apple/Downloads/sample_images/' #下载图片的保存地址



'''读取本地文件'''
def read_file():
    contant =open(DATA_FILE).read()
    return contant

'''拼接url'''
def get_url(data_id):
    return "/data/" + info_id +"?data_id=20&data_type=d"

'''获取response内容'''
def get_http(url):
    conn = httplib.HTTPConnection(MAIN_URL)
    conn.request(method="GET",url=url)
    response = conn.getresponse()
    if response.status != 200:
        return None

    data = response.read()
    conn.close()
    return data

'''解析response返回的内容'''
def get_image(data):
    pos = data.find('Pic')
    city_pos = data.find('City')
    if pos < 0:
        return None
    if city_pos < 0:
        return None

    if city_pos - pos < 20:
        return None

    colon_pos = data[pos:].find(':')
    if colon_pos < 0:
        return None
    first_tail_pos = data[pos:].find('.jpg')
    if first_tail_pos < 0:
        return None
    return data[pos:][colon_pos + 1:first_tail_pos + 4]

'''保存图片文件到本地'''
def save_image(image_name):
    file_name = image_name[8:]
    url = "http://image.xxx.com" + image_name
    data = urllib.urlopen(url).read()
    path = IMAGE_FILE_PATH + file_name
    f = file(path, "wb")
    f.write(data)
    f.close()

if __name__ == '__main__':
    content = read_file()
    info_array = content.split('\n')
    for id in info_array:
        url = get_url(id)
        data = get_http(url)
        if data == None:
            continue

        image_name = get_image(data)
        if image_name == None:
            continue

        save_image(image_name)
