# mac下安装postgresql@9.6

1. brew install postgresql@9.6

2. 按照install结果将postgresql相关目录放在环境变量，启动postgresql，启动命令为

   ```bash
   pg_ctl -D /Users/wsj/data/psql  -l /Users/wsj/log/postgre/server.log start
   ```

   如果已经指定了环境变量PGDATA，则可以省略-D参数

3. 启动成功后在终端输入psql，会显示没有wsj这个database，psql默认是使用postgres这个用户去访问的，如果再linux下，psql安装完成之后会自动创建postgres用户，但是mac的系统保护无法创建，所以我们有两种解决办法

   1. 手动创建postgres用户
   2. 创建wsj（本机用户）的database

   我这里选择第二种,指定data路径

   ```
   export PGDATA="/Users/wsj/data/psql"  
   ```
   
   将目录格式化
   
   ```
   initdb
   ```
   
   启动postgresql
   
   ```bash
   pg_ctl -D /Users/wsj/data/psql  -l /Users/wsj/log/postgre/server.log start
   ```
   
   创建database
   
   ```bash
   createdb wsj -W python123 -E UTF8 -e
   ```
   
   现在执行psql，就可以进去

