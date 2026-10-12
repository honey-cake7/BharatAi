import cv2
import json
import time
import os
from datetime import datetime

LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../shared/telemetry_stream.jsonl"))

def emit_defect(score, bbox, area_pct):
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "component_type": "metal_nut",
        "anomaly_score": round(score, 3),
        "threshold": 0.50,
        "defect_characteristics": {
            "category": "surface_scratch" if score < 0.8 else "structural_crack",
            "bounding_box": bbox,
            "affected_area_pct": round(area_pct, 2)
        }
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(payload) + "\n")
    print(f"[Vision Alert] Defect logged: Score={score}")

def main():
    print("[Vision] Camera capture pipeline started...")
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.5)
                continue
            
            # Simulated trigger for verification
            # Replace with TRT forward pass output
            time.sleep(2)
            emit_defect(0.87, [110, 45, 60, 55], 4.2)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()

if __name__ == "__main__":
    main()
