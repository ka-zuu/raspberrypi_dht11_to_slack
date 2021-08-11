# raspberrypi_dht11_to_slack
DHT11から温度・湿度を取得して、Slackへ投げる

## DHT11のPythonライブラリを取得
`git clone https://github.com/szazo/DHT11_Python.git`
* 参考URL：https://qiita.com/mininobu/items/1ba0223af84be153b850

## ライブラリをimportするために、リンクを貼る
`ln -s DHT11_Python/dht11`

## slackwebも取得
`sudo pip install slackweb`
* 参考：https://blog.serverworks.co.jp/tech/2017/08/08/pi-zero-slack/

## SlackのWebHook URL
config.pyに記載
`slack_url = "https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxx"`
* config.pyは.gitignoreにセット

