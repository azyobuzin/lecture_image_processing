from IPython.display import display
import PIL
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 定数
IMAGE1_PATH = 'photo-92-600x400.jpg'

# from prelude import * でインポートするものリスト
__all__ = [
    # ライブラリ
    'PIL', 'display', 'matplotlib', 'np', 'plt',
    # 定義
    'IMAGE1_PATH'
]

# 日本語対応フォントに変更
matplotlib.rcParams['font.family'] = ['IPAexGothic', 'YuGothic', 'Yu Mincho'] + matplotlib.rcParams['font.family']
