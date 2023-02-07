# 项目简介

本项目为山东大学2021届数据科学与人工智能实验班学期作业项目

本项目使用HTML5程序完成用户注册、登录、修改密码界面及对应功能，在登陆后的对话界面接入百度paddlepaddle/百度大脑unit所训练的问答机器人，可以回答关于山东大学威海校区的校园基本问题

## 项目架构

### 一 项目技术栈

① 前端：

HTML/CSS --- 前端页面设计

JS - axios --- 与后端完成消息传输

② 后端：

Python(Flask) --- 响应前端请求

③ 数据库：

mysql/sqlserver --- 数据存放与查询

④ 百度unit API接口调用

### 二 项目目录结构

> 项目根据使用的数据库不同，具有mysql与sqlserver两个版本，见文件夹命名称

**目录结构如下：**

​	|--static  （HTML页面设计所需静态文件）

​		|--css

​		|--js

​	|--templates  （渲染的HTML页面）

​	|--app.py  （后端flask回调主程序）

​	|--answer.py  （百度API调用封装）

​    |--requirements.txt   （需要安装的依赖）

### 三 参数调整

> 项目直接调用时需要更改的所有信息参数

① 将 answer.py 中 client_id、client_secret、service_id 改成您的百度大脑问答机器人对应的API和服务编号

② 若使用mysql版，将DB.py 中的数据库库名、表名、登陆账号及密码参数改为您自己参数

​	 若使用sqlserver版，将 app.py 回调函数中数据库库名、表名、登陆账号及密码参数改为您自己的参数

③ 将 index.html、find.html、talk.html 中本地测试的IP 127.0.0.1 全部更改为您的服务器域名或IP

## 服务器部署帮助

### 一 创建实例

购买云服务器，采用CentOS7操作系统

登录到阿里云控制台

> https://ecs.console.aliyun.com/home?spm=5176.12818093.ProductAndResource--ali--widget-product-recent.dre0.3be916d0gC5VLn#/

> 教程：https://help.aliyun.com/document_detail/163467.html

<img src="C:\Users\liufangfei\AppData\Roaming\Typora\typora-user-images\image-20221201105803319.png" alt="image-20221201105803319" style="zoom:67%;" />

#### 1 设置安全组

#### 2 解析域名

> 云解析DNS：
>
> https://dns.console.aliyun.com/?spm=5176.12818093.top-nav.22.3be916d0gC5VLn#/dns/domainList

#### 3 申领SSL证书

> SSL 证书就是遵守SSL协议，由受信任的数字证书颁发机构CA在验证服务器身份后颁发的数字证书，具有服务器身份验证和数据传输加密功能。
>
> SSL证书通过在客户端浏览器和Web服务器之间建立一条SSL安全通道（SSL安全协议主要用来提供对用户和服务器的认证；对传送的数据进行加密和隐藏；确保数据在传送中不被改变即确保数据的完整性，现已成为该领域中全球化的标准）

> 数字证书管理服务：
>
> https://yundun.console.aliyun.com/?spm=5176.7968328.J_8413632810.1.4c4065c3yn4ZDh&p=cas&showBuy=1#/certExtend/free

#### 4 其他调试功能

##### ① 更改登录密码

##### ② VNC远程连接

> VNC：远程控制工具
>
> RFB：VNC工具所使用的远程连接协议，倾向于传输图像

##### ③ 创建快照

### 二 SSH远程连接

远程连接：

① 软件：Xshell

② 协议：SSH

> Linux下广泛使用OpenSSH程序来实现SSH协议，同时支持SSH1和SSH2协议
>
> Openssh软件包包括两部分：openssh-server和openssh-client

------------------

> XShell/Xftp下载地址：https://www.xshell.com
>
> XShell新建会话：https://blog.csdn.net/weixin_43533164/article/details/124718302

使用公网ip和root登录密码远程连接

> XShell警告⚠：
>
> WARNING! The remote SSH server rejected X11 forwarding request
>
> > 不影响实际使用
>
> 解决方法：https://blog.csdn.net/SoloVersion/article/details/123814568?spm=1001.2014.3001.5501

> 断连调试：
>
> ① 无法连接服务器：
>
> > https://blog.csdn.net/qq_21782255/article/details/84633623/
>
> 阿里云控制台VNC远程连接实例
>
> ```
> // 查看ssh服务状态
> service sshd status
> // 检查
> // 提示服务无法加载ssh_host_rsa_key,ssh_host_ecdsa_key 推测是权限问题
> sshd -t
> // 更新权限
> chmod 600 /etc/ssh/ssh_host_rsa_key
> chmod 600 /etc/ssh/ssh_host_ecdsa_key
> // 重启ssh服务
> service sshd restart
> ```
>
> 重启后采用XShell连接
>
> ② 连接后自动中断
>
> 情况一：静态ip冲突 → 别连校园网就行了...
>
> 情况二：ClientAliveCountMax
>
> > https://blog.csdn.net/qq_44039494/article/details/125832328

### 三 服务器端配置

> 有

> https://blog.csdn.net/weixin_45745641/article/details/119223601

```bash
// 实时查看日志
tail -f 文件名
// control+c 退出实时查看
```

#### 1 搭建Nginx服务器

##### ① 下载安装包及环境依赖

