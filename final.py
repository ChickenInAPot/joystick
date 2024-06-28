import pygame
import serial
import sys

pygame.init()

#pygame settings
width, height = 500,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("l0vy2tr4ppy")
black = (0,0,0)
white = (255,255,255)
running = True
clock = pygame.time.Clock()
framerate = 120

#serial settings
ser = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)  
lastpos = (250,250)


#read data function 
def xnypos(ser):
    global lastpos
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if "," in data:
                xpos, ypos = map(int, data.split(','))
                lastpos = (xpos, ypos)
                return xpos, ypos
            else:
                print("Data format error: no comma found.")
        else:
            print("No data waiting in serial buffer.")
    except Exception as e:
        print(f"Exception during serial read: {e}")
    # Notice: We do not close the serial port here anymore
    return lastpos
# main function


if __name__ == "__main__":
    try:
        while running:
            clock.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(black)
            circler = 50
            circlepos= (50,50)
            pygame.draw.circle(screen, white, xnypos(ser) , circler)
            pygame.display.flip()
            
    finally:
        ser.close()  

        



pygame.quit()
sys.exit()