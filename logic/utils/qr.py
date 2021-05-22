import pyqrcode


class Qr:
    def __init__(self, val):
        self.val = val

    def generate(self):
        print("Generating QR code")
        # Generate QR code
        url = pyqrcode.create(self.val)

        # Create and save the svg file naming "myqr.svg"
        url.svg("static/qr.svg", scale=8)
