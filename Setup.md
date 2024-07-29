# 別端末で使用する場合のセットアップ方法

## 操作手順
1. gitのインストール
1. gitconfigを設定
1. このリポジトリをcloneする
1. アカウント認証をする

## 1.gitのインストール
```bash
winget install --id Git.Git -e --source winget
```
上記コマンドを実行することでGitをインストールすることができる  
[参考サイト](https://git-scm.com/download/win)

## 2.gitconfigを設定する！
> usernameの設定
```sh
git config --global user.name "John Doe"
```
emailアドレスの設定！
```sh
git config --global user.email johndoe@example.com
```
[参考サイト](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-%E6%9C%80%E5%88%9D%E3%81%AEGit%E3%81%AE%E6%A7%8B%E6%88%90)

## 3.このリポジトリをcloneする
```sh
git clone https://github.com/ogane0112/ganesya-certification.git
```
## 4.アカウント認証
```sh
git add .
git commit -m "example"
git push
```
上記コマンドを実行するとログイン認証画面が出現するのでログインする
！