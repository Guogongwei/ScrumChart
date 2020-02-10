# 

a tool for draw burn down chart


# 
## mac安装环境
* brew install python@2
* cd 至相应的项目目录
* pip install -r Requirements.txt
（如果没有pip则安装）
* python run.py 
* 修改 config.py
```
根据自己的mysql账号密码和数据库
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/scrum'
```
* 访问http://127.0.0.1:5000/查看是否可运行
