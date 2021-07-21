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


if __name__ == '__main__':
    CHS().chs1(2013);
