import jaconv
import pyopenjtalk # require: python3.10
import sys

def g2p(str):
    katakana = pyopenjtalk.g2p(str, kana=True)
    hira = jaconv.kata2hira(katakana)
    phonemes = jaconv.hiragana2julius(hira)
    return katakana, hira, phonemes

if __name__ == '__main__':
    
    args = sys.argv
    if len(args) != 2:
        print('Usage: python text_to_julius_phoneme.py <text>')
        sys.exit()
    str = args[1] # 漢字まじりの文字列

    katakana, hira, phonemes = g2p(str)
    print(katakana)
    print(hira)
    print(phonemes)
    
    # 保存する場合
    # output_dir = "/home/takeshun256/Julius-Test/segmentation-kit/wav"
    # with open(output_dir + '/sample_phoneme.txt', 'w') as f:
    #     f.write(phonemes)
