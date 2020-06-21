cd sta#!/bin/bash

ps -ef | grep uwsgi9021 | grep -v grep | awk '{print $2}' | xargs kill -9;
svn update /home/ops-em/nnems/backend/;
source /home/ops-em/.venv/bin/activate;
/home/ops-em/.venv/bin/uwsgi --ini /home/ops-em/nnems/backend/uwsgi/uwsgi9021_test.ini;
tail -f /home/ops-em/nnems/backend/uwsgi/nnems.log;