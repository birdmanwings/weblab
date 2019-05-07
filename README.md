# weblab
计网的实验，计算机网络自顶向下实验   
```
git clone https://github.com/birdmanwings/weblab.git
```
## Lab1  
socket套接字编程，支持多线程避免服务挂掉    
```
$ pipenv shell (进入虚拟环境)    
$ python lab1.py 2333 （监听本地2333端口）   
```
访问127.0.0.1:2333   
结果如图
![image](https://github.com/birdmanwings/picture/raw/master/images/1.png)
![image](https://github.com/birdmanwings/picture/raw/master/images/2.png)
## Lab2
```
$ pipenv shell
$ python lab2_server.py (启动服务端程序)
$ python lab2_client.py (启动客户端程序，发送报文) 
```
结果如图
![image](https://github.com/birdmanwings/picture/raw/master/images/3.png)
![image](https://github.com/birdmanwings/picture/raw/master/images/4.png)  
## Lab3
smtp发送邮件，使用qq邮箱，首先获取qq邮箱smtp授权码填入相应位置 
```
$ pipenv shell
$ python lab3.py
```
结果如图
![image](https://github.com/birdmanwings/picture/raw/master/images/5.png)
![image](https://github.com/birdmanwings/picture/raw/master/images/6.jpg)
