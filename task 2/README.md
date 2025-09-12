# TASK 2:
# For task 2, I first loaded the data 
# I then loaded tensorflow, matplotlib, numpy, layers, sequential and other libraries
# I split the data into 50000 training and 10000 testing based on the website.
# I converted the data type of the training data and testing data into float 32 because CNN works better with continuous float values
# I then divided the the data with 255 so that all the data ranges from 0 to 1
# For CNN I used TinyVGG Architecture which i found in the streamlit app online.
# I used 50 epochs per cnn model.
# For the augmentation model, I performed flips, roations and std normalisation
# I also standardized the testing data   
# Moving onto transfer learning
# I am using MobileNetV3 large because it is lighter than resnet 50 and has faster compute rates and good accuracy and doesnt burn my laptop
# MobileNet takes input in (96,96) format so i resized the training data
# I also used preprocess_input in ImageGenerator so that the input is processed in accordance to MobileNet
# I ran 30 epochs for transfer learning as they are more heavier than the CNN
# Final Accuracy of :
# CNN without augmentation: 98.78 %
# CNN with augmentation: 83.63 %
# Transfer model without augmentation : 99.18 %
# Transfer Model with augmentaion: 92.57%
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/e4e2ff8b-30e5-43d7-8bc2-334299093fcf" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/15dd5248-4300-4654-888a-fe30dfd1d651" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/e30c095e-5e2c-4a60-a1b3-3e378dfcd3e5" />
<img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/655a9243-b06b-4212-9e3c-7325ac388a40" />
# Please note that the accuracies maybe higher as i stopped the models before they completed all the epochs so as to save time and my laptop
# Hope you like this too :-)

