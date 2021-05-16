# Facebook's DETR object detection
Automatic localization and classification of thoracic abnormalities from chest radiographs for the VinBigData Chest X-ray Abnormalities Detection Kaggle competition. 

1) Input Datasets
2) Modeling 
3) Visualization 

<b><H3> Input Datasets: </b> </H3>
1) <b> Image dataset:</b>  18000 images (train set: 15000 images, test set: 3000 images)

The image dataset includes 14 types of thoracic abnormalities from chest radiographs as well as images with no abnormality detected (no finding). The different labels are as follows: <br/>
Aortic enlargement [label 0] <br/>
Atelectasis [1] <br/>
Calcification [2] <br/>
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

2) <b>Image metadata</b>- the train set metadata, each row represents an abnormality of one image, its class and bounding box. Some images can contain multiple abnormalities.



<b> <H4> Prerequisites:</b></H4>
Running the DETR model requires the use of a GPU and <b> Kaggle's notebook environment </b> can provide that. <br/>
Download the notebook from this repository, upload it in Kaggle's notebook environment and brfore start running it  <br/>
1) Click on the "Add data" button and add the data from the "VinBigData Chest X-ray Abnormalities Detection" competition  <br/>
2) Add the data from the "vinbigdata-chest-xray-original-png"  <br/>
