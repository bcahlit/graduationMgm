#!/usr/bin/env python
# encoding: utf-8

# Before running this program, first Start HFO server:
# $> ./bin/HFO --offense-agents 1

import itertools
from hfo import *

def main():
  # Create the HFO Environment
  hfo = HFOEnvironment()
  # Connect to the server with the specified
  # feature set. See feature sets in hfo.py/hfo.hpp.
  hfo.connectToServer(LOW_LEVEL_FEATURE_SET,
                      'bin/teams/base/config/formations-dt', 6000,
                      'localhost', 'base_right', True, "./log")
  for episode in itertools.count():
    status = IN_GAME
    i = 1
    while status == IN_GAME:
      # Grab the state features from the environment
      features = hfo.getState()
      # Take an action and get the current game status
      hfo.act(TURN, i%90)
      print(TURN)
      # Advance the environment and get the game status
      status = hfo.step()
      i+=1
    # Check the outcome of the episode
    print(('Episode %d ended with %s'%(episode, hfo.statusToString(status))))
    # Quit if the server goes down
    if status == SERVER_DOWN:
      hfo.act(QUIT)
      exit()

if __name__ == '__main__':
  main()
