# xps-smart-origin
Origin script (Labtalk + Embedded Python) to import and analyze XPS data generated from the SMART software.

## Table of contents:
- [Requirements](#requirements-)
- [How to install SMART](#how-to-install-smart-)
- [How to generate: 2) dat files from the dispersive plane HDF-4 files of SMART(IDL)](#how-to-generate--2--dat-files-from-the-dispersive-plane-hdf-4-files-of-smart-idl--)
- [How to install: 4) Embedded (origin) Python packages](#how-to-install--4--embedded--origin--python-packages-)
- [How to run for the first time](#how-to-run-for-the-first-time-)
- [How to run for the next time](#how-to-run-for-the-next-time-)
- [Successfull run](#successfull-run-)
- [How to change the input parameters for data analysis](#how-to-change-the-input-parameters-for-data-analysis-)
- [Common issues](#common-issues-)

## Author
1) The different scripts to import, export, and analyse data were written by:<br>
Lucas de Souza Caldas <br>
ldesouzacaldas@gmail.com<br>
In the case of using these scripts, the author should be in the Acknowledgments section of your paper. In the case of a more direct contribution, the author should be included as an author in your upcoming paper.
2) The SMART program was written by Thomas Schmidt et al.

## Changelog



## Requirements
1) SMART(IDL).
2) dat files generated through SMART (analysis --> dispersive plane --> with saving single cross-sections.
3) Origin pro 2021b (9.85) and above. https://www.originlab.com/index.aspx?go=SUPPORT&pid=3325
4) Embedded (origin) Python packages:<br>
  a) originpro<br>
  b) numpy<br>
  c) pandas<br>
  d) python-dateutil<br>
  e) pytz<br>
  f) scipy<br>
  g) six<br>  
5) Latest version of "XPS_import_v" coppied into your originlab user files folder. For instance: "\Documents\OriginLab\User Files". 
6) Follow the How to run for the first time section of this README.

## How to install SMART
1) Install the IDL virtual machine 6.1.<br>
a) Create an account at:<br>
https://www.l3harrisgeospatial.com/Company/Create-Account?returnurl=%2fProduct-Downloads<br>
b) Wait until your account is approved.<br>
c) Download IDL 6.1.<br>
d) If these steps don´t work, contact us.<br>
2) Copy and paste the "Start.sav" (SMART) in any folder of your computer.

## How to generate: 2) dat files from the dispersive plane HDF-4 files of SMART(IDL)
Follow the video tutorials in:
https://www.youtube.com/watch?v=JYyRREdR35U&list=PLHerV2cxrTb8_BMmp7CxpvhuTCDJTOV3S

## How to install: 4) Embedded (origin) Python packages
1) Origin-->Connectivity tab on origin-->Python Packages.<br>  
![image](https://user-images.githubusercontent.com/42618468/230044368-e53bc0a3-60bb-4c04-a5e9-bcf2cea19bda.png)<br>  
2) Install-->Package Names-->Follow the blue-worded-instruction-->Ok.<br>  
![image](https://user-images.githubusercontent.com/42618468/230045835-3f662a4d-5688-4553-8610-0e64ac552e9f.png)<br>  

## How to run for the first time
1) Origin--> Import Multiple ASCII.<br> 
![image](https://user-images.githubusercontent.com/42618468/230052843-2ff83562-2a3c-45f9-a10f-9da7e80456ff.png)<br>  
2) Go to the folder with your DAT files--> Select them all--> Add File(s).<br> 
![image](https://user-images.githubusercontent.com/42618468/230053332-b6a1b302-e8d4-492b-bd6b-37358518aa10.png)<br>  
3) Change the default settings to the ones highlighted by red boxes.
4) Add the text inside the txt "labtalk-script-v" in the input box (Script after All files Imported). Be aware to use the same version as the "XPS_import_v".<br> 
![image](https://user-images.githubusercontent.com/42618468/230055577-5e2cd8f0-66c4-4c8f-b6cb-f4d6c6c9bb89.png)<br>  
5) Save as default or as a different theme. If you save as a different theme, you will have to load this during each import of the data.<br> 
![image](https://user-images.githubusercontent.com/42618468/230056742-1c7393b1-7061-4dea-a228-ec29ce182d9e.png)<br>  
6) Press Ok to save the theme.
7) Press Ok to to run the program.

## How to run for the next time
1) Origin--> Import Multiple ASCII.<br> 
2) Go to the folder with your DAT files--> Select them all--> Add File(s).<br> 
3) Only if it was not saved in default, Select the theme that you saved.
4) Press Ok to to run the program.

## Successfull run
A successfull run will create a workbook with 4 spreadsheets and a scriptwindow saying the number of columns which were created: 
1) The first one contains the raw data (only y values). From this spreadsheet you can select the columns which contain the e-beam information. You can copy these columns to a new workbook, and create an x axis, by typing in "F(X)=" i-1 . You can plot these data (after averaging-see youtube videos) and get the e-beam value.
![image](https://user-images.githubusercontent.com/42618468/230058626-e5046ac4-cc88-4743-8cae-55f14dc8fcb9.png)
2) The second spreadsheet is called Result_BE_correction, which contains the data with the X axis added, which is the corrected binding energy axis.
3) The third spreadsheet is called Result_intensity_correction, which contains the data after some corrections to the y axis, due to inhomogeneities of the camera.
4) The fourth spreadsheet is the parameters one, in which you can add the values from the labbook. Please, dont add new columns, or new files. Read the next section on how to alter these values.

## How to change the input parameters for data analysis
You can simply alter any number and all the data will be updated automalically in the other spreadsheets. You should change the ug value, photon energy, e-beam, and time columns. The other columns change the correction factors we use to treat the raw data. Ask for advice, or watch the youtube videos.<br>  
![image](https://user-images.githubusercontent.com/42618468/230059556-79e9f563-5e17-43bc-a9b2-2ddd35e6effb.png)<br>  

## Common issues
1) The number of files you can import is limited. With each file being a single acquisition. For instance we can measure 5 images of 1s each. Therefore these data will contain 5 files. The maximum value of files you can import for "XPS_import_v10" is 210.
