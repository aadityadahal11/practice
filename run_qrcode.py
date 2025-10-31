from pimaker import model

if __name__ == "__main__":
    qr = model("barcodeqr")
    qr.OpenCamera()

    while True:
        qr.ReadBarcodeQR()
        if qr.StopAll('f'):  
            break

    qr.Close()