import pygame 


class physics:
  def __init__():
    self.velocity = vector()
    self.pos = vector()
    self.acc = vector()
    
class creature(physics):
  def __init__():
    supre.__init__()
    self.body = list()
    self.health = 0.0
    self.dna = list()
    self.sensors = list()
  def createRandomPopulation(self):
    
    self.health = 100
    self.Bpart = pygame.image.load("resources/images/back.png")
    self.body.append(self.Bpart)
  def CreateRandomPopulation(self):#this should create each time differently
            
          self.pos.addVertex(50,200,0)
          self.fitness = 0
          tempx = self.pos.x
          tempy = self.pos.y
          x = 0.0
          y = 0.0
          for i in range(0,60):
              v = vector()
              v.copyVector(random.uniform(0,360),20,"D")#create a random vector
              
              # copying the value of temp location for restore into x,y
              x = tempx
              y = tempy
              
              tempx += v.magnitude*math.cos(v.direction)
              tempy += v.magnitude*math.sin(v.direction)
              if tempx < 30 or tempx > 400 or tempy < 30 or tempy > 400 :
                    #print("Collision :",tempx," | " ,tempy)
                    tempx = x#restore
                    tempy = y#restore
              else:
                    self.dna.append(v)
                    #arrow = canvas.create_line(x,y,tempx,tempy,fill="#5500ff")
                    #root.update()
    
    
  
def main():
  pass

main()
  
