from input import input
from finder import finder
from window import window
from process import process

def main():
    input.init()
    window.displayBDO()
    #finder.detectionTest()
    process.start()
    #input.getCoords()

    print("Hello")

if __name__== "__main__":
  main()