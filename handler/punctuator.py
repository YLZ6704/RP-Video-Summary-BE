from punctuator import Punctuator

def handlePunctuation(text):
    #Punctuatoråº“
    #https://drive.google.com/drive/folders/0B7BsN5f2F1fZQnFsbzJ3TWxxMms
    p = Punctuator('Demo-Europarl-EN.pcl')
    return p.punctuate(text)