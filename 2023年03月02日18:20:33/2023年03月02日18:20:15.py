# # -*- coding: utf-8 -*-
# # @Time    : 2023/3/2 6:20 PM
# # @Author  : junbo.zhao
# # @File    : 2023年03月02日18:20:15.py
# Docker + Jenkins + Gitlab + Pytest + Allure 接口自动化测试之持续集成

# 安装docker：https://www.cnblogs.com/poloyy/p/13921450.html
# 下载jenkins镜像
# docker search jenkins
# 第一个是官方的镜像，但是版本很旧，不推荐
# 第二个镜像虽然不是官方的，但是 jenkins 的版本会跟随 jenkins官方的版本，也就是说会保持拉下来的镜像的 jenkins 版本是最新的，推荐，我也用这个
# 第三个镜像是中文 jenkins 镜像， 但是镜像的系统不是我们所熟悉的 centos、ubuntu、Debian 等，而是 Alpine，安装依赖库的方式也不常见，不推荐
# docker pull jenkins/jenkins
# docker images
# 创建jenkins容器：
# 创建目录用于挂载目录
# mkdir -p /var/jenkins_node
# 给它最高权限
# chmod -R 777 /var/jenkins_node
# 创建启动jenkins
# -d：守护模式
# -uroot：使用 root 身份进入容器，推荐加上，避免容器内执行某些命令时报权限错误
# -p：主机 80 端口映射容器的 8080 端口，后面访问 jenkins 直接访问主机 ip 就行了，不需要加 8080 端口
# -v：目录映射
# --name：自定义一个容器名称
# docker run -d -uroot -p 80:8080 --name jenkins1 -v /var/jenkins_node:/var/jenkins_home jenkins/jenkins
# docker ps
# 进入容器
# docker exec -it -uroot jenkins1 bash
# 先安装一些需要的包
# apt-get update # 获取最新的软件包
# apt-get upgrade # 升级已安装的软件包
# apt-get -y install gcc automake autoconf libtool make
# apt-get -y install make*
# apt-get -y install zlib*
# apt-get -y install openssl libssl-dev
# apt-get install sudo
# 报错不用管，继续
# 安装python
# cd /var/jenkins_home # 进入jenkins的安装目录
# mkdir python3   # 新建一个python3目录
# cd python3
# wget https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
# tar -zxvf Python-3.8.6.tgz
# mv Python-3.8.6 py3.8
# cd py3.8
# 先配置下环境变量
#  vim /etc/profile(注意：如果没有vim命令，使用apt-get -y install vim* 安装)
#  在最后一行加上如下命令
#  #Python3.8
# export PYTHON_HOME=/var/jenkins_home/python3
# export PATH=$PATH:$PYTHON_HOME/bin
# source /etc/profile
# 进入到py3.8,即在路径 /var/jenkins_home/python3/py3.8下执行python3 的安装
# ./configure --prefix=/var/jenkins_home/python3  --with-ssl # 指定安装的目录
# make   # 编译
# make install  # 安装
# 添加软链
# 　ln -s /var/jenkins_home/python3/bin/python3.8  /usr/bin/python3
# 　ln -s /var/jenkins_home/python3/bin/pip3 /usr/bin/pip3