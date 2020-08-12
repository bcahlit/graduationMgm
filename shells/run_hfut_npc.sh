#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $DIR
export PYTHONPATH=$PYTHONPATH:$DIR/..
HFO_mgm/bin/HFO --fullstate --no-logging --headless --defense-agents=0 --offense-agents=0 --defense-npcs=1 --offense-npcs=1 --offense-team=helios --defense-team=hfut --trials 100 &

# Sleep is needed to make sure doesn't get connected too soon, as unum 1 (goalie)
sleep 5
echo "python agent"
python ./agents/agent.py helios&
sleep 1

trap "kill -TERM -$$" SIGINT
wait
