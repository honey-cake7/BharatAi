import os
import subprocess

def compile_engine(onnx_path, engine_path):
    trtexec_bin = "/usr/src/tensorrt/bin/trtexec"
    if not os.path.exists(trtexec_bin):
        print("[Warn] trtexec not found. Run this script directly on the Jetson Orin.")
        return

    cmd = [
        trtexec_bin,
        f"--onnx={onnx_path}",
        f"--saveEngine={engine_path}",
        "--fp16"
    ]
    print(f"[TensorRT] Compiling {onnx_path} to {engine_path}...")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))
    onnx_file = os.path.join(models_dir, "model.onnx")
    engine_file = os.path.join(models_dir, "model.engine")
    compile_engine(onnx_file, engine_file)
