
def getCellState(universe, x, y):
    """ 
    Return true if the cell from a run-length encoded pattern is alive
    """
    
    lines = 0
    cols = 0
    repeatCount = 0

    for cell in universe:
        if lines == x and cols == y:
            return cell == 'o'

        if cell == '$':
            if repeat == True:
                lines += repeatCount
            else:
                lines += 1

            cols = 0
            repeatCount = 0
            repeat = False
        elif cell in range(0, 9):
            repeatCount = cell
            repeat = True

            if repeat == True:
                repeatCount * 10
                repeatCount += cell
        else:
            if repeat == true:
                for i in range(repeatCount):
                    col += 1
                    if lines == x and cols == y:
                        return cell == 'o'
                repeatCount = 0
                repeat = False
                    
            



def metafy(universe, height, width, onCell, offCell):
    newPattern = [[0 for x in range(width)] for y in range(height)]

    for x in height:
        for y in width:
            if (getCellState(universe, x, y)) == True:
                applyMatrix(x * 2048 - 5, j * 2048 - 5, newPattern, onCell)
            else:
                applyMatrix(x * 2048 - 5, j * 2048 - 5, newPattern, offCell)
            
        

def loadCell(path):
    with open(patternPath, 'r') as f:
        return f.read() 


patternPath="pattern.rle"
meta_on = loadCell("metapixel-OFF.rle")
meta_off = loadCell("metapixel-ON.rle")
with open(patternPath, 'r') as f:
    for line in f:
        print line,


