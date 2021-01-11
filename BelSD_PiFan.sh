#! /bin/sh

### BEGIN INIT INFO
# Provides:          pifan.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting BelSD PiFan Control"
    /usr/local/bin/BelSD_pifan.py &
    ;;
  stop)
    echo "Stopping BelSD PiFan Control"
    pkill -f /usr/local/bin/BelSD_pifan.py
    ;;
  restart)
    echo "Stopping BelSD PiFan Control"
    pkill -f /usr/local/bin/BelSD_pifan.py
    echo "Restarting BelSD PiFan Control"
    /usr/local/bin/BelSD_pifan.py &
    ;;
  *)
    echo "Usage: /etc/init.d/BelSD_PiFan.sh {start|stop|restart}"
    exit 1
    ;;
esac

exit 0