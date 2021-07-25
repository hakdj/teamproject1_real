## 청하님 part

import pandas as pd
import numpy as np
import json
from config.settings import DATA_DIRS


class RCH:
    def TP1(self):
        df = pd.read_csv(DATA_DIRS[0] + '//MoviesOnStreamingPlatforms_updated.csv', header=0);

        netflix_movies_count = len(df[df['Netflix'] == 1].index);
        hulu_movies_count = len(df[df['Hulu'] == 1].index);
        prime_movies_count = len(df[df['Prime Video'] == 1].index);
        disney_movies_count = len(df[df['Disney+'] == 1].index);
        label = ['Prime Video', 'Netflix', 'Hulu', 'Disney+'];
        count = [prime_movies_count, netflix_movies_count, hulu_movies_count, disney_movies_count];
        scount = sum(count);
        pcount = [prime_movies_count / scount * 100, netflix_movies_count / scount * 100,
                  hulu_movies_count / scount * 100, disney_movies_count / scount * 100];
        num = [];
        final = [];

        for i in range(0, len(pcount)):
            num.append(round(pcount[i], 2));
            line = [];
            line.append(label[i]);
            line.append(num[i]);
            final.append(line);
        data = final.copy();

        return data

    def TP32(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv');
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True);
        df = df.dropna(subset=["Rotten Tomatoes", "Runtime", "Year"]);
        setott = df[ott] == 1;
        setrun = df['Runtime'] <= 180;
        setyear = df['Year'] >= 1900;
        x = df[setott & setrun & setyear];
        scatterdata = [];

        for i in range(len(x)):
            run_RT = [];
            run_RT.append(int(x.iloc[i]['Runtime']));
            run_RT.append(int(x.iloc[i]['Rotten Tomatoes'][:-1]));
            run_RT.append(int(x.iloc[i]['Year']));
            scatterdata.append(run_RT);
        data = scatterdata;

        return data

    def TPex(self):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df['Country'] = df['Country'].str.split(',')

        df = (df
              .set_index(['ID', 'Title', 'Year', 'Age', 'IMDb', 'Rotten Tomatoes', 'Netflix', 'Hulu',
                          'Prime Video', 'Disney+', 'Directors', 'Genres', 'Language', 'Runtime'])['Country']
              .apply(pd.Series)
              .stack()
              .reset_index()
              .drop('level_14', axis=1)
              .rename(columns={0: 'Country'}))
        chains = df['Country'].value_counts()[:20]
        label = []
        count = []
        for i in chains.index:
            label.append(i)
        for j in chains.values:
            count.append(j)

        data = []
        for p in range(len(label)):
            for q in range(len(label)):
                fdata = {
                    'name': label[q],
                    'y': int(count[q]),
                    'drilldown': 'null'
                }
                data.append(fdata)
        return (data)


if __name__ == '__main__':
    # RCH().TP32('Netflix');
    RCH().TP1();
