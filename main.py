import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def firmScalePercentage(self):
    df = pd.read_csv('51job.csv',encoding= 'utf-8')
    # print(ds.to_string())
    # print(df.index)
    # print(type(df['公司类型']))
    firmScale = df['公司类型']
    list = []
    for i in firmScale:
        i = i.split('|')[1]
        list.append(i)
    result = pd.value_counts(list)
    scale = [218/523,248/523,57/523]
    y = np.array(scale)
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    labels = ['小型公司','中型公司','大型公司']
    plt.pie(y,labels=labels,autopct='%1.1f%%',shadow=True)
    plt.title('公司规模比例')
    plt.axis('equal')
    plt.legend(loc ='right',fontsize = 10,bbox_to_anchor=(1,1),borderaxespad=0.4 )
    plt.savefig("D:\\公司规模.png",dpi = 150,bbox_inches = 'tight')
    plt.show()

def eduRequire(self):
    df = pd.read_csv('51job.csv', encoding='utf-8')

    edu = df['地点']
    list = []
    for i in edu:
        inner = i.split('|')
        del inner[0:2]
        if inner:
            list.append(inner[0])

    print(list)
    print(pd.value_counts(list))
    sum = 0
    # for i in range(6):
    #     sum = sum + pd.value_counts(list)[i]
    for i in pd.value_counts(list):
        sum = sum + i

    scale = []
    for i in pd.value_counts(list):
        scale.append(i / sum)
    y = np.array(scale)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    labels = ['本科', '大专', '硕士', '中专', '博士', '高中']
    explode = [0, 0, 0, 0.8, 0.8, 0.8]
    plt.pie(y, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False)
    plt.title('元宇宙行业需要的学历要求')
    plt.axis('equal')
    plt.legend(loc='right', fontsize=10, bbox_to_anchor=(1, 1), borderaxespad=0.4)
    plt.savefig("D:\\学历要求.png", dpi=150, bbox_inches='tight')
    plt.show()
if __name__ == '__main__':

    firmScalePercentage()
    eduRequire()
