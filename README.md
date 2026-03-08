# AtCoder-Workspace

AtCoderを快適に行うためのワークスペースです。
C++とPythonに両対応しており、自動で言語を判別してコンパイル・テスト・提出を行います。

## セットアップ
### 1. 依存ツールの導入
- Node.js (atcoder-cli用)
- Python 3.13+ (online-judge-tools用)
- (C++を使う場合) MinGW-w64 (g++) など

```powershell
npm install -g atcoder-cli
pip install online-judge-tools
```
### 2. エイリアスと環境の設定
初回のセットアップ時に、以下のスクリプトを一度だけ実行してください。
```powershell
.\setup.ps1
```
これを実行すると、自動的にPowerShellのプロフィール（`$PROFILE`）にエイリアス設定が追記されます。
以降は、**新しくターミナルを開くたびに自動で `an`, `t`, `s` などの便利な短縮コマンドが使える**ようになります。

### 3. 認証設定
AtCoderのクッキーを `Netscape` 形式で `atcoder_cookies.txt` に貼り付けた後、以下のコマンドを実行します。
```powershell
python login.py
```

## 使い方
### 1. 初回の設定 (初回のみ)
ターミナルで一度だけ以下を実行し、問題の一括ダウンロードの設定などを反映します。
```powershell
acc config default-test-dirname tests
acc config default-task-choice all
```

### 2. コンテスト（問題群）のダウンロード
`contests` フォルダ内に移動し、コンテスト全体をダウンロードします。（例として `abs` をダウンロードします）
```powershell
cd contests
an abs
```
これによって、`contests/abs` の中に `practicea` や `abc086a` などの各問題のフォルダが一括で作られます。

### 3. 問題を解く
各問題のフォルダに移動して、コードを書きます。

1. **移動**
   ```powershell
   cd abs\practicea
   ```
2. **テンプレートのコピー**
   利用する言語に合わせて、`library` フォルダにあるテンプレートを現在のフォルダに `main.py` または `main.cpp` としてコピーします。
   - **Pythonの場合**
     ```powershell
     Copy-Item ..\..\..\library\template.py .\main.py
     ```
   - **C++の場合**
     ```powershell
     Copy-Item ..\..\..\library\template.cpp .\main.cpp
     ```
3. **コーディング**
   コピーした `main.py` または `main.cpp` をエディタ（VSCodeなど）で開き、問題を解くコードを記述します。

### 4. ローカル検証 (テスト実行)
問題が解けたら、同じフォルダで自動テストを実行します。
```powershell
t
```
`main.cpp` がある場合は自動でコンパイルされ、その後自動で `tests` フォルダのサンプルテストが実行されます。`main.py` の場合も同様です。
全て `AC` になればOKです。（※ `t` コマンドはPowerShellのプロフィール設定により、新しく開いたターミナルでも常に使用可能です）

### 5. 提出
テストが全て通ったら、以下を実行してAtCoderへ自動提出します。
```powershell
s
```
こちらも常に自動的に `main.py` や `main.cpp` を認識して提出します。

## ディレクトリ構成
- `contests/`: 各コンテストの作業ディレクトリ
- `library/`: 共通ライブラリ・テンプレート
- `login.py`: クッキー注入スクリプト
- `setup.ps1`: エイリアス設定スクリプト
- `atcoder_cookies.txt`: クッキーデータ保存用