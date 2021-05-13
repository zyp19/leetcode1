def kMeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]
    # 保存每行数据对应的聚类中心和距离，第一个值表示这行数据对应的k是几 ，第二个值表示这行数据与聚类中心的距离
    clusterAssment = mat(zeros((m, 2)))
    # 首次选出聚簇点，选取这列数据最大值最小值点之间的一个随机点
    n = shape(dataSet)[1] # 数据集列数
    # 随机创建k*n的聚类中心矩阵
    centroids = mat(zeros((k, n)))
    for x in range(n):
        min_data = min(dataSet[:][x])
        max_data = max(dataSet[:][x])
        range_data = float(max_data - min_data)
        centroids[:, x] = mat(min_data + range_data * random.rand(k, 1))

    # 聚类中心是否变化的标志位
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        # 第一个for循环是赋值步骤 ,对于每一个样例，计算其应该属于的类
        for i in range(m):
            minDist = inf
            minIndex = -1
            # 每行数据都需要计算和各个聚类中心的距离找出最小的
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i][:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print centroids
        # 第二个for循环是聚类中心的移动，即：对于每一个类，重新计算该类的质心
        for cent in range(k):  # recalculate centroids
            # nonzero函数是numpy中用于得到数组array中非零元素的位置（数组索引）的函数。
            # 它的返回值是一个长度为a.ndim(数组a的轴数)的元组，元组的每个元素都是一个整数数组，其值为非零元素的下标在对应轴上的值
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0][0]]  # 获取聚类中心
            # 然后计算每一个组的平均值，将该组所关联的中心点移动到平均值的位置
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

# 距离计算 欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))
