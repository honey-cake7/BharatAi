from anomalib.engine import Engine
from anomalib.models import EfficientAd
from anomalib.data import MVTecAD

def main():
    print("[Vision] Initializing Testing Phase...")
    
    # 1. Setup the dataset for evaluation
    datamodule = MVTecAD(root="data", category="metal_nut", eval_batch_size=1)
    
    # 2. Initialize the EfficientAD model architecture
    model = EfficientAd(model_size="small")
    
    # 3. Initialize the Engine
    engine = Engine()
    
    # 4. Point to the latest successfully trained checkpoint
    ckpt_path = "results/EfficientAd/MVTecAD/metal_nut/latest/weights/lightning/model.ckpt"
    print(f"[Vision] Loading weights from: {ckpt_path}")
    
    # 5. Run the built-in test suite
    engine.test(
        model=model,
        datamodule=datamodule,
        ckpt_path=ckpt_path
    )

if __name__ == "__main__":
    main()