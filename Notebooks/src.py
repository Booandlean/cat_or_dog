def data_prep():

    import numpy as np
    import pandas as pd 
    import matplotlib.pyplot as plt
    import random
    import os
    import seaborn as sns
    from PIL import Image
    
    data_path = '../Data/train'
    
    filenames = os.listdir(data_path)
    labels = []
    
    for filename in filenames:
        label = filename.split('.')[0]
        if label == 'dog':
            labels.append(1) #1 for dog
        else:
            labels.append(0) #0 for gat-0
        
    df = pd.DataFrame({
    'filename': filenames,
    'label': labels
    })

    df['label'] = df['label'].replace({0:'cat', 1:'dog'})
    
    return df

def avg_size() #might wanna use it later, also good practice to get this as a method

    width = []#these guys should have been here
    height = [] 
    
    for filename in filenames:
    #ooh I made an error with this part, I reset the lists every time, this is why I got such clean numbers for the avg's
    
    data_path = '../Data/train'#will expand this later
    
        img_path = os.path.join(data_path, filename)
        im = Image.open(img_path)
    
        w, h = im.size
    
        width.append(w)
        height.append(h)
    
    w_avg = sum(width)/len(width)
    h_avg = sum(height)/len(height)
    
    width = int(w_avg)
    height = int(h_avg)
    img_size = (width, height)
    
    return img_size