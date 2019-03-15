#!/usr/bin/env python
# encoding: utf-8
# Author: guoxudong
"""
Author: guoxudong
Time: 2019-03-15

This script is used to merge the file of kubeconfig
Before using it, you should make sure your python has package: PyYAML
Install it: pip install PyYAML

---
这个脚本用于合并多个kubeconfig文件，用于在一台终端操作多个kubernetes集群
需要提前安装的Python包：PyYAML
安装：pip install PyYAML

---
Before Usage:
1. Install package PyYAML
2. Set your infomation at the top of the scripts

---
使用之前：
1. 安装PyYAML包
2. 可以传入参数 -d kubeconfig文件所在的目录

---
Usage:
  Select directory:
    python switch.py -d configfile

---
使用：
  自定义选择目录
    python switch.py -d configfile

"""
import argparse
import json
import os

import yaml

FLAGS = None

KUBECONFIG = {
    "kind": "Config",
    "apiVersion": "v1",
    "preferences": {},
    "clusters": [],
    "users": [],
    "contexts": [],
    "current-context": ""
}

ALLCONTEXTS = []


def getLocalFiles():
    """
    Process local files
    处理本地文件
    :param dir:
    :return: 配置文件路径
    """
    return os.path.dirname(os.path.realpath(__file__)) + '/' + FLAGS.directory + '/'


def readFiles(curPath):
    """
    读取
    :return:
    """
    fileList = os.listdir(curPath)
    for filename in fileList:
        handleConfig(curPath + filename, filename)


def handleConfig(path, filename):
    """
    处理配置
    :param path: 配置文件路径
    :return:
    """
    cluster = ''
    user = ''
    with open(path, 'r') as f:
        all = yaml.load(f.read(), Loader=yaml.FullLoader)

        for i, context in enumerate(all.get('contexts', '')):
            cluster = context['context']['cluster']
            user = context['context']['user']
            name = filename + '-' + str(i)
            context['name'] = name
            ALLCONTEXTS.append(name)

            for clu in all.get('clusters', ''):
                if cluster == clu['name']:
                    cluster_name = name + '-cluster'
                    clu['name'] = cluster_name
                    context['context']['cluster'] = cluster_name

            if len(all.get('clusters')) > len(all.get('users')):
                user_name = name + '-user'
                all['users'][0]['name'] = user_name
                context['context']['user'] = user_name
            else:
                for usr in all.get('users', ''):
                    if user == usr['name']:
                        user_name = name + '-user'
                        usr['name'] = user_name
                        context['context']['user'] = user_name

        KUBECONFIG['clusters'].extend(all.get('clusters', ''))
        KUBECONFIG['users'].extend(all.get('users', ''))
        KUBECONFIG['contexts'].extend(all.get('contexts', ''))


def outputFile():
    """
    输出文件
    :return:
    """
    with open('config', 'w') as f:
        f.write(json.dumps(KUBECONFIG))


def main():
    """
    主方法
    :return:
    """
    readFiles(getLocalFiles())
    outputFile()
    print('# COPY configfile to .kube:')
    print('cp config ~/.kube\n')
    print('# View all users:')
    print('kubectl config get-contexts\n')
    print('# learn more:')
    print('kubectl config --help\n')
    print('# Cluster switching command:')
    for command in ALLCONTEXTS:
        print('kubectl config use-context {0}'.format(command))
    # print(ALLCONTEXTS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        default="configfile",
        type=str,
        help="the directory kubeconfig!")
    FLAGS, unparsed = parser.parse_known_args()
    main()
