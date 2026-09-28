# 霞桜団 公式サイト

`index.html` 1枚だけの静的サイトです（ビルド不要・外部ライブラリなし）。

## 編集してから公開してほしい箇所

- **入団案内**（`#recruit`）: ランク目安・ノルマ・活動時間帯は仮の内容です。実際の条件に差し替えてください。
- **連絡先**（`#contact`）: Discord招待リンク・X(Twitter)のURLが `href="#"` のままです。実際のURLに差し替えてください。

## GitHub Pagesで公開する手順（無料）

リポジトリ名を `masama1019-hash.github.io` にしているため、GitHubのユーザー/組織ページとして
`https://masama1019-hash.github.io/` にそのまま公開されます。

1. このリポジトリの GitHub ページを開く
2. 上部メニュー **Settings → Pages** を開く
3. 「Build and deployment」の **Source** を `Deploy from a branch` にする
4. **Branch** で `main` を選び、フォルダは `/docs` を選択 → Save
5. 数分後、`https://masama1019-hash.github.io/` で公開されます

## ローカルで確認する

```bash
open /Applications/gbf/webapp/docs/index.html
```
