from sklearn.model_selection import train_test_split
from src.utils.all_utils import read_yaml,create_directory, save_local_df
from sklearn.linear_model import ElasticNet
import argparse
import pandas as pd
import os

def split_and_save_data(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    train_data_filename = config['artifacts']['split_data_dir']["train"]

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    train_data = pd.read_csv(train_data_path)   # load the training data via path directory
    print(train_data.head())
    train_x = train_data["quality"]
    train_y = train_data.drop("quality",axis = 1)

    random_state = params['base']['random_state']
    alpha =  ["model_params"]["ElasticNet"]["alpha"]
    l1_ratio =  ["model_params"]["ElasticNet"]["l1_ratio"]
    
    lr = ElasticNet(alpha = alpha,L1_ratio = l1_ratio,random_state = random_state)
    lr.fit(train_x,train_y)
    print("done")


    if __name__ == '__main__':
        args = argparse.ArgumentParser()
        args.add_argument("--config","-c",default= "config/config.yaml")
        args.add_argument("--params","-p",default= "params.yaml")

        parsed_args = args.parse_args()
        print(parsed_args.config)


        split_and_save_data(config_path = parsed_args.config,params_path = parsed_args.params)

