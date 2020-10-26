#1- Backup current user home directory.
#2- Create a daily differential backup.
#3- Create a weekly full backup.
#4- Upload each backup compressed and encrypted to an S3 bucket.
#5- Create a restore task in a different directory taking the last full backup.
#6- Maintain last month of backups.
#7- Generate a log file with the name of the files backed up including the date, name and size plus md5 hash.

#!bin/bash

USER="$(whoami)"
HOME="/home/$USER"
BACKUP_DIR="/backup"
DAILY_DIR="/backup/daily"
FULL_DIR="/backup/full"
RESTORE_DIR="/backup/restore"
DATE=$(date +%Y-%m-%d--%H:%M:%S)
DAY=$(date +%Y-%m-%d)
LOG_FILE="backup.log"
LOG="$BACKUP_DIR/$LOG_FILE"

if [ ! -d $BACKUP_DIR ] ; then
  mkdir $BACKUP_DIR
fi
if [ ! -d $DAYLI_DIR ] ; then
  mkdir $DAILY_DIR
fi
if [ ! -d $FULL_DIR ] ; then
  mkdir $FULL_DIR
fi
if [ ! -d $RESTORE_DIR ] ; then
  mkdir $RESTORE_DIR
fi
if [ ! -f $LOG ]; then
    touch $LOG
fi


function usage { echo  "Usage: $0 [-j <Job Type: full-backup; incremental-backup; restore; list backups>" 1>&2; exit 1; }

while getopts :j:h: option
do
 case "${option}"
 in
 j) JOB_TYPE=${OPTARG};;
 h) usage ;;
 *) usage ;;
 esac
done

if [ -z "${JOB_TYPE}" ] ; then
    usage
fi
function cleanup {
aws s3 ls s3://s3-bucket | while read -r line;
  do
    createDate=`echo $line|awk {'print $1" "$2'}`
    createDate=`date -d"$createDate" +%s`
    olderThan=`date -d -30 days +%s`
    if [[ $createDate -lt $olderThan ]]
      then
        fileName=`echo $line|awk {'print $4'}`
        echo $fileName
        if [[ $fileName != "" ]]
          then
            aws s3 del "$fileName"
        fi
    fi
  done;
}

if [["${JOB_TYPE}" == "full-backup" ]] ; then
  echo "Starting Full backup at $DATE" >> $LOG
  FILE="FULL-$USER-$DATE.tar.gz"
  tar czvf $FULL_DIR/$FILE $HOME
  aws s3 cp --sse $FULL_DIR/$FILE s3://s3-bucket/
  SIZE="$(du -hs $FULL_DIR/$FILE | awk '{print $1}')"
  MD5="$(md5 $FULL_DIR/$FILE | awk '{print $4}')"
  echo "Full backup finished $DATE" >> $LOG
  echo "Date created: $DATE"
  echo "File name: $FILE"
  echo "File Size: $SIZE"
  echo "MD5 Hash: $MD5"
  echo "----------------------------------------------"
fi

if [["${JOB_TYPE}" == "incremental-backup" ]] ; then
  echo "Starting Incremental Backup at $DATE" >> $LOG
  rsync -arvz $HOME/ $DAILY_DIR/
  FILE="INC-$USER-$DATE.tar.gz"
  tar czvf $DAILY_DIR/$FILE $DAILY_DIR/
  aws s3 cp --sse $DAILY_DIR/$FILE s3://s3-bucket/
  SIZE="$(du -hs $DAILY_DIR/$FILE | awk '{print $1}')"
  MD5="$(md5 $DAILY_DIR/$FILE | awk '{print $4}')"
  echo "Incremental backup for $DAY finished" >> $LOG
  echo "Date created: $DATE"
  echo "File name: $FILE"
  echo "File Size: $SIZE"
  echo "MD5 Hash: $MD5"
  echo "----------------------------------------------"
fi

if [["${JOB_TYPE}" == "restore" ]] ; then
  echo "Starting restore process of latest backup $DATE" >> $LOG
  LATEST_FULL="$(aws s3 ls s3://s3-bucket --recursive | sort | grep FULL-* | tail -n 1 | awk '{print $4}')"
  aws s3 cp --sse s3://s3-backup/$LATEST_FULL $RESTORE_DIR/
  cd $RESTORE_DIR/
  tar xvzf $RESTORE_DIR/$LATEST_FULL
  echo "Restore complete" >> $LOG
fi

cleanup

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Vairiables globales

LOG=/var/log/backup.log
USER=`(whoiam)`
HOME=/home/$USER
BACKUPDIR=/tmp/backup/$USER
BACKUPRESTORE=/tmp/backuprestore/$USER
DATE=`date +%F`

# Check if home exist
if [ ! -d $HOME ]; then
        echo '[ERROR] Directory HOME doesn't exist :(' >> $LOG
        exit
fi

# Make a directory if it doesn't exist
echo '[INFO] Make a directory if it doesn't exist' >> $LOG
mkdir -p BACKUPDIR

# Parameters
case $1 in

  "daily")
  echo '[INFO] Make a incremental backup' >> $LOG
  tar -cvpz -f $BACKUPDIR/daily/backup$DATE -g snapshot
  ;;

  "weekly")
  echo '[INFO] Make a full backup' >> $LOG
  tar -cvpz -f $BACKUPDIR/weekly/backup$DATE $HOME
  ;;

  "monthly")
  echo '[INFO] Make a full backup' >> $LOG
  tar -cvpz -f $BACKUPDIR/monthly/backup$DATE $HOME
  ;;

  "restore")
  echo '[INFO] Make a restore task in a different directory'
  tar -cvpx -f $BACKUPRESTORE/backup $(ls -tC  | sed "1q;d") 
  ;;
 
  *)
  echo '[ERROR] Invaleid parameter $1 >> LOG
  ;;
esac