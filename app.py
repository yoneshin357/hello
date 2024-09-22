
import streamlit as st
import pandas as pd
import numpy as np

def main():
    # タイトル
    st.title('Application title2')
    # ヘッダ
    st.header('Header')
    # 純粋なテキスト
    st.text('Some text')
    # サブレベルヘッダ
    st.subheader('Sub header')
    # マークダウンテキスト
    st.markdown('**Markdown is available **')
    # LaTeX テキスト
    st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
    # コードスニペット
    st.code('print(\'Hello, World!\')')
    # エラーメッセージ
    st.error('Error message')
    # 警告メッセージ
    st.warning('Warning message')
    # 情報メッセージ
    st.info('Information message')
    # 成功メッセージ
    st.success('Success message')
    # 例外の出力
    st.exception(Exception('Oops!'))
    # 辞書の出力
    d = {
        'foo': 'bar',
        'users': [
            'alice',
            'bob',
        ],
    }
    st.json(d)
        # Pandas のデータフレームを可視化してみる
    data = {
        # ランダムな値で初期化する
        'x': np.random.random(20),
        'y': np.random.random(20),
    }
    df = pd.DataFrame(data)
    # データフレームを書き出す
    st.dataframe(df)
    # st.write(df)  でも良い
    # スクロールバーを使わず一度に表示したいとき
    st.table(df)
        # 東京のランダムな経度・緯度を生成する
    data = {
        'lat': np.random.randn(100) / 100 + 35.68,
        'lon': np.random.randn(100) / 100 + 139.75,
    }
    map_data = pd.DataFrame(data)
    # 地図に散布図を描く
    st.map(map_data)


if __name__ == '__main__':
    main()
