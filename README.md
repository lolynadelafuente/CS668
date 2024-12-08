# Predicting Wind Speeds of Storms in the Atlantic and East Pacific Oceans using NASA IMPACT team and Radiant Earth Foundation satellite images

Lolyna de la Fuente Ordaz

* *This work was realized as part of the capstone project of the MS in Data Science at Pace University.*
* **Abstract:** Tropical cyclones are one of the costliest natural disasters globally. Determining an accurate tropical cyclone intensity helps better initialization in forecast models, leading to more accurate forecasts, more accurate historical records of tropical cyclones and providing consistent intensity estimates. The goal of this project is motivated by the contribution to public safety by improving storm predictions by apply machine learning and statistical models, potentially helping communities prepare for and respond to natural disasters.

* **Dataset:**
   * The training data consists of single-band satellite images from 494 different storms from 2000 to 2019 in the Atlantic and East Pacific Oceans, prepared by the NASA IMPACT team and Radiant Earth Foundation.
   * The train set consists of  70,257 images and the test set consists of 44,377 images.
   * Each image is 366x366 pixels containing 4 features and 1 label.
   * The dataset is available here: [Tropical Cyclone Wind Estimation Competition](https://source.coop/repositories/nasa/tropical-storm-competition/access)
* **Methodology:**
  - The first step was the access to the dataset using S3 Client to make a copy of the Source Cooperative repository containing all images and .csv files.
  - Then, a short EDA was conducted since what we are more interested in are the images and the data frames don’t hold that much information for a complete analysis.
  - After, a preprocessing of the data was applied before the model creation. We confirmed all images were the same size as well as we joined both training csv files together.
  - Then, a development of a deep learning model for objective estimation of tropical cyclone intensity using a pretrained convolutional neural network (CNN) on the satellite images. We used this approach as creating a new CNN from scratch would be too time consuming as well as the training.
  - Lastly, an extensive evaluation of the deep learning model and analysis of how well the model estimates wind speeds was performed. To calculate the loss in the model we used the Root-Squared Mean Error (RSME).
* **Results:**
  - 
* **Poster** (as an image)
