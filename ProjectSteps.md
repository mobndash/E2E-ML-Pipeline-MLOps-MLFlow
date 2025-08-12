1) Create a project template.py

2) Create a setup.py

3) Create a logger file, a custom logging file under src -> ML_MLOps_MLFlow_Pipeline -> __init__.py

4) Create a utils file, a custom file that reads common functions across the project e.g read a YAML file, save object, read object etc under
        src -> ML_MLOps_MLFlow_Pipeline -> utils -> common.py
        read_yaml()
        save_json()
        load_json(), etc

5) Below is the workflow for this project :
    ### WorkFlow
            1. Update config.yaml --config related to dataset filepath, directories for data_ingestion
            2. Update schema.yaml
            3. Update params.yaml
            4. Update the entity --
            5. Update the configuration manager in src config
            6. Update the components
            7. Update the pipeline
            8. Update the main.py
            9. Update the app.yaml

6) Update constants -> __init__.py with the CONFIG_FILE_PATH, PARAMS and SCHEMA and import them to data ingestion

7) Perform data ingestion in research -> data_ingestion.ipynb

8) Udate data_ingestion.py and stage_data_ingestion.py

9) Enter config for data_validateion in config.yaml file

10) Update the schema.yaml according to dtypes of the data

11) Update everything as per he workflow in step 5

12) Perform data transformaition in research -> data_transformation.ipynb

13) Enter config for data_transformation in config.yaml file

14) Update everything as per he workflow in step 5 i.e config_entity, configuration.py, data_transformation.py under components, stage_data_transformation.py under pipeline, 
                main.py
