# 霞桜団 公式サイト

`index.html`（TOP）と `record.html`（古戦場戦績）の2ページ構成の静的サイトです（ビルド不要・外部ライブラリなし）。
スタイルは共通の `assets/style.css` を両ページで参照しています。

ナビゲーションは 団紹介 / 古戦場戦績 / 貢献度サイト（外部リンク） / Discord（外部リンク）の4項目です。

## GitHub Pagesで公開する手順（無料）

リポジトリ名を `kasumi-gbf.github.io` にしているため、GitHubのユーザー/組織ページとして
`https://kasumi-gbf.github.io/` にそのまま公開されます。

1. このリポジトリの GitHub ページを開く
2. 上部メニュー **Settings → Pages** を開く
3. 「Build and deployment」の **Source** を `Deploy from a branch` にする
4. **Branch** で `main` を選び、フォルダは `/docs` を選択 → Save
5. 数分後、`https://kasumi-gbf.github.io/` で公開されます

## ローカルで確認する

```bash
open /Applications/gbf/webapp/docs/index.html
```
