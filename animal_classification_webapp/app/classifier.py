from tensorflow.keras.models import load_model
import os
import cv2
from django.core.files.storage import default_storage
from django.conf import settings
import numpy as np
class Classifier:
    
    def preprocess_image(image_path,target_size=(224,224)):
        image=cv2.imread(image_path)
        image=cv2.resize(image,target_size)
        image = image.reshape((1,) + target_size + (3,))
        return image
    
    def predict_class(image_path):
        # Load the model
        model_path = os.path.join('G:\OneDrive - northsouth.edu\CODES\PROJECTS\PROJECT - Animal Classification\Models\cnn_model.h5')
        model = load_model(model_path)
        
        image_storage=default_storage.save('tmp/'+image_path.name,image_path)
        
        image_storage_path=os.path.join(settings.MEDIA_ROOT,image_storage)
        
        preprocessed_image=Classifier.preprocess_image(image_path=image_storage_path)
        
        prediction=model.predict(preprocessed_image)
        predicted_class = np.argmax(prediction, axis=1)
        
        default_storage.delete(image_storage_path)
        
        labels={'aardvark': 0, 'albatross': 1, 'alligator': 2, 'alpaca': 3, 'ant': 4, 'anteater': 5, 'antelope': 6, 'ape': 7, 'armadillo': 8, 'baboon': 9, 
         'badger': 10, 'bat': 11, 'bear': 12, 'bee': 13, 'beetle': 14, 'bird': 15, 'bison': 16, 'boar': 17, 'bull': 18, 'butterfly': 19, 'camel': 20, 
         'capybara': 21, 'cat': 22, 'caterpillar': 23, 'cattle': 24, 'cheetah': 25, 'chicken': 26, 'chimpanzee': 27, 'cow': 28, 'coyote': 29, 'crab': 30, 
         'crocodile': 31, 'crow': 32, 'deer': 33, 'dog': 34, 'dolphin': 35, 'donkey': 36, 'dragonfly': 37, 'duck': 38, 'eagle': 39, 'echinda': 40, 
         'elephant': 41, 'elk': 42, 'emu': 43, 'ferret': 44, 'fish': 45, 'flamingo': 46, 'fly': 47, 'fox': 48, 'frog': 49, 'giraffe': 50, 'goat': 51, 
         'goldfish': 52, 'gorilla': 53, 'grasshopper': 54, 'hamster': 55, 'hedgehog': 56, 'hippopotamus': 57, 'horse': 58, 'jellyfish': 59, 'kangaroo': 60, 
         'koala': 61, 'ladybugs': 62, 'lion': 63, 'lizard': 64, 'lobster': 65, 'manatee': 66, 'meerkat': 67, 'mongoose': 68, 'monkey': 69, 'mouse': 70, 
         'octopus': 71, 'ostrich': 72, 'otter': 73, 'owl': 74, 'oyster': 75, 'panda': 76, 'parrot': 77, 'penguin': 78, 'pig': 79, 'pigeon': 80, 
         'polar bear': 81, 'porcupine': 82, 'rabbit': 83, 'raccoon': 84, 'rat': 85, 'reindeer': 86, 'rhinoceros': 87, 'seahorse': 88, 'seal': 89, 'shark': 90, 
         'sheep': 91, 'shrimp': 92, 'snail': 93, 'snake': 94, 'squid': 95, 'squirrel': 96, 'starfish': 97, 'swan': 98, 'tiger': 99, 'turkey': 100, 
         'turtle': 101, 'whale': 102, 'wolf': 103, 'wombat': 104, 'zebra': 105}
        
        labels = dict((v,k) for k,v in labels.items())
        prediction = [labels[k] for k in predicted_class]
        
        return prediction[0]


