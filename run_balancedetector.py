from pimaker import model

if __name__ == "__main__":
    draw = model("balancedetector")
    draw.OpenCamera()

    while True:
        draw.Draw()
        if draw.StopAll('f'):
            break

    draw.Close()