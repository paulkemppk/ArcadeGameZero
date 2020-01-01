from threading import Thread
from gpiozero import LED
from gpiozero import Button
import time

done = False
done1 = False
secondstoSleep = False
quitgame = False

secondsToSleep = 0.05
secondsPause = 2

led = [LED(4), LED(5), LED(6), LED(7), LED(8), LED(9), LED(10), LED(11)]
ledButton = [LED(12), LED(13)]
ButtonBlue = Button(2)
ButtonRed = Button(3)

# led = ["LED 1", "LED 2", "LED 3", "LED 4", "LED 5", "LED 6", "LED 7", "LED 8"]
# ledButton = ["LED_BUTTON1", "LED_BUTTON2"]


class MyThreadBUTTON(Thread):

    def __init__(self):
        """ Constructor. """
        Thread.__init__(self)

    def run(self):
        global done
        global done1
        global quitgame

        while True:

            if ButtonBlue.is_pressed:
                done = True
            if ButtonRed.is_pressed:
                done1 = True
            if ButtonRed.is_pressed and ButtonBlue.is_pressed:
                time.sleep(10)
                if ButtonRed.is_pressed and ButtonBlue.is_pressed:
                    quitgame = True
                else:
                    break


class MyThreadLED(Thread):

    def __init__(self):
        """ Constructor. """
        Thread.__init__(self)

    def run(self):

        global done
        global done1
        global secondstoSleep

        ScorePlayer1 = 0
        ScorePlayer2 = 0

        while not quitgame:

            for i in range(7):

                led[i].on()

                #print(led[i] + "on")

                if i == 0 and done:
                    ScorePlayer1 += 1

                    if ScorePlayer1 == 5:
                        ScorePlayer1 = 0
                        led[0].on()
                        led[1].on()
                        led[2].on()
                        led[3].on()
                        led[4].on()
                        for j in range(10):
                            ledButton[1].on()
                            secondstoSleep(1)
                            ledButton[1].off()
                        led[0].off()
                        led[1].off()
                        led[2].off()
                        led[3].off()
                        led[4].off()
                        done = False
                        break

                    for k in range(ScorePlayer1):
                        led[k].on()
                    secondstoSleep(secondsPause)
                    for m in range(ScorePlayer1):
                        led[m].off()
                    done = False

                elif i == 7 and done1:

                    ScorePlayer2 += 1

                    if ScorePlayer2 == 5:
                        ScorePlayer2 = 0
                        led[7].on()
                        led[6].on()
                        led[5].on()
                        led[4].on()
                        led[3].on()

                        for j in range(10):
                            ledButton[0].on()
                            secondstoSleep(1)
                            ledButton[0].off()
                        led[7].off()
                        led[6].off()
                        led[5].off()
                        led[4].off()
                        led[3].off()
                        done1 = False
                        break

                    for k in range(ScorePlayer1):
                        led[k].on()
                    secondstoSleep(secondsPause)
                    for m in range(ScorePlayer1):
                        led[m].off()
                    done1 = False

                elif done or done1:

                    for j in range(5):
                        led[i].on()
                        secondstoSleep(0.5)
                        led[i].off()
                        secondstoSleep(0.5)

                    done = False
                    done1 = False

                time.sleep(secondstoSleep)
                led[i].off()
                #print(led[i] + "off")

            for i in range(7, 0, -1):

                led[i].on()

                #print(led[i] + "on")

                if i == 0 and done:
                    ScorePlayer1 += 1

                    if ScorePlayer1 == 5:
                        ScorePlayer1 = 0
                        led[0].on()
                        led[1].on()
                        led[2].on()
                        led[3].on()
                        led[4].on()
                        for j in range(10):
                            ledButton[1].on()
                            secondstoSleep(1)
                            ledButton[1].off()
                        led[0].off()
                        led[1].off()
                        led[2].off()
                        led[3].off()
                        led[4].off()
                        done = False
                        break

                    for k in range(ScorePlayer1):
                        led[k].on()
                    secondstoSleep(secondsPause)
                    for m in range(ScorePlayer1):
                        led[m].off()
                    done = False

                elif i == 7 and done1:

                    ScorePlayer2 += 1

                    if ScorePlayer2 == 5:
                        ScorePlayer2 = 0
                        led[7].on()
                        led[6].on()
                        led[5].on()
                        led[4].on()
                        led[3].on()

                        for j in range(10):
                            ledButton[0].on()
                            secondstoSleep(1)
                            ledButton[0].off()
                        led[7].off()
                        led[6].off()
                        led[5].off()
                        led[4].off()
                        led[3].off()
                        done1 = False
                        break

                    for k in range(ScorePlayer1):
                        led[k].on()
                    secondstoSleep(secondsPause)
                    for m in range(ScorePlayer1):
                        led[m].off()
                    done1 = False

                elif done or done1:

                    for j in range(5):
                        led[i].on()
                        secondstoSleep(0.5)
                        led[i].off()
                        secondstoSleep(0.5)

                    done = False
                    done1 = False

                time.sleep(secondstoSleep)
                led[i].off()
                #print(led[i] + "off")
        initgame()


def startgame():
    myThreadOb2 = MyThreadBUTTON()

    myThreadOb3 = MyThreadLED()

    myThreadOb2.start()
    myThreadOb3.start()

    myThreadOb2.join()
    myThreadOb3.join()


def initgame():

    global secondstoSleep
    global quitgame

    secondstoSleep = 0.1
    isON = 0

    while True:

        if ButtonRed.is_pressed and ButtonBlue.is_pressed:
            led[isON].on()
            secondstoSleep = 0.5

            if ButtonRed.is_pressed:
                isON += 1
                secondstoSleep -= 0.1
                if secondstoSleep < 0.1:
                    secondstoSleep = 0.1
                if isON > 4:
                    isON = 4
                for i in range(isON):
                    led[i].on
            elif ButtonBlue.is_pressed:
                isON -= 1
                secondstoSleep += 0.1
                if secondstoSleep > 0.5:
                    secondstoSleep = 0.5
                if isON < 0:
                    isON = 0
                for i in range(isON):
                    led[i].off
            if ButtonRed.is_pressed and ButtonBlue.is_pressed:
                startgame()



# Run following code when the program starts
if __name__ == '__main__':

    initgame()
    print('Main Terminating...')
