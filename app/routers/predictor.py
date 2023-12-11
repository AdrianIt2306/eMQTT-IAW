import json
import logging
import pandas as pd
from typing import Dict
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
logging.basicConfig(filename='eMQTT-IAPI.log', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d | %(message)s')

class Predictor:

    def analyze_packet(self, clf: DecisionTreeClassifier,clfrf:RandomForestClassifier,modelmlp:MLPClassifier,gnb:GaussianNB,modelgb:GradientBoostingClassifier,clf_knn:KNeighborsClassifier, raw_packet: Dict):
        mapping={0: 'dos', 1: 'legitimate'}
        validation = False
        results = []
        try:
            dfonline = pd.DataFrame.from_dict(raw_packet,orient='index')
            dfonline = dfonline.transpose()
            dfonline=dfonline.astype('category')
            cat_columns_train = dfonline.select_dtypes(['category']).columns
            dfonline[cat_columns_train] = dfonline[cat_columns_train].apply(lambda x: x.cat.codes)
            x_columns = dfonline.columns
            x_online = dfonline[x_columns].values
            logging.debug("Predicting Decision Tree")
            y_pred_online_dt = clf.predict(x_online)
            logging.debug("Predicting Random Forest")
            y_pred_online_rf  =  clfrf.predict(x_online)
            logging.debug("Predicting MultiLayer Perceptron")
            y_pred_online_mlp  =  modelmlp.predict(x_online)
            logging.debug("Predicting Nayve Bayes")
            y_pred_online_nb  =  gnb.predict(x_online)
            logging.debug("Predicting GradienBoost")
            y_pred_online_gb  =  modelgb.predict(x_online)
            logging.debug("Predicting KNN")
            y_pred_online_knn  =  clf_knn.predict(x_online)
            y_pred_online_names_dt = [mapping[i] for i in y_pred_online_dt]
            y_pred_online_names_nb =  [mapping[i] for i in y_pred_online_nb]
            y_pred_online_names_rf =  [mapping[i] for i in y_pred_online_rf]
            y_pred_online_names_mlp =  [mapping[i] for i in y_pred_online_mlp]
            y_pred_online_names_gb =  [mapping[i] for i in y_pred_online_gb]
            y_pred_online_names_knn =  [mapping[i] for i in y_pred_online_knn]

            logging.debug("{:<20}  {:<20}  {:<20}  {:<20}      {:<20}   {:<20}   {}".format("*************" ,"***********","*************","*********************","************","***********", "*****************"))
            logging.debug("{:<20}  {:<20}  {:<20}  {:<20}      {:<20}   {:<20}   {}".format("Decision Tree" , "Nayve Bayes" ,"Random Forest", "MultiLayer Perceptron","GradienBoost" ,"    KNN    ", "Comparison result"))
            logging.debug("{:<20}  {:<20}  {:<20}  {:<20}      {:<20}   {:<20}   {}".format("*************" ,"***********","*************","*********************","************","***********", "*****************"))
            for idx in dfonline.index:
                validation = (y_pred_online_rf[idx] == y_pred_online_nb[idx] == y_pred_online_dt[idx] == y_pred_online_mlp[idx] == y_pred_online_gb[idx] == y_pred_online_knn[idx])
                logging.debug("{:<20}  {:<20}  {:<20}  {:<20}       {:<20}   {:<20}   {}".format(y_pred_online_names_dt[idx],y_pred_online_names_nb[idx],y_pred_online_names_rf[idx],y_pred_online_names_mlp[idx],y_pred_online_names_gb[idx],y_pred_online_names_knn[idx],validation))

            classifiers = ['Decision Tree', 'Nayve Bayes', 'Random Forest', 'MultiLayer Perceptron', 'GradienBoost', 'KNN']
            predictions = [y_pred_online_names_dt, y_pred_online_names_nb, y_pred_online_names_rf, y_pred_online_names_mlp, y_pred_online_names_gb, y_pred_online_names_knn]

            for idx in range(len(predictions[0])):  # Asume que todas las listas de predicciones tienen la misma longitud
                result = {}
                for classifier, prediction_list in zip(classifiers, predictions):
                    result[classifier] = prediction_list[idx]
                results.append(result)
                json_str = json.dumps(result)
                json_str_without_slashes = json_str.replace("\\", "")
                logging.debug(json_str_without_slashes)
            return json_str_without_slashes
        except Exception as e:
            logging.debug(e)
            result = {"error": "error"}
            return json.dumps(result)