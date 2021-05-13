import os
import gdal
from cv2 import cv2
import numpy as np
import sys


# 拉伸图像  #图片的16位转8位
def uint16to8(bands, lower_percent=0.001, higher_percent=99.999):
    out = np.zeros_like(bands, dtype=np.uint8)
    n = bands.shape[0]
    for i in range(n):
        a = 0  # np.min(band)
        b = 255  # np.max(band)
        c = np.percentile(bands[i, :, :], lower_percent)
        d = np.percentile(bands[i, :, :], higher_percent)
        t = a + (bands[i, :, :] - c) * (b - a) / (d - c)
        t[t < a] = a
        t[t > b] = b
        out[i, :, :] = t
    return out


path = sys.path[0]  # 获取当前代码路径
tif_list = [x for x in os.listdir(path) if x.endswith(".tif")]
for num, i in enumerate(tif_list):
    print(path + '\\' + i)
    dataset = gdal.Open(path + '\\' + i)
    width = dataset.RasterXSize  # 获取数据宽度
    height = dataset.RasterYSize  # 获取数据高度
    outbandsize = dataset.RasterCount  # 获取数据波段数
    im_geotrans = dataset.GetGeoTransform()  # 获取仿射矩阵信息
    im_proj = dataset.GetProjection()  # 获取投影信息
    datatype = dataset.GetRasterBand(1).DataType
    im_data = dataset.ReadAsArray()  # 获取数据
    # print(im_data.shape)
    img3 = uint16to8(im_data)
    img2 = img3[0:3, :, :]
    img2 = np.transpose(img2, (1, 2, 0))
    out = img2[:, :, ::-1]  # rgb->bgr
    cv2.imwrite(path + '\\' + i, out)
    print(num)

