# 네이버 api사용하는 기능 클래스
import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):
    # 생성자
    def __init__(self):
        print('Naver Search API 생성')

    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', 'oarZN_KRrmiTUg_iEZvL')
        req.add_header('X-Naver-Client-Secret', 'PGexsN7aMd')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: # 웹 정상작동
                print('[{0}] URL Request Succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
        except Exception as e:
            print(e)
            return None

    # 네이버 검색 API를 사용하는 함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode) 
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uparse.quote(search_word))
        url = base + node + param # get값을 만듦 : https://openapi.naver.com...nodeval.json?start=1&display=10&query=코로나

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)

    # 데이터 처리하는 함수
    def getPostData(self, post, jsonResult):
        title = post['title']
        desc = post['description']
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900') # 문자열 형태의 시간을 시간 형식으로 변환
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S')

        jsonResult.append({})
        pass
        return
        