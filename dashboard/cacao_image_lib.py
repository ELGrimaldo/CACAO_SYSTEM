from .models import CacaoImages
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

class CacaoImageFunctions:
    
    def deleteImages():
        images = CacaoImages.objects.all()
        image_keys = []
        for image_key in images:
            image_keys.append(image_key.pk)
            print(CacaoImages.objects.get(pk=image_key.pk).delete(), 'images')
        return image_keys
    
    def getImages():
        images = []
        for image in CacaoImages.objects.all():
            images.append(str(CacaoImages.objects.get(pk=image.pk).upload))
        return images 
        
    def predictImages():
        
        # Load the saved model
        model = tf.keras.models.load_model('DNN_model_image/best_model.h5')

        # Directory containing multiple images
        images_dir = 'static/media/images'

        # Dictionary to store filenames and their corresponding predictions
        predictions_dict = {}

        # Iterate through images in the directory
        for filename in os.listdir(images_dir):
            if filename.endswith('.JPG') or filename.endswith('.png'):  # Filter for image file extensions
                img_path = os.path.join(images_dir, filename)

                # Pre-process the image
                img = image.load_img(img_path, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = img_array / 255.0

                # Make predictions
                predictions = model.predict(img_array)
                pred = predictions.tolist()
                print(pred.index(max(pred)))
                print(predictions[0])
                # Assuming the model does classification and returns class probabilities
                predicted_label = np.argmax(predictions, axis=1)  # Get the index of the class with the highest probability

                labels = {
                    '0': 'Fermented',
                    '1': 'Partially Fermented',
                    '2': 'Under Fermented',
                    '3': 'Unfermented'
                }
                
                # Store the filename and its predicted label
                predictions_dict[filename] = {
                    'Classification_Result': labels[str(predicted_label[0])], 
                    'Fermented':  "{:.2f}%".format(predictions[0][0]),
                    'Partially_Fermented': "{:.2f}%".format(predictions[0][1]),
                    'Under_Fermented': "{:.2f}%".format(predictions[0][2]),
                    'Unfermented': "{:.2f}%".format(predictions[0][3]),
                    }

        # Return predicted labels in dictionary
        # CacaoImageFunctions.delete_files_in_directory('media/images')
        return predictions_dict
    
    def delete_files_in_directory(directory):
        # List all files in the directory
        file_list = os.listdir(directory)

        # Iterate through the files and delete each one
        for file_name in file_list:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")