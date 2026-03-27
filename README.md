IoT设备（传感器）
   ↓
Azure IoT Hub
   ↓
Azure Stream Analytics
   ↓
Azure Functions（Python）
   ↓
Azure Data Lake / Cosmos DB
   ↓
Azure Machine Learning（预测）
   ↓
Power BI（可视化）
Azure IoTを活用したスマートファクトリー向け予知保全システムを構築。
IoT Hubによりセンサーデータを収集し、Stream Analyticsでリアルタイム処理を実施。
Azure Functions（Python）でデータ処理および異常検知ロジックを実装。
Azure Machine Learningを用いて設備故障の予測モデルを構築。
Power BIにてダッシュボードを作成し、可視化を実現。

industrial-energy-ai-demo/
│
├── README.md
├── .gitignore
├── requirements.txt
├── docker-compose.yml
│
├── docs/                         # 文档（面试重点）
│   ├── architecture.md
│   ├── api-design.md
│   ├── deployment.md
│
├── infrastructure/              # 云资源（核心加分）
│   ├── azure/
│   │   ├── iot-hub.tf
│   │   ├── stream-analytics.tf
│   │   ├── function-app.tf
│   │
│   ├── aws/
│   │   ├── rds.tf
│   │   ├── ecs-fargate.tf
│
│   └── scripts/
│       ├── deploy.sh
│       ├── destroy.sh
│
├── simulator/                   # IoT设备模拟（必须有）
│   ├── device_simulator.py
│   ├── config.yaml
│
├── ingestion/                   # 数据接入（Azure Functions）
│   ├── function_app/
│   │   ├── __init__.py
│   │   ├── iot_handler.py
│   │   ├── requirements.txt
│
├── processing/                  # 数据处理（流处理/规则）
│   ├── anomaly_detection.py
│   ├── stream_job.sql
│
├── ml/                          # AI模型（核心亮点）
│   ├── train.py
│   ├── predict.py
│   ├── model/
│   │   ├── model.pkl
│
├── api/                         # backend API
│   ├── app.py
│   ├── routes/
│   │   ├── health.py
│   │   ├── prediction.py
│   ├── services/
│   │   ├── db_service.py
│   │   ├── ml_service.py
│
├── data/                        # test data
│   ├── sample_sensor_data.csv
│
├── dashboard/                   # 可视化
│   ├── powerbi/
│   │   ├── dashboard.pbix
│
├── tests/                       # test
│   ├── test_api.py
│   ├── test_ml.py
│
└── scripts/                     # script
    ├── run_local.sh
    ├── seed_data.py
