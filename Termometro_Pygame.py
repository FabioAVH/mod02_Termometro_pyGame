import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.vestido = pygame.image.load('images/termo1.png')
        
    def Convertir(self, grados, toUnidad):
        resultado = 0
        
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return '{:10.2f}'.format(resultado)
        
        
        
        
    
 
class Selector():
    __tipoUnidad = 'C'
    
    def __init__(self, unidad = 'C'):
        self.__vestidosSelector = []
        self.__vestidosSelector.append(pygame.image.load('images/posiF.png'))
        self.__vestidosSelector.append(pygame.image.load('images/posiC.png'))
        
        self.__tipoUnidad = unidad
        
    def Vestido(self):
        if self.__tipoUnidad == 'F':
            return self.__vestidosSelector[0]
        else:
            return self.__vestidosSelector[1]
 
    def Change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def Unidad(self):
        return self.__tipoUnidad
             
         
         

         
 
#-------------- INICIO NumberInput -------------------------------    
class NumberInput():
    __value =  0
    __StrValue = ""
    __position = [0,0]
    __size = [0,0]
    __pointscount = 0
    
    def __init__(self, value = 0):
        self.__font = pygame.font.SysFont('Arial', 24)
        self.value(value)
        
        '''
        try:
            self.__StrValue = int(value)
            self.__StrValue = str(value)
        except:
            pass
        '''
  
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__StrValue)<10 or (event.unicode == '.' and self.__pointscount == 0):
                self.__StrValue += event.unicode
                self.value(self.__StrValue)
                '''print(self.__StrValue,'   ',str(self.__value))'''
                if event.unicode == '.':
                    self.__pointscount = 1
                    
                
            elif event.key == K_BACKSPACE:
                if self.__StrValue[-1] == '.':
                    self.__pointscount = 0
                    
                
                self.__StrValue = self.__StrValue[0:-1] # le quita el ultimo caracter
                self.value(self.__StrValue)
                
                
                
                
                
    def render(self):
        textBlock = self.__font.render(self.__StrValue, True, (74,74,74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
        
            
    #Actualiza la variavle __value y __strValue
    def value(self,val=None):
        if val == None:
            return self.__value
        else:
            try:
                self.__value = float(val)
                self.__StrValue = str(val)
            except:
                pass
            
    def posX(self, val=None):
        if val == 0:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
    
    def posY(self, val=None):
        if val == 0:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self,val=None):
        if val == None:
            return self.__position
        else:
            try:
               self.__position = [int(val[0]),int(val[1])]
            except:
                pass
    
    
    def width(self, val=None):
        if val == 0:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val=None):
        if val == 0:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self,val=None):
        if val == None:
            return sef.__size
        else:
            try:
                self.__size = [int(val[0]),int(val[1])]
            except:
                pass
    
#-------------- FIN NumberInput -------------------------------        
        
    
    
    
#============================== MAIN ================================

class mainApp():
    termometo = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415)) #crea la pantalla
        pygame.display.set_caption('Termometro') #Titulo
        self.__screen.fill((244, 236, 203)) #Colorea la pantalla
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))
        
        self.selector = Selector()
    
    def __onClose(self):
        pygame.quit()
        sys.exit()
    
    
    def Start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__onClose()
                   
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.Change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.Unidad()
                    print(grados)
                    print(nuevaUnidad)
                    temperatura = self.termometro.Convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                
                #self.termometro.Convertir(self.entrada.__value,)
                    
            #Renderizacion
            self.__screen.fill((244, 236, 203)) #pintamos el fondo de pantalla
            self.__screen.blit(self.termometro.vestido, (50,34)) #pinta el termometro
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) #pinta rectangulo blanco
            self.__screen.blit(text[1],self.entrada.pos()) #pinta foto del texto
            self.__screen.blit(self.selector.Vestido(),(112,153))
            
                        
            pygame.display.flip()
    
 
#============================== EJECUCION ================================
 
if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.Start()