> nginx不仅支持 http协议，还支持 https（即在 ssl 协议上传输 http），如果使用了 https，需要安装 OpenSSL 库

```bash
// 进入安装目录
cd /usr/local

// nginx安装包下载+解压
wget -c https://nginx.org/download/nginx-1.14.0.tar.gz
tar -zxvf nginx-1.14.0.tar.gz

// 依赖
yum install -y pcre pcre-devel
yum install -y zlib zlib-devel
yum install gcc-c++
// ssl模块
yum install -y openssl openssl-devel
```

##### ② 配置与编译安装

>然后需要进行配置，一般使用默认配置，即输入./configure
>**如果需要使用https支持，则需要加上SSL模块**

```bash
// 进入解压后的文件夹
cd nginx-1.14.0

// 配置
./configure --with-http_ssl_module

// 编译安装
make
make install
```

##### ③ 启动nginx

```bash
cd usr/local/nginx/sbin
./nginx

// 查看进程
ps aux|grep nginx

// 启动/关闭/重启均需在/usr/local/nginx/sbin目录下执行
./nginx
./nginx -s stop
./nginx -s reload
```

##### ④ ssl证书文件

**验证配置文件**

```bash
// 查看配置文件路径
nginx -t
// 在nginx文件夹下存放证书
mkdir /usr/local/nginx/cert
// 上传证书文件到文件夹（可用Xftp可视化操作）
```

> Command not found 解决方案：
>
> ```bash
> // 查看nginx使用路径，将含sbin的路径添加到/usr/bin
> find / -name nginx
> ln -s /winning/winmid/nginx/sbin/nginx /usr/bin
> ```

#####⑤ 修改conf文件

> https://blog.csdn.net/m0_59092234/article/details/125398461

> 在conf中注释需要去掉或改为#

```
server {
    listen 443 ssl;
    server_name your-domain.com; // 你的域名
    root /opt/WebWork/html; // 前台文件存放文件夹，一般使用 Nginx 初始化的文件夹，当然也可以自己修改
    index index.html;// 上面配置的文件夹里面的index.html
    ssl_certificate  /usr/local/nginx/cert/chichibomm.com.pem;// 改成你的证书的名字
    ssl_certificate_key /usr/local/nginx/cert/chichibomm.com.key;// 你的证书的名字
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    location / {
    	// 将Web请求转发到uwsgi运行的5000端口
        proxy_pass http://127.0.0.1:5000;
    }
}
server {
    listen 80;
    server_name your-domain.com;// 你的域名
    rewrite ^(.*)$ https://$host:443$1 permanent;// 把http的域名请求转成https且转发到443端口
}
```

```
// listen 80端口的请求时添加行
rewrite ^(.*)$ https://$host:443$1 permanent;
include ...(路径)/nginx/default.d/*.conf
```

#### 2 安装Python编译器

> https://blog.csdn.net/weixin_45745641/article/details/119617866?spm=1001.2014.3001.5506

##### ① 创建python目录

```
which python
mkdir /usr/local/python3 
cd /usr/local/python3
```

##### ② 安装python及依赖

```bash
// 安装依赖
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

// 安装python
wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz

// 解压编译安装
tar -xvJf  Python-3.7.1.tar.xz
cd Python-3.7.1
./configure --prefix=/usr/local/python3
make && make install
```

##### ③ 将python添加到环境变量

```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

#### 3 配置conda虚拟环境

##### ① 安装conda及配置镜像

> https://www.jianshu.com/p/2f5cf2edaaef

##### ②创建虚拟环境

```
conda create --name 环境名 --python=3.7 flask
```

##### ③ 在虚拟环境中安装依赖包

```bash
conda activate 环境名
pip install os
pip install flask
pip install flask_cors
pip install pymssql
```

##### ③ 在虚拟环境中运行flask

```bash
conda activate 环境名
python3 项目名
// ctrl+c 停止运行
conda deactivate
```

#### 4 搭建uWSGI服务器

##### ① 安装 uwsgi

> pip安装uwsgi会自动调用centos自带的python2.7.5版本 → 改用uwsgi压缩包安装
>
> > https://www.cnblogs.com/zoujl/p/11011041.html

```
// 切换到项目文件夹
cd /opt/WebWork
// 下载压缩包
wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
tar zxvf uwsgi-latest.tar.gz
// 切入uwsgi安装文件
cd uwsgi-2.0.20/
// 编译
python3 uwsgiconfig.py --build
// 安装
python3 setup.py install
// 添入环境变量
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
```

##### ② 配置 uwsgi

> 开conda虚拟环境 --- 重启uwsgi

```
// 进入项目文件夹
cd /opt/WebWork
// 新建uwsgi.ini配置文件（用Xftp可视化操作）
```

```
// .ini配置文件内容，注意部署时将注释删去或改为#
[uwsgi]
http-socket = 127.0.0.1:5000  // 启动地址
chdir = /opt/WebWork // 项目地址
wsgi-file = app.py  // 项目的启动文件
callable = app
processes = 2
threads = 10
buffer-size = 32768
master = true
daemonize=flaskweb.log  // 日志文件保存在falskweb.log中
pidfile=uwsgi.pid
```

```
// 项目根目录下启动uwsgi
uwsgi --ini uwsgi.ini      // 启动
uwsgi --reload uwsgi.pid   // 重启
```
