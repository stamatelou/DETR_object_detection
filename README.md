# Facebook's DETR object detection: 
Automatic localization and classification of thoracic abnormalities from chest radiographs for the VinBigData Chest X-ray Abnormalities Detection Kaggle competition. 

<b> Input Datasets: </b>
The provided images include 14 types of thoracic abnormalities from chest radiographs as well as images with no abnormality detected (no object). 
0 - Aortic enlargement </>
1 - Atelectasis
2 - Calcification
3 - Cardiomegaly
4 - Consolidation
5 - ILD
6 - Infiltration
7 - Lung Opacity
8 - Nodule/Mass
9 - Other lesion
10 - Pleural effusion
11 - Pleural thickening
12 - Pneumothorax
13 - Pulmonary fibrosis
14 - no object 



1) 18,000 images annotated by 3 radiologists (train set: 15000, test set: 3000) 
2) 

train.csv - the train set metadata, with one row for each object, including a class and a bounding box. Some images in both test and train have multiple objects.



Step #1: 
Download the dataset from the Data section of the [Kaggle competition][https://www.kaggle.com/c/vinbigdata-chest-xray-abnormalities-detection/data?select=test] or open the notebook in kaggle's notebook section, click on the "Add data" and 
