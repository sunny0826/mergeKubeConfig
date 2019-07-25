# 合并kubeconfig文件

__该项目已由 golang 重写，后续 python 版本将不再更新__，新项目地址：https://github.com/sunny0826/kubecm

## 适用环境

* 需要在终端使用命令行管理多集群
* kubernetes集群中安装了istio，需要使用```istioctl```命令，但是集群节点并没有安装```istioctl```，需要在本地终端操作
* 不愿频繁编辑 ```.kube``` 目录中的config文件的同学

## 注意事项
* 使用本脚本合并前，请先备份您您的配置文件，以免发生意外
* 使用增量添加时，默认新增文件在```merge.py```同级目录，使用相对路径

## 准备工作

* Python环境：2.7或者3均可
* 需要依赖包：```PyYAML```

## 快速使用

* 安装依赖：

        pip install PyYAML
        
* 运行脚本

    * 默认运行方式，kubeconfig文件放入```configfile```文件,注意删掉作为示例的两个文件
    
            python merge.py
            
    * 自定义kubeconfig文件目录
    
            python merge.py -d {custom-dir}
            
    * 向已合并的配置文件中增加新的配置，这里默认新增文件在```merge.py```同级目录，使用相对路径
    
            python merge.py -a addfilename -t tofilename
            
## 运行后操作

* 将生成的config文件放入.kube目录中

        cp config ~/.kube

* 查看所有的可使用的kubernetes集群角色

        kubectl config get-contexts

* 更多关于kubernetes配置文件操作

        kubectl config --help

* 切换kubernetes配置

        kubectl config use-context {your-contexts}
  
## 2019-04-28 更新内容
新增增量合并，在已使用本脚本合并后的 kubeconfig 后，可以使用 ```-a addfilename -t tofilename``` 参数将新的配置合并到原来已经合并好的文件中

        
## 问题反馈

* 直接提 issue
* 个人博客 https://blog.maoxianplay.com 上面有联系方式
* 邮箱： sunnydog0826@gmail.com

## 代码许可

MIT许可证，参见LICENSE文件。