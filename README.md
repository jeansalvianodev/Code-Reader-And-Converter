<h1 align="center">
<br>
  <img src="https://i.imgur.com/75HuSbS.png" alt="Code Reader and Converter" width="300">
<br>
<br>
<b>Code Reader and Converter</b>
</h1>

<p align="center"><b>Scan your code and convert straight from an image!</b></p>



[//]: # (Add your gifs/images here:)
<div align="center">

  <img src="https://i.imgur.com/HKIbY9I.gif" alt="demo" height="480">
  
</div>

<hr />

## <b>What does it do?</b> 
The code reader and converter (QR Code and Barcode) is able to find the code in an image, return the result, and, if desired, convert it to a different type.

## <b>Getting started</b>

### - <b>You'll need to install the following libraries</b>


- **PySimpleGUI** — A Python package that enables Python programmers of all levels to create GUIs.
- **OpenCV-Python** — A Python Library that provides a real-time optimized Computer Vision library, tools, and hardware. It also supports model execution for Machine Learning (ML).
- **QRCode** — A pure python QR Code generator.
- **Pillow** — A Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.
- **Python-Barcode** — A Python library that provides a simple way to create barcodes in Python.
- **Pyzbar** — A pure Python library that reads one-dimensional barcodes and QR codes using the zbar library.


``` 
pip install PySimpleGUI
pip install pyzbar
pip install opencv-python
pip install qrcode
pip install Pillow
pip install python-barcode
```
### <b>Notes</b>: 
- Do not remove the image "logo.png"
- The software will not always be able to find the barcode in the image, so it will be necessary to cut and leave only the code in the image (this problem does not happen with qrcode).
- Is necessary to remove any type of accent from the name of the image that will be decoded, so that there is no error in the path.
- Although possible, converting a QR code to an EAN13 barcode makes it invalid, so think carefully (This doesn't happen when converting to a QR code).
