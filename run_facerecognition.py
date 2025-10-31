from pimaker import model

if __name__ == "__main__":
    draw = model("facerecognition")
    draw.OpenCamera()

    print("Press 'a' to add a new face to dataset.")
    print("Press 'f' to stop the program.")

    while True:
        signal = draw.Draw()

        # These signals come from FaceRecognition.Draw()
        if signal == "add":
            name = input("Enter the person's name: ")
            draw.add_new_face(name)
            draw.load_dataset()  # retrain after adding

        elif signal == "stop":
            break

    draw.Close()
