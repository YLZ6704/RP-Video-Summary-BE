from punctuator import Punctuator

def handlePunctuation(text):
    p = Punctuator('Demo-Europarl-EN.pcl')
    return p.punctuate(text)