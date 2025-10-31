from pimaker import model

if __name__ == "__main__":
    pose = model("poseestimation")
    pose.OpenCamera()

    while True:
        pose.TrackPose()
        if pose.StopAll('f'): 
            break

    pose.Close()