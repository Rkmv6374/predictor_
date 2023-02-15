# this file is used to extract all the important funxtion  
import numpy as np 
import pandas as pd
import json
import joblib

data_col_= None
location_= None
model_= None


def get_estimated(location,sqft,bhk,bath):
     
     input_format = np.zeros(len(data_col_))
     i=0  
     for key  in data_col_:
        if key==location:input_format[i]=1
        elif key=='total_sqft':input_format[i]=sqft
        elif key=='bath':input_format[i]=bath
        elif key=='bhk':input_format[i]=bhk
        else: input_format[i]=0
        i = i+1
     return round(model_.predict([input_format])[0],2)
     


def get_upload():


    with open("./models_file/columns.json",'rb') as f:
         global data_col_
         global location_
         global model_
         json_str = f.read()
         data_col_ = json.loads(json_str)['data_columns']
         not_place =['bhk','total_sqft','bath']
         temp=[]
         for val in data_col_:
              if val not in not_place: temp.append(val)
         location_ = temp
    
    with open('./models_file/predictor.joblib','rb') as f:
         model_ = joblib.load(f)
    
    print('get upload occured along with coloumns and model is imported successfully!')

def get_location():
     return location_

def get_data_col():
     return data_col_


         


if __name__ == "__main__":
     get_upload()
     print(get_location())
     print(get_data_col())
     print(get_estimated('1st Phase JP Nagar',1000, 3, 3))
     print(get_estimated('1st Phase JP Nagar', 1000, 2, 2))

