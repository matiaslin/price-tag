Author: Matias Lin
Date: 03/27/2019

Description: This program will allow you to see the prices of the houses you are
walking around.

======= Getting the Estimates ========

1. Accessing the WebPage:

In order to access the web page we need the URL.

Sample URL:
https://www.zillow.com/homes/for_sale/globalrelevanceex_sort/

Following this first section, we should add the coordinates, all X, Y, and Z
values. For instance: 
33.052342,-117.201119,32.96453,-117.353039_rect
Note that it should end with "X,Y,Z_rect"

After the coordinatees we should add the zoom factor:
/X_zm/
I recommend 18_zm, because this will give you at most 6 houses to check around
your circle.

2. Reading the Estimates

Sequence (Plan A):
  - Click on one property
  - Read the Estimated price
  - Close the opened tab
Sequenceee (Plan B):
  - Read directly from the label of the buttons
  Cons: Sometimes it doesn't say the price. It just says "2 units". 
  Check:
  https://www.zillow.com/homes/for_sale/globalrelevanceex_sort/33.021608,-117.275532,33.020236,-117.277464_rect/18_zm/

2.B.1) Using Tesseract OCR with Python. We should first takke aa screenshot of
the page and the run the text recognition. Problem: We would have to select the
are where to run the text recognition.

#2.A.1) Getting clickers in:
#Once we accessed the webpage correctly and have it responsive to our real time
#location, we need to set 2-4 clickers soo that we can click on the houses.
#Note: There's no need to click on the buttons. We can just hover over the
#properties and it will allow us to select it.
