import pygame
import random


class App:

    def actionButtonClick():
        print("Button Clicked")
    
    def __init__(self):
        
        self.size = self.weight, self.height = 1475, 1000
        self.displaySurf = pygame.display.set_mode(self.size)

        self.lightGreen = (4, 189, 53)
        self.darkGreen = (1, 112, 31)

        self.go = pygame.image.load('Go.png')
        self.goRect = self.go.get_rect()
        self.goRect.x = 1275
        self.goRect.y = 0

        self.up = pygame.image.load('Up.png')
        self.upRect = self.up.get_rect()
        self.upRect.x = 1025
        self.upRect.y = 800

        self.down = pygame.image.load('Down.png')
        self.downRect = self.down.get_rect()
        self.downRect.x = 1025
        self.downRect.y = 875

        self.left = pygame.image.load('Left.png')
        self.leftRect = self.left.get_rect()
        self.leftRect.x = 1250
        self.leftRect.y = 800

        self.right = pygame.image.load('Right.png')
        self.rightRect = self.right.get_rect()
        self.rightRect.x = 1250
        self.rightRect.y = 875

        self.displaySurf.blit(self.go, self.goRect)

        self.displaySurf.blit(self.up, self.upRect)
        self.displaySurf.blit(self.down, self.downRect)
        self.displaySurf.blit(self.left, self.leftRect)
        self.displaySurf.blit(self.right, self.rightRect)

        self.bird = pygame.image.load('bird.png')
        self.birdx = 900
        self.birdy = 900

        self.snake = pygame.image.load('snake.png')
        self.snakeDead = pygame.image.load('snakeDead.png')
        self.snakex = random.randint(0, 9) * 100
        self.snakey = random.randint(0, 9) * 100

        self.cmdStack = []
        
        self.running = True
        self.isSnakeDead = False

        self.run()
        

    def run(self):

        while self.running:
            
            for event in pygame.event.get():
                self.event(event)
            
            self.loop()
            self.render()
        
        pygame.quit()

    def event(self, event):

        if event.type == pygame.QUIT:
            self.quit()

        elif event.type == pygame.MOUSEBUTTONUP:

            if self.upRect.collidepoint(event.pos):
                self.displaySurf.blit(self.up, (1000, len(self.cmdStack) * 50))
                self.cmdStack.append("UP")

            elif self.downRect.collidepoint(event.pos):
                self.displaySurf.blit(self.down, (1000, len(self.cmdStack) * 50))
                self.cmdStack.append("DOWN")

            elif self.leftRect.collidepoint(event.pos): 
                self.displaySurf.blit(self.left, (1000, len(self.cmdStack) * 50)) 
                self.cmdStack.append("LEFT")

            elif self.rightRect.collidepoint(event.pos):
                self.displaySurf.blit(self.right, (1000, len(self.cmdStack) * 50))
                self.cmdStack.append("RIGHT")
  
            elif self.goRect.collidepoint(event.pos):
                self.executeStack()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.birdx > 0:
                    self.birdx -= 100
            
            elif event.key == pygame.K_RIGHT:
                if self.birdx < 900:
                    self.birdx += 100
            
            elif event.key == pygame.K_UP:
                if self.birdy > 0:
                    self.birdy -= 100
            
            elif event.key == pygame.K_DOWN:
                if self.birdy < 900:
                    self.birdy += 100
            
            if self.birdx == self.snakex and self.birdy == self.snakey:
                self.isSnakeDead = True
    
    def loop(self):
        pass#print("loop")

    def render(self):

        for col in range(10):
            for row in range(10):
                if (col+row) % 2:
                    pygame.draw.rect(self.displaySurf, self.lightGreen, pygame.Rect(row * 100, col * 100, 100, 100))
                else:
                    pygame.draw.rect(self.displaySurf, self.darkGreen, pygame.Rect(row * 100, col * 100, 100, 100))

        if self.isSnakeDead:
            self.displaySurf.blit(self.snakeDead, (self.snakex, self.snakey))
        else:
            self.displaySurf.blit(self.snake, (self.snakex, self.snakey))

        self.displaySurf.blit(self.bird, (self.birdx, self.birdy))
        pygame.display.flip()

    def executeStack(self):
        
        for cmd in self.cmdStack:
            
            if cmd == "UP":
                if self.birdy > 0:
                    self.birdy -= 100
                    self.render()

            elif cmd == "DOWN":
                if self.birdy < 900:
                    self.birdy += 100
                    self.render()

            elif cmd == "LEFT":
                if self.birdx > 0:
                    self.birdx -= 100
                    self.render()

            elif cmd == "RIGHT":
                if self.birdy < 900:
                    self.birdy += 100
                    self.render()
            
            pygame.time.wait(1000)
            pygame.event.get()

    
    def quit(self):
        self.running = False

if __name__ == "__main__":
    theApp = App()