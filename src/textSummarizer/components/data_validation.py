
import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self)-> bool:
        try:
            # 預設驗證狀態為 True
            validation_status = True

            # 獲取 artifacts/data_ingestion 目錄下的所有檔案
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))

            # 檢查 ALL_REQUIRED_FILES 中的每個檔案是否都存在
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    break  # 一旦發現缺少某個必須檔案，立即停止檢查

            # 將驗證結果寫入 STATUS_FILE
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            # 如果發生異常，記錄錯誤並返回 False
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation failed due to error: {str(e)}")
            return False