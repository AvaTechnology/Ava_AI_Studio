import os
import pyaudio
import wave
import speech_recognition as sr
from pydub import AudioSegment

# 设置录音参数
CHUNK = 1024  # 每次读取的音频数据大小
FORMAT = pyaudio.paInt16  # 音频格式为16位PCM
CHANNELS = 1  # 单声道
RATE = 16000  # 采样率为16kHz
RECORD_SECONDS = 20  # 录音时长为20秒

# 创建一个Recognizer对象
r = sr.Recognizer()

# 开始录音
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
frames = []

print("开始录音...")
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("录音结束.")

# 停止录音并保存音频文件
stream.stop_stream()
stream.close()
audio.terminate()

# 保存录制的音频为.wav文件
audio_file = "D:/AvaStudio/output.wav"
wf = wave.open(audio_file, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# 提取人声
audio_segment = AudioSegment.from_wav(audio_file)
extracted_audio = audio_segment.high_pass_filter(300)  # 进行人声提取处理

# 保存提取的人声音频为.wav文件
extracted_audio_file = "D:/AvaStudio/extracted_output.wav"
extracted_audio.export(extracted_audio_file, format="wav")

# 将音频文件加载到Recognizer对象
with sr.AudioFile(extracted_audio_file) as source:
    audio = r.record(source)

    # 使用Google Speech Recognition引擎进行语音识别
    text = r.recognize_google(audio, language="zh-CN")

# 打印转换的文本
print("转换的文本：", text)

# 删除生成的音频文件
os.remove(audio_file)
os.remove(extracted_audio_file)
