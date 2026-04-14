import urllib.request
import json
import time
import os
import pandas as pd

class NaverNewsCrawler:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_pwd = client_secret
        self.result_all = []

    def crawlNaverNews(self, keyword, start, display=10):
        encText = urllib.parse.quote(keyword)
        url = "https://openapi.naver.com/v1/search/news?query=" + encText
        new_url = url + f'&start={start}&display={display}'
        
        request = urllib.request.Request(new_url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_pwd)
        
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            json_data = response_body.decode('utf-8')
            py_data = json.loads(json_data)
            time.sleep(0.2)
            return py_data
        else:
            print("Error Code:" + str(rescode))
            return None

    def run(self, keyword):
        self.result_all = []
        start = 1
        while start < 1000:
            crawled_data = self.crawlNaverNews(keyword, start)
            if crawled_data:
                print('crawling 성공 :', start)
                self.result_all += crawled_data['items']
                start += 10
            else:
                print('crawling 실패 :', start)
                break

        data_df = pd.DataFrame(self.result_all)
        
        save_path = 'C:/news_crawled/'
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            
        result_filename = f'{save_path}{keyword}_navernews.csv'
        data_df.to_csv(result_filename)
        
        print(f"파일 저장 완료 : {result_filename}")

        return pd.read_csv(result_filename, index_col=0)

# 실행 부분
#client_id = "naver api id"
#client_secret = "naver api pwd"

#crawler = NaverNewsCrawler(client_id, client_secret)
#loaded_data_df = crawler.run('원유')