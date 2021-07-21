import bs4
import pandas as pd
import numpy as np
import requests              # url 불러오기 위해서
from config.settings import DATA_DIRS

## 1. 다운받은 파일에서 데이터 불러오기----------------------------------------------------------------------------------

class Titanic:
    def t1(self, feature):
    
        df = pd.read_csv(DATA_DIRS[0] + '/titanic.csv')
        x = df.groupby([feature, 'Survived']).count()['Name']

        result = []
        for i in range(0, len(x), 2):           # range는 짝수만 뽑히도록 함
            category = dict()
            category['name'] = x.index[i][0]
            if type(category['name']) != str :      
                category['name'] = int(x.index[i][0])
            category['data'] = x[i:i+2].tolist()
            result.append(category)
        print(result)
        return result



class Galaxy:
    def g1(self):
        df = pd.read_csv(DATA_DIRS[0] + '/galaxy.csv')
        print(df)



## 2. 웹 스크래핑으로 데이터 불러오기------------------------------------------------------------------------------------

class Naver:
    def n1(self):
        df = pd.read_html('https://finance.naver.com/marketindex/?tabSel=materials#tab_section', encoding='euc-kr')
        df1 = df[2]             # 리스트 중 dataframe 하나만 뽑아짐

        # 현재가(컬럼), 등락율(선)으로 highcharts 그릴 예정
        nm = df1['상품명'].tolist()       # 향후 카테고리에 사용할 내용

        # 등락율은 숫자로 바꿔주어야 함
        # print(df1.dtypes)     # 현재가: float, 등락율: object
        cur = df1['현재가'].tolist()
        rate = df1['등락율'].str.strip('%').astype(float).tolist()

        result = {
            'category': nm,
            'data1': cur,
            'data2': rate
        }

        return result



## 3. open API에서 데이터 불러오기-------------------------------------------------------------------------------------

class Open:
    def o1(self, startdt, enddt):
        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=5GaLPV2oPbawS%2B9h5gtGq9f98t6Cr%2FVdc%2B1VVzOCySwo5yzF8yo%2BH1GWB0iI6rugXuuKn4He9Uwkn9Y4X2VUCg%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startdt+'&endCreateDt='+enddt
        result = requests.get(url)

        response = result.text.encode('utf-8')
 
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml')
        rows = xml_obj.find_all('item')
    
        a = rows[0].find('accDefRate').text    # accDefRate 태그 안 글자만 string으로 가져옴

        result = []                           # dataframe 만들기 위한 [[], [], [], ...] 형태
        nameList = []                         # 컬럼명
        for i in range(0, len(rows)):
            item = rows[i].find_all()         # item 안의 모든 태그를 하나의 리스트로 반환

            itemData = []                     # 태그 안 text만 모은 리스트
            for j in range(len(item)):
                text = item[j].text           # 각 태그의 문자열만 str으로 가져옴
                itemData.append(text)
                if i == 0:
                    nameList.append(item[j].name)       # tag 이름을 가져와서 컬럼명으로 만듦
            result.append(itemData)

        df = pd.DataFrame(result, columns=nameList)   
       
        # Highcharts 그리기-----------------------------------------------------------
        # 기준일(stateDt)에 따른 확진자수(decideCnt), 누적검사완료수(accExamCompCnt), 사망자수(deathCnt), 치료환자수(careCnt) plotting
        # 날짜 순서가 역순이므로 날짜를 다시 정렬해야함!
        x = df.sort_values('stateDt')

        result = {
            'xaxis': x['stateDt'].tolist(),
            'case': x['decideCnt'].astype(int).tolist(),        
            'death': x['deathCnt'].astype(int).tolist(),
            'care': x['careCnt'].astype(int).tolist()
        }
        print(result)
        return result


## ws0621-----------------------------------------------------------------------------------------------------

class Api:
    def covid19(self):
        df = pd.read_json('https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=1&returnType=json&serviceKey=5GaLPV2oPbawS%2B9h5gtGq9f98t6Cr%2FVdc%2B1VVzOCySwo5yzF8yo%2BH1GWB0iI6rugXuuKn4He9Uwkn9Y4X2VUCg%3D%3D')
        t_cnt = df.loc[0, 'totalCount']         # 빠르게 로딩한 뒤 totalCount만 찾아서 다시 로딩

        df = pd.read_json('https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=' + str(t_cnt) + '&returnType=json&serviceKey=5GaLPV2oPbawS%2B9h5gtGq9f98t6Cr%2FVdc%2B1VVzOCySwo5yzF8yo%2BH1GWB0iI6rugXuuKn4He9Uwkn9Y4X2VUCg%3D%3D')
        result = df['data'].tolist()            # [{병원정보1}, {병원정보2}, ...] 처럼 얻어짐 --> "data" 부분만 얻은 것과 같음

        lst = []
        for r in result:
            if r['sttTm'] != None:       # 중간 중간 None이어서 오류나는 지점 있음!
                r['sttTm'] = r['sttTm'][0:2] + ':' + r['sttTm'][2:4]     # 시간 '1200' -> '12:00'
            if r['endTm'] != None:
                r['endTm'] = r['endTm'][0:2] + ':' + r['endTm'][2:4]
            if r['hldyYn'] != None :
                r['hldyYn'] = r['hldyYn'].replace('N', '진료함')         # 운영여부 한글로 바꿈
                r['hldyYn'] = r['hldyYn'].replace('Y', '진료안함')
            r['slrYmd'] = r['slrYmd'][0:4] + '년 ' + r['slrYmd'][4:6] + '월 ' + r['slrYmd'][6:8] + '일'
            lst.append(r)

        return lst




# 잘 동작하는지 확인
if __name__ == '__main__':
    Api().covid19()
    # Titanic().t1('Pclass')
    # Galaxy().g1()
    # Naver().n1()
    # Open().o1('20210601', '20210603')
    # Titanic().t1('Embark')