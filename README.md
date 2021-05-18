# Facebook's DETR object detection
Automatic localization and classification of thoracic abnormalities from chest radiographs for the VinBigData Chest X-ray Abnormalities Detection Kaggle competition using <a href="https://github.com/facebookresearch/detr">Facebook DETR's detection</a>.

<b><H3> Input Datasets: </b> </H3>
A) <b> Image dataset:</b> <a href="https://www.kaggle.com/corochann/vinbigdata-chest-xray-original-png?select=train_meta.csv">(test and train folder)</a>  
18000 images (train set: 15000 images, test set: 3000 images)

The image dataset includes 14 types of thoracic abnormalities from chest radiographs as well as images with no abnormality detected (no finding). The different labels are as follows: <br/>
0 - Aortic enlargement <br/>
1 - Atelectasis <br/>
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

B) <b>Image metadata</b>  <a href="https://www.kaggle.com/c/vinbigdata-chest-xray-abnormalities-detection/data">(train.csv)</a>  
the train set metadata, each row represents an abnormality of one image, its class and bounding box. Some images can contain multiple abnormalities.

<b> <H3> Prerequisites:</b></H3>
Running the DETR model requires the use of a GPU and <b> Kaggle's notebook environment </b> can provide that. <br/>
The code of this repository can be also found in this Kaggle's public notebook. 

OR 

1) Download the notebook from this repository <br/>
2) Upload it in Kaggle's notebook environment and before start running it  <br/>
3) Click on the "Add data" button and add the data from the "VinBigData Chest X-ray Abnormalities Detection" competition  <br/>
4) Add the data from the "vinbigdata-chest-xray-original-png"  <br/>
5) Run the notebook (it might take approximately 8 hours to train the model) <br/>

For the training: <br/>
1) Run the function "model_training()" which gives as an output the trained model "detr_model.pth" <br/>

For the testing: <br/>
1) Load the "detr_model.pth" as a new dataset in Kaggle's environment <br/>
2) Go to the main notebook <br/>
3) Click on the "Add data" button and search the model by the URL of the "detr_model.pth" and add it to the data  <br/>

C) <b>Results</b>

Learning curve
<a href="https://github.com/stamatelou/DETR_object_detection/blob/main/training_validation_curve.jpg"><img src="https://github.com/stamatelou/DETR_object_detection/blob/main/training_validation_curve.jpg"  width="350" ></a>   

Mean average precision 
<a href="https://github.com/stamatelou/DETR_object_detection/blob/main/map_curve.jpg"><img src="https://github.com/stamatelou/DETR_object_detection/blob/main/map_curve.jpg"  width="350" ></a>    
                                                                                                                              
