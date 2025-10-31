from pimaker import model

if __name__ == "__main__":
    eye = model("eyemouse")
    eye.OpenCamera()

    while True:
        eye.TrackEye()
        if eye.StopAll('f'):
            break

    eye.Close()