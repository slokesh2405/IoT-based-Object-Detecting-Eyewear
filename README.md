# 1. IoT-based-Object-Detecting-Eyewear
The Object Detecting Eyewear includes ESP32 Cam based Object Detection & Identification with OpenCV. We have used ESP32 Camera with FTDI Module. We also set up the Arduino IDE for the ESP32 Camera Module, uploaded the firmware, and then worked on the object detection & identification part. It enables us to capture live video feed and process it in real-time using OpenCV and cvlib libraries.
In the project, the MobileNet SSD model with a frozen graph is loaded into the system. The frozen graph provides the necessary network architecture and weights for object detection. The COCO dataset's class labels are used to identify and label the detected objects accurately.
The project implementation involves capturing a live video feed using a camera integrated into the eyewear. Each video frame is passed through the MobileNet SSD model, which performs object detection by analyzing the image and identifying objects present. The model outputs the bounding box coordinates, class labels, and confidence scores for each detected object.
Once the objects are detected, the eyewear system can provide audio feedback to the wearer about the identified objects. By converting the object detection results into audio feedback, the wearer can receive real-time information about the objects in their surroundings.
Additionally, the project involves storing the object detection results in a database for further analysis or logging. In this case, a MySQL database is used to store the class labels, confidence scores, and other relevant information for each detected object.
# 2. System Design
![Screenshot (59)](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/78da15fb-f145-4aea-a4c1-c9be802fdc4d)
# 3. System Implementation
3.1 ESP32 Camera Module and FTDI Connection

![p1](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/f2ed4ed6-235d-45e6-b6c2-debca49418c1) 

3.2 Wi-fi Connection (both laptop and ESP32 should be on same network)

![p2](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/513fd682-e80d-4271-9044-92cbf221cec5)

3.3 Hardware Connection (Adapter, TTL, ESP32, USB Cable)

![p3](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/3b1d41ae-6a4e-4ef3-ae8f-aab918a541ec)

3.4 Power supply (from adapter to ESP32 Cam)

![p4](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/f1ce9d3e-5754-472d-967c-a0f2393c0c76)

3.5 Detecting Mobile Phone

![p5](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/e4c3c6fb-826e-48f8-9974-7f820f3b3bff)

3.6 Detecting Bottle

![p6](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/44242ed1-6661-49df-9722-3a8effd32d87)

3.7 Detecting Chair

![p7](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/ead58d34-aa10-48ac-9487-56671782068b)

3.8 Database table (storing visited objects with date and time)

![p8](https://github.com/slokesh2405/IoT-based-Object-Detecting-Eyewear/assets/62741314/2ffc56dd-0956-4ea6-8aaf-c5138840981b)
