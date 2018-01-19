# -*- coding:utf-8 -*-

#2018_1_15 created by tars qq 1558249222@qq.com
#注意
#次脚本中没有拷贝csd文件使用的字体文件
#此脚本用于处理多工程公用一套资源的情况
#具体把公用的资源文件拷贝到指定的目录中 包括csd,png 暂时没有处理字体文件

import re
import os
import time
import shutil
# from shutil import copy
import os.path
import stat


# csdList = ['ClubDetailMsg.csd', 'ClubPopUpMsg.csd', 'ClubRank.csd', 'InputClubIdPanel.csd', 'culbRoomInfo.csd', 'culbInfo.csd']
csdList = ['Play1.csd']
dirPathDest = "tempFile"

def updateDir():

    #清理目录
    if os.path.exists(dirPathDest):
        shutil.rmtree(dirPathDest)

    #新建目录
    if not os.path.exists(dirPathDest):
        os.makedirs(dirPathDest)

    abslotelyPath = os.getcwd()
    print "当前路径:"+abslotelyPath

fileCount = 0

#处理字体文件
def delZiTi(file_object):
    print "处理字体文件"
    global fileCount
    for line in file_object:
        content = line.find(".ttf")
        if content != -1:
            print line
            strStart = line.find("Path=")
            strEnd = line.find('.ttf')
            # print strStart, strEnd

            strContent = line[strStart + 6 : strEnd + 4]
            # print strContent

            #提取文件夹名称
            dirName = strContent.split('/')
            # print dirName

            #创建临时目录存放png文件
            dirPathDestTemp = "tempFile/"
            for dir in dirName:
                if dir.find(".ttf") == -1:
                    dirPathDestTemp = dirPathDestTemp + dir + "/"

            print "strContent", strContent
            print "dirPathDestTemp", dirPathDestTemp
            if not os.path.exists(dirPathDestTemp):
                # print("该目录当前不存在")
                os.makedirs(dirPathDestTemp)

            #拷贝csd文件中用到的图片到临时目录
            try:
                shutil.copy(strContent, dirPathDestTemp)
            except IOError:
                print "Error: 没有找到:"+strContent
            else:
                fileCount += 1
                # print "找到文件并转移成功:"+strContent

#处理Pic图片
def dealPic(file_object):
    print "处理Pic图片"
    global fileCount
    for line in file_object:
        content = line.find(".png")
        if content != -1:
            strStart = line.find("Path=")
            strEnd = line.find('.png')

            strContent = line[strStart + 6: strEnd + 4]

            # 提取文件夹名称
            dirName = strContent.split('/')

            # 创建临时目录存放png文件
            dirPathDestTemp = "tempFile/"
            for dir in dirName:
                if dir.find(".png") == -1:
                    dirPathDestTemp = dirPathDestTemp + dir + "/"

            # print "strContent", strContent
            # print "dirPathDestTemp", dirPathDestTemp
            if not os.path.exists(dirPathDestTemp):
                # print("该目录当前不存在")
                os.makedirs(dirPathDestTemp)

            # 拷贝csd文件中用到的图片到临时目录
            try:
                shutil.copy(strContent, dirPathDestTemp)
            except IOError:
                print "Error: 没有找到:" + strContent
            else:
                fileCount += 1
                # print "找到文件并转移成功:"+strContent

def anylizeFile():
    updateDir()
    global fileCount
    for csd in csdList:
        try:
            shutil.copy(csd, dirPathDest)
            file_object = open(csd, 'rb')
        except IOError:
            print "Error: 没有找到:" + csd
        else:
            fileCount += 1
            # print "找到文件并转移成功:" + csd
            #这里为什么file_object不能连续给两个函数去使用呢?
            # delZiTi(file_object.read())
            dealPic(file_object)

    #完成后打开指定路径
    if os.path.isdir(dirPathDest):
        os.chmod(dirPathDest, stat.S_IRWXU)
        os.startfile(dirPathDest)

    print "共处理文件数量:"+str(fileCount)


anylizeFile()


