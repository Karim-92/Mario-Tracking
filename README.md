# Mario Tracking
A simple program to track Super Mario using OpenCV. The algorithm used is Template Matching.

Environment:
---
The program was tested using OpenCV 3.4, Python 3.5 on a Windows 10 machine.

Running the program:
---
1. Clone the repository, install the dependencies and build using `make` after navigating to the repository root folder.
2. [Download the video file.](https://drive.google.com/open?id=0B95Sp237mrsTT3drTlNPdElJOXlOb1gtQjBwWkNiZzBpTXlr)
3. Execute the following in your terminal:
```
python trackingMario.py
```
4. The result will be viewed onscreen as well as saved into the cloned folder.
5. You can take different crops of Super Mario and use them as templates to find out whichever template works best for you.

Algorithm Description:
---
+ The algorithm used is Template Matching. It's probably one of the least robust but also on the simplest. It basically works as a convolution where
it scans the image for a matching image to the given template. It can be made more robust via selecting a proper template, especially for videos.
+ The algorithm is known to be translation invariant, but if you try it with rotated objects it will fail horribly. Other more robust algorithms exist for that purpose such as keypoint matching.

Discussion:
---
+ Template matching can be more robust to different scales by taking many matches and selecting one with the highest correlation region (Image Pyramids could work in theory too).
+ Template matching expects grayscale images for both the template and the image on which it'll be scanned so it shouldn't be affected much by the difference in colors.