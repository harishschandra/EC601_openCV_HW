# EC601_openCV_HW

Exercise 1

Question 1:

CvMat is used to represent the pixels of an image in a matrix form. We can access these pixel values using the cvMatName.at(x,y), where x=0, y=0 will be the top left entry of the matrix.

Exercise 2

Question 1:

In the Cb image, the spatial resolution of the image is reduced because the human eye is more perceptible to the luminance part of an image. This is done to save bandwidth. In the Cb image the image is formed by taking the difference between the blue component and the luminance of the image. In the Cb image, the darker colors are highlighted, such as the baboon’s red nose and yellow eyes. The Cr image looks like the inverted image of Cb where the lighter colors are highlighted, such as the blue colored area around the nose of the baboon. The red, green and blue images show the picture with the respective colors highlighted. The saturation picture tells us about the amount of gray in a particular color.

Question 2:

R[20][25] = 225 										                                                                                                G[20][25] = 122 									               
B[20][25] = 106 										                       
Y[20][25] = 151 										                
Cb[20][25] = 181 									                 
Cr[20][25] = 103		 							
H[20][25] = 4 				
S[20][25] = 135 	
V[20][25] = 225 
The pixel values range from 0 to 255

Exercise 4

Question 1:

The output shows us the original picture after different thresholding techniques are used. The binary thresholding output seems to be inverted to the banded threshold output. The adaptive threshold output seems to be a combination of the banded and binary threshold output. The thresholded output keeps the features of the face relatively intact except for the nose area.

Question 2:

Binary Thresholding, as the name implies, only keeps the pixel values that are greater than the threshold value and rejects all others. Because of this, it can’t represent the details of pictures with varying lighting, such as the details of foreground and background, for example, and hence a lot of information will be lost.

Question 3:

Adaptive thresholding is advantageous because we can apply many thresholds at the same time. In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.




