import os
import pandas as pd
##运行bert进行测试后，生成test_reeults.tsv文件,并不是直接结果，是各个标签概率值，本函数就是将其转换

if __name__ == '__main__':
    path = "output/"
    test_label = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)
    test=pd.read_csv("data/test.tsv",sep='\t',header=None)#读取测试集数据
    id=test[0]#测试集第0列是id
    final=[]
    #print(test.shape)
    #print(id)

#可以先看一下test_result.tsv是n行3列的，表示n组数据，3个label各个label的概率， 根据def get_labels(self)函数里的顺序
    #第一列是label为0的概率，第二列是label为1的概率，第三列是label为2的概率，哪个概率大，认为分为哪一类
    for index in test_label.index:
        score_zero = test_label.loc[index].values[0]
        score_one = test_label.loc[index].values[1]
        score_two = test_label.loc[index].values[2]

        if max(score_zero, score_one, score_two) ==score_zero:
            final.append([id.loc[index],0])
        elif max(score_zero, score_one, score_two) == score_one:
            final.append([id.loc[index],1])
        else:
            final.append([id.loc[index],2])
    #print(final)
    to_final = pd.DataFrame(final)
    to_final.to_csv(os.path.join(path, "final_result.tsv"),sep = '\t',index=None, header=['id', 'label'])  # index为false表示不保留行索引,若想分隔符为/t，可加入sep=/t

