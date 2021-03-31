# pd.Series.value_counts()
import pandas as pd
import random
from memory_profiler import profile


@profile
def counting_multiple_dataframe(df):  # 比較するソースコード
    cols = ["group", "value"]
    ser = df[cols].astype(str)\
            .apply(lambda lis: [ x for x in lis], axis=1)\
            .str.join(" | ")\
            .value_counts()


if __name__ == '__main__':

    dataframe_len = 50000  # Dataframeのindexの長さ　データサイズ

    # データ作成
    random.seed(0)
    group_list = [random.randint(0, 60) for j in range(dataframe_len)]
    random.seed(1)
    value_list = [random.randint(0, 100) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group': group_list,
                                'value': value_list})

    counting_multiple_dataframe(sample_df)  # 複数列の組み合わせのカウント
