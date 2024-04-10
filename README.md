# QR Code Generator

This project is a simple QR code generator that creates a QR code for a given phone number. The generated QR code is saved as an SVG file named "myContactQR.svg".

## Requirements

* Python 3.x
* pyqrcode library

## Installation

To install the required library, run the following command:

```
pip install pyqrcode
```

## Usage

1. Run the Python script.
2. Enter your phone number when prompted.
3. The QR code will be generated and saved as an SVG file named "myContactQR.svg".

## Example

```
$ python qr_generator.py
Enter your Phone number: 1234567890
```

This will generate a QR code for the phone number 1234567890 and save it as "myContactQR.svg".


## Screenshot


## Notes

* The QR code is generated using the pyqrcode library.
* The generated QR code is saved as an SVG file for high-quality output.
* The scale of the QR code can be adjusted by changing the `scale` parameter in the `qr.svg()` function.

## License

This project is licensed under the MIT License.
