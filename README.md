# A traffic sign recognition task based on Yolo version 5, for electronic system design course in UCAS
-----
Contributors: Y. F. Chen, S. P. Fu, T. Li, G. X. Yang, H. Y. Zhang.  
-----
This repository contains code for electronic system design course in the spring 2024 semester, UCAS. The code implements the recognition of eight traffic signs using YOLOv5 model to simulate Chinese motor vehicle driver's test subject 3. 

We deployed the model into Jetson Nano Developer Kit from NVIDIA, while using tensorRTx to improve the inference speed on the development board. 

We utilized some open source traffic signage datasets, including CCTSDB from Changsha University of Technology and TT100K from Tsinghua University and Tencent, then selected the required images from them. After training, the recognition accuracy for each sign are all above 0.85. 

Any questions please email: shipingfuucas@gmail.com
