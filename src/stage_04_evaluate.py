from sklearn.model_selection import train_test_split
from src.utils.all_utils import read_yaml,create_directory, save_local_df,save_reports
from sklearn.linear_model import ElasticNet
import argparse
import pandas as pd
import joblib
import os
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import numpy as np

def evaluate_metrics(actual_value,predicted_value):
    rmse = np.sqrt(mean_squared_error(actual_value,predicted_value))
    mae = mean_absolute_error(actual_value,predicted_value)
    r2 = r2_score(actual_value,predicted_value)
    return rmse,mae,r2

def evaluation(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    test_data_filename = config['artifacts']['test']

    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    test_data = pd.read_csv(test_data_path)


    test_y = test_data["quality"]
    test_x = test_data.drop("quality",axis = 1)

    model_dir =  config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_filename']# for joining the artifacts directory 
    model_path = os.path.join(artifacts_dir,model_dir,model_filename)


    print("model_filename",model_path)
    loaded_model = joblib.load(open(model_path, 'rb'))
    result = loaded_model.score(test_x,test_y)
    
    predicted_value = loaded_model.predict(test_x)

    rmse , mae,r2 = evaluate_metrics(test_y,predicted_value)

    report_dir = config['artifacts']['report_dir']
    reports_filename = config['artifacts']['reports']
    report_dir_path = os.path.join(artifacts_dir,report_dir)

    create_directory([report_dir_path])
    
    report_dir_filepath = os.path.join(report_dir_path,reports_filename)


    # reports_file_path = os.path.join(report_dir_path)

    reports={"rmse": rmse,
                  "mae":mae,
                  "r2":r2}

    save_reports(reports,report_dir_filepath)
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default= "config/config.yaml")
    args.add_argument("--params","-p",default= "params.yaml")

    parsed_args = args.parse_args()
    print(parsed_args.config)


    evaluation(config_path = parsed_args.config,params_path = parsed_args.params)

