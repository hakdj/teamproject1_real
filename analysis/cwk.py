# import csv
# import numpy as np;
# import pandas as pd;
# import seaborn as sns;
# import matplotlib;
# import matplotlib.pyplot as plt;
# import plotly.express as px;
# from plotly.offline import iplot;
# import plotly.graph_objs as go;
# from plotly import tools;


from config.settings import DATA_DIRS, BASE_DIR, STATICFILES_DIRS


class CorMatrix:
    def M(request):
        import pandas as pd
        import numpy as np;
        import seaborn as sns
        import matplotlib.pyplot as plt

        df = pd.read_csv(DATA_DIRS[0] + '//MoviesOnStreamingPlatforms_updated.csv',
                         header=0);
        df.drop(['Unnamed: 0', 'Type'], axis=1, inplace=True);
        #print(df.head());
        #print(df.tail());

        # 컬럼별 type 확인 및 결측치 확인
        #print(df.info());
        #print(df.isnull().sum());

        df['Rotten Tomatoes'] = df['Rotten Tomatoes'].str.replace('%', '');
        #print(type(df['Rotten Tomatoes'].dtype));

        df['Rotten Tomatoes'] = df['Rotten Tomatoes'].apply(pd.to_numeric)
        #print(df.dtypes);

        sns.set(font_scale=1.1);  ## 폰트사이즈 조절
        sns.set_style('ticks');  ## 축 눈금 표시
        data = df[['Runtime', 'Rotten Tomatoes', 'IMDb', 'Age', 'Year']];
        sns.pairplot(data,
                     diag_kind=None);
        plt.show();
        plt.savefig(STATICFILES_DIRS[0] +'//img//matrix.png');


if __name__ == '__main__':
    CorMatrix().M();
