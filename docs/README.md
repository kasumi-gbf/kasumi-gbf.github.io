# 霞桜団 公式サイト

`index.html` 1枚だけの静的サイトです（ビルド不要・外部ライブラリなし）。

## 編集してから公開してほしい箇所

- **入団案内**（`#recruit`）: ランク目安・ノルマ・活動時間帯は仮の内容です。実際の条件に差し替えてください。
- **連絡先**（`#contact`）: Discord招待リンク・X(Twitter)のURLが `href="#"` のままです。実際のURLに差し替えてください。

## GitHub Pagesで公開する手順（無料）

1. このリポジトリ（`gbf-kasumi`）の GitHub ページを開く
2. 上部メニュー **Settings → Pages** を開く
3. 「Build and deployment」の **Source** を `Deploy from a branch` にする
4. **Branch** で `main` を選び、フォルダは `/site` を選択（`/site` が選択肢に出ない場合は下記「別ブランチで公開する場合」を参照）→ Save
5. 数分後、`https://<ユーザー名>.github.io/gbf-kasumi/` で公開されます

### 別ブランチで公開する場合（`/site` フォルダが選べないとき）

GitHub Pagesはリポジトリ直下か `/docs` フォルダしか選べないことがあります。その場合は `gh-pages` という専用ブランチを作り、そこに `site/` の中身だけを置く方法が簡単です（お声がけいただければ設定します）。

## ローカルで確認する

```bash
open /Applications/gbf/webapp/site/index.html
```
