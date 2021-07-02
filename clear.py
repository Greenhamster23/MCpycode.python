from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
#256 x 256 x 128 blocks.
air = 0
#mc.setBlocks(start x, start y,start z , end x ,end y, end z,air) # clear some air        
mc.setBlocks(48.5,0.0 ,8.9,-47.6,-5,116.9,98) # clear some air                                               
x, y, z = mc.player.getPos()
mc.setBlocks(0,62,0,35,3)
#mc.player.setPos(-10.5,1,69.7)     #Player Postion

mc.setBlocks(127.7, 0, -127.7,-127.7,55,127.7,air)