from pathlib import Path
import time
import re


class StaticMethods:

    @staticmethod
    def get_size_of_file(text: str) -> float:
        match = re.search(r'(\d+(?:\.\d+)?)\s*МБ', text)
        if match:
            return float(match.group(1))
        raise ValueError("Размер в МБ не найден в строке")

    @staticmethod
    def wait_for_download(dir_path, timeout=30):
        for _ in range(timeout):
            files = list(Path(dir_path).glob("*.exe"))
            if files:
                return files[0]
            time.sleep(1)
        raise TimeoutError("Файл не скачался за отведённое время")

    @staticmethod
    def delete_file(file):
        if Path.exists(file):
            Path.unlink(file)
            return True
        else:
            return False
