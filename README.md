# Python-Visualization
※`dc` = `docker-compose`

* コンテナの起動
```
$ dc up -d --build
```

## Dash
https://dash.plotly.com/
* 起動
```
$ dc exec python-visualization zsh -c "python src/dash/app.py"
```

* 以下URLにアクセス
  * http://0.0.0.0:8001/

## Streamlit
https://www.streamlit.io/
* 起動
```
$ dc exec python-visualization zsh -c "cd src/streamlit && streamlit run app.py"
```

* 以下URLにアクセス
  * http://0.0.0.0:8001/

* 設定確認
```
$ streamlit config show
```