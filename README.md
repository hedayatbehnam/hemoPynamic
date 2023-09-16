# HemoPynamic App
A single page desktop application for calculation of common hemodynamic equations.

## Introduction
HemoPynamic has been written in python language using **PyQt5** module. \
Using concept of `BoxLayout` to arrange sections of the app.  

![App main window](images/hemoPynamic.png "HemoPy GUI")  

## How to use
1. Distributed version  
You can download distribution version of the app from the link bellow and go to `dist` directoryand open `HemoPy` file.  
At the moment only linux executable distribution version is available.  

2. Using python  
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
If you are in linux, you should use `unzip` command in terminal.
___
  
Then install dependencies:


```
pip install -r requirements.txt
```



To run app type following command in terminal in app main dir:

```
python entry.py
```
