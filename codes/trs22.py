import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
print(f'Action Space:{env.action_space}')
print(f'Observation Space:{env.observation_space}')
episodes=10
observation, info = env.reset(seed=42)
for i in range(episodes):
    state=env.reset()
    reward_sum=0
    while True:
        env.render()
        action = 1 if observation[2]>0 else 0
        observation, reward, terminated, truncated, info = env.step(action)
        reward_sum+=reward
        if terminated or truncated:
            print(f'episode{i} reward {reward_sum}')
            observation, info = env.reset()
            break
    
      # this is where you would insert your policy
    

    

env.close()     

