# Copyright Jun Jo, May. 28. 2018. Allright reserved.
# KIST Europe http://www.kist-europe.de
# Contact Email: j.jo@kist-europe.de

import math
import random

# ASSUMPTION
# - emitters are evenly distributed at vertices of equilateral triangles
# - the equilateral triangles have edge length X_STEP

# WIDTH: emitter grid width (ex. WIDTH=100 for 100 x 100 grid)
# RADIUS: emitter radius
# EFFECT_D: the effective distance of a quencher
# X_STEP: edge length of the equilateral triangle
# Y_STEP: height of the equilateral triangle

WIDTH = 100
RADIUS = 1.0
EFFECT_D = 10.0
X_STEP = 6.1
Y_STEP = math.sqrt(0.75) * X_STEP


class Emitter(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.status = 1

  def getDistance(self, x, y):
    return math.sqrt((self.x - x)**2 + (self.y - y)**2)

  def react(self, x, y):
    d = self.getDistance(x,y)
    if d > EFFECT_D:
      pass
    elif d <= RADIUS:
      return -1
    else:
      self.status = 0
    return self.status


def makeEmitterGrid(width):
  points = []
  for y in range(width):
    for x in range(width):
      if y % 2:
        points.append(Emitter((x*X_STEP)+(X_STEP/2), y*Y_STEP))
      else:
        points.append(Emitter(x*X_STEP, y*Y_STEP))
  return points


def countActive(x, y, emitters):
  count = 0
  for e in emitters:
    result = e.react(x,y)
    if result == -1:
      return -1
    else:
      count += result
  return count


if __name__ == "__main__":
  emitters = makeEmitterGrid(WIDTH)
  N0 = len(emitters)
  limit_x = emitters[WIDTH-1].x+(X_STEP/2)
  limit_y = emitters[N0-1].y
  print("num emitters (N0): %d"%N0)
  print("emitter radius: %f"%RADIUS)
  print("effective dist: %f"%EFFECT_D)
  print("simulation zone: %f, %f"%(limit_x, limit_y))

  num_q = 5000

  q_count = 0
  while q_count < num_q:
    q_x = random.random() * limit_x
    q_y = random.random() * limit_y

    active = countActive(q_x, q_y, emitters)
    if active >= 0:
      q_count += 1
      if (q_count%10 == 0):
        print("Q: %6d,   N: %6d,   (N0-N)/N0: %f"%(q_count, active, (N0-active)/N0))
