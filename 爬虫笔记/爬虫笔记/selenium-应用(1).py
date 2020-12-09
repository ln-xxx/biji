import requests,re,os,glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Comic:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    def down_img(self, img_name, img_url):
        r = requests.get(img_url, headers=self.headers)
        with open(img_name, 'wb') as f:
            f.write(r.content)
            print('{}图像保存成功'.format(img_name))

##########################################图片特征函数########################################################################
    def comic_info(self, url='https://www.zymk.cn/2446/'):#特征函数
        r = requests.get(url, headers=self.headers)
        r.encoding = r.apparent_encoding
        html = r.text
        regex = '<li class=".*?" data-id=".*?"><a href="(.*?)" title=".*?">(.*?)</a>'
        regex_book_name_author = '<meta property="og:novel:author" content="(?P<book_author>.*?)"><meta property="og:novel:book_name" content="(?P<book_name>.*?)">'
        info = sorted(re.findall(regex, html))[1:]#测试纸下载前三话
        info = {i[1]: url+i[0] for i in info}
        name_author = re.search(regex_book_name_author, html).groupdict()
        info.update(name_author)
        return info

###################################################################################################################

    def get_selenium_source(self, url):#功能函数
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        return driver.page_source #返回JS渲染过后网页源代码

    def get_img_url(self, url):#传入画链接返回话中所有图像链接,特征函数
        regex = '</script><div class="comicpage" data-page="\d+?"><img src="(.*?)" class="comicimg" data-img="\d+?" onerror="__cr.imgOnError\(\)" />'
        regex_page_num = '<!--<p class="page-info">第 1 页/共 (\d+) 页</p>-->'
        html = self.get_selenium_source(url)
        return {'url': 'http:' + re.search(regex, html).group(1),
                'page_num': int(re.search(regex_page_num, html).group(1))
                }

    def get_img_queue(self, url):
        info = self.get_img_url(url)
        queue = []
        for i in range(1, info['page_num']+1):
            img_url = info['url']
            x = re.sub('%2F\d+.jpg-zymk.middle.webp',
                       '%2F{}.jpg-zymk.middle.webp'.format(i),
                       img_url,
                       )
            queue.append(x)
        return queue

    def save_img_hua(self, url, path=None):#传入一个画链接，实现画的下载
        queue = self.get_img_queue(url)
        for i in range(1, len(queue)+1):
            if path == None:
                self.down_img('{}.jpg'.format(i), queue[i-1])
            else:
                if not glob.glob(path):
                    os.makedirs(path)
                self.down_img('{}/{}.jpg'.format(path, i), queue[i-1])

    def save_img_book(self, url):
        info = self.comic_info(url)
        book_name = info.pop('book_name')#pop提出来并删除
        book_author = info.pop('book_author')
        book_dir = '漫画名称：{}-作者：{}'.format(book_name, book_author)
        if not glob.glob(book_dir):
            os.makedirs(book_dir)
        for name, url in info.items():
            self.save_img_hua(url, '{}/{}'.format(book_dir, name.strip()))



class TxComic(Comic):

    def comic_info(self, url='https://ac.qq.com/Comic/comicInfo/id/622694'):
        '''
        :param url: 传入一个目录链接
        :return: {话名：链接，漫画名称：zzz，作者：xxx}
        '''
        r = requests.get(url, headers=self.headers)
        r.encoding = r.apparent_encoding
        html = r.text
        regex = '<a target="_blank" title=".*?" href="(.*?)">([\S\s]*?)</a>'
        regex_book_name_author = '<h2 class="works-intro-title ui-left"><strong>(?P<book_name>.*?)</strong></h2>' \
                            '[\s\S]*?<span class="first" style="padding-right: 10px;">作者：<em style="max-width: 168px;">(?P<book_author>.*?)&nbsp;图：文东绘 文：六道</em></span>'
        info = re.findall(regex, html)[:3]#测试纸下载前三话
        info = {i[1].replace('\r\n                                        ', '').replace('                                    ', ''): 'https://ac.qq.com'+i[0] for i in info}
        name_author = re.search(regex_book_name_author, html).groupdict()
        info.update(name_author)
        return info

    def get_selenium_source(self, url):#功能函数
        '''
        接受上面的详情字典，访问章节url，进入章节详情页面，返回章节详情页面源码
        '''
        try:
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            driver = webdriver.Chrome(options=option)
            driver.get(url)
            body = driver.find_element_by_css_selector('body')
            body.click()
            for i in range(1, 50):
                body.send_keys(Keys.SPACE)
                time.sleep(0.5)
            return driver.page_source
        except TimeoutError:
            return '超时啦'
    def get_img_url(self, url):
        '''
        :param url: 传入一个话的链接
        :return: {'url':'图片的链接'}
        '''
        regex = '<img src="(.*?)" alt=".*?" data-pid="\d+" data-w="\d+" data-h="\d+" class=".*?" style=".*?" />'
        html = self.get_selenium_source(url)
        info = re.findall(regex, html)
        return {'url': info}

    def save_img_hua(self, url, path=None):#传入一个画链接，实现画的下载
        '''
        :param url: 传入一个话的链接
        :param path: 创建文件的路径
        :return: 创建文件夹，里面保存图片
        '''
        queue = self.get_img_url(url)
        for i in range(1, len(queue['url'])+1):
            if path == None:
                self.down_img('{}.jpg'.format(i), queue['url'][i-1])
            else:
                if not glob.glob(path):
                    os.makedirs(path)
                self.down_img('{}/{}.jpg'.format(path, i), queue['url'][i-1])

if __name__ == '__main__':

    #url = 'https://mhpic.zymkcdn.com/comic/Z%2F%E7%B0%AA%E4%B8%AD%E5%BD%95%2F1%E8%AF%9DGQV%2F6.jpg-zymk.middle.webp'
    '''
    https://mhpic.zymkcdn.com/comic/Z/簪中录/1话GQV/1.jpg-zymk.middle.webp
    https://manhua.qpic.cn/manhua_detail/0/17_20_34_9d9930717829744afbfe4598ed3d23bd_6525.jpg/0
    '''
    #url = 'https://www.zymk.cn/2446/115899.html'
    #url = 'https://www.zymk.cn/2446/'
    #url = 'https://ac.qq.com/ComicView/index/id/622694/cid/1'
    url = 'https://ac.qq.com/Comic/comicInfo/id/622694'
    #x = Comic()
    #print(x.comic_info())
    #print(TxComic().get_selenium_source(url))
    #TxComic().down_img('xx.jpg')
    #print(TxComic().get_img_url(url))
    #TxComic().save_img_hua(url, '谢文东')
    TxComic().save_img_book(url)
