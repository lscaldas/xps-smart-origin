# xps-smart-origin
Origin script (Labtalk + Embedded Python) to import and analyze XPS data generated from the SMART software.

## Requirements:
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

## How to install 4) Embedded (origin) Python packages:
Origin-->Connectivity tab on origin-->Python Packages<br>  
![image](https://user-images.githubusercontent.com/42618468/230044368-e53bc0a3-60bb-4c04-a5e9-bcf2cea19bda.png)
