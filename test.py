# coding=utf-8

import time
from tqdm import tqdm

def t():
  for i in tqdm(range(10)):
    time.sleep(0.1)
  return 'ok'
