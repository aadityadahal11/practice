from pimaker import model

if __name__ == "__main__":
    hv = model("handvolume")
    hv.OpenCamera()

    while True:
        hv.AdjustVolume()
        if hv.StopAll('f'):
            break

    hv.Close()