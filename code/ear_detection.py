"""
Module: EAR Detection
Detects eye aspect ratio (EAR) using eye landmarks.
"""

from scipy.spatial import distance as dist

def compute_ear(eye):
    """
    Calculates the Eye Aspect Ratio (EAR).
    
    Args:
        eye (list of tuples): 6 eye landmark points [(x1, y1), ..., (x6, y6)]
    
    Returns:
        float: EAR value
    """
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


if __name__ == "__main__":
    sample_eye = [(1, 2), (2, 3), (3, 4), (1, 5), (2, 6), (3, 7)]
    ear = compute_ear(sample_eye)
    print("EAR:", ear)
