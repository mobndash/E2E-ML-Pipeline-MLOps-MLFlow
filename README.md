# E2E-ML-Pipeline-MLOps
This is an End to End ML project implementation with ML Ops.

```
E2E-ML-Pipeline-MLOps-MLFlow
├─ app.py
├─ config
│  └─ config.yaml
├─ Dockerfile
├─ dvc.yaml
├─ LICENSE
├─ main.py
├─ params.yaml
├─ ProjectSteps.md
├─ README.md
├─ requirements.txt
├─ research
│  └─ trials.ipynb
├─ schema.yaml
├─ setup.py
├─ src
│  └─ ML_MLOps_MLFlow_Pipeline
│     ├─ components
│     │  └─ __init__.py
│     ├─ config
│     │  ├─ configuration.py
│     │  └─ __init__.py
│     ├─ constants
│     │  └─ __init__.py
│     ├─ entity
│     │  ├─ config_entity.py
│     │  └─ __init__.py
│     ├─ pipeline
│     │  └─ __init__.py
│     ├─ utils
│     │  ├─ common.py
│     │  └─ __init__.py
│     └─ __init__.py
├─ template.py
└─ templates
   └─ index.html

```

```
https://dagshub.com/mobndash/E2E-ML-Pipeline-MLOps-MLFlow.mlflow

import dagshub
dagshub.init(repo_owner='mobndash', repo_name='E2E-ML-Pipeline-MLOps-MLFlow', mlflow=True)

Bucket Name : E2E-ML-Pipeline-MLOps-MLFlow
Endpoint URL : https://dagshub.com/api/v1/repo-buckets/s3/mobndash
Public Key Id : 8ba3f29223901e8f121aa24fe4e49db1d09adc15
Region : us-east-1

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

 ```

 export MLFLOW_TRACKING_URI=https://dagshub.com/mobndash/E2E-ML-Pipeline-MLOps-MLFlow.mlflow
 export MLFLOW_TRACKING_USERNAME=mobndash
 export MLFLOW_TRACKING_PASSWORD=8ba3f29223901e8f121aa24fe4e49db1d09adc15