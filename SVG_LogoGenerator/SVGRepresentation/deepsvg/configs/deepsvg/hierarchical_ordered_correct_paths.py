from .default_icons import *
import os


class ModelConfig(Hierarchical):
    def __init__(self):
        super().__init__()

        self.label_condition = False
        self.use_vae = False


class Config(Config):
    def __init__(self, num_gpus=2):
        super().__init__(num_gpus=num_gpus)

        datafolder = "../../../SVG_Data/"   # Make sure to set this to where your SVG_Data folder is located

        self.model_cfg = ModelConfig()
        self.model_args = self.model_cfg.get_model_args()

        self.dataloader_module = "deepsvg.svgtensor_dataset"
        self.data_dir = os.path.join(datafolder, "data_for_training_deepsvg_model/icons_tensor/")
        self.meta_filepath = os.path.join(datafolder,  "data_for_training_deepsvg_model/icons_meta.csv")
        
        self.filter_category = None

        self.learning_rate = 1e-3 * num_gpus
        self.batch_size = 60 * num_gpus

        self.val_every = 2000
