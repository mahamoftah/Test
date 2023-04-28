from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from flask import Flask
object = Flask(__main__)

@object.route('detect')
def detectObjects():
    key = "078e943cda2145bf9866e5fe8668faa6"
    endpoint = "https://other-apis.cognitiveservices.azure.com/"
    text = ""
    list = []
    numOfDuplicates = {}
    noDuplicatesList = set()
    computerVision = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUi3aScDQX-j9EZyAoJII2mp7ArMAe9TYY5w&usqp=CAU"

    object_detect = computerVision.detect_objects(image_url)

    print(object_detect)
    for object in object_detect.objects:
        list.append(object.object_property)
        noDuplicatesList.add(object.object_property)
    for i in noDuplicatesList:
        numOfDuplicates[i] = list.count(i)
    for key in numOfDuplicates:
        text = text + " " + str(numOfDuplicates[key]) + " " + key
    return text


'''
list = ['car', 'car', 'car', 'person', 'cat', 'cat']
noDuplicatesList = ['car', 'person', 'cat']
numOfDuplicates = \
    {
        'car': 3,
        'person': 1,
        'cat': 2
    }
'''







'''     if text.find(object.object_property) != -1:
            print(text.find(object.object_property))
            continue
        if len(object_detect.objects) == count + 1:
            text = text + " and " + object.object_property
        else:
            text = text + object.object_property
        count = count + 1
'''
