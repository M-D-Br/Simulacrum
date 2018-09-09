# Simulacrum
A steganography program written in Python for the concealing of strings (private keys, signed transactions) in an image of the user's choice. Run the program again to extract the key.

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

You'll notice two files – one takes 64-bit strings (i.e. private keys), whilst the second takes a longer input (i.e. signed transactions – it's set at 494 characters, though the numbers can easily be changed to accommodate more or less). Just make sure that the number of pixels in the concealing image exceeds that of the pixels in the generated QR code. 

It's also possible to embed three different keys in a given image (one for each RGB value). I'll be looking into it.

The motivations for implementing the _ImageHash_ concept are part of an overarching attempt at ensuring Bitcoin can be used by those in highly adversarial environments.
