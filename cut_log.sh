#!/bin/bash
date_d=`/bin/date +%Y-%m-%d`
for i in `cat /opt/myshell/cut_log/config.txt`
do
  days=`echo $i | awk -F '&' '{print $2}'`
  log_path=`echo $i | awk -F '&' '{print $1}'`
  #name=${log_path##*/}-${date_d}
  #save_path=${log_path%/*}
  file_name=`basename ${log_path}`
  name=`basename ${log_path}-${date_d}`
  save_path=`dirname ${log_path}`
###############variable#######################
  [ ! -f $log_path ] && exit 1
  cd $save_path
  /usr/bin/split -b 2048m $file_name "$file_name-pack"
  tar zcvf $name.tar.gz ${file_name}-pack*
  rm -fr ${file_name}-pack*
  cat /dev/null > $log_path
  find $save_path/ -type f -name "${file_name}*.tar.gz" -mtime +${days} -exec rm -fr {} \;
  sleep 2
done
