# PCB Defect Detection Using Image Processing

 A bunch of javascript functions which wraps around the [opencv_js](http://opencv.org/) functions to do image processing tasks more conveniently(without going to the details of image processing operations) at the client side of web application.

By this release,we can do translation,rotation and resizing(it take care of aspect ratio if required) in images.
# Lets talk about the functions currently available in imutils_js 
* ## Translation

```java script
translation(image,x,y)

/*image:on which translation is required
x:translation along x_axis
y:translation along y-axis
returns:output image which has to be shown in canvas element
*/
```
* ## Rotation

```java script
rotation(image,x,y)

/*image:on which rotation is required
angle:how much rotation(currently accepts value in degree)
center_x: x-Axis of rotation
center_y: y-axis of roatation
returns: output image which has to be shown in canvas element
*/
```


* ## Resizing

```java script
resize(image,x,y)

/*image:on which resizing is required
width:how much width is required.(if provided and height=0 resize the image by taking care of its aspect ratio )
height:how much height is required.(if provided and width = 0 ,resize the image by taking care of its aspect ratio)
           if both width and height are given resize the image by the given parameters.
returns: array of image,width_of_resized_image,height_of_resized_image.

*/
```
* # Demonstration

![](https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/git_gif.gif)

![](https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/arrow1.jpg)
![](https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/test%20_js.jpg)

 # How to use it?

* Download the whole package.Execute the  ``test.php`` in ``test`` folder through the server.
 
![]( https://github.com/hasanlatif/Snapchat-like-Filters-python/blob/master/Readme_pics/local_host.gif)

 see [this](https://github.com/hasanlatif/imutils_js/tree/master/test) example to test the package.


## Having problems?

If you run into problems, please read the [Common Errors](https://github.com/hasanlatif/imutils_js/wiki/Common-Errors) section of the wiki before filing a github issue.

## Thanks

* Many, many thanks to [opencv](https://opencv.org) for providing the actual implementation  of algorithm.
* This work is inspired from the work of [Dr.Adrian Rosbrock](https://github.com/jrosebr1/imutils),who actually did this in python
* Many Many Thanks to [affordis.pk](https://affordis.pk) who is sponsoring this work.


# Note:
  * Waiting for your suggestions.If you find any lag in documentation in any ways,shoot me an email at hasanlateef@outlook.com




