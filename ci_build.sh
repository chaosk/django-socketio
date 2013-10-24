#!/bin/bash
#ci_build.sh
#sets up example_project, and runs tests
#returns 0 if all is well, 1 if unittests failed, 2 if bddtests failed, 3 if all failed
#
##################################################################################################
#
# Django-socketio testsuite script
# Runs using ./manage.py test and py.test afterwards
#
# This can take quite a while to execute, so prepare for that :D
# You need to manually install system-wide requirements, as python-pip and virtualenv.
#
##################################################################################################

# set pythonpath and settings
export PYTHONPATH=`pwd`:`pwd`/django_socketio/example_project/
export DJANGO_SETTINGS_MODULE=django_socketio.example_project.settings
rm dev.db

#run unittests
python django_socketio/example_project/manage.py test
TEST_EXIT_CODE=$?

echo "Creating bddtests database"
python django_socketio/example_project/manage.py syncdb --noinput > /dev/null 2>&1

#start our server in the background
python django_socketio/example_project/manage.py runserver_socketio > /dev/null 2>&1 &
SERVER_PID=$!
# wait for server to properly start
sleep 5

#now actually run some tests!
cd tests
py.test $@
BDD_EXIT_CODE=$?

echo "Killing runserver with pid $SERVER_PID"
kill -9 $SERVER_PID

# Return exit code of test process so travis knows when we've failed.
if [[ $TEST_EXIT_CODE != 0 && $BDD_EXIT_CODE != 0 ]]; then
    exit 3;
elif [[ $TEST_EXIT_CODE != 0 ]]; then
    exit 1;
elif [[ $BDD_EXIT_CODE != 0 ]]; then
    exit 2;
else
    exit 0;
fi
