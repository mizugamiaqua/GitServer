# GitServer — GitHub Actions で Python を無料実行

サーバーをレンタルせずに、GitHub Actions を使って Python スクリプトを
**無料** で実行・定期実行するためのリポジトリです。

- パブリックリポジトリ: 実行時間 **無制限で無料**
- プライベートリポジトリ: 毎月 **2,000 分まで無料**(無料プランの場合)

## 仕組み

GitHub Actions は、GitHub が用意した仮想マシン(Ubuntu)上でコードを実行してくれる
サービスです。`.github/workflows/run-python.yml` に「いつ・何を実行するか」を定義
しておくと、GitHub が自動でスクリプトを実行します。

## ファイル構成

| ファイル | 役割 |
|---|---|
| `main.py` | 実行される Python スクリプト(ここに処理を書く) |
| `requirements.txt` | 必要なパッケージの一覧 |
| `.github/workflows/run-python.yml` | 実行スケジュールなどの設定 |
| `output/latest_run.json` | 実行結果(自動でコミットされる) |

## 使い方

### 1. 手動で実行する

1. GitHub のリポジトリページで **Actions** タブを開く
2. 左側の **Run Python** を選択
3. **Run workflow** ボタンを押す

### 2. 定期実行のスケジュールを変える

`.github/workflows/run-python.yml` の `cron` を編集します。
**時刻は UTC(日本時間 −9 時間)** で指定する点に注意してください。

```yaml
schedule:
  - cron: "0 15 * * *"   # 毎日 00:00 JST
```

よく使う例(JST 換算):

| cron (UTC) | 実行タイミング (JST) |
|---|---|
| `0 15 * * *` | 毎日 0:00 |
| `0 0 * * *` | 毎日 9:00 |
| `0 * * * *` | 毎時 0 分 |
| `*/30 * * * *` | 30 分ごと |
| `0 15 * * 0` | 毎週月曜 0:00 |

> **注意**: 定期実行はデフォルトブランチ(main)にあるワークフローだけが動きます。
> また、GitHub の混雑状況により数分〜十数分遅れることがあります。
> 60 日間リポジトリに更新がないと定期実行は自動停止します(Actions タブから再有効化できます)。

### 3. 自分の処理を書く

`main.py` の「ここから実際の処理を書く」の部分を書き換えてください。
外部パッケージが必要な場合は `requirements.txt` に追加します。

```txt
requests
beautifulsoup4
```

### 4. API キーなどの秘密情報を使う

コードに直接書かず、GitHub の Secrets を使います。

1. リポジトリの **Settings → Secrets and variables → Actions** を開く
2. **New repository secret** で登録(例: `MY_API_KEY`)
3. `run-python.yml` のコメントアウトを外して環境変数として渡す

```yaml
env:
  MY_API_KEY: ${{ secrets.MY_API_KEY }}
```

4. Python からは `os.environ["MY_API_KEY"]` で読み取れます

## 制限事項

- 1 回の実行は最長 6 時間まで(このリポジトリでは 30 分に設定)
- 常時起動のサーバー(Web サーバー等)としては使えません。
  「決まったタイミングで処理を実行する」用途向けです
- 定期実行の最短間隔は 5 分です
