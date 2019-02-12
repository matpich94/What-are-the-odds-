"""
This is the function to display the probability of 
the falcon millenium to reach Endor without being captured
"""

def result_image(prob):
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw 
    import time
    import os, glob
    
    fontsize = 40
    font = ImageFont.truetype("arial.ttf", fontsize) #Warning: this font might not be uploaded on your computer. 
    
    if prob == 0:
        img = Image.open("images/dark_vador.jpg")
        draw = ImageDraw.Draw(img)        
        draw.text((0, 200),"Too Late...\n" + "You have " + str(prob) + " % chance of success",(255,255,255), font = font)
        
    else :
        img = Image.open("images/falcon.jpg")
        draw = ImageDraw.Draw(img)
        draw.text((0, 425),"You have " + str(prob) + " % chance of success" + "\n" + "May the force be with you !",(255,255,255), font = font)   
        
        
    if not os.path.isdir('static'):    
        os.mkdir('static')
        
    # remove all the previous pictures stored
    else:
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser can find
    plotfile = os.path.join('static', str(time.time()) + '.png')
    img.save(plotfile)
    return (plotfile)
