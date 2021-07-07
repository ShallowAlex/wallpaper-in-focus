# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:48:35 2019

@author: Alex
"""

import os
import shutil
from PIL import Image
import re
import time

# adname = []
# ad = []
#生成路径
env_dic = os.environ
IMG_PATH = env_dic["LOCALAPPDATA"] + "/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"

# #读取其他图标名
# Path = './设置'
# if os.path.exists(Path):
#     with open(Path + '/adname.txt','r') as f:
#         ad = f.read()
#         ad = ad[2:-2]
#     adname = re.split(r"[\'\,\s]+",ad)

#创建横板、竖版文件夹
if os.path.exists('./横版'):
    pass
else:
    os.mkdir('./竖版')
    os.mkdir('./横版')

print('-'.center(50, '-'))
#处理
new = 0
old = 0
for i in os.listdir(IMG_PATH):
    # if i in adname:
    #     continue
    if os.path.isfile('./横版/{}.jpg'.format(i)) or os.path.isfile('./竖版/{}.jpg'.format(i)):
        old += 1
        #print('\r'+('重复%d张图片，新增%d张图片'%(old/2, new)).center(40), end='')
        continue
    img = Image.open(IMG_PATH + i)
    w = img.width
    h = img.height
    if w > h:
        shutil.copyfile(IMG_PATH + i, "./横版/"+ i + ".jpg")
        new += 1
        #print('\r'+('重复%d张图片，新增%d张图片'%(old, new)).center(40), end='')
    elif w < h:
        shutil.copyfile(IMG_PATH + i, "./竖版/" + i + ".jpg")
        
print(('重复%d张图片，新增%d张图片'%(old/2, new)).center(40))

print('-'.center(50, '-'))
for i in range(3, -1, -1):
    print('\r'+('即将退出，剩余时间：%d秒'%i).center(38), end='') # end='' 默认为换行符\n ，修改为空不换行
    time.sleep(1) # 暂停1秒
#input("按任意键退出：")
