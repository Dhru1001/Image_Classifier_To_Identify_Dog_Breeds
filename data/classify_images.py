#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Dhrumil Shah
# DATE CREATED: 17/07/2024                               
# REVISED DATE: 17/07/2024         
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        # TODO: 3a. Use the classifier function to get the model_label
        # Construct the full path to the image file
        img_path = images_dir + key
        # Use the classifier function to get the model_label
        model_label = classifier(img_path, model)

        # TODO: 3b. Process the model_label
        # Convert to lowercase and remove leading/trailing whitespace
        model_label = model_label.lower().strip()

        # defines truth as pet image label 
        truth = results_dic[key][0]

        # TODO: 3c. If there's a match between pet image label and classifier label
        if truth in model_label:
            # Add model_label and 1 (indicating a match) to results_dic
            results_dic[key].extend([model_label, 1])

        # TODO: 3d. If there's no match between pet image label and classifier label
        else:
            # Add model_label and 0 (indicating no match) to results_dic
            results_dic[key].extend([model_label, 0])

    # No return needed as results_dic is modified in place