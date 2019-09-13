from base_agent import Agent as DQNAgent
from base_agent_ddpg import DDPGAgent
from graduationmgm.Neural_Networks.DQN import Model as DQN
from graduationmgm.Neural_Networks.Dueling_DQN import Model as DuelingDQN
from graduationmgm.Neural_Networks.DDPG import Model as DDPG


def main():
    agent = DQNAgent(DuelingDQN, True)
    # agent = DDPGAgent(DDPG, True)
    try:
        agent.run()
    except KeyboardInterrupt:
        agent.bye()


if __name__ == "__main__":
    main()