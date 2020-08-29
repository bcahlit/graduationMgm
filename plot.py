#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
from matplotlib import pyplot as plt


def plot(name, frame_idx, rewards):
    plt.title('frame %s. %s: %s' % (frame_idx, name, rewards[-1]))
    plt.plot(rewards)
    plt.savefig("%s.png" % (name))
    plt.close()


def main(filename):
    weight = 100
    endtrial_re = re.compile(r'EndOfTrial:\s(\d+)\s\/\s(\d+)\s\d+')
    goal_list = []
    _file = open(filename)
    endindex = 0
    while 1:
        line = _file.readline()
        if not line:
            break
        end_m = endtrial_re.match(line)
        if end_m:
            goal_list.append(int(end_m.group(1)))
            endindex = end_m.group(2)
    _file.close()
    #  print(goal_list)
    goal_rate = []
    for i in range(weight, len(goal_list), weight):
        # 进球数/周期数
        goal_rate.append((goal_list[i-1] - goal_list[i-weight])/weight)
    #  print(goal_rate)
    plot(filename[:-4], endindex, goal_rate)


if __name__ == "__main__":
    main(filename=sys.argv[1])
