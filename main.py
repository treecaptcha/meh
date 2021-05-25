# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2021 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# meh
# Copyright (c) 2021 TreeCaptcha
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# stopwatch
# MIT License
#
# Copyright (c) 2018-2019 PoLLeN
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

import pyglet
import random
from stopwatch import Stopwatch
score = 0
window = pyglet.window.Window(width=500, height=400)
breadmans = pyglet.graphics.Batch()

bred1 = pyglet.sprite.Sprite(pyglet.image.load('france.png'),50,50,batch=breadmans)
bred2 = pyglet.sprite.Sprite(pyglet.image.load('france.png'),50,200,batch=breadmans)
bred3 = pyglet.sprite.Sprite(pyglet.image.load('france.png'),50,100,batch=breadmans)
kitten = pyglet.image.load('background.png')
bred1.scale = 0.15
bred2.scale = 0.16
bred3.scale = 0.17
bagete = pyglet.sprite.Sprite(pyglet.image.load('bagg.png'))
bagete.scale = 0.2
window.set_mouse_visible(False)
times = Stopwatch()
game = True
print(times.start())
enabble = True
def enable(dt):
    global enabble
    enabble = True
@window.event
def on_draw():
    global game
    global enabble
    window.clear()
    kitten.blit(0,0)
    if game:
        breadmans.draw()
        bagete.draw()
        pyglet.text.Label(text=str(score), font_size=20, x=10, y=370, color=[0,25,25,255]).draw()
        pyglet.text.Label(text=str(round(times.duration, 1)), font_size=20, x=10, y=350, color=[0, 25, 25, 255]).draw()
    if times.duration >= 5.0:
        window.set_mouse_visible(True)
        game = False
        times.reset()
        enabble = False
        pyglet.clock.schedule_once(enable, 1.0)
        pyglet.text.Label(text='Play Again!', font_size=30, x=150, y=250, color=[0, 25, 25, 255]).draw()
        pyglet.text.Label(text=str(score*53682), font_size=20, x=200, y=200, color=[0, 25, 25, 255]).draw()

    if not game:
        pyglet.text.Label(text='Play Again!', font_size=30, x=150, y=250, color=[0, 25, 25, 255]).draw()
        pyglet.text.Label(text=str(score*53682), font_size=20, x=200, y=200, color=[0, 25, 25, 255]).draw()
def update(dt):
    global game
    global enabble
    if times.duration >= 5:
        window.set_mouse_visible(True)
        game = False
        times.reset()
        enabble = False
        pyglet.clock.schedule_once(enable, 1.0)
        pyglet.text.Label(text=str(score*53682), font_size=30, x=200, y=200, color=[0, 25, 25, 255]).draw()
    pyglet.text.Label(text=str(round(times.duration, 1)), font_size=20, x=10, y=350, color=[0, 25, 25, 255]).draw()

pyglet.clock.schedule_interval(update, 0.1)

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x)
    global score
    global game
    global enabble
    if game:
        if (x - (bred1.x +35) < 50) and (x - (bred1.x) > 0):
            if (y - (bred1.y + 35) < 50) and (y - (bred1.y) > 0):
                print('bred1')
                bred1.update(random.randint(0,470),random.randint(0,350))
                score += 1
        if (x - (bred2.x +35) < 50) and (x - (bred2.x) > 0):
            if (y - (bred2.y + 35) < 50) and (y - (bred2.y) > 0):
                print('bred2')
                bred2.update(random.randint(0, 470), random.randint(0, 350))
                score += 1
        if (x - (bred3.x +35) < 50) and (x - (bred3.x) > 0):
            if (y - (bred3.y + 35) < 50) and (y - (bred3.y) > 0):
                print('bred3')
                bred3.update(random.randint(0, 470), random.randint(0, 350))
                score += 1
    elif enabble:
        if (x < 300) and (x > 100):
            if (y < 300) and (y > 250):
                print('bred3')
                game = True
                score = 0
                score == 0
                window.set_mouse_visible(False)
                times.restart()


@window.event
def on_mouse_motion(x, y, dx, dy):
    bagete.update(x-30,y-80)

pyglet.app.run()