# HemoPynamic App
A single page desktop application for calculation of common hemodynamic equations.

## Introduction
HemoPynamic has been written in python language using **PyQt5** module. \
Using concept of `BoxLayout` to arrange sections of the app.  

![App main window](images/hemoPynamic.png "HemoPy GUI")  

## How to use
### **Run Distributed version**    
You can download distribution version of the app from the link bellow and go to `dist` directory and open ***HemoPy*** file.  

[HemoPy Distribution Version](https://drive.google.com/drive/folders/1_7By4Yms85XvC2QTSMnhCembRtPQIDT9?usp=drive_link)  
At the moment only linux executable distribution version is available.  

### **Run by python**    
You can clone repo by github CLI:

```
git clone https://github.com/hedayatbehnam/hemoPynamic
```
or using website link to download **zip** folder.
\
\
![zip download image](images/zip_download.png "zip download")
\
\
If you are in linux, you should use `unzip` command in terminal to extract its contents.

  
Then install dependencies:


```
pip install -r requirements.txt
```



To run app type following command in terminal in app main dir:

```
python entry.py
```
