from pimaker import model

if __name__ == "__main__":
    sign = model("signlanguage")
    sign.OpenCamera()

    while True:
        sign.DetectSign()
        if sign.StopAll('f'):
            break

    sign.Close()
