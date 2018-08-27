# Simulacrum
A steganography program written in Python for the concealing of private keys in an image of the user's choice. Run the program again to extract the key.

Credit for the idea implemented goes to @elisklar on Medium, who presented the [_ImageHash_](https://medium.com/@elisklar/imagehash-easy-steganography-240b92b586e2) concept. 


# Requirements

The program relies on the Python Imaging Library (PIL), as well as pyqrcode and qrtools .

Install them from your command line like so:

```
pip install PIL
pip install pyqrcode
pip install qrtools
```

Replace the segments in double square brackets with the filenames of your desired images.

Currently takes a 64-character input (haven't really played around with different lengths yet). Can be used for any string of data, and isn't exclusive to private keys.

It's also possible to embed three different keys in a given image (one for each RGB value). I'll be looking into it.

The motivations for implementing the _ImageHash_ concept are part of an overarching attempt at ensuring Bitcoin can be used by those in highly adversarial environments.
