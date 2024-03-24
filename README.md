# rye VSCode Settings Template

`rye + vscode` の設定テンプレート

## 使用方法

### 前提

以下がインストール済

- [Visual Studio Code](https://code.visualstudio.com/)
- [rye](https://github.com/mitsuhiko/rye)
- [pre-commit](https://pre-commit.com/index.html)

```bash
## rye install ##
curl -sSf https://rye-up.com/get  RYE_INSTALL_OPTION="--yes" | bash
# パス追加
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
source "$HOME/.rye/env"

## pre-commit install ##
rye add --dev pre-commit
rye sync
```

### pyproject.toml編集

`pyproject.toml`の編集を行う。
以下該当項目を列挙

```toml
[project]
name = "{プロジェクト名記載}"
description = "{説明追加}"
authors = ["{必要であれば記載}"]

[tool.mypy]
strict = true

[tool.ruff]
select = [
    "F", # pyflakes
    "E", # pycodestyle
    "W", # pycodestyle warnings
    "I", # isort
]
ignore = []
line-length = 88

[tool.ruff.per-file-ignores]
# 個別設定
# __init__.pyは未使用インポートを許容
"__init__.py" = ["F401"]
```

初期設定。最低限必要なファイルをインストール。

```bash
make install
```

動作確認

```bash
make run_main
```

---

### ryeの使い方

#### pythonバージョン管理

```bash
# Pythonのバージョン選択(ファイル`.python-version`で管理される)
rye pin 3.12
```

#### pyproject.tomlに記述されたパッケージのインストール

```bash
rye sync
```

#### pyproject.tomlの変更

```bash
# 開発用のツールをpyproject.tomlに追加
rye add --dev ruff mypy ...<ライブラリ名>
# 必要なライブラリをpyproject.tomlに追加
rye add <ライブラリ名>
# 不要なライブラリを消す
rye remove <ライブラリ名>
# pyproject.tomlの反映
rye sync
```

### 仮想環境

接続は以下コマンド実行

#### linux

`. .venv/bin/activate`

#### windows

`.venv\Scripts\activate`

抜けるには`deactivate`コマンド実行
※仮想環境内で有効なコマンド

## Formatter Linter

本テンプレートは以下のフォーマッター・リンターを採用している。

- [ruff](https://github.com/astral-sh/ruff)
- [mypy](https://github.com/python/mypy)

## VSCode 設定

### 拡張機能

`vscode`の拡張機能について、必須・推奨の拡張機能を記載。

#### 必須

| Name    | ID                            |
| ------- | ----------------------------- |
| Python  | `ms-python.python`            |
| Pylance | `ms-python.vscode-pylance`    |
| Ruff    | `charliermarsh.ruff`          |
| Mypy    | `ms-python.mypy-type-checker` |

#### 推奨

| Name             | ID                         |
| ---------------- | -------------------------- |
| autodocstring    | `njpwerner.autodocstring`  |
| even-better-toml | `tamasfe.even-better-toml` |

### settings.json

windowsで使用する方は

`"${workspaceFolder}/.venv/bin/{file}"`を
`"${workspaceFolder}/.venv/Scripts/{file}`に変更して使用する。

## Github Actions

`lint`と`pytest`を行うCI/CDのtemplateを用意している。

### lint.yml

以下の静的解析を行う

- ruff
- mypy
- cspell

### test.yml

`pytest`によるテストコードの自動実施
カバレッジを表示してくれる
