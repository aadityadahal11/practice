from pimaker import model

if __name__ == "__main__":
    smile = model("smilecapture")
    smile.OpenCamera()

    while True:
        smile.DetectSmile()
        if smile.StopAll('f'):
            break

    smile.Close()