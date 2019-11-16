import os
import pandas as pd
##运行bert进行测试后，生成test_reeults.tsv文件,并不是直接结果，是各个标签概率值，本函数就是将其转换

if __name__ == '__main__':
    path = "output/"
    pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)
    data = pd.DataFrame(columns=['label'])
    print(pd_all.shape)

    for index in pd_all.index:
        score_zero = pd_all.loc[index].values[0]
        score_one = pd_all.loc[index].values[1]
        score_two = pd_all.loc[index].values[2]

        if max(score_zero, score_one, score_two) ==score_zero:
            # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["0"]
        elif max(score_zero, score_one, score_two) == score_one:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = [ "1"]
        else:
            #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = [ "2"]
        #print(negative_score, positive_score, negative_score)

    data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')
