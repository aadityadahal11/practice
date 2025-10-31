from pimaker import model

if __name__ == "__main__":
    sleep = model("sleepdetection")
    sleep.OpenCamera()

    while True:
        sleep.TrackSleep()
        if sleep.StopAll('f'):   # Press F to stop everything
            break

    sleep.Close()