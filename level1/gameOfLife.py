import pygame,random,time

from physics import *



class creature(physics):
  def __init__(self,pos,type='herbivore'):
    super(creature,self).__init__(pos)
    self.body = list()
    self.health = 0.0
    self.dna = list()
    self.sensors = list()
    self.state = 1
    self.eggcycle = 0
    self.gender = 0 # female
  def CreateRandomPopulation(self):#this should create each time differently
          self.health = 100
          self.state = 1
          self.eggcycle = 10
          self.gender = int(random.uniform(0,2))
          self.Bpart = pygame.image.load("resources/images/body.png")
          self.body.append(self.Bpart)
          #  genrate random velocity
          self.velocity.x = int(random.uniform(0,10))
          self.velocity.y = int(random.uniform(0,10))
          self.velocity.z = 0
          
          self.dna.append(DeciToBinary(self.velocity.x))
          self.dna.append(DeciToBinary(self.velocity.y))
  def eggCycle(self):
    self.eggcycle -= 0.3
          
          
'''
=======================================================
 global functions
=======================================================
'''
def DeciToBinary(D_num):
    D_num = int(D_num)
    B_num = list()
    binary = list()
    
    while(D_num > 0):
        B_num.append(D_num%2)
        D_num = int(D_num / 2)
        
    i = len(B_num)
    while(i > 0):
        binary.append(B_num[i-1])
        i -= 1
    return binary
  
def _input_():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit();exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
      pygame.getpos()
def display(creature):
  if creature.state == 1:
    screen.blit(creature.body[0],(creature.pos[0],creature.pos[1]))
  elif creature.state == 0:
    pass
  
def genrateInitialPopulation():
    global population

    for i in range(0,30):
       x = random.uniform(0,window[0])
       y = random.uniform(0,window[1])
       p = creature((x,y,0))
       # print help(p)
       p.CreateRandomPopulation()
       population.append(p)
def birth(c):
    global population
    
    x = c.pos[0]
    y = c.pos[1]
    p = creature((x,y,0))
    p.CreateRandomPopulation()
    population.append(p)
    
def timeline(creatures = []):
  for c in  creatures:
      display(c)
      
def gameLogic():
    global population,food
    for i in  range(0,len(population)):
          
          population[i].pos[0] += population[i].velocity.x
          population[i].pos[1] += population[i].velocity.y
          
    for i in  range(0,len(population)):
          
         if population[i].pos[0] >= window[0] :
            population[i].velocity.reverseDir("x")

         if population[i].pos[0] < 0 :
            population[i].velocity.reverseDir("x")

         if population[i].pos[1] >= window[1] :
            population[i].velocity.reverseDir("y")

         if population[i].pos[1] < 0 :
            population[i].velocity.reverseDir("y")

    for p in population:
      for f in food:
        
        if  IsPointInside(f[0],f[1],p.pos,20,12):
          food.remove(f)
          foodDisplay()
          p.health += 10
          if p.health > 100 :p.health = 100
          
# # # collision between each other
    for p in population:
      for f in population:
        
        if  IsPointInside(p.pos[0],p.pos[1],f.pos,20,12):
          if p.health > f.health :
              population.remove(f)
          else:
              # population.remove(p)
              pass
          
# # # if food decrease less then 40 it genrate new food
    if len(food) < 40:
       genrateFood()
    for p in population:
      p.health -= 0.5
      p.eggCycle()
      if p.health < 20 : p.state = 3;# dead state
      if p.health > 80 and p.eggcycle <= 2 and p.state == 1: birth(p);p.eggcycle = 10

def genrateFood():
    global food
    h,v = 3,3
    for f in range(0,100):
      posx,posy = random.uniform(0,window[0]),random.uniform(0,window[1])
      food.append([posx,posy])
    
def foodDisplay():
    global food
    h,v = 3,3
    
    for f in food:
      posx,posy = f[0],f[1]
      pygame.draw.rect(screen,RED,[[posx,posy],[h,v]])  
'''
=======================================================
 main functions
=======================================================
'''      


def main():
    global population
    # main loop
    genrateInitialPopulation()
    genrateFood()
    while(1):
       timeline(population)
       foodDisplay()
       gameLogic()
       # input from user
       _input_()
       # update the screen
       pygame.display.update()
       # clear the screen
       screen.fill(WHITE)
       # frame rate
       clock.tick(30)
       if len(population) == 0:
         break


# colors
WHITE = (254,254,254)
RED = (200,20,20)

window = (900,600)
pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()


population = list()
food = list()

main()
