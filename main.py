"""GitHub Actions 上で定期実行されるサンプルスクリプト。

ここに実行したい処理を書いてください。
実行結果は output/ ディレクトリに保存され、リポジトリにコミットされます。
"""

import json
import os
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
OUTPUT_DIR = "output"


def main() -> None:
    now = datetime.now(JST)
    print(f"実行時刻 (JST): {now.isoformat()}")

    # ===== ここから実際の処理を書く =====
    # 例: API からデータ取得、スクレイピング、通知送信 など
    result = {
        "executed_at": now.isoformat(),
        "message": "GitHub Actions からの実行に成功しました",
    }
    # ===== ここまで =====

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log_path = os.path.join(OUTPUT_DIR, "latest_run.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"結果を {log_path} に保存しました")


if __name__ == "__main__":
    main()
