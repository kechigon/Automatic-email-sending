# Automatic-email-sending
gmailで複数のアドレスにメールを自動送信します。

# 使い方
1. 送信先アドレスとテンプレート文に挿入する文字列を記入したCSVファイルを用意してください。この時、各行の先頭をメールアドレスにしてください。  
2. テンプレート文を記入したテキストファイルを用意してください。送信先ごとに変えたい部分は`<<1>>`のような形で指定してください。CSVの各行の数字に対応した文字列が挿入されます。
3. 送信元のgmailの設定で「安全性の低いアプリのアクセス」をオンにしてください。
4. プログラムを実行し、送信元gmailのアドレス、パスワード、メールのタイトル、CSVファイルのパス、テンプレート文のパス、を入力してください。
