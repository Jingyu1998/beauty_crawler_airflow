import sys
from PTT_Beauty_Spider.crawler import PttSpider, Download, ArticleInfo
from datetime import datetime

def main(board="beauty", page_term=2, push_rate=10):
    # python beauty_spider2.py [版名] [爬幾頁] [推文多少以上]
    # python beauty_spider2.py beauty 3 10
    # board, page_term, push_rate = 'beauty', 5, 20  # for debugger
    print('start crawler ptt {}...'.format(board))
    crawler_datetime = datetime.now()
    spider = PttSpider(board=board,
                       parser_page=page_term,
                       push_rate=push_rate)
    spider.run()
    datetime_format = '%Y%m%d'
    crawler_time = '/home/happy_pic/{}_PttImg_{:{}}'.format(spider.board, crawler_datetime, datetime_format)
    info = ArticleInfo.data_process(spider.info, crawler_time)
    download = Download(info)
    download.run()
    print("下載完畢...")


if __name__ == '__main__':
    main()

