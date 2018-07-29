#coding: utf-8

import requests
import urllib
import urllib2
import sys
headers = {
    "User-Agent": "Aweme/2.2.0 (iPhone; iOS 12.0; Scale/2.00)",
    "Host": "aweme.snssdk.com",
    "cookie": "_ga=GA1.3.1871980470.1532876253; _gid=GA1.3.198196564.1532876253; odin_tt=23c532f33d254837735e18aa296d730f3729c1e62a978f668783319d6740d9ea9b8944cbec4d38fa6e7242cda7e683c6; sessionid=7f6698568977ce6ca69c7f8446055987; sid_guard=7f6698568977ce6ca69c7f8446055987%7C1532875749%7C5184000%7CThu%2C+27-Sep-2018+14%3A49%3A09+GMT; sid_tt=7f6698568977ce6ca69c7f8446055987; uid_tt=fb48d41c69e5cbaa7e71b306a4a62ee0; qh[360]=1; install_id=39311693456; ttreq=1$24982a0491751c7714e9591bdee278d6a4047b90"
}
#完成百分比
def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()

#下载视频
def downLoad_MultiTry(name, url, maxTryNum = 6):
    for tries in range(maxTryNum):
        try:
            #urllib.urlretrieve(url, './%s.mp4'% (name), report)
            urllib.urlretrieve(url, name+'.mp4')
            print (u"%s  下载成功！\n" % name)
            break
        except Exception:
            if tries < (maxTryNum - 1):
                print (u' 进行第 %d 次尝试' % (tries+1))
                continue
            else:
                print (u"%s  下载失败! \n" % name)
                break

s = requests.session()
# urlList = "https://aweme.snssdk.com/aweme/v1/hot/search/list/"
# for word in s.get(urlList).json()['data']['word_list']:
#     print word['word'], word['hot_value']


urlSearch = "https://aweme.snssdk.com/aweme/v1/general/search/?iid=39311693456&device_id=55474542293&os_api=18&app_name=aweme&channel=App%20Store&idfa=7976D515-42EC-4C74-AE06-AD312FBF7577&device_platform=iphone&build_number=22009&vid=9D8CA096-223B-4060-9833-0BA5B1F91C9B&openudid=cfdeb247c391912ed9ab871f760e123615ef21ab&device_type=iPhone10,1&app_version=2.2.0&version_code=2.2.0&os_version=12.0&screen_width=750&aid=1128&ac=WIFI&count=12&keyword=%E6%92%B8%E7%8C%AB%E7%AC%AC%E4%B8%80%E8%A7%86%E8%A7%92&offset=0&mas=01ee01e726c88d12e340fc8637e35c9aa5879e4fbe47f7abe506ae&as=a1f5dcb5a47acbf6dd1513&ts=1532872356"
urlSearch = "https://aweme.snssdk.com/aweme/v1/general/search/?iid=39311693456&device_id=55474542293&os_api=18&app_name=aweme&channel=App%20Store&idfa=7976D515-42EC-4C74-AE06-AD312FBF7577&device_platform=iphone&build_number=22009&vid=9D8CA096-223B-4060-9833-0BA5B1F91C9B&openudid=cfdeb247c391912ed9ab871f760e123615ef21ab&device_type=iPhone10,1&app_version=2.2.0&version_code=2.2.0&os_version=12.0&screen_width=750&aid=1128&ac=WIFI&count=12&keyword=%E6%92%B8%E7%8C%AB%E7%AC%AC%E4%B8%80%E8%A7%86%E8%A7%92&offset=0&mas=017c6db199347edd92d74df181105d64ed64a09377e5d17781028e"
# urlSearch = "https://aweme.snssdk.com/aweme/v1/general/search/?iid=39311693456&device_id=55474542293&os_api=18&app_name=aweme&channel=App%20Store&idfa=7976D515-42EC-4C74-AE06-AD312FBF7577&device_platform=iphone&build_number=22009&vid=9D8CA096-223B-4060-9833-0BA5B1F91C9B&openudid=cfdeb247c391912ed9ab871f760e123615ef21ab&device_type=iPhone10,1&app_version=2.2.0&version_code=2.2.0&os_version=12.0&screen_width=750&aid=1128&ac=WIFI&count=12&keyword=%E6%92%B8%E7%8C%AB%E7%AC%AC%E4%B8%80%E8%A7%86%E8%A7%92&offset=0&mas=017c6db199347edd92d74df181105d64ed64a09377e5d17781028e&as=a1657da588debb6c9d9333&ts=1532878056"
urlList = s.get(urlSearch, headers=headers).json()['aweme_list']
print (urlList)

for li in urlList[:4]:
    urlVideo = li['video']['play_addr']['url_list'][0]
    r = requests.get(urlVideo, allow_redirects=False)
    downLoad_MultiTry(li['desc'], r.headers['Location'])




