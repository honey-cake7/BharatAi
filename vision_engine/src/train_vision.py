import os
from anomalib.data import MVTecAD
from anomalib.models import EfficientAd
from anomalib.engine import Engine
from anomalib.deploy import ExportType

def main():
    print("[Vision] Initializing EfficientAD-M Training...")
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
    export_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))
    os.makedirs(export_dir, exist_ok=True)

    datamodule = MVTecAD(root=data_dir, category="metal_nut", train_batch_size=1, eval_batch_size=1)
    model = EfficientAd(model_size="small")
    engine = Engine(max_epochs=70)

    engine.fit(model=model, datamodule=datamodule)

    engine.export(
        model=model,
        export_type=ExportType.ONNX,
        datamodule=datamodule,
        export_root=export_dir
    )
    print(f"[Vision] Training done. ONNX exported to: {export_dir}")

if __name__ == "__main__":
    main()
