# df[cols].astype(str).apply(lambda lis: [ x for x in lis], axis=1).str.join().value_counts()
import pandas as pd
import random
from memory_profiler import profile


@profile
def counting_multiple_dataframe(df):  # 比較するソースコード
    cols = ["group", "value1", "value2"]
    ser = df[cols].astype(str)\
            .apply(lambda lis: [ x for x in lis], axis=1)\
            .str.join(" | ")\
            .value_counts()


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
