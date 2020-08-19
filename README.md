# Python-Visualization
※`dc` = `docker-compose`

* コンテナの起動
```
$ dc up -d --build
```

* Dashの起動
```
$ dc exec python-visualization zsh -c "python src/dash/app.py"
```

* 以下URLにアクセス
  * http://0.0.0.0:8001/