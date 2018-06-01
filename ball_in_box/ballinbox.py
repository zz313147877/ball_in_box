import math
import random
from .validate import validate

__all__ = ['ball_in_box']


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.

    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    circles = []
    for circle_index in range(m):
        ox = -0.2237
        oy = 0.2237
        d = 0.9315
        circle = max_in_nine_points(ox, oy, d, circles, blockers)
        circles.append(circle)

    return circles


def max_in_nine_points(ox, oy, d, circles, blockers):
    max_circle = center_circle = (ox, oy, max_circle_one_point(ox, oy, circles, blockers))
    for i in range(1, 29):
        #x0 = d*math.cos((i/9) * math.pi / 4)
        #y0 = d*math.sin((i/9) * math.pi / 4)
        if i == 1 or i == 6 or i == 11 or i == 16 or i == 21:
            x0 = ox - d
        if i == 2 or i == 7 or i == 12 or i == 17 or i == 22:
            x0 = ox - d/3
        if i == 3 or i == 8 or i == 13 or i == 18 or i == 23:
            x0 = ox
        if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
            x0 = ox + d/3
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
            x0 = ox + d
        if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
            y0 = oy - d
        if i == 6 or i == 7 or i == 8 or i == 9 or i == 10:
            y0 = oy - d/3
        if i == 11 or i == 12 or i == 13 or i == 14 or i == 15:
            y0 = oy
        if i == 16 or i == 17 or i == 18 or i == 19 or i == 20:
            y0 = oy + d/3
        if i == 21 or i == 22 or i == 23 or i == 24 or i == 25:
            y0 = oy + d
        if i == 26:
            x0 = ox - d/6
            y0 = oy - d/6
        if i == 27:
            x0 = ox - d/6
            y0 = oy + d/6
        if i == 28:
            x0 = ox + d/6
            y0 = oy - d/6
        if i == 29:
            x0 = ox + d/6
            y0 = oy + d/6
        if i == 30:
            x0 = ox
            y0 = oy - d/6
        if i == 31:
            x0 = ox
            y0 = oy + d/6
        if i == 32:
            x0 = ox + d/6
            y0 = oy
        if i == 33:
            x0 = ox - d/6
            y0 = oy


        this_circle = (x0, y0, max_circle_one_point(x0, y0, circles, blockers))
        if this_circle[2] >= max_circle[2]:
            center_circle = max_circle
            center_circle2 = second_circle = max_circle
            max_circle = this_circle
    if (max_circle[0] - center_circle[0])**2 + (max_circle[1] - center_circle[1])**2 < 0.00000000001 :
        return max_circle
        #if second_circle[2] - center_circle2 <0.0000001:
            #if max_circle[2] > second_circle[2]:
                #return max_circle
        # else:
        #return second_circle
        #else:
            #return max_in_nine_points(second_circle[0], second_circle[1], d/2, circles, blockers)
    else:
        return max_in_nine_points(max_circle[0], max_circle[1], d/6.11, circles, blockers)


def max_circle_one_point(ox, oy, circles, blockers):
    if (not (ox <= 1 and ox >= -1)) \
            or (not (oy <= 1 and oy >= -1)):
        return 0
    if ox < 0 and oy < 0:
        oxd = ox + 1
        oyd = oy + 1
    elif ox >= 0 and oy < 0:
        oxd = 1 - ox
        oyd = oy + 1
    elif ox < 0 and oy >= 0:
        oxd = ox + 1
        oyd = 1 - oy
    else:
        oxd = 1 - ox
        oyd = 1 - oy
    minb = min(oxd, oyd)
    minc = 2
    for circle in circles:
        if math.sqrt((ox - circle[0])**2 + (oy - circle[1])**2) - circle[2] < minc:
            minc = math.sqrt((ox - circle[0])**2 + (oy - circle[1])**2) - circle[2]
    mind = 2
    for blocker in blockers:
        if math.sqrt((ox - blocker[0])**2 + (oy - blocker[1])**2) < mind:
            mind = math.sqrt((ox - blocker[0])**2 + (oy - blocker[1])**2)
    if min(minb, minc, mind) >= 0:
        r = min(minb, minc, mind)
    else:
        r = 0
    return r
