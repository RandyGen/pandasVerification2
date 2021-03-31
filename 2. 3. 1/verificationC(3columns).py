# df.value_counts(sort=False).reset_index()
import pandas as pd
import time
import random
from statistics import mean, median,variance,stdev


def counting_multiple_dataframe(df):  # 比較するソースコード
    tmp_df = df.value_counts().reset_index()


if __name__ == '__main__':

    repeat_time = 100  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 10000  # Dataframeのindexの長さ　データサイズ
    execute_time = []  # 処理時間リスト

    for i in range(repeat_time):
        # データ作成
        random.seed(i)
        group_list = [random.randint(0, 60) for j in range(dataframe_len)]
        random.seed(i+2)
        value_list1 = [random.randint(0, 100) for j in range(dataframe_len)]
        # カラムの追加
        random.seed(i+4)
        value_list2 = [random.randint(0, 100) for j in range(dataframe_len)]
        sample_df = pd.DataFrame({'group': group_list,
                                  'value1': value_list1,
                                  'value2': value_list2})

        start = time.time()  # 処理開始時間
        counting_multiple_dataframe(sample_df)  # 複数列の組み合わせのカウント
        end = time.time()  # 処理終了時間
        execute_time.append(end - start)  # 1回の処理時間計算
        if(i % 10 == 0):
            print('one time runtime(', i, '):', execute_time[i])  # 10*i回の処理時間表示

    print('平均:{0:.5f} [sec]'.format(mean(execute_time)))  # 100回の処理時間の平均表示
    print('分散:{0:.8f} [sec]'.format(variance(execute_time)))  # 分散
    print('標準偏差:{0:.8f} [sec]'.format(stdev(execute_time)))  # 標準偏差
