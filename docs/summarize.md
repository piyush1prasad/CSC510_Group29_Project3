# About MyDollarBot's summarize.py file
The summarize.py file defines a custom PDF document class that allows users to generate a summary report containing multiple sections. These sections include a header, body, and footer, which can be populated with various content. The code sets up a PDF document and provides functions for adding content to different sections. The file also uses the math, fpdf, and PIL libraries for various operations.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/21Tulasi/MyDollarBot-newPhase/blob/main/code/summarize.py)

# Code Description
## Functions
1. PDF(FPDF):
   This class is a subclass of the FPDF class, extending it to create a custom PDF document. The PDF class defines functions for the header, footer, and chapter body, enabling users to customize the content and appearance of each section. It also provides functions for adding images to the document. The class allows for creating complex multi-page PDFs with different sections.

2. header(self):
   This function defines the content and styling for the header section of the PDF. It includes a background color, a title, and an image logo. The title is centered, and the image is positioned in the top right corner.

3. footer(self):
   This function sets up the footer section, displaying the page number at the bottom right corner of each page. It also defines the font and text color for the footer.

4. chapter_body(self, body, image_path):
   This function adds content to the body of a chapter within the PDF. It starts with a title, displays the main textual content, and adds an image next to the text. The function takes the text content (body) and an image file path (image_path) as parameters.

5. chapter_displaybody(self, data, data_image):
   This function adds content to display summaries in the PDF. It consists of a spending report for the day and month, including text and images. The text and images are aligned based on available space, and new pages are added if necessary.

6. chapter_estimatebody(self, data_day, data_month):
   This function adds content to estimate summaries in the PDF, including spending for the day and month. It follows a similar structure to other chapter functions.

7. chapter_asc_descbody(self, data_asc, data_desc):
   This function adds content to show summaries of spending in ascending and descending order of the spent amount. Like the other chapter functions, it arranges text content accordingly.

# How to run this feature?
After you've added sufficient input data, use the /summary command and you can see the output in a spending_history_beautified.pdf . 
