# Facebook's DETR object detection
Automatic localization and classification of thoracic abnormalities from chest radiographs for the VinBigData Chest X-ray Abnormalities Detection Kaggle competition. 

<b><H2> Input Datasets: </b> </H2> <br/>
1) Image dataset:  18000 images (train set: 15000 images, test set: 3000 images)

The image dataset includes 14 types of thoracic abnormalities from chest radiographs as well as images with no abnormality detected (no finding). The different labels are as follows: <br/>
0 - Aortic enlargement  <br/>
1 - Atelectasis  <br/>
2 - Calcification <br/>
3 - Cardiomegaly <br/>
4 - Consolidation <br/>
5 - ILD <br/>
6 - Infiltration <br/>
7 - Lung Opacity <br/>
8 - Nodule/Mass <br/>
9 - Other lesion <br/>
10 - Pleural effusion <br/>
11 - Pleural thickening <br/>
12 - Pneumothorax <br/>
13 - Pulmonary fibrosis <br/>
14 - No finding <br/>


2) 

train.csv - the train set metadata, with one row for each object, including a class and a bounding box. Some images in both test and train have multiple objects.



Step #1: 
Download the dataset from the Data section of the <a href="https://www.kaggle.com/c/vinbigdata-chest-xray-abnormalities-detection/data?select=test">Kaggle competition</a> or open the notebook in kaggle's notebook section, click on the "Add data" and 
