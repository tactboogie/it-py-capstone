Capstone: IT Automation Python Program by Google
Supplier Data Report
Author: Torrey Adams, Copilot, Gemini, Tabnine, QuickLab


Objective

I work for an online fruit store, and need to develop a system that will update the catalog information 
with data provided by the suppliers. The suppliers send the data as large images with an associated 
description of the products in two files (.TIF for the image and .txt for the description). 
The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML 
file that shows the image and the product description. The contents of the HTML file need to be uploaded 
to a web service that is already running using Django. 

I also need to gather the name and weight of all fruits from the .txt files and use a Python request to 
upload it to your Django server. I need to create a Python script that will process the images and 
descriptions and then update your company's online website to add the new products. When the task is 
complete, the supplier should be notified with an email that indicates the total weight of fruit 
(in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and 
its total weight (in lbs) in a table.

Finally, in parallel to the automation running, I want to check the health of the system and send an 
email if something goes wrong. 


Goals

Write a python script that summarizes and processes sales data into different categories 
Write a python script that generates a PDF
Write a python script that automatically sends the PDF by email
Write a python script to check the health status of the system


Things to remember:

Break the problem down into smaller pieces.
Write unit tests to make sure that each new part of the solution works.
Use version control Git (Github)
Code should be written with 2 space indents.


Modules

PIL, Requests, ReportLab, emails, psutil, shutil, smtplib, unittest


Milestones

1. Setting up the environment: Install Python3 and Conda. Set up a new Conda environment and install the 
necessary modules: PIL, Requests, ReportLab, emails, psutil, shutil, smtplib, and unittest.

2. Processing the supplier data: Write a script that reads the .txt files and extracts the name and 
weight of the fruits. Convert the weight to lbs if necessary.

3. Image processing: Write a script that uses PIL to open the .TIF images, resize them, and save them as .jpeg.

4. Creating the HTML file: Write a script that takes the product description and the path to the image, 
and writes an HTML file that displays this information.

5. Uploading to the Django server: Write a script that uses the Requests module to upload the HTML file 
to your Django server.

6. Generating the PDF: Write a script that uses ReportLab to generate a PDF that contains a table with 
the name of the fruit and its total weight.

7. Sending the email: Write a script that uses the emails module to send an email to the supplier. 
The email should contain the total weight of the uploaded fruit and have the PDF attached.

8. System health check: Write a script that uses psutil and shutil to check the system’s health. 
If something goes wrong, use smtplib to send an email alert.

9. Unit testing: For each part of your solution, write unit tests that ensure it works as expected.

10. Version control: Initialize a Git repository in your project directory. Make regular commits and 
push your changes to GitHub.
