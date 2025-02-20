class Keypoints:
    def __init__(self, keypoints):
        self.keypoints = keypoints

    @property
    def nose(self):
        return self.keypoints[0]

    @property
    def left_eye_inner(self):
        return self.keypoints[1]

    @property
    def left_eye(self):
        return self.keypoints[2]

    @property
    def left_eye_outer(self):
        return self.keypoints[3]

    @property
    def right_eye_inner(self):
        return self.keypoints[4]

    @property
    def right_eye(self):
        return self.keypoints[5]

    @property
    def right_eye_outer(self):
        return self.keypoints[6]

    @property
    def left_ear(self):
        return self.keypoints[7]

    @property
    def right_ear(self):
        return self.keypoints[8]

    @property
    def mouth_left(self):
        return self.keypoints[9]

    @property
    def mouth_right(self):
        return self.keypoints[10]

    @property
    def left_shoulder(self):
        return self.keypoints[11]

    @property
    def right_shoulder(self):
        return self.keypoints[12]

    @property
    def left_elbow(self):
        return self.keypoints[13]

    @property
    def right_elbow(self):
        return self.keypoints[14]

    @property
    def left_wrist(self):
        return self.keypoints[15]

    @property
    def right_wrist(self):
        return self.keypoints[16]

    @property
    def left_pinky(self):
        return self.keypoints[17]

    @property
    def right_pinky(self):
        return self.keypoints[18]

    @property
    def left_index(self):
        return self.keypoints[19]

    @property
    def right_index(self):
        return self.keypoints[20]

    @property
    def left_thumb(self):
        return self.keypoints[21]

    @property
    def right_thumb(self):
        return self.keypoints[22]

    @property
    def left_hip(self):
        return self.keypoints[23]

    @property
    def right_hip(self):
        return self.keypoints[24]

    @property
    def left_knee(self):
        return self.keypoints[25]

    @property
    def right_knee(self):
        return self.keypoints[26]

    @property
    def left_ankle(self):
        return self.keypoints[27]

    @property
    def right_ankle(self):
        return self.keypoints[28]

    @property
    def left_heel(self):
        return self.keypoints[29]

    @property
    def right_heel(self):
        return self.keypoints[30]

    @property
    def left_foot_index(self):
        return self.keypoints[31]

    @property
    def right_foot_index(self):
        return self.keypoints[32]

class KeypointsProcessor:
    def extract_coordinates(self, keypoints):
        return Keypoints(keypoints)