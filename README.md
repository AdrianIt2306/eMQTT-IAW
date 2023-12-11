# eMQTT-IA API

This is an implementation of the next classificators to use them in a web (API interface Decision Tree , Nayve Bayes , Random Forest , MultiLayer Perceptron , GradienBoost , KNN). To use it, the API receives a packet from TCP/IP in json format (dict), as response you'll receive a json with the result of the classificators.


## Setup

To setup the API, you must define the next parameters in the .env file which is located in the root of the app

- LOG_FILE : Contains the file which will be use to write all the messages defined in the code with the different kind of levels
- MODEL_PATH : Path of the folder which contain the models trainned
- DT,RF,MLP,NB,GB,KNN : The name of the file (model trainned)

```.env
LOG_FILE=eMQTT-IAPI.log
MODEL_PATH=C:\Users\itadr\OneDrive\Documentos\Development\trainned\
DT=${MODEL_PATH}decision_tree_ddos.pkl
RF=${MODEL_PATH}random_forest_ddos.pkl
MLP=${MODEL_PATH}multi_layer_perceptron_ddos.pkl
NB=${MODEL_PATH}naive_bayes_ddos.pkl
GB=${MODEL_PATH}gradienboost_ddos.pkl
KNN=${MODEL_PATH}knn_ddos.pkl

```

## Usage

### Request Example
```json
{
    "tcp_flags": "0x00000018",
    "tcp_time_delta": 0.000001,
    "tcp_len": 51,
    "mqtt_conack_flags": 0,
    "mqtt_conack_flags_rserved": 0,
    "mqtt_conack_flags_sp": 0,
    "mqtt_conack_val": 0,
    "mqtt_conflag_cleansess": 0,
    "mqtt_conflag_passwd": 0,
    "mqtt_conflag_qos": 0,
    "mqtt_conflag_reserved": 0,
    "mqtt_conflag_retain": 0,
    "mqtt_conflag_uname": 0,
    "mqtt_conflag_willflag": 0,
    "mqtt_conflags": 0,
    "mqtt_dupflag": 1,
    "mqtt_hdrflags": "0x0000003a",
    "mqtt_kalive": 0,
    "mqtt_len": 171,
    "mqtt_msg": 4.630456339613062e+203,
    "mqtt_msgid": 5754,
    "mqtt_msgtype": 3,
    "mqtt_proto_len": 0,
    "mqtt_protoname": 0,
    "mqtt_qos": 1,
    "mqtt_retain": 0,
    "mqtt_sub_qos": 0,
    "mqtt_suback_qos": 0,
    "mqtt_ver": 0,
    "mqtt_willmsg": 0,
    "mqtt_willmsg_len": 0,
    "mqtt_willtopic": 0,
    "mqtt_willtopic_len": 0
  }
```
### Response Example
```json
{
  "Decision Tree": "dos",
  "Nayve Bayes": "legitimate",
  "Random Forest": "dos",
  "MultiLayer Perceptron": "dos",
  "GradienBoost": "dos",
  "KNN": "dos"
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
