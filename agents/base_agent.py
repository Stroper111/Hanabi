class BaseAgent:
    def __init__(self):
        pass

    def act(self, obs, action_space):
        raise NotImplementedError

    def episode_end(self, reward):
        """
        This is called at the end of the episode to let the agent know that
        the episode has ended and what is the reward.

        :param reward: int
            The single reward scalar to this agent.
        """
        pass

    def init_agent(self, id_, game_type):
        pass

    def shutdown(self):
        pass
