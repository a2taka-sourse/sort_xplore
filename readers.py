import csv #csvモジュールの読み込み(1)
import pyaudio
import wave
import time
import speech_recognition as sr
import re

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 44100
INPUT_DEVICE_INDEX = 0       # マイクのチャンネル
CALL_BACK_FREQUENCY = 3   # コールバック呼び出しの周期[sec]

 
def convert_kanji_to_int(string):
    result = string.translate(str.maketrans("零〇一壱二弐三参四五六七八九拾", "00112233456789十", ""))
    convert_table = {"十": "0", "百": "00", "千": "000", "万": "0000", "億": "00000000", "兆": "000000000000", "京": "0000000000000000"}
    unit_list = "|".join(convert_table.keys())
    while re.search(unit_list, result):
        for unit in convert_table.keys():
            zeros = convert_table[unit]
            for numbers in re.findall(f"(\d+){unit}(\d+)", result):
                result = result.replace(numbers[0] + unit + numbers[1], numbers[0] + zeros[len(numbers[1]):len(zeros)] + numbers[1])
            for number in re.findall(f"(\d+){unit}", result):
                result = result.replace(number + unit, number + zeros)
            for number in re.findall(f"{unit}(\d+)", result):
                result = result.replace(unit + number, "1" + zeros[len(number):len(zeros)] + number)
            result = result.replace(unit, "1" + zeros)
    return int(result)


file = './reader.csv' #ファイルのパスを指定(2)
f = open(file,'r') #ファイルをオープン (3)

rows = csv.reader(f) #ファイルからデータを読み込み(4)
lrow = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
h = 0
for row in rows:
    for i in range(7):# for文で行を1つずつ取り出す(5)
        lrow[h][i] = row[i]
    h += 1
        
f.close() #開いたファイルをクローズ(7)
for r in lrow:
    print(r)

def callback(in_data, frame_count, time_info, status):
    """
    コールバック関数の定義
    """
    
    global sprec # speech_recognitionオブジェクトを毎回作成するのではなく、使いまわすために、グローバル変数で定義しておく

    try:
        audiodata  = sr.AudioData(in_data, SAMPLE_RATE, 2)
        print("listening...")
        sprec_text = sprec.recognize_google(audiodata, language='ja-JP')
        print(sprec_text)
        
        try:
            int(sprec_text)
            print("waiting...")
            for y, brow in enumerate(lrow):
                try:
                    pos = (y + 1, brow.index(sprec_text) + 1)
                    break
                except ValueError:
                    pass
            answer = pos[0]
            print(f"{answer}列目")
        except ValueError:
            

            pass
        
        try:
            convert_kanji_to_int(sprec_text)
            print("waiting...")
            for y, brow in enumerate(lrow):
                try:
                    pos = (y + 1, brow.index(sprec_text) + 1)
                    break
                except ValueError:
                    pass
            answer = pos[0]
            print(answer)

        except ValueError:
            if sprec_text=='ストップ':
                print('wait to close...')
                stream.stop_stream()
                stream.close()
                audio.terminate()
            pass
        
    except sr.UnknownValueError:
        pass
    
    except sr.RequestError as e:
        pass
    
    finally:
        return (None, pyaudio.paContinue)


global sprec # speech_recognitionオブジェクトを毎回作成するのではなく、使いまわすために、グローバル変数で定義しておく
    
    # speech recogniserインスタンスを生成
sprec = sr.Recognizer() 
    
    # Audio インスタンス取得
audio  = pyaudio.PyAudio() 
    
    # ストリームオブジェクトを作成
stream = audio.open(format             = FORMAT,
                    rate               = SAMPLE_RATE,
                    channels           = CHANNELS,
                    input_device_index = INPUT_DEVICE_INDEX,
                    input              = True, 
                    frames_per_buffer  = SAMPLE_RATE*CALL_BACK_FREQUENCY, # CALL_BACK_FREQUENCY 秒周期でコールバック
                    stream_callback    = callback)
    
stream.start_stream()
    
while stream.is_active():
    time.sleep(0.1)
        

