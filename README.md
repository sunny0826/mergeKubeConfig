# 合并kubeconfig文件

## 适用环境

* 需要在终端使用命令行管理多集群
* kubernetes集群中安装了istio，需要使用```istioctl```命令，但是集群节点并没有安装```istioctl```，需要在本地终端操作
* 不愿频繁编辑.kube目录中的config文件的同学

## 准备工作

* Python环境：2.7或者3均可
* 需要依赖包：```PyYAML```

## 开始使用

* 安装依赖：

        pip install PyYAML
        
* 运行脚本

    * 默认运行方式，kubeconfig文件放入```configfile```文件
    
            python merge.py
            
    * 自定义kubeconfig文件目录
    
            python merge.py -d {custom-dir}
            
## 运行后操作

* 将生成的config文件放入.kube目录中

        cp config ~/.kube

* 查看所有的可使用的kubernetes集群角色

        kubectl config get-contexts

* 更多关于kubernetes配置文件操作

        kubectl config --help

* 切换kubernetes配置

        kubectl config use-context {your-contexts}
