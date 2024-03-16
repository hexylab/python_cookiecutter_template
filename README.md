# How to Use

テンプレートを作成したいディレクトリで以下のコマンドを実行する
```
python -m cookiecutter https://github.com/hexylab/python_cookiecutter_template.git
```

- project_name

プロジェクトの正式名称です。これは通常、ゲームのタイトルやユニークな名前で、人が読んで理解できる形式です。
```
例: "Dungeon Explorer"
```
- project_slug

プロジェクトのスラッグ（URLやディレクトリ名に適した形式）です。通常はproject_nameを小文字にし、空白をハイフンやアンダースコアに置き換えて生成します。これは自動的に生成されることが多いですが、手動で設定することも可能です。

```
例: project_nameが"Dungeon Explorer"の場合、project_slugは"dungeon_explorer"
```

- package_name

Pythonパッケージの名前です。これはプロジェクト内でのモジュールやライブラリの名前に使われます。通常はproject_slugを基にして、ハイフンをアンダースコアに置き換えたものを使用します。
```
例: project_slugが"dungeon_explorer"の場合、package_nameは"dungeon_explorer"
```

- project_short_description

プロジェクトの短い説明です。これはゲームの概要や特徴を簡潔に表現したもので、READMEファイルやドキュメントの冒頭に記載されることが多いです。
```
例: "A roguelike dungeon exploration game where you fight monsters, collect treasures, and uncover mysteries."
```