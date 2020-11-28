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

def vis_history(history): 
    fig, ax = plt.subplots(1, 2, figsize=(15,5))
    ax[0].set_title('loss')
    ax[0].plot(history.epoch, history.history["loss"], label="Train loss")
    ax[0].plot(history.epoch, history.history["val_loss"], label="Validation loss")
    ax[1].set_title('acc')
    ax[1].plot(history.epoch, history.history["acc"], label="Train acc")
    ax[1].plot(history.epoch, history.history["val_acc"], label="Validation acc")
    ax[0].legend()
    ax[1].legend()