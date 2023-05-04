CREATE OR REPLACE EXTERNAL TABLE `source.volume` (
    `NLF_ID` STRING,
    `DLY_TRK_VM` STRING,
    `GIS_UPDATE` STRING,
    `GPID` STRING,
    `WKDY_TRK_C` STRING,
    `CUM_OFFSET` STRING,
    `TRAFF_PATT` STRING,
    `SIDE_IND` STRING,
    `SEG_LNGTH_` STRING,
    `BASE_YR_CL`STRING,
    `SEG_END` STRING,
    `BASE_ADT_Y` STRING,
    `OFFSET_END` STRING,
    `SEG_BGN` STRING,
    `RECORD_UPD` STRING,
    `CUM_OFFS_1` STRING,
    `CTY_CODE` STRING,
    `DIR_IND` STRING,
    `T_FACTOR` STRING,
    `K_FACTOR` STRING,
    `WKDY_TRK_B` STRING,
    `RMSTRAFFIC` STRING,
    `TRK_PCT` STRING,
    `NLF_CNTL_B` STRING,
    `SEG_PT_BGN` STRING,
    `VOL_CNT_DA` STRING,
    `CUR_AADT` STRING,
    `ADLR_TRK_B` STRING,
    `ADLR_TRK_C` STRING,
    `DLY_VMT` STRING,
    `GIS_GEOMET` STRING,
    `MAPID` STRING,
    `MSLINK` STRING,
    `D_FACTOR` STRING,
    `ADLF_TRK_B` STRING,
    `ADLF_TRK_C` STRING,
    `Shape_Leng` STRING,
    `DUR_CLS_CN` STRING,
    `DISTRICT_N` STRING,
    `JURIS` STRING,
    `BASE_ADT` STRING,
    `VOL_CNT_KE` STRING,
    `SEG_PT_END` STRING,
    `LEN` STRING,
    `ST_RT_NO` STRING,
    `NLF_CNTL_E` STRING,
    `SEQ_NO` STRING,
    `RAW_CNT_HI` STRING,
    `TYPE_OF_CN` STRING,
    `ADTT_BASE` STRING,
    `OFFSET_BGN` STRING,
    `ADTT_CUR` STRING,
    `geog` STRING

)
OPTIONS (
    uris = ['gs://509final_processed_data/volumn/data.jsonl'],
    format = 'JSON'
    )