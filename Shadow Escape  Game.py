import pygame
from collections import deque

pygame.init()    
W,H=1000,760        
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("Shadow Escape")
clock=pygame.time.Clock()

WHITE=(255,255,255);BLACK=(10,10,10);BLUE=(0,180,255);RED=(255,60,60)
GREEN=(0,255,120);PURPLE=(120,0,180);YELLOW=(255,220,0);GRAY=(50,50,50)

ROWS=15;COLS=15;CELL=45
OX=160;OY=60

font_big=pygame.font.SysFont("Arial",45,True)
font_small=pygame.font.SysFont("Arial",28)

levels=[
{"maze":[
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],
[1,1,1,0,1,0,1,1,1,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
[0,1,1,1,1,1,1,1,0,1,1,1,0,1,0],
[0,0,0,0,0,0,0,1,0,0,0,1,0,0,0],
[0,1,1,1,1,1,0,1,1,1,0,1,1,1,0],
[0,0,0,0,0,1,0,0,0,1,0,0,0,1,0],
[1,1,1,1,0,1,1,1,0,1,1,1,0,1,0],
[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
[0,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
[0,1,1,1,0,1,1,1,0,1,1,1,0,1,0],
[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
[0,1,1,1,0,1,1,1,0,1,1,1,0,1,0]],
"monster_speed":20,"traps":[(4,5),(8,8)],"color":BLUE},

{"maze":[
[0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,1,0,1,1,0,1,0,1,1,0,1,0,1],
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
[1,1,1,0,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
[0,1,1,1,1,1,1,0,1,1,1,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
[1,1,1,1,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[0,1,1,0,1,1,1,0,1,1,1,0,1,0,0],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,1,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[0,1,1,0,0,0,1,0,0,0,1,0,0,0,0],
[0,0,0,1,1,0,1,1,1,0,1,1,1,0,0]],
"monster_speed":18,"traps":[(3,3),(6,7),(10,11)],"color":PURPLE},

{"maze":[
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
[1,1,1,0,1,0,1,1,1,0,1,0,1,1,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
[0,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
[1,1,1,1,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[0,1,1,0,1,1,1,0,1,1,1,0,1,0,0],
[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,1,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[0,1,1,0,1,1,1,0,1,1,1,0,1,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
[0,0,1,1,1,0,1,1,1,0,1,1,1,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]],
"monster_speed":10,"traps":[(2,2),(5,5),(8,8),(12,12)],"color":RED}
]

def bfs(s,g,m):
 q=deque([s]);v={tuple(s):None}
 while q:
  c=q.popleft()
  if c==g:break
  x,y=c
  for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:
   nx,ny=x+dx,y+dy
   if 0<=nx<ROWS and 0<=ny<COLS and m[nx][ny]==0 and (nx,ny) not in v:
    q.append([nx,ny]);v[(nx,ny)]=c
 p=[];c=g
 while tuple(c) in v and v[tuple(c)]:
  p.append(c);c=v[tuple(c)]
 p.reverse();return p

class Player:
 def __init__(s,x,y):s.x=x;s.y=y;s.hp=3
 def draw(s):
  pygame.draw.rect(screen,WHITE,(OX+s.y*CELL+10,OY+s.x*CELL+10,CELL-20,CELL-20),border_radius=8)
 def move(s,dx,dy,m):
  nx,ny=s.x+dx,s.y+dy
  if 0<=nx<ROWS and 0<=ny<COLS and m[nx][ny]==0:s.x,s.y=nx,ny

class Monster:
 def __init__(s,x,y):s.x=x;s.y=y
 def draw(s):
  pygame.draw.circle(screen,BLACK,(OX+s.y*CELL+CELL//2,OY+s.x*CELL+CELL//2),22)
  pygame.draw.circle(screen,RED,(OX+s.y*CELL+15,OY+s.x*CELL+18),4)
  pygame.draw.circle(screen,RED,(OX+s.y*CELL+30,OY+s.x*CELL+18),4)
 def chase(s,p,m):
  path=bfs([s.x,s.y],[p.x,p.y],m)
  if path:s.x,s.y=path[0]

class Trap:
 def __init__(s,x,y):s.x=x;s.y=y
 def draw(s):
  pts=[(OX+s.y*CELL+10,OY+s.x*CELL+35),(OX+s.y*CELL+22,OY+s.x*CELL+10),(OX+s.y*CELL+35,OY+s.x*CELL+35)]
  pygame.draw.polygon(screen,RED,pts)

class Game:
 def __init__(s):
  s.level=0
  s.load()
  s.running=1
  s.start()

 def start(s):
  screen.fill(BLACK)
  t=font_big.render("HALOO TO SHADOW GAME",1,WHITE)
  st=font_small.render("PRESS SPACE TO START",1,YELLOW)
  screen.blit(t,(W//2-t.get_width()//2,250))
  screen.blit(st,(W//2-st.get_width()//2,350))
  pygame.display.update()

  wait=1
  while wait:
   for e in pygame.event.get():
    if e.type==pygame.QUIT:
     pygame.quit();exit()
    if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
     wait=0

 def load(s):
  d=levels[s.level]
  s.maze=d["maze"];s.player=Player(14,0);s.monster=Monster(0,14)
  s.exit=[0,0];s.color=d["color"];s.ms=d["monster_speed"]
  s.timer=0;s.traps=[Trap(*t) for t in d["traps"]]

 def draw_maze(s):
  for i in range(ROWS):
   for j in range(COLS):
    r=pygame.Rect(OX+j*CELL,OY+i*CELL,CELL,CELL)
    pygame.draw.rect(screen,s.color if s.maze[i][j] else GRAY,r,0 if s.maze[i][j] else 0,border_radius=6 if s.maze[i][j] else 0)
    pygame.draw.rect(screen,BLACK,r,1)

 def draw_exit(s):
  pygame.draw.rect(screen,YELLOW,(OX+s.exit[1]*CELL+8,OY+s.exit[0]*CELL+8,CELL-16,CELL-16),border_radius=10)

 def draw_ui(s):
  screen.blit(font_big.render("SHADOW ESCAPE",1,WHITE),(300,10))
  screen.blit(font_small.render(f"LEVEL:{s.level+1}",1,WHITE),(30,690))
  screen.blit(font_small.render(f"HP:{s.player.hp}",1,WHITE),(220,690))

 def draw(s):
  screen.fill((15,15,20))
  s.draw_maze();s.draw_exit()
  [t.draw() for t in s.traps]
  s.player.draw();s.monster.draw()
  s.draw_ui()
  pygame.display.update()

 def traps_check(s):
  for t in s.traps:
   if s.player.x==t.x and s.player.y==t.y:
    s.player.hp-=1
    s.player.x,s.player.y=14,0
    break

 def end(s,t,c):
  screen.fill(BLACK)
  msg=font_big.render(t,1,c)
  screen.blit(msg,(W//2-msg.get_width()//2,H//2-msg.get_height()//2))
  pygame.display.update()
  pygame.time.delay(3000)

 def next(s):
  s.level+=1
  if s.level>=len(levels):
   s.end("YOU ESCAPED",GREEN)
   s.running=0
  else:s.load()

 def run(s):
  while s.running:
   clock.tick(60)

   for e in pygame.event.get():
    if e.type==pygame.QUIT:s.running=0

    if e.type==pygame.KEYDOWN:
     k=e.key
     if k==pygame.K_UP:s.player.move(-1,0,s.maze)
     if k==pygame.K_DOWN:s.player.move(1,0,s.maze)
     if k==pygame.K_LEFT:s.player.move(0,-1,s.maze)
     if k==pygame.K_RIGHT:s.player.move(0,1,s.maze)

   s.timer+=1

   if s.timer>=s.ms:
    s.monster.chase(s.player,s.maze)
    s.timer=0

   s.traps_check()

   if [s.player.x,s.player.y]==[s.monster.x,s.monster.y]:
    s.end("GAME OVER",RED)
    s.running=0

   if s.player.hp<=0:
    s.end("YOU DIED",RED)
    s.running=0

   if [s.player.x,s.player.y]==s.exit:
    s.next()

   s.draw()

game=Game()
game.run()
pygame.quit()