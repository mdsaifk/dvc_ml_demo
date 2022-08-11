from sklearn.model_selection import train_test_split
from src.utils.all_utils import read_yaml,create_directory, save_local_df
from sklearn.linear_model import ElasticNet
import argparse
import pandas as pd
import joblib
import os
import pickle

def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    train_data_filename = config['artifacts']['train']

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    train_data = pd.read_csv(train_data_path)   # load the training data via path directory
    
    train_y = train_data["quality"]
    train_x = train_data.drop("quality",axis = 1)

    random_state = params['base']['random_state']
    alpha =  params['model_params']['ElasticNet']['alpha']
    l1_ratio =  params['model_params']['ElasticNet']['l1_ratio']
    
    lr = ElasticNet(alpha = alpha,l1_ratio = l1_ratio,random_state = random_state)
    lr.fit(train_x,train_y)
    

    model_dir =  config['artifacts']['model_dir']

    model_dir =  os.path.join(artifacts_dir,model_dir)   # for joining the artifacts directory 

    model_filename = config['artifacts']['model_filename']
    model_path = os.path.join(model_dir,model_filename)

    create_directory([model_dir])
    
    # pickle.dump(lr, open(model_path, 'wb'))
    joblib.dump(lr ,model_path)
    print("done")

    # ##testing
  
    # test_data_filename = config['artifacts']['test']

    # test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    # test_data = pd.read_csv(test_data_path)

    # test_y = test_data["quality"]
    # test_x = test_data.drop("quality",axis = 1)

    # model_pathss = config['artifacts']['model_filename']

    # print("model_filename",model_pathss)
    # loaded_model = pickle.load(open(model_pathss, 'rb'))
    # result = loaded_model.score(test_x,test_y)
    # print(result)
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default= "config/config.yaml")
    args.add_argument("--params","-p",default= "params.yaml")

    parsed_args = args.parse_args()
    print(parsed_args.config)


    train(config_path = parsed_args.config,params_path = parsed_args.params)

