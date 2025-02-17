from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split

'''
    @:param
    @:return classifier svm分类器
    通过训练集的向量集训练出svm分类器
'''
def getSVMclf():
    # 1.读取数据集
    path = './text.data'
    data = np.loadtxt(path, dtype=float, delimiter=',')

    # 2.划分数据与标签
    x, y = np.split(data, indices_or_sections=(20,), axis=1)  # x为数据，y为标签
    train_data, test_data, train_label, test_label = train_test_split(x, y, random_state=0, train_size=0.8,
                                                                      test_size=0.2)  # sklearn.model_selection.

    # 3.训练svm分类器
    classifier = svm.SVC(C=100, kernel='rbf', gamma=0.01, decision_function_shape='ovr')  # ovr:一对多策略
    classifier.fit(train_data, train_label.ravel())  # ravel函数在降维时默认是行序优先

    # 4.计算svc分类器的准确率
    print("训练集：", classifier.score(train_data, train_label))
    print("测试集：", classifier.score(test_data, test_label))

    # # 查看决策函数
    # dec = classifier.decision_function(train_data)
    # print('train_decision_function:\n', dec)
    return classifier


if __name__ == '__main__':
    getSVMclf()