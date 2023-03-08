#! /bin/sh

### BEGIN INIT INFO
# Provides:          pi-keyboard-api
# Required-Start:
# Required-Stop:
# Should-Stop:
# Default-Start:     3 5
# Default-Stop:
# Short-Description: Start FastAPI pi-keyboard-api.
### END INIT INFO

case "$1" in
 start)
 WEB_CONCURRENCY=1 uvicorn --host 0.0.0.0 --port 80 --app-dir /opt/pi-keyboard-api/ app.main:app
 ;;
esac

exit 0