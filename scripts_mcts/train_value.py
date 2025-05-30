import yaml
import os
from train.value_trainer import ValueTrainer

########################################################
i = 6
os.environ["CUDA_VISIBLE_DEVICES"] = "7"
########################################################s

def main():
    with open("train/config_value.yaml", "r") as f:
        config_value = yaml.safe_load(f)

    config_value['model_name'] += str(i)
    config_value['dataset_file'] += str(i)
    config_value['plot_path'] += str(i)
    config_value['hub_model_id'] += str(i+1)

    config_value['learning_rate'] = 5e-6
    config_value['per_device_train_batch_size'] = 256
    config_value['gradient_accumulation_steps'] = 4
    config_value['logging_steps'] = 1

    value_trainer = ValueTrainer(config_value)
    value_trainer.train()

if __name__ == "__main__":
    main()







