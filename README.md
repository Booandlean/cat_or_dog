# README

## Table of contents

[Notebooks](https://github.com/Booandlean/cat_or_dog/tree/master/Notebooks) 

*Contains .ipynb notebooks and src file with helper methods*

--- [Data_prep_plus_FSM.ipynb](https://github.com/Booandlean/cat_or_dog/blob/master/Notebooks/Data_prep_plus_FSM.ipynb)
    
    *Contains organization of data, EDA, and the FSM*

--- [Final_Notebook.ipynb](https://github.com/Booandlean/cat_or_dog/blob/master/Notebooks/Final_Notebook.ipynb)

    *Contains discussion of data, modeling process, and results*
    
--- [Modeling.ipynb](https://github.com/Booandlean/cat_or_dog/blob/master/Notebooks/Modeling.ipynb)

    *contains all models (minus the fsm) and discussion of modeling*

--- [src.py](https://github.com/Booandlean/cat_or_dog/blob/master/Notebooks/src.py)

[Visualizations](https://github.com/Booandlean/cat_or_dog/tree/master/Visualizations)

*Contains image files used in final notebook*

[.gitignore](https://github.com/Booandlean/cat_or_dog/blob/master/.gitignore)

*ingores pycache, model names, and .jpg files*

[README](https://github.com/Booandlean/cat_or_dog/blob/master/README.md)

*you are here :)*

## Goal:

This project aims to make a image classification model that can determine if an image contains a cat or a dog.

## About the data

This dataset was taken from an old kaggle competition that can be found [here](https://www.kaggle.com/c/dogs-vs-cats). The images are from an old CAPTCHA known as *Animal Species Image Recognition for Restricting Access* (or *Asirra* for short) which asked the user to identify whether or not several images displayed contained either a cat or a dog.

There are 25,000 images total evenly split between cats(0) and dogs(1). 

## How do I use this?


## Results

While delta did perform better than alpha in terms of accuracy score (.89 vs .83), what cannot be ignored is that delta labeled signifigantly more images as 'cat' or 0 and is therefor biased towards that class, while 'dog' or 1 was under represented. Alpha may have a lower accuracy score, but it does not show any signifigant evidence of bias, which is why I am choosing it as the final model. 

## Next Steps

You may notice while looking through 'Modeling' and 'Final_Notebook' that there is no evidence of a test set being used. As this is a kaggle competition there was a test set but the images were not labeled. In the future I will grab 100-200 images from the unlabeled test set and manualy label them cat or dog to get a score out of 100-200 on its test accuracy to produce a proper accuracy score. 