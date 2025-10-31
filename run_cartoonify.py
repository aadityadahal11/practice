from pimaker import model

if __name__ == "__main__":
    draw = model("cartoonify")()   # <-- Notice the extra () to create an instance
    draw.OpenCamera()

    while True:
        draw.Draw()
        if draw.StopAll('f'):
            break

    draw.Close()
