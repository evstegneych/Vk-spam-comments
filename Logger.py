import logging

"""Console colors"""
PINK = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
PULSE = '\033[35m'

logging.basicConfig(format='[%(asctime)s] %(message)s',
                    #filemode='at',
                    #filename='Yui_Bot.log',
                    level=logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(message)s')
console.setFormatter(formatter)
#logging.getLogger('').addHandler(console)


def printColored(string, color):
    logging.info("{}{}{}".format(color, string, ENDC))

def Plog(msg):
    printColored(msg, PINK)

def Rlog(msg):
    printColored(msg, RED)

def Ylog(msg):
    printColored(msg, YELLOW)

def Glog(msg):
    printColored(msg, GREEN)

def Blog(msg):
    printColored(msg, BLUE)

def Wlog(msg):
    printColored(msg, BOLD)

def Linelog(msg):
    printColored(msg, UNDERLINE)

def Pulselog(msg):
    printColored(msg, PULSE)