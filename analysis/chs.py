## 현수님 part
# def chs1 :
# 데이터 set에서 연도별로 영화 장르가 몇개씩 있는지 결과 출력

import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np;
import random;
import seaborn as sns;
import json;
from config.settings import DATA_DIRS


class CHS:
    def chs1(self, year):
        df = pd.read_csv(DATA_DIRS[0] + '//MoviesOnStreamingPlatforms_updated.csv',
                         header=0);
        year_data = df[df['Year'] == int(year)];
        genres_d = year_data['Genres'].str.get_dummies(',');
        genre = genres_d.columns.tolist();
        num = [];
        final = [];

        for i in range(0, len(genres_d.columns)):
            num.append(int(genres_d[genre[i]].value_counts().loc[1]));
            line = [];
            line.append(genre[i]);
            line.append(num[i]);
            final.append(line);

        data = final.copy();

        return data;

    def chs2(self):
        df = pd.read_csv(DATA_DIRS[0] + '//MoviesOnStreamingPlatforms_updated.csv',
                         header=0);
        df.fillna('-', inplace=True);
        data = [];
        for i in range(0, len(df)):
            movie = {};
            movie['Title'] = df['Title'][i];
            movie['Year'] = df['Year'][i];
            movie['Age'] = df['Age'][i];
            movie['IMDb'] = df['IMDb'][i];
            movie['Rotten_Tomatoes'] = df['Rotten Tomatoes'][i];
            movie['Directors'] = df['Directors'][i];
            movie['Genres'] = df['Genres'][i];
            movie['Country'] = df['Country'][i];
            movie['Language'] = df['Language'][i];
            movie['Runtime'] = df['Runtime'][i];
            data.append(movie);
        return data;

    def chs3(self):
        df = pd.read_excel(DATA_DIRS[0] + '//naver.xls', header=0, )
        df.fillna('-', inplace=True);
        data = [];
        for i in range(0, len(df)):
            naver = {};
            naver['Title'] = df['제목'][i];
            naver['audience_rating'] = df['관람객평점'][i];
            naver['Genres'] = df['장르'][i];
            naver['Directors'] = df['감독'][i];
            naver['Actor'] = df['출연배우'][i];
            naver['Opening_date'] = df['개봉일'][i];
            naver['Runtime'] = df['상영시간'][i];
            data.append(naver);
        return data;


if __name__ == '__main__':
    CHS().chs1(2013);
