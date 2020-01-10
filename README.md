#

a tool for draw burn down chart


#mac安装环境
brew install python@2
cd 至相应的项目目录
pip install -r Requirements.txt
（如果没有pip则安装）
python run.py 
访问http://127.0.0.1:5000/查看是否可运行
tip：如果报错，ImportError: No module named MySQLdb
     运行pip install pymysql 
     修改/scrum_chart/_init_.py加上
        import pymysql
        pymysql.install_as_MySQLdb()
     再次访问http://127.0.0.1:5000/