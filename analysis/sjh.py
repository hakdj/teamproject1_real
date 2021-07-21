## 재현님 part
## def forage :
# 데이터 set에서 OTT플랫폼별 구분 후 시청연령별 영화 개수 결과 출력
## def IMDbScatter :
# 데이터 set에서 OTT플랫폼별 Runtime과 IMDb지수 관계 파악을 위해 데이터 출력
import csv
import pandas as pd
from config.settings import DATA_DIRS


class MyAnalysis:
    def forage(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
        df['Age'].replace('all', '0+', inplace=True)
        AgeList = [0 for _ in range(5)]
        AgeRange = ['0+', '+7', '+13', '+16', '18+']

        for i in range(len(df)):
            if df.iloc[i][ott] == 1:
                if df.iloc[i]['Age'] == '0+':
                    AgeList[0] += 1
                elif df.iloc[i]['Age'] == '7+':
                    AgeList[1] += 1
                elif df.iloc[i]['Age'] == '13+':
                    AgeList[2] += 1
                elif df.iloc[i]['Age'] == '16+':
                    AgeList[3] += 1
                elif df.iloc[i]['Age'] == '18+':
                    AgeList[4] += 1
                else:
                    continue
        result = []

        for i in range(len(AgeRange)):
            d = []
            d.append(AgeRange[i])
            d.append(AgeList[i])
            result.append(d)

        return result

    def ImdbScatter(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
        df = df.dropna(subset=["IMDb", "Runtime"])
        setott = df[ott] == 1
        setrun = df['Runtime'] <= 180
        x = df[setott & setrun]

        scatterdata = []
        colors = {'Netflix': '#C8FAC8', 'Hulu': '#ED561B', 'Prime Video': '#B4B4FF',
                  'Disney+': '#FF28A7'}

        for i in range(len(x)):
            run_im = []
            run_im.append(x.iloc[i]['Runtime'])
            run_im.append(x.iloc[i]['IMDb'])
            scatterdata.append(run_im)

        result = [
            {'name': ott, 'color': colors[ott], 'data': scatterdata}
        ]

        return result


if __name__ == '__main__':
     # MyAnalysis().forage('Netflix')
     MyAnalysis().ImdbScatter('Disney+')
