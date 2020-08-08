# Comparing DQN, Dueling Double DQN and Deep Deterministic Policy Gradient applied to Robocup Soccer Simulation 2D

ddpg and dqn can't run well. you can run that to back old version.
```shell
git reset 721c1f8f539d1e014a0be3ffeb26132734f7c6a4
```
This work is designed to help RoboCIn team.
Inside you'll find codes comparing each technique.

For 3000 test episodes:

 - Helios2013 vs Helios2013 -> 77,5% defenses of Helios2013
 - RoboCIn2019 vs Helios2013 -> 77.4% defenses of Helios2013
 - Helios2013 vs RoboCIn2019 -> 71% defenses of RoboCIn2019
 - RoboCIn2019 vs RoboCIn2019 -> 53.3% defenses of RoboCIn2019

100k training dqn:
 - With Helios2013 goalie:
    - 52.2% defenses against Helios2013
    - 74% defenses against RoboCIn2019

 - With RoboCIn2019 goalie:
    - 51.3% defenses against Helios2013
    - 80% defenses against RoboCIn2019

100k training ddqn:
 - With Helios2013 goalie:
    - 55% defenses against Helios2013
    - 70.3% defenses against RoboCIn2019

 - With RoboCIn2019 goalie:
    - 49.3% defenses against Helios2013
    - 57.1% defenses against RoboCIn2019

100k training ddpg:
 - With Helios2013 goalie:
    - 30.2% defenses against Helios2013
    - 65.8% defenses against RoboCIn2019

 - With RoboCIn2019 goalie:
    - 10.2% defenses against Helios2013
    - 35.7% defenses against RoboCIn2019
