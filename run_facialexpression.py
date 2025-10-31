from pimaker import model

if __name__ == "__main__":
    face = model("facialexpression")
    face.OpenCamera()

    while True:
        face.TrackExpression()
        if face.StopAll('f'):
            break

    face.Close()
