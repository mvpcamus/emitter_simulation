# Copyright Jun Jo, May. 28. 2018. Allright reserved.
# KIST Europe http://www.kist-europe.de
# Contact Email: j.jo@kist-europe.de

import sys
import math
import random

# ASSUMPTION
# - emitters are evenly distributed at vertices of equilateral triangles
# - the equilateral triangles have edge length step_x

class Emitter(object):
  def __init__(self, x, y, z, act_rate):
    self.x = x
    self.y = y
    self.z = z
    active = random.random()
    if active > act_rate:
      self.status = 0
    else:
      self.status = 1

  def react(self, x, y, z, effect_d, radius):
    d = math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2)
    if d > effect_d:
      pass
    elif d <= radius:
      return -1
    else:
      self.status = 0
    return self.status


def makeEmitterGrid(width, layer, step_x, step_y, step_z, act_rate):
  points = []
  for z in range(layer):
    for y in range(width):
      for x in range(width):
        if y % 2:
          points.append(Emitter((x*step_x)+(step_x/2), y*step_y, z*step_z, act_rate))
        else:
          points.append(Emitter(x*step_x, y*step_y, z*step_z, act_rate))
  return points


def countActive(x, y, z, emitters, effect_d = 0, radius = 1.0):
  count = 0
  for e in emitters:
    result = e.react(x, y, z, effect_d, radius)
    if result == -1:
      return -1
    else:
      count += result
  return count


if __name__ == "__main__":
  # WIDTH: emitter grid width (ex. WIDTH=100 for 100 x 100 grid)
  # LAYER: number of emitter grid layers
  # RADIUS: emitter radius
  # EFFECT_D: the effective distance of a quencher
  # STEP_X: edge length of the equilateral triangle
  # STEP_Y: height of the equilateral triangle
  # STEP_Z: distance between emitter grid layers
  # ACT_RATE: initial emitter activation ratio in grid layers
  # NUM_Q: maximum number of quencher

  if len(sys.argv) == 9:
    WIDTH = int(sys.argv[1])
    LAYER = int(sys.argv[2])
    RADIUS = float(sys.argv[3])
    EFFECT_D = float(sys.argv[4])
    STEP_X = float(sys.argv[5])
    STEP_Z = float(sys.argv[6])
    ACT_RATE = float(sys.argv[7])/100.0
    NUM_Q = int(sys.argv[8])
  else:
    WIDTH = 50
    LAYER = 3
    RADIUS = 1.0
    EFFECT_D = 15.0
    STEP_X = 6.1
    STEP_Z = 8.0
    ACT_RATE = 0.8
    NUM_Q = 200

  STEP_Y = math.sqrt(0.75) * STEP_X

  emitters = makeEmitterGrid(WIDTH, LAYER, STEP_X, STEP_Y, STEP_Z, ACT_RATE)
  N0 = countActive(0,0,-100, emitters)
  limit_x = emitters[WIDTH-1].x+(STEP_X/2)
  limit_y = emitters[len(emitters)-1].y
  limit_z = emitters[len(emitters)-1].z
  print("num emitters (N0): %d"%N0)
  print("emitter radius: %f"%RADIUS)
  print("effective dist: %f"%EFFECT_D)
  print("simulation zone: %f, %f, %f"%(limit_x, limit_y, limit_z))

  q_count = 0
  while q_count < NUM_Q:
    q_x = random.random() * limit_x
    q_y = random.random() * limit_y
    q_z = 0

    active = countActive(q_x, q_y, q_z, emitters, EFFECT_D, RADIUS)
    if active >= 0:
      q_count += 1
      if (q_count%10 == 0):
        print("Q: %6d,   N: %6d,   (N0-N)/N0: %f"%(q_count, active, (N0-active)/N0))
