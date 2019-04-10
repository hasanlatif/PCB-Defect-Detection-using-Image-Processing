from skimage import io, feature, color
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
ground_truth_img = io.imread('ground_truth.png')   #Reading ground truth image
gray_ground_truth_img = color.rgb2gray(ground_truth_img)  #Converting image to gray scale
edges_ground_truth = feature.canny(gray_ground_truth_img, sigma=3) #Canny Edge Detector
test_img = io.imread('test.png')     ##Reading Test image
gray_test_img = color.rgb2gray(test_img)  #Converting image to gray scale
edges_test_img = feature.canny(gray_test_img, sigma=3) # Getting Edges of test image
result = np.bitwise_xor(edges_ground_truth, edges_test_img)  # see xor truth table table
plt.subplot(131)
plt.imshow(ground_truth_img, cm.gray)
plt.xlabel('Orignal PCB')
plt.subplot(132)

plt.imshow(test_img, cm.gray)
plt.xlabel('Faulty PCB')
plt.subplot(133)

plt.imshow(result, cm.gray)
plt.xlabel('Faults Detected')
plt.show()

