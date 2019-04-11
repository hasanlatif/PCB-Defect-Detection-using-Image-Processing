# PCB Defect Detection Using Image Processing
* System uses canny edge detection algorithm to get edges on test and ground-truth imaeg .After getting the edges, Just use the bitwise xor operation to get the defects in pcb.
* Canny Edge Detector firstly applies gaussian filter to remove any unwanted noise.Then it finds the intensity gradients to get edges.
* XOR Truth Table

![](https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/xor.png)

# Results
![](https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/Result.png)



# Limitations: 
* This  system is not ment to use for Industrial Puprose.
# Note:
  * Waiting for your suggestions.If you find any lag in documentation in any ways,shoot me an email at hasanlateef@outlook.com
  * This code requires scikit-image,numpy and matplotlib in order to give the output




