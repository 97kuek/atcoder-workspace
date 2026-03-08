# AtCoder-Workspace

AtCoderを快適に行うためのワークスペース。
`atcoder-cli`と `online-judge-tools`を使用して、テストから提出までをコマンドラインで行う。

## セットアップ

### 1. 依存ツールの導入
- Node.js (atcoder-cli用)
- Python 3.13+ (online-judge-tools用)
- (C++を使う場合) MinGW-w64 (g++) など

```powershell
npm install -g atcoder-cli
pip install online-judge-tools
```

### 2. 認証設定
AtCoderのクッキーを `Netscape` 形式で `atcoder_cookies.txt` に貼り付けた後、以下のコマンドを実行する。
```powershell
python login.py
```

## 使い方

### 1. 初回の設定
ターミナルで以下の設定を行い、テストディレクトリ名を `tests` に固定する。
```powershell
acc config default-test-dirname tests
acc config default-task-choice all
```

### 2. コンテストの問題をダウンロード
`contests` フォルダへ移動し、コンテストIDを指定して問題をダウンロードします。
```powershell
cd contests
acc new [contest_id]  # 例: acc new abs
```

### 3. 問題を解く
各問題のフォルダ（例: `practicea`）に移動し、`library` フォルダにあるテンプレートを `main.py` または `main.cpp` としてコピーして編集する。

### 4. ローカル検証 (テスト実行)
問題フォルダ内でサンプルケースに対するテストを実行する。

- **Pythonの場合**
  ```powershell
  oj t -c "python main.py" -d tests
  ```
- **C++の場合** (コンパイルしてから実行)
  ```powershell
  g++ -O3 -std=c++20 main.cpp -o main.exe
  oj t -c ".\main.exe" -d tests
  ```

### 5. 提出
テストが通ったら、以下のコマンドで提出する。
```powershell
acc s main.py    # Pythonの場合
acc s main.cpp   # C++の場合
```

## ディレクトリ構成
- `contests/`: 各コンテストの問題フォルダ
- `library/`: 共通テンプレート (`template.py`, `template.cpp`)
- `login.py`: クッキー注入用スクリプト
- `atcoder_cookies.txt`: クッキー保存用