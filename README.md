# CloudMLOps - Data Pipeline for Traffic Risk Prediction in Reading, PA


Author: Yuhao Jia, Hanzhi Zhang

<img src="https://yuhaochrisj.github.io/yuhao_portofolio/Images/Pipeline.png" width:"700">

We built up a data pipeline for the counts of car crashes prediction model. By automating the data collection and analysis process, a data pipeline can provide real-time or near real-time insights into traffic patterns and risk factors. This can help transportation agencies and emergency services respond more quickly to accidents or other incidents. This is a MUSA Capstone Project. 

 Check the Prediction map [here](https://hazellla.github.io/CloudMLOps-CarCrashesPrediction/site/index.html).

## 

### Data Resources

In the `musa509s23_team<N>_raw_data` bucket, there are three folders. Each folder may contain one or multiple files, depending on the type of data loaded (for example, a shapefile may be stored as multiple files). The folders are as follows:

| Folder | Contents |
|--------|----------|
| `/volumn/` | Contains the "traffic volumn" data downloaded from the [Pennsylvania traffic counts](https://www.pasda.psu.edu/download/padot/state/PaTraffic2023_04.zip) dataset. |
| `/crashes/` | Contains the "car crashes history" data downloaded from the [Pennsylvania Crash Information Tool](https://www.arcgis.com/sharing/rest/content/items/cbb78b74142b46a3b1698cd769d983c8/data) dataset on Pennsylvania Department of Transportation. |

