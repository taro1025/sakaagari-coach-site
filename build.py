#!/usr/bin/env python3
"""さかあがりコーチの公開ページ（GitHub Pages）を書き出す。 python3 build.py"""
import os

MAIL = "rintaro.sakino@process-craft-ai.com"
CSS = """body{margin:0;background:#F7F3EA;color:#1E2540;font-family:-apple-system,"Hiragino Sans","Hiragino Kaku Gothic ProN",sans-serif;line-height:1.8}
main{max-width:720px;margin:0 auto;padding:40px 22px 64px}h1{color:#24409A;font-size:1.7em;line-height:1.4}h2{color:#24409A;font-size:1.15em;margin-top:2em}
a{color:#24409A}.bar{height:8px;background:#F2C230;border-radius:4px;width:72px;margin:8px 0 24px}footer{margin-top:48px;font-size:.85em;color:#5C6178}
nav a{margin-right:14px}img.icon{width:96px;height:96px;border-radius:22px}
@media (prefers-color-scheme:dark){body{background:#121A33;color:#F1F3F9}h1,h2,a{color:#9FB3F2}footer{color:#A9B1C9}}"""

PAGES = {
 "ja": {
  "lang": "ja", "home": "./", "other": "en/", "other_label": "English",
  "nav": ("ホーム", "プライバシーポリシー", "利用規約", "サポート"),
  "index": ("さかあがりコーチ", f"""<p><img class="icon" src="{{root}}icon.png" alt=""></p>
<p>横から撮った 1 回の逆上がりの動画から、回れない原因を 1 つに絞り、その原因に合う練習だけを出す iPhone アプリです。</p>
<ul><li>踏み込みの位置・肘の曲がり・蹴り足の高さ・おへそと鉄棒の距離を、端末の中で測ります</li>
<li>原因ごとに 3 段の練習（回数の目安・補助の手の位置・かける言葉）</li>
<li>初日とできた日を並べた比較動画を、顔を自動でぼかして書き出せます</li>
<li>動画は iPhone の外に送りません。アカウント登録もいりません</li></ul>"""),
  "privacy": ("プライバシーポリシー", f"""<p>このポリシーは、iPhone アプリ「さかあがりコーチ」（以下「本アプリ」）で運営者が情報をどう扱うかを定めます。</p>
<h2>集める情報</h2><p>運営者は、本アプリから個人を特定できる情報を集めません。本アプリにはアカウント・広告・解析ツールがありません。</p>
<h2>動画と記録</h2><p>撮影した動画、写真から選んだ動画、姿勢の読み取りの結果、お子さんの呼び名と学年、練習の記録は、すべて端末の中にだけ保存します。姿勢の読み取りは Apple の Vision フレームワークで端末の中で行い、動画や結果を外部に送ることはありません。</p>
<h2>カメラと写真</h2><p>カメラは逆上がりの動画を撮るために使います。音声は録りません。写真ライブラリへは、比較動画を保存するときだけ追加の許可を求めます。写真から動画を選ぶときは、選んだ動画だけを本アプリが受け取ります。</p>
<h2>購入</h2><p>Pro の購入は Apple の App Store で処理されます。運営者は支払いの情報を受け取りません。</p>
<h2>半額の案内</h2><p>月額の自動更新を止めた方には、App Store の割引（プロモーションオファー）で半額の案内を出します。止めた理由を伺いますが、答えは端末の中で次の画面の文言を変えるのにだけ使い、外部には送りません。半額で続けるボタンを押したときだけ、App Store の割引に必要な署名を受け取るため、アプリ・商品・割引の番号を運営者のサーバーに送ります。お子さんの情報・動画・止めた理由・Apple ID は送りません。</p>
<h2>消す方法</h2><p>本アプリの［設定］→［動画と見立てをすべて消す］で、動画と記録を消せます。本アプリを削除すると、すべてのデータが消えます。</p>
<h2>子どもの情報</h2><p>本アプリは保護者が使うアプリです。お子さんの映像や情報は端末の外に出ないため、運営者が受け取ることはありません。</p>
<h2>変更</h2><p>このポリシーを変えるときは、このページで知らせます。</p>
<h2>問い合わせ</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>制定: 2026 年 11 月 2 日（同日、半額の案内の項を追加）</p>"""),
  "terms": ("利用規約", f"""<p>この規約は、iPhone アプリ「さかあがりコーチ」（以下「本アプリ」）の利用条件を定めます。本アプリを使うことで、この規約に同意したものとします。</p>
<h2>本アプリの内容</h2><p>本アプリは、動画から姿勢を読み取って逆上がりの練習の目安を示すものです。医療・診断・指導資格に基づく助言ではありません。読み取りの結果には誤りが含まれることがあります。</p>
<h2>安全</h2><p>練習は保護者が付き添い、お子さんの体力と体調に合わせて行ってください。鉄棒の下の地面や周りの安全を確かめてください。本アプリの利用中に起きたけがや事故について、運営者は責任を負いません。</p>
<h2>撮影</h2><p>撮影はお子さん本人と保護者の同意のもとで行い、周りの人が写らないよう配慮してください。</p>
<h2>Pro（有料）</h2><p>Pro には月額（自動更新・はじめの 3 日間無料）と買い切りがあります。月額は、無料期間の終了後に毎月自動で更新され、Apple ID に請求されます。更新日の 24 時間前までに解約しない限り自動で更新されます。解約は iPhone の設定アプリの［ユーザ名］→［サブスクリプション］から行えます。返金は Apple の規定に従います。</p>
<h2>禁止事項</h2><p>本アプリの改変・再配布・逆コンパイル、法令や公序良俗に反する使い方を禁じます。</p>
<h2>変更と終了</h2><p>運営者は、本アプリの内容やこの規約を変えたり、提供を終えたりすることがあります。</p>
<h2>準拠法</h2><p>この規約は日本の法律に従います。</p>
<h2>問い合わせ</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>制定: 2026 年 11 月 2 日</p>"""),
  "support": ("サポート", f"""<h2>うまく測れないとき</h2><ul><li>スマホを横にして、3 歩ほど離れた真横から撮ってください</li><li>頭から足先と、鉄棒の柱が入るようにしてください</li><li>太陽を背にすると体の線がはっきり写ります</li><li>測れなかったときは、止まった場所を 3 つから選ぶと練習が出ます</li></ul>
<h2>購入を復元するには</h2><p>［設定］→［購入を復元］を押してください。</p>
<h2>解約するには</h2><p>iPhone の設定アプリの［ユーザ名］→［サブスクリプション］から解約できます。</p>
<h2>動画を消すには</h2><p>［設定］→［動画と見立てをすべて消す］で消せます。動画はこの iPhone の中にだけあります。</p>
<h2>問い合わせ</h2><p>ご意見・不具合は <a href="mailto:{MAIL}">{MAIL}</a> までお送りください。</p>"""),
 },
 "en": {
  "lang": "en", "home": "./", "other": "../", "other_label": "日本語",
  "nav": ("Home", "Privacy Policy", "Terms", "Support"),
  "index": ("Pullover Coach", """<p><img class="icon" src="{root}icon.png" alt=""></p>
<p>An iPhone app that reads one side-view video of your child's pullover on the bar, narrows it down to the one thing to fix first, and shows drills for exactly that.</p>
<ul><li>Measures foot position, elbow bend, kick height and hip-to-bar distance on the device</li>
<li>Three-step drills for each cause, with reps, where to spot and what to say</li>
<li>Export a day-one vs. latest comparison video with faces blurred automatically</li>
<li>Videos never leave your iPhone. No account needed</li></ul>"""),
  "privacy": ("Privacy Policy", f"""<p>This policy describes how the iPhone app “Pullover Coach” (the App) handles information.</p>
<h2>What we collect</h2><p>We do not collect any personal information from the App. The App has no accounts, no ads and no analytics.</p>
<h2>Videos and records</h2><p>Videos you film or choose, the results of body tracking, your child's name and school year, and practice records are stored only on your device. Body tracking runs on the device using Apple's Vision framework; nothing is sent outside.</p>
<h2>Camera and Photos</h2><p>The camera is used to film the pullover. No audio is recorded. The App asks for add-only access to Photos only when saving a comparison video. When you pick a video from Photos, the App receives only that video.</p>
<h2>Purchases</h2><p>Pro purchases are processed by Apple's App Store. We do not receive payment information.</p>
<h2>Half-price offer</h2><p>If you turn off auto-renewal for the monthly plan, the App offers half price through an App Store promotional offer. The App asks why you turned it off; your answer is used only on the device to adjust the next screen and is never sent. Only when you tap the button to keep Pro at half price does the App send the app, product and offer IDs to our server to receive the signature the App Store requires. Your child's details, videos, your answer and your Apple ID are not sent.</p>
<h2>Deleting data</h2><p>Settings &gt; Delete all videos and analyses removes them. Deleting the App removes all data.</p>
<h2>Children</h2><p>The App is used by parents. Your child's videos and details stay on the device and are never received by us.</p>
<h2>Changes</h2><p>We will post any changes to this policy on this page.</p>
<h2>Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>Effective: November 2, 2026</p>"""),
  "terms": ("Terms of Use", f"""<p>These terms govern your use of the iPhone app “Pullover Coach” (the App). By using the App you agree to them.</p>
<h2>What the App does</h2><p>The App reads body positions from video and offers practice suggestions for the pullover. It is not medical advice or professional coaching, and readings may contain errors.</p>
<h2>Safety</h2><p>A parent should always be present during practice, matched to the child's strength and condition. Check the ground and surroundings of the bar. We are not responsible for injuries or accidents while using the App.</p>
<h2>Filming</h2><p>Film only with the consent of your child and take care not to film other people.</p>
<h2>Pro (paid)</h2><p>Pro is available as a monthly auto-renewing subscription (first 3 days free) or a one-time lifetime purchase. The monthly plan renews automatically each month after the free trial and is charged to your Apple ID unless canceled at least 24 hours before the renewal date. Cancel in Settings &gt; your name &gt; Subscriptions. Refunds follow Apple's policies.</p>
<h2>Prohibited use</h2><p>Do not modify, redistribute or decompile the App, or use it unlawfully.</p>
<h2>Changes and termination</h2><p>We may change the App or these terms, or stop providing the App.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of Japan.</p>
<h2>Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>Effective: November 2, 2026</p>"""),
  "support": ("Support", f"""<h2>If the video can't be measured</h2><ul><li>Hold the phone sideways and film directly from the side, about three steps away</li><li>Keep the whole body, head to toe, and the bar's post in the frame</li><li>Keep the sun behind you</li><li>If measuring fails, choose where your child got stuck from three options to get drills</li></ul>
<h2>Restoring purchases</h2><p>Settings &gt; Restore Purchases.</p>
<h2>Canceling</h2><p>Settings app &gt; your name &gt; Subscriptions.</p>
<h2>Deleting videos</h2><p>Settings &gt; Delete all videos and analyses. Videos are stored only on this iPhone.</p>
<h2>Contact</h2><p>Send feedback or bug reports to <a href="mailto:{MAIL}">{MAIL}</a>.</p>"""),
 },
}
FILES = {"index": "index.html", "privacy": "privacy.html", "terms": "terms.html", "support": "support.html"}


def page(p, kind, root):
    title, body = p[kind]
    links = " ".join(f'<a href="{FILES[k]}">{label}</a>' for k, label in zip(FILES, p["nav"]))
    app = p["index"][0]
    head_title = app if kind == "index" else f"{title} | {app}"
    return f"""<!doctype html><html lang="{p['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{head_title}</title><link rel="stylesheet" href="{root}style.css"></head><body><main>
<nav>{links} <a href="{p['other']}{FILES[kind]}">{p['other_label']}</a></nav>
<h1>{title}</h1><div class="bar"></div>{body.replace('{root}', root)}
<footer>© 2026 Process Craft AI</footer></main></body></html>
"""


def main():
    open("style.css", "w").write(CSS)
    os.makedirs("en", exist_ok=True)
    for lang, root, folder in (("ja", "", "."), ("en", "../", "en")):
        for kind, name in FILES.items():
            open(os.path.join(folder, name), "w").write(page(PAGES[lang], kind, root))


if __name__ == "__main__":
    main()
