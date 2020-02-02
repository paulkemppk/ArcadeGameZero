from threading import Thread
from gpiozero import LED, Button
import time

done = False
done1 = False
secondstoSleep = False
quitgame = False
quitgame2 = False
buttonDetect = False

secondsPause = 1
secondsLedButton = 0.3
secondsLedButtonWin = 0.3

led = [LED(17), LED(27), LED(22), LED(5), LED(6), LED(13), LED(26), LED(16)]
ledButton = [LED(24), LED(25)]
ButtonGreen = Button(20)
ButtonYellow = Button(21)


class MyThreadBUTTON(Thread):

    def __init__(self):
        """ Constructor. """
        Thread.__init__(self)

    def run(self):
        global done
        global done1
        global quitgame
        global buttonDetect

        time.sleep(2)

        ButtonGreen.hold_time = 2
        ButtonYellow.hold_time = 2

        while not buttonDetect:

            if ButtonYellow.is_held and ButtonGreen.is_held:
                quitgame = True
                buttonDetect = True
            elif ButtonGreen.is_pressed and not ButtonGreen.is_held:
                if not ButtonYellow.is_pressed or not ButtonGreen.is_held:
                    done = True
            elif ButtonYellow.is_pressed and not ButtonYellow.is_held:
                ButtonYellow.hold_time = 0.5
                if not ButtonGreen.is_pressed or not ButtonYellow.is_held:
                    done1 = True
           
               
                
class MyThreadLED(Thread):

    def __init__(self):
        """ Constructor. """
        Thread.__init__(self)

    def run(self):

        global done
        global done1
        global secondstoSleep
        global quitgame2

        ScorePlayer1 = 0
        ScorePlayer2 = 0

        done = False
        done1 = False

        time.sleep(2)

        while not quitgame:

            for i in range(7):

                led[i].on()

                if i == 0 and done:

                    if secondstoSleep < 0.03:
                        secondstoSleep = 0.03
                    else:
                        secondstoSleep -= 0.01

                    ScorePlayer1 += 1
                    if ScorePlayer1 == 5:
                        ScorePlayer1 = 0
                        ScorePlayer2 = 0
                        ledButton[1].on()
                        for j in range(10):
                            for i in range(8):
                                led[i].on()
                            time.sleep(0.5)
                            for i in range(8):
                                led[i].off()
                            time.sleep(0.5)
                        done = False
                        ledButton[1].off()
                        secondstoSleep = 0.08
                        break
                    else:
                        for k in range(ScorePlayer1):
                            ledButton[1].on()
                            time.sleep(secondsLedButton)
                            ledButton[1].off()
                            time.sleep(secondsLedButton)
                        done = False

                elif i == 7 and done1:

                    if secondstoSleep < 0.03:
                        secondstoSleep = 0.03
                    else:
                        secondstoSleep -= 0.01

                    ScorePlayer2 += 1
                    if ScorePlayer2 == 5:
                        ScorePlayer2 = 0
                        ScorePlayer1 = 0

                        ledButton[0].on()
                        for j in range(10):
                            for i in range(8):
                                led[i].on()
                            time.sleep(0.5)
                            for i in range(8):
                                led[i].off()
                            time.sleep(0.5)
                        done = False
                        ledButton[0].off()
                        secondstoSleep = 0.08
                        break
                    else:
                        for k in range(ScorePlayer2):
                            ledButton[0].on()
                            time.sleep(secondsLedButton)
                            ledButton[0].off()
                            time.sleep(secondsLedButton)
                        done1 = False

                elif done or done1:

                    time.sleep(secondsPause)
                    done = False
                    done1 = False

                time.sleep(secondstoSleep)
                led[i].off()

            for i in range(7, 0, -1):

                led[i].on()

                if i == 0 and done:

                    if secondstoSleep < 0.03:
                        secondstoSleep = 0.03
                    else:
                        secondstoSleep -= 0.01

                    ScorePlayer1 += 1
                    if ScorePlayer1 == 5:
                        ScorePlayer1 = 0
                        ScorePlayer2 = 0
                        
                        ledButton[1].on()
                        for j in range(10):
                            for i in range(8):
                                led[i].on()
                            time.sleep(0.5)
                            for i in range(8):
                                led[i].off()
                            time.sleep(0.5)
                        done = False
                        ledButton[1].off()
                        secondstoSleep = 0.08
                        break
                    else:
                        for k in range(ScorePlayer1):
                            ledButton[1].on()
                            time.sleep(secondsLedButton)
                            ledButton[1].off()
                            time.sleep(secondsLedButton)
                        time.sleep(secondsPause)
                        done = False

                elif i == 7 and done1:

                    if secondstoSleep < 0.03:
                        secondstoSleep = 0.03
                    else:
                        secondstoSleep -= 0.01

                    ScorePlayer2 += 1
                    if ScorePlayer2 == 5:
                        ScorePlayer2 = 0
                        ScorePlayer1 = 0

                        ledButton[0].on()
                        for j in range(10):
                            for i in range(8):
                                led[i].on()
                            time.sleep(0.5)
                            for i in range(8):
                                led[i].off()
                            time.sleep(0.5)
                        done = False
                        ledButton[0].off()
                        secondstoSleep = 0.08
                        break
                    else:
                        for k in range(ScorePlayer2):
                            ledButton[0].on()
                            time.sleep(secondsLedButton)
                            ledButton[0].off()
                            time.sleep(secondsLedButton)
                        time.sleep(secondsPause)
                        done1 = False

                elif done or done1:
                   
                    time.sleep(secondsPause)
                    done = False
                    done1 = False

                time.sleep(secondstoSleep)
                led[i].off()
        initgame()


def startgame():
    myThreadOb2 = MyThreadBUTTON()
    myThreadOb3 = MyThreadLED()

    myThreadOb2.start()
    myThreadOb3.start()
   


def initgame():

    global secondstoSleep
    global quitgame
    global buttonDetect

    secondstoSleep = 0.08

    quitgame = False

    while True:

        for i in range(8):
            led[i].on()
        time.sleep(0.5)
        for i in range(8):
            led[i].off()
        time.sleep(0.5)
        
    
        if ButtonYellow.is_held and ButtonGreen.is_held:
            buttonDetect = False
            break
    
    
    startgame()
        

# Run following code when the program starts
if __name__ == '__main__':

    initgame()
