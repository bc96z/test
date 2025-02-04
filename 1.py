import os
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 設定要遍歷的資料夾 (請改為你的根目錄)
root_folder = "C:/Users/brad8/OneDrive/桌面/---MP3 ---"
# 支援的音訊格式
AUDIO_FORMATS = [".flac", ".wma", ".wav"]

def convert_audio_to_mp3(input_file):
    """轉換 FLAC/WMA/WAV 到 MP3 並覆蓋原始檔案"""
    ext = os.path.splitext(input_file)[1].lower()  # 取得副檔名
    if ext not in AUDIO_FORMATS:
        return  # 不是要轉換的格式，跳過

    output_file = os.path.splitext(input_file)[0] + ".mp3"  # 產生相同名稱的 .mp3 檔

    # 如果 MP3 已經存在，則不轉換
    if os.path.exists(output_file):
        print(f"已存在，跳過: {output_file}")
        return

    # 執行 ffmpeg 轉換
    command = [
        "ffmpeg", "-i", input_file,
        "-ab", "320k",  # 設定比特率 320kbps
        "-map_metadata", "0",  # 保留 metadata
        "-y",  # 自動覆蓋輸出檔案
        output_file
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 如果轉換成功，刪除原始檔案
    if os.path.exists(output_file):
        print(f"轉換完成: {input_file} -> {output_file}")
        os.remove(input_file)
    else:
        print(f"轉換失敗: {input_file}")

def process_folder(folder):
    """遍歷所有檔案，處理 FLAC/WMA/WAV 檔案"""
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            convert_audio_to_mp3(file_path)

# 執行轉換
process_folder(root_folder)
print("批量轉換完成！")




#test

