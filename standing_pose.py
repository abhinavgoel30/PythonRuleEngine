from fastapi import APIRouter
import numpy as np
import mediapipe as mp
from pydantic import BaseModel
from typing import List
import keypoint_processor

router = APIRouter()

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose


class Keypoint(BaseModel):
    x: float
    y: float
    visibility: float


class PoseInput(BaseModel):
    landmarks: List[Keypoint]


class KeypointsProcessor:
    @staticmethod
    def extract_coordinates(keypoints):
        return keypoint_processor.Keypoints(keypoints)


def calculate_angle(a, b, c):
    a = np.array([a.x, a.y])
    b = np.array([b.x, b.y])
    c = np.array([c.x, c.y])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))  # Prevents NaN issues
    return angle


@router.post("/check_posture")
def check_full_posture(pose_input: PoseInput):
    if len(pose_input.landmarks) < 33:
        return {"feedback": "❌ Invalid input - Not enough keypoints"}

    keypoints = KeypointsProcessor.extract_coordinates(pose_input.landmarks)

    # Head Alignment
    shoulder_center_x = (keypoints.left_shoulder.x + keypoints.right_shoulder.x) / 2
    head_alignment = abs(keypoints.nose.x - shoulder_center_x)

    # Shoulder & Hip Symmetry
    shoulder_height_diff = abs(keypoints.left_shoulder.y - keypoints.right_shoulder.y)
    hip_height_diff = abs(keypoints.left_hip.y - keypoints.right_hip.y)

    # Feet Position
    feet_distance = np.sqrt((keypoints.left_foot_index.x - keypoints.right_foot_index.x) ** 2 +
                            (keypoints.left_foot_index.y - keypoints.right_foot_index.y) ** 2)

    # Spine Alignment
    shoulder_hip_angle = calculate_angle(keypoints.left_shoulder, keypoints.left_hip, keypoints.left_knee)
    hip_knee_angle = calculate_angle(keypoints.left_hip, keypoints.left_knee, keypoints.left_ankle)

    # Dynamic Thresholds
    head_threshold = 0.02
    symmetry_threshold = 0.03
    vertical_threshold = (165, 190)
    feet_together_threshold = 0.12  # Feet together threshold, set to 0.12 as mentioned
    feet_hip_width_threshold = 0.18  # Hip-width apart threshold, slightly larger than feet_together_threshold

    # Determine if feet are together or hip-width apart
    if feet_distance <= feet_together_threshold:
        feet_position = "together"
    elif feet_distance <= feet_hip_width_threshold:
        feet_position = "hip_width"
    else:
        feet_position = "too_wide"
    print(feet_position)
    print(shoulder_hip_angle)
    print(hip_knee_angle)
    # Collect posture issues
    issues = []
    if head_alignment >= head_threshold:
        issues.append("⚠️ Adjust Head - Center it with shoulders")
    if shoulder_height_diff >= symmetry_threshold:
        issues.append("⚠️ Adjust Shoulders - Keep level")
    if hip_height_diff >= symmetry_threshold:
        issues.append("⚠️ Adjust Hips - Keep level")
    if feet_position == "too_wide":
        issues.append(f"⚠️ Feet are too wide - Distance: {feet_distance}")
        issues.append("⚠️ Bring Feet Closer Together")
    if shoulder_hip_angle < vertical_threshold[0]:
        issues.append("⚠️ Straighten Back")
    if hip_knee_angle < vertical_threshold[0]:
        issues.append("⚠️ Straighten Legs")

    if not issues:
        return {"feedback": "✅ Perfect Posture - Ready for Yoga"}

    return {"feedback": issues}

