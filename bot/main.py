from input import input
from finder import finder
from window import window
from process import process

def main():
    input.init()
    window.displayBDO()
    process.start()
    #finder.detectionTest()
    #input.getCoords()

if __name__== "__main__":
  main()