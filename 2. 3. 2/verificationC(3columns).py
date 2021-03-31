# df.value_counts(sort=False).reset_index()
import pandas as pd
import random
from memory_profiler import profile


@profile
def counting_multiple_dataframe(df):  # 比較するソースコード
    tmp_df = df.value_counts().reset_index()


if __name__ == '__main__':

    dataframe_len = 10000  # Dataframeのindexの長さ　データサイズ

    random.seed(0)
    group_list = [random.randint(0, 60) for j in range(dataframe_len)]
    random.seed(1)
    value_list1 = [random.randint(0, 100) for j in range(dataframe_len)]
    # カラムの追加
    random.seed(2)
    value_list2 = [random.randint(0, 100) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group': group_list,
                                'value1': value_list1,
                                'value2': value_list2})

    counting_multiple_dataframe(sample_df)
