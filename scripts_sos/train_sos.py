import yaml
import os
from train.policy_trainer import PolicyTrainer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--iter", type=int, required=True)
parser.add_argument("--gpu", type=int, required=True)
parser.add_argument("--epochs", type=int, required=True)
parser.add_argument("--b", type=int, required=False)
parser.add_argument("--e", type=int, required=False)
args = parser.parse_args()

########################################################
checkpoint = args.iter
os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu) 
########################################################s
if args.b is not None and args.e is not None:
    be_extension = f"_b{args.b}_e{args.e}"
else:
    be_extension = ""

def main():
    with open("train/config_sos.yaml", "r") as f:
        config_sos = yaml.safe_load(f)

    config_sos['model_name'] += str(checkpoint + 1) + be_extension + f"_epochs{24}"
    config_sos['dataset_file'] += str(checkpoint) + be_extension
    config_sos['plot_path'] += str(checkpoint) + be_extension
    config_sos['hub_model_id'] += str(checkpoint+1) + be_extension + f"_epochs{24 + args.epochs}"

    config_sos['learning_rate'] = 2e-5
    config_sos['per_device_train_batch_size'] = 16
    config_sos['gradient_accumulation_steps'] = 4
    config_sos['logging_steps'] = 1
    config_sos['num_train_epochs'] = args.epochs

    sos_trainer = PolicyTrainer(config_sos)
    sos_trainer.train()

if __name__ == "__main__":
    main()







