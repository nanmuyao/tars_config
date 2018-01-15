# -*- coding:utf-8 -*-

#2018_1_15 created by tars qq 1558249222@qq.com
#注意
#次脚本中没有拷贝csd文件使用的字体文件
#此脚本用于处理多工程公用一套资源的情况
#具体把公用的资源文件拷贝到指定的目录中 包括csd,png 暂时没有处理字体文件
#次脚本功能再是不完善

import re
import os
import time
import shutil
# from shutil import copy
import os.path

def anylizeFile():
    dirPathDest = "tempFile/"
    if os.path.exists(dirPathDest):
        shutil.rmtree(dirPathDest)

    csdList = ['ClubDetailMsg.csd', 'ClubPopUpMsg.csd', 'ClubRank.csd', 'InputClubIdPanel.csd', 'culbRoomInfo.csd', 'culbInfo.csd']
    # csdList = ['culbRoomInfo.csd']

    for csd in csdList:

        #首先拷贝csd文件
        print csd
        if not os.path.exists("tempFile/"):
            os.makedirs("tempFile/")
        shutil.copy(csd, "tempFile/")

        file_object = open(csd, 'rb')
        for line in file_object:
            content = line.find(".png")
            if content != -1:
                # print line
                strStart = line.find("Path=")
                strEnd = line.find('.png')
                # print strStart, strEnd

                strContent = line[strStart + 6 : strEnd + 4]
                # print strContent

                #提取文件夹名称
                dirName = strContent.split('/')
                # print dirName

                #创建临时目录存放png文件
                dirPathDest = "tempFile/"
                for dir in dirName:
                    if dir.find(".png") == -1:
                        dirPathDest = dirPathDest + dir
                        if not os.path.exists(dirPathDest):
                            # print("该目录当前不存在")
                            os.makedirs(dirPathDest)

                        print strContent
                        # print dirPathDest
                        # 拷贝csd文件中用到的图片到临时目录
                        try:
                            shutil.copy(strContent, dirPathDest)
                        except IOError:
                            print "Error: 没有找到文件或读取文件失败"
                        else:
                            print "内容写入文件成功"

                            # print "strContent:" + strContent

anylizeFile()

