from gym.envs.registration import register

register(
    id='futures-exchange-v0',
    entry_point='gym_futures_exchange.envs:FuturesExchangeEnv',
)