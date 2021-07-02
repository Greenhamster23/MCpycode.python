from mcpi.minecraft import Minecraft
from mcpi import block

ip = "10.183.0.28"
mc = Minecraft.create(ip, 4711)
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

mc.setBlocks(16.5,-9, 40.5 ,-2.5, 1, 71.5 ,air)
mc.setBlocks(-2.5,-9, 40.5 ,16.5, 0, 36.5 ,155)
mc.setBlocks(17.5,0, 76.5 ,21.5, -9, 36.5 ,155)
mc.setBlocks(-7.4,0, 72.5 ,17.5, -9, 76.5 ,155)
mc.setBlocks(-7.5,0, 71.5 ,-3.5, -9, 36.5 ,155)
mc.setBlocks(-2.5,-10, 71.5 ,16.5, -10, 41 ,89)
mc.setBlocks(-2.5,-9, 71.5 ,16.5, -0, 41 ,8)
mc.setBlocks(8.5,1, 40.5 ,5.5, 15, 40.5 ,155)
mc.setBlocks(8.5,16, 40.5 ,5.5, 16, 47.5 ,155)
mc.setBlocks(6.5,16, 48.5 ,7.5, 16, 48.5 ,155)
mc.setBlocks(8.5,16, 40.5 ,5.5, 16, 40.45 ,air)
mc.setBlocks(5.5,15, 41.5 ,8.5, 15, 41.5 ,155)
