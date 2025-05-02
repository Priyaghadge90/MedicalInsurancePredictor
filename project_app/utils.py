import numpy as np
import pandas as pd

import project_config

import pickle
import json

class MedicalInsurance():
    def __init__(self):
        pass

    def load_model(self):
        """This method is used to load linear regression model

        """
        with open(project_config.MODEL_FILE_PATH,"rb") as f:
            self.lin_reg_model=pickle.load(f)

        self.feature_names=self.lin_reg_model.feature_names_in_
        return self.feature_names
    

    def load_json_data(self):
        """ This method is used to load  data from json files.
            Data:
            Label encoding data
            one hot encoding data
        """

        with open (project_config.Label_encoded_data_path,"r") as f:
            self.column_encoded_data=json.load(f)
            return self.column_encoded_data
        
    def get_data_from_user(self):

        self.load_model()
        self.load_json_data()

        age=eval(self.data["age"])
        bmi=eval(self.data["bmi"])
        children=int(self.data["children"])
        smoker=self.data["smoker"]
        gender=self.data["gender"]
        region=self.data["region"]

        test_array=np.zeros((1,self.feature_names.size))

        test_array[0,0]= age
        test_array[0,1]= self.column_encoded_data["gender"][gender]
        test_array[0,2]= bmi
        test_array[0,3]=children
        test_array[0,4]=self.column_encoded_data["smoker"][smoker]

        region= f"region_{region}"
        region_index=np.where(self.feature_names==region)[0][0]

        test_array[0,region_index]=1
        self.df_test=pd.DataFrame(test_array,columns=self.feature_names)

        print(self.df_test)

    def predict_charges(self,data):
        self.data=data
        self.get_data_from_user()
        prediction=self.lin_reg_model.predict(self.df_test)[0]
        print("predicted charges is:",np.around(prediction,3))
        return prediction
    




        