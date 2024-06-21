# mlops-zoomcamp


- [X] 01-intro
    - [X] setup environment
    - [X] download data
    - [X] added training notebook
    - [X] done homework

- [X] 02-experiment-tracking
    - [X] setup mlflow
    - [X] do experiment tracking
    - [X] Model tracking
    - [X] Model Registry
    - [X] Launch tracking server:- mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root artifacts

- [X] 03-orchestration
    - [X] setup mage: ```git clone https://github.com/mage-ai/mlops.git```
    - [X] run mage server: ```cd 03-orchestration/mlops && scripts/start.sh```
    - [X] unit_1_data_preparation
        - [X] make pipeline
        - [X] data ingestion
        - [X] data transformation
        - [X] data visualization
        - [X] data exporters
    - [X] unit_2_training
        - [X] sklearn models: hyperparameter tuning
        - [X] sklearn models: training models with best hyperparameters
        - [X] XGBoost model: hyperparameter tuning
        - [X] XGBoost model: training model with best hyperparameters
    - [ ] unit_3_observability
        - didn't did all the charts and deployment

- [X] 04-deployment
- [X] 05-monitoring
    - [X] Environment setup(conda activate py11)
    - [X] Prepare reference data and model
    - [X] Evidently metrics calculation
    - [X] Evidently dashboard
    - [X] Grafana dashboard with dummy data
    - [X] Grafana Dashboard with real data
    - [X] Saved dashboard to config json file
    - [X] Evidently ReportPreset and TestSuitePreset
         
## Useful Stuff

- Tool to download github sub directory: https://download-directory.github.io/
- Module 3 sorted video playlist: https://www.youtube.com/playlist?list=PLJlrBE4yPIzg9W9LaAp-3DOtZ9JnDd23J
- Docker remove all cache: ```docker system prune -a```
- conda deactivate