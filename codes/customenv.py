import gymnasium as gym
import sys
from math import ceil
from random import random,randint

import collections
class catchcoinsenv(gym.Env):
    metadata={"render.modes":["ascii"]}

def __init__(self,display_width=10,display_height=10,density=0.8):
    self.display_width=display_width
    self.display_height=display_height
    self.density=density
    self.display=collections.deque(maxlen=display_height)
    self.last_action=None
    self.last_reward=None
    self.total_score=0
    self.v_position=0
    self.game_scr=None
    
def line_generator(self):
    line=[0]*self.display_width
    if random()>(1-self.density):
        r=random()
        if r<.6:
            v=1
        elif r<.9:
            v=2
        else:
            v=3
        line[randint(0,self.display_width-1)]=v
    return line


def step(self,action):
    self.last_action=action
    self.v_position=min(max(self.v_position+action,0),self.display_width-1)
    reward=self.display[0][self.v_position]
    self.last_reward=reward
    self.total_score+=reward
    self.display.append(self.line_generator())
    state=self.display,self.v_position
    done=False
    info={}
    return state,reward,done,info


def reset(self):
    for _ in range(self.display_height):
        self.display.append(self.line_generator())
        self.v_position=ceil(self.display_width/2)
        state=self.display,self.v_position
        return state
    


def render(self,mode="ascii"):
    if mode=="ascii":
        self._render_ascii()
    else:
        raise Exception('Not Implemented')
def _render_ascii(self):
    outfile=sys.stdout
    area=[]
    for i in range(self.display_height):
        line=self.display[self.display_height-1-i]


