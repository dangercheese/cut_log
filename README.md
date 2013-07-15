cut_log
=======
#汉语注释：
#本脚本作为切割日志脚本，可以定时清除掉多余备份，解决日志不断增加对磁盘的占用问题。
log_path.xml #为切割日志配置文件\n
<path>/var/log/cron-20130630</path>  #为需要备份的日志 \n
<save>/home/test/</save> #切割后日志保存到的路径\n
<name>cron_log</name>  #切割后日志保存的名称\n
<days>5</days>  # 保留切割日志的天数\n

使用方法：\n
1、填写好log_path.xml 里面配置\n
2、如果需要切割多个Log只需复制 <log> .. </log>  填写新的配置\n
3、建议清空掉现有需要切割的Log，因为第一次运行脚本会比较占用资源。\n
4、把cut_log.py 放到crontab 里面定时执行，因crontab 里面需要绝对路径\n
所以需要修改 cut_log.py 里面  dom = minidom.parse('./log_path.xml') 的 log_path.xml 为绝对路径。\n
