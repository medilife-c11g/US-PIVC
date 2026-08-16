#!/usr/bin/env python3
# Generate 21 teaching slides (1920x1080 HTML) + narration.json for the US-PIVC 20-min lecture
import json, os, html

W = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(W, "fig")

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden}
body{font-family:"PingFang TC","Noto Sans TC",-apple-system,sans-serif;background:#FFFFFF;color:#16324F;
     display:flex;flex-direction:column}
.top{height:14px;background:linear-gradient(90deg,#0E7C86,#16324F)}
.wrap{flex:1;padding:56px 88px 40px;display:flex;flex-direction:column}
h1.big{font-size:88px;font-weight:800;line-height:1.2;letter-spacing:.01em}
h2.slide-title{font-size:60px;font-weight:800;color:#16324F;margin-bottom:12px}
.kicker{font-size:26px;font-weight:700;color:#0E7C86;text-transform:uppercase;letter-spacing:.14em;margin-bottom:14px}
.sub{font-size:34px;color:#5B6B7C;margin-top:22px;line-height:1.5}
.rule{height:5px;width:150px;background:#0E7C86;border-radius:3px;margin:26px 0 34px}
ul.b{list-style:none;font-size:38px;line-height:1.55}
ul.b li{padding-left:52px;position:relative;margin-bottom:26px}
ul.b li::before{content:"";position:absolute;left:8px;top:22px;width:16px;height:16px;border-radius:4px;background:#0E7C86}
ul.b li.warn::before{background:#C2542D}
ul.b b{color:#0E7C86}.warn b{color:#C2542D}
.cols{display:flex;gap:56px;flex:1;min-height:0}
.col-t{flex:0 0 620px;display:flex;flex-direction:column}
.col-f{flex:1;display:flex;align-items:center;justify-content:center;background:#F6F8FA;border:1px solid #E3E9EF;border-radius:18px;padding:26px}
.col-f img{max-width:100%;max-height:100%;object-fit:contain}
.statrow{display:flex;gap:44px;margin-top:8px}
.stat{flex:1;background:#F2F7F8;border:1px solid #DBE7EA;border-left:10px solid #0E7C86;border-radius:16px;padding:34px 38px}
.stat.warn{border-left-color:#C2542D;background:#FBF3EF;border-color:#EFDCD2}
.stat .n{font-size:76px;font-weight:800;color:#16324F;line-height:1.05}
.stat .l{font-size:27px;color:#5B6B7C;margin-top:12px;line-height:1.4}
.foot{height:56px;display:flex;align-items:center;justify-content:space-between;padding:0 88px;
      font-size:21px;color:#8896A5;border-top:1px solid #EDF1F5}
.badge{display:inline-block;background:#0E7C86;color:#fff;font-size:26px;font-weight:700;
       border-radius:999px;padding:8px 26px;margin-right:14px}
.note{margin-top:auto;background:#FFF8E8;border:1px solid #F0E3BB;border-radius:14px;padding:20px 28px;font-size:28px;color:#7A5B12;line-height:1.45}
table.t{border-collapse:collapse;font-size:30px;width:100%}
table.t th{background:#16324F;color:#fff;padding:16px 20px;text-align:left;font-weight:700}
table.t td{padding:15px 20px;border-bottom:1px solid #E3E9EF;line-height:1.4}
table.t tr td:first-child{font-weight:700}
.center{display:flex;flex-direction:column;justify-content:center;flex:1}
"""

def page(body, idx, total=21, footer="US-PIVC Post-insertion Outcomes — The Ultrasound Journal 2026 · 陳家慶"):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="top"></div><div class="wrap">{body}</div>
<div class="foot"><span>{footer}</span><span>{idx} / {total}</span></div></body></html>"""

S = []  # (body_html, narration)

# ---- S1 Title
S.append((f"""
<div class="center" style="align-items:flex-start">
 <div class="kicker">20 分鐘教學 · Journal Club</div>
 <h1 class="big">超音波導引 PIVC:<br>放進去<span style="color:#0E7C86">之後</span>表現如何?</h1>
 <div class="rule"></div>
 <div class="sub">Post-insertion outcomes of ultrasound-guided versus landmark<br>peripheral intravenous catheters: a systematic review and meta-analysis</div>
 <div class="sub" style="font-size:29px;margin-top:30px">Lee TA†, Wang YL†, Lin JT, Chen PM, <b>Chen CC*</b> — <i>The Ultrasound Journal</i> 2026(#19152)<br>PROSPERO:CRD420261354170</div>
</div>""",
"大家好,歡迎來到今天二十分鐘的教學。今天要講的是我們團隊發表在 The Ultrasound Journal 的系統性回顧與統合分析,主題是超音波導引的周邊靜脈導管。過去我們都知道,超音波能幫助困難靜脈的病人成功打上點滴,但是今天要問一個更進一步、也更少人問的問題:針放進去之後,這條管路的表現,超音波導引真的比較好嗎?它會活得比較久、比較不會壞掉嗎?這篇研究整合了十五篇文獻、將近八萬名受試者的資料,給了一個可能顛覆直覺的答案。"))

# ---- S2 Objectives
S.append(("""
<div class="kicker">Learning Objectives</div>
<h2 class="slide-title">今天結束後,你能夠</h2>
<div class="rule"></div>
<ul class="b" style="font-size:42px">
 <li>區分 USG-PIVC 的 <b>insertion-phase</b> 與 <b>post-insertion</b> 證據 — 兩者不能互相推論</li>
 <li>說出本統合分析的核心數字:<b>catheter failure RR 1.23(95% CI 1.00–1.51)</b>的正確解讀方式</li>
 <li>辨識文獻中的關鍵混雜:<b>導管長度與規格</b>(catheter-specification confounding)</li>
 <li class="warn">把結論帶回床邊:<b>選導管,而不只是選 guidance</b></li>
</ul>""",
"先講今天的四個學習目標。第一,學會把超音波導引靜脈留置的證據切成兩段:插入階段的證據,和插入之後的證據,並且理解前者的成功不能直接推論後者。第二,掌握這篇統合分析的核心數字:導管失敗的相對風險一點二三,信賴區間一點零零到一點五一,以及為什麼這樣一個邊緣性的結果需要特別小心解讀。第三,學會辨識這個領域文獻裡最重要的混雜因子:導管的長度與規格。最後,也是最實用的,把這些證據轉成床邊決策:如果你在乎的是這條管路能活多久,重點可能不是有沒有用超音波,而是你選了什麼導管。"))

# ---- S3 Background
S.append(("""
<div class="kicker">Background</div>
<h2 class="slide-title">PIVC:最普遍,也最常壞掉的處置</h2>
<div class="rule"></div>
<div class="statrow">
 <div class="stat"><div class="n">~10 億支/年</div><div class="l">全球每年置放的 PIVC 數量 — 醫院裡最常見的侵入性處置</div></div>
 <div class="stat"><div class="n">DIVA</div><div class="l">困難靜脈(difficult IV access)病人:反覆穿刺、延誤治療、耗用人力</div></div>
 <div class="stat"><div class="n">USG ↑</div><div class="l">近二十年超音波導引成為 guideline 背書的解方 — 但背書的是「插入」</div></div>
</div>
<div class="note">失敗的 PIVC = 重打一次 + 治療中斷 + 病人疼痛 + 醫療成本 — post-insertion 表現才決定這條管路的實際價值</div>""",
"先看背景。周邊靜脈導管是全世界醫院最常執行的侵入性處置,估計每年放置約十億支。但它同時也是一個很容易失敗的裝置:靜脈炎、滲漏、阻塞、滑脫,常常在治療完成之前就陣亡,然後就是重打一次、治療中斷、病人多挨一針。對困難靜脈的病人,也就是所謂 DIVA 族群,這個問題更嚴重。過去二十年,超音波導引成為各大指引背書的解方,急診、加護病房都在推。但請注意,指引背書的核心證據,幾乎都集中在插入那一刻的成功率。管路放進去之後的日子,反而很少被系統性地檢視,而那才是決定這條管路臨床價值的關鍵。"))

# ---- S4 Known evidence & gap
S.append(("""
<div class="kicker">What We Know vs. The Gap</div>
<h2 class="slide-title">插入證據很強;插入之後是空白</h2>
<div class="rule"></div>
<ul class="b">
 <li><b>已確立(多篇 SR/MA)</b>:USG 提升 first-attempt success、減少穿刺次數 — 尤其 DIVA 病人;已寫入 guideline 與訓練課程</li>
 <li>但成功插入只是導管生命週期的<b>起點</b>:dwell time、failure、phlebitis、infiltration、extravasation、occlusion、dislodgement…</li>
 <li class="warn"><b>缺口</b>:在本研究之前,<b>沒有任何 SR 專門整合</b> USG vs landmark 的 post-insertion 表現</li>
 <li class="warn">大家默默假設「插得好=活得久」— 這個假設<b>從未被驗證</b></li>
</ul>""",
"這頁把已知與未知講清楚。已知的部分:多篇系統性回顧一致顯示,超音波導引提高第一次嘗試成功率、減少皮膚穿刺次數,在困難靜脈族群效果特別明顯。這是紮實的證據,也是它進入指引的理由。但是,成功插入只是這個裝置生命週期的起點。之後的留置時間、導管失敗、靜脈炎、滲漏、外滲、阻塞、滑脫,這些結局其實同等重要,甚至更重要。而在我們這篇研究之前,文獻裡沒有任何一篇系統性回顧,專門去整合超音波導引與傳統定位法在插入之後的表現比較。大家心裡默默假設,插得漂亮等於活得長久。這個假設,從來沒有被驗證過。這就是我們做這篇研究的理由。"))

# ---- S5 PICO
S.append(("""
<div class="kicker">Research Question</div>
<h2 class="slide-title">PICO 與註冊</h2>
<div class="rule"></div>
<table class="t" style="font-size:34px">
 <tr><th style="width:220px">P</th><td>接受 PIVC 置放的病人(成人與兒科;含 DIVA)</td></tr>
 <tr><th>I</th><td>超音波導引(USG)PIVC 置放</td></tr>
 <tr><th>C</th><td>Landmark / palpation 傳統定位置放</td></tr>
 <tr><th>O</th><td><b>主要:catheter failure、dwell time</b>;次要:infiltration、extravasation、phlebitis、occlusion、dislodgement、感染</td></tr>
 <tr><th>設計</th><td>RCT + 比較性 cohort;PRISMA 2020;<b>PROSPERO CRD420261354170(前瞻註冊)</b></td></tr>
</table>""",
"研究問題用 PICO 架構整理。族群是所有接受周邊靜脈導管置放的病人,成人與兒科都收,包含困難靜脈族群。介入是超音波導引置放,對照是傳統的體表定位或觸診置放。結局方面,主要結局有兩個:導管失敗,以及留置時間;次要結局包括滲漏、外滲、靜脈炎、阻塞、滑脫和導管相關感染。設計上,我們同時納入隨機對照試驗與比較性世代研究,依循 PRISMA 2020 規範,並且在動手之前就在 PROSPERO 完成前瞻性註冊,註冊號 CRD420261354170。前瞻註冊很重要,它把我們的主要結局和分析計畫先鎖定,避免事後挑好看的結果來報告。"))

# ---- S6 Methods
S.append(("""
<div class="kicker">Methods</div>
<h2 class="slide-title">方法重點:雙人盲篩 + 保守的合併原則</h2>
<div class="rule"></div>
<ul class="b" style="font-size:36px">
 <li><b>檢索</b>:PubMed、Embase、Cochrane CENTRAL、CINAHL(2000/01–2026/03)</li>
 <li><b>篩選</b>:Rayyan 雙人獨立盲篩(T/A 一致率 95.8%,κ=0.330 — κ paradox:高排除率下 κ 偏低,非實質歧見);資深作者仲裁</li>
 <li><b>RoB</b>:RCT 用 <b>RoB 2</b>;cohort 用 <b>Newcastle–Ottawa Scale</b></li>
 <li><b>統計</b>:random-effects(DL,PROSPERO 預設);REML+HKSJ 作 post-hoc 敏感度;<b>I²>75% 不合併</b>(pre-specified)</li>
 <li><b>證據確定性</b>:GRADE</li>
</ul>""",
"方法的重點有五個。第一,檢索四個資料庫:PubMed、Embase、Cochrane CENTRAL 和 CINAHL,涵蓋兩千年一月到二零二六年三月。第二,標題摘要用 Rayyan 做雙人獨立盲篩,一致率百分之九十五點八,kappa 零點三三。這裡順便教一個觀念:在排除率極高的篩選情境,kappa 會被壓低,這叫 kappa paradox,反映的是統計性質而不是審查者真的意見分歧,爭議由資深作者仲裁解決。第三,偏誤風險評估,隨機試驗用 RoB 2,世代研究用 Newcastle-Ottawa 量表。第四,統計採隨機效應模式,以 DerSimonian-Laird 為預先註冊的主要方法,另外用 REML 加 HKSJ 校正做事後敏感度分析;而且我們預先規定,異質性 I 平方超過百分之七十五就不合併,寧可誠實呈現分歧,也不硬算一個沒有意義的平均。最後,證據確定性用 GRADE 分級。"))

# ---- S7 PRISMA (figure)
S.append((f"""
<div class="kicker">Study Selection</div>
<h2 class="slide-title">PRISMA:1,632 → 15 篇</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t"><ul class="b" style="font-size:33px">
  <li>4 資料庫共 <b>1,632</b> 筆 → 去重後 <b>1,359</b></li>
  <li>雙人盲篩:1,287 雙方排除;72 進入 union 名單,53 筆經第二輪共識程序排除</li>
  <li><b>19 篇全文審查</b> → 排除 4(無比較組、葡語重複報告、未發表、EPIC 重複)</li>
  <li><b>15 篇納入質性整合</b>;各 meta-analysis 依結局取子集</li>
 </ul></div>
 <div class="col-f"><img src="file://{FIG}/prisma.png"></div>
</div>""",
"這是 PRISMA 流程。四個資料庫總共找到一千六百三十二筆,去除重複後一千三百五十九筆進入標題摘要篩選。兩位審查者獨立作業,一千二百八十七筆被雙方一致排除;七十二筆至少一人勾選納入,再經過預先規定的共識討論程序,排除五十三筆,留下十九篇進入全文審查。全文階段再排除四篇:一篇沒有比較組、一篇是葡萄牙文的重複報告、一篇未正式發表、一篇是同一個 EPIC 試驗的重複紀錄。最後十五篇納入質性整合。要注意的是,不是十五篇都能進每一個統合分析,而是依照各篇報告的結局與合併適格性,分別取子集合併,等一下每張 forest plot 的篇數都會不一樣,這是正常的。"))

# ---- S8 Included studies
S.append(("""
<div class="kicker">Included Studies</div>
<h2 class="slide-title">15 篇:6 RCT + 9 cohort,n = 78,591</h2>
<div class="rule"></div>
<ul class="b" style="font-size:35px">
 <li><b>地理分布</b>:美國多篇 + 澳洲、巴西、法國、印度、義大利(×2)、日本等 — 外部效度佳</li>
 <li><b>代表性 RCT</b>:Kleidon 2025(EPIC trial,兒科 164 人,澳洲)、Varghese 2025、Nishizawa 2020、Bridey 2018、Avelar 2015</li>
 <li><b>最大 cohort</b>:Feinsmith 2023 — <b>43,470 位成人 DIVA</b>(美國)</li>
 <li><b>唯一「無混雜且正向」</b>:Cottrell 2021 — 專責血管通路團隊,兒科</li>
 <li class="warn"><b>4 篇因導管規格混雜被排除於合併</b>:Refosco 2025、Dachepally 2023、Desai 2018、Paladini(兩組導管長度/材質系統性不同)</li>
</ul>""",
"十五篇研究的樣貌。設計上六篇隨機試驗、九篇世代研究,合計七萬八千五百九十一位受試者;地理上橫跨美國、澳洲、巴西、法國、印度、義大利、日本等地,外部效度相當不錯。幾篇值得認識的:兒科的 EPIC 隨機試驗,Kleidon 二零二五年發表;最大的世代研究是 Feinsmith 二零二三,單篇就有四萬三千多位成人困難靜脈病人;還有一篇很特別的 Cottrell 二零二一,它是全部文獻裡唯一一篇沒有導管規格混雜、又報告超音波顯著優勢的研究,特色是由經驗豐富的專責血管通路團隊執行。最後注意紅字:有四篇研究,因為超音波組和對照組用的導管長度或材質系統性不同,結果無法歸因於導引方式本身,被我們排除在合併分析之外。這個混雜等一下會是整堂課的關鍵轉折。"))

# ---- S9 RoB (figure)
S.append((f"""
<div class="kicker">Risk of Bias</div>
<h2 class="slide-title">偏誤風險:open-label 是天生限制</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t"><ul class="b" style="font-size:33px">
  <li><b>RCT(RoB 2)</b>:6 篇中 5 篇整體「some concerns」— 主因是無法盲化操作者的 <b>performance bias</b></li>
  <li><b>Cohort(NOS)</b>:5–9 分;Shokoohi 2019 拿滿分 9/9</li>
  <li class="warn">Avelar 試驗:USG 組用超音波確認併發症、對照組僅臨床評估 — <b>differential ascertainment</b> 可能高估 USG 組 infiltration</li>
 </ul></div>
 <div class="col-f"><img src="file://{FIG}/rob.png"></div>
</div>""",
"偏誤風險評估。六篇隨機試驗裡有五篇整體評為 some concerns,最主要的原因很好理解:打針這件事不可能對操作者設盲,你一定知道自己手上有沒有拿探頭,所以 performance bias 是這類研究的天生限制。九篇世代研究的 Newcastle-Ottawa 分數從五分到九分,其中 Shokoohi 二零一九拿到滿分。這裡再教一個精緻的偏誤:Avelar 試驗在超音波組是用超音波影像去確認滲漏,對照組卻只用臨床評估,兩組的偵測敏感度不同,這叫差異性確認偏誤,它會讓超音波組的滲漏看起來比較多。這個偏誤方向等一下解讀滲漏結果時要放在心上。"))

# ---- S10 Catheter failure (figure)
S.append((f"""
<div class="kicker">Primary Outcome ①</div>
<h2 class="slide-title">Catheter Failure:RR 1.23,擦線而過</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t">
  <div class="stat warn" style="margin-bottom:26px"><div class="n">RR 1.23</div><div class="l">95% CI 1.00–1.51;p=0.056;I²=0%(k=4;精確下界 0.995)</div></div>
  <ul class="b" style="font-size:31px">
   <li>點估計<b>方向不利 USG</b>(失敗多 23%)</li>
   <li>REML+HKSJ 敏感度:RR 1.23,p=<b>0.047</b> — 顯著性<b>跨在 α=0.05 兩側</b>,取決於估計法</li>
   <li class="warn">正確讀法:看點估計與整體證據型態,<b>不要被 p 值兩側跳動綁架</b></li>
  </ul>
 </div>
 <div class="col-f"><img src="file://{FIG}/failure.png"></div>
</div>""",
"進入主要結局:導管失敗。四篇研究可合併,隨機效應相對風險一點二三,信賴區間一點零零到一點五一,p 值零點零五六,研究間異質性是零。三個重點。第一,點估計的方向對超音波不利:超音波組的導管失敗率高了約百分之二十三。第二,這是一個標準的擦線結果:主要分析 p 等於零點零五六,換一個估計方法做敏感度分析,p 變成零點零四七,一個在線上、一個在線下。第三,也是統計素養的重點:當顯著性隨估計方法在零點零五兩側跳動,正確的做法不是宣告顯著或不顯著,而是回頭看點估計的方向、信賴區間的寬度,和整體證據的型態。這筆資料告訴我們的是:超音波導引至少沒有讓導管比較不會壞,方向上甚至偏向更容易壞。"))

# ---- S11 Sensitivity dissection
S.append(("""
<div class="kicker">Sensitivity Dissection</div>
<h2 class="slide-title">訊號從哪來?拆開看就懂</h2>
<div class="rule"></div>
<div class="statrow" style="margin-bottom:30px">
 <div class="stat"><div class="n" style="font-size:56px">Cohort RR 1.29</div><div class="l">(1.02–1.63) p=0.036 — <b>訊號主要來自世代研究</b></div></div>
 <div class="stat"><div class="n" style="font-size:56px">RCT RR 1.03</div><div class="l">(0.66–1.61) p=0.91 — 隨機試驗基本上是平的</div></div>
</div>
<ul class="b" style="font-size:34px">
 <li><b>Leave-one-out</b>:移除 <b>Saltarelli</b>(最大權重 49.8%,僅會議摘要)→ RR 1.18(0.88–1.58)<b>轉不顯著</b></li>
 <li>移除 <b>Kleidon</b>(唯一兒科)→ RR 1.28(1.02–1.60)<b>轉顯著</b></li>
 <li class="warn">結論:borderline 訊號<b>依賴單一大型研究</b>、且由觀察性資料驅動 — hypothesis-generating,不是定論</li>
</ul>""",
"擦線的訊號,拆開來看就知道它從哪裡來。第一刀,按設計分層:世代研究單獨合併,相對風險一點二九,達統計顯著;隨機試驗單獨合併,一點零三,幾乎完全是平的。訊號主要由觀察性資料驅動,而觀察性資料裡,醫師本來就傾向把超音波用在血管條件最差的病人身上,這種適應症混雜天然會讓超音波組看起來比較差。第二刀,逐一剔除:移除權重最大、佔將近一半、而且只有會議摘要形式的 Saltarelli,估計值衰減成一點一八、不再顯著;反過來移除唯一的兒科研究 Kleidon,估計值變成一點二八、變成顯著。一個結果會因為拿掉任何一篇就翻面,就代表它高度依賴個別研究。所以這個訊號的定位是:值得提出假說、值得後續驗證,但絕對不是定論。"))

# ---- S12 Dwell time (figure)
S.append((f"""
<div class="kicker">Primary Outcome ②</div>
<h2 class="slide-title">Dwell Time:I²=91.9%,誠實不合併</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t"><ul class="b" style="font-size:31px">
  <li><b>Kleidon 2025</b>(兒科 RCT):47.1 vs 47.7 h — 無差異</li>
  <li><b>Leroux 2023</b>:23.5 vs 24.7 h(p=0.808)— 無差異</li>
  <li><b>Cottrell 2021</b>:96.1 vs 59.4 h(p&lt;0.001)— <b>+36.7 小時</b>優勢!但:專責血管通路團隊、兒科情境</li>
  <li class="warn">解讀:dwell time 的好處是 <b>setting- 與 operator-dependent</b>,不是 guidance 本身的普遍效果</li>
 </ul></div>
 <div class="col-f"><img src="file://{FIG}/dwell.png"></div>
</div>""",
"第二個主要結局,留置時間。三篇無混雜研究可用,但 I 平方高達百分之九十一點九,依照預先規定,我們不合併,改用敘事整合。三篇的故事非常分歧:兒科 EPIC 試驗,四十七點一對四十七點七小時,沒差;Leroux,二十三點五對二十四點七小時,也沒差;但 Cottrell 卻報告超音波組平均多活三十六點七個小時,差距顯著。怎麼理解這個矛盾?看誰在操作。Cottrell 的超音波是由經驗豐富的專責血管通路團隊執行,在兒科這種血管特別難的情境。所以合理的解讀是:留置時間的好處,取決於場域和操作者,是團隊專業加上超音波的組合效果,而不是超音波這個工具本身放諸四海皆準的效果。這也提醒我們,買了機器不等於買到結果,人和制度才是關鍵配方。"))

# ---- S13 Infiltration (figure)
S.append((f"""
<div class="kicker">Secondary Outcome</div>
<h2 class="slide-title">Infiltration:RR 1.30,無顯著差異</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t">
  <div class="stat" style="margin-bottom:26px"><div class="n" style="font-size:62px">RR 1.30</div><div class="l">95% CI 0.82–2.05;p=0.26;I²=48.8%(k=3)</div></div>
  <ul class="b" style="font-size:30px">
   <li>Varghese:2.2% vs 11.1%(偏好 USG,p=0.09)</li>
   <li>Saltarelli:7.6% vs 5.9%(偏不利 USG)</li>
   <li class="warn">Avelar:21.1% vs 12.9%(p=0.025 不利 USG)— 但 USG 組用超音波偵測,<b>differential ascertainment</b> 可能灌水</li>
  </ul>
 </div>
 <div class="col-f"><img src="file://{FIG}/infil.png"></div>
</div>""",
"次要結局,滲漏。三篇合併,相對風險一點三零,信賴區間零點八二到二點零五,統計上沒有顯著差異,中度異質性。三篇的方向並不一致:Varghese 偏向超音波比較好,Saltarelli 稍微不利超音波,而 Avelar 顯示超音波組滲漏顯著較多,百分之二十一對百分之十三。但記得前面講過的偵測偏誤嗎?Avelar 的超音波組是用超音波去找滲漏,對照組只用肉眼和臨床判斷,偵測工具靈敏度不同,超音波組的數字很可能被灌水。整體而言,滲漏這個結局的誠實結論是:證據不足以說哪邊比較好,但同樣也沒有證據支持超音波導引能減少滲漏。"))

# ---- S14 Extravasation (figure)
S.append((f"""
<div class="kicker">Safety Signal</div>
<h2 class="slide-title">Extravasation:GRADE ⊕◯◯◯ 的警訊</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t"><ul class="b" style="font-size:31px">
  <li>3 篇定義/族群互不相容,I²=95.7% → <b>不合併</b>,逐篇讀</li>
  <li class="warn"><b>Favot 2019</b>:CT 顯影劑外滲 4.1% vs 0.21% — <b>RR 19.4</b>(10.6–35.6)!高壓注射情境</li>
  <li class="warn"><b>Bridey 2018</b>(ICU):34% vs 18%(p=0.094)</li>
  <li><b>Nishizawa 2020</b>:方向相反(13.6% vs 28.5%)</li>
  <li>定位:<b>hypothesis-generating 安全訊號</b>,證據確定性極低 — 但機轉合理(下頁)</li>
 </ul></div>
 <div class="col-f"><img src="file://{FIG}/extrav.png"></div>
</div>""",
"再來是外滲,這是本篇最值得急診人注意的安全訊號。三篇研究的族群和定義完全不相容,異質性百分之九十五點七,所以不合併,逐篇解讀。Favot 二零一九最驚人:在電腦斷層顯影劑高壓注射的情境下,超音波置放的導管外滲率百分之四點一,對照組只有百分之零點二一,相對風險十九點四倍。Bridey 在加護病房看到百分之三十四對百分之十八的差距,未達顯著。但 Nishizawa 的方向卻相反。方向不一致加上極低的證據確定性,GRADE 是最低的一顆星都不到,所以這只能定位為假說性的安全訊號。不過,它背後有一個非常合理的生物力學機轉,值得認真對待,下一頁講。"))

# ---- S15 Adult subgroup (figure)
S.append((f"""
<div class="kicker">Subgroup</div>
<h2 class="slide-title">成人亞組:RR 1.28(1.02–1.60)</h2>
<div class="rule"></div>
<div class="cols">
 <div class="col-t"><ul class="b" style="font-size:32px">
  <li><b>成人(k=3)</b>:RR 1.28,p=0.03 — 點估計不利 USG</li>
  <li><b>兒科(k=1,Kleidon)</b>:RR 0.95 — 無差異</li>
  <li>亞組交互作用檢定 <b>p=0.32(不顯著)</b> → 只能當 hypothesis-generating</li>
  <li class="warn">且成人 pool 被 Saltarelli(~50% 權重、會議摘要)主導 — <b>不要過度解讀</b></li>
 </ul></div>
 <div class="col-f"><img src="file://{FIG}/age.png"></div>
</div>""",
"年齡亞組分析。成人三篇合併,相對風險一點二八,p 零點零三,方向不利超音波;兒科只有一篇,相對風險零點九五,看不出差別。但是有兩個煞車要踩。第一,亞組之間的交互作用檢定 p 值零點三二,並不顯著,意思是成人和兒科的差別本身可能只是機遇,統計方法學上這種亞組結果只能當作產生假說。第二,成人這個池子有一半的權重來自那篇只有會議摘要的 Saltarelli,前面已經看過,把它拿掉整個結果就翻面。所以正確的態度是:記下這個成人方向不利的觀察,期待未來研究驗證,但不要拿去改變臨床。"))

# ---- S16 Confounding
S.append(("""
<div class="kicker">The Key Confounder</div>
<h2 class="slide-title">導管規格混雜:正向研究的共同秘密</h2>
<div class="rule"></div>
<ul class="b" style="font-size:35px">
 <li>4 篇「USG 較好」的研究 — <b>Refosco、Dachepally、Desai、Paladini</b> — USG 組同時用了<b>更長/不同材質的導管</b></li>
 <li>例:Refosco 2025 — dwell 5.3 vs 2.5 天、併發症 34% vs 70%…但 USG 組用長導管,<b>效果無法歸因於超音波</b></li>
 <li class="warn">關鍵問題:USG 是否<b>天生誘使</b>使用長導管?— 因為它讓你打到 1–2 cm 深的 brachial/basilic/深前臂靜脈</li>
 <li><b>教訓</b>:讀這領域文獻,第一個問題永遠是「<b>兩組導管一樣嗎?</b>」</li>
</ul>""",
"現在揭曉整堂課的關鍵轉折:導管規格混雜。文獻裡報告超音波明顯較好的四篇研究,Refosco、Dachepally、Desai、Paladini,有一個共同的秘密:它們的超音波組同時用了更長、或材質不同的導管。以 Refosco 為例,留置天數五點三對二點五天,併發症百分之三十四對七十,看起來壓倒性勝利,但超音波組用的是長導管,你根本分不清楚是超音波的功勞,還是長導管的功勞。更深一層想,這個混雜可能是結構性的:超音波讓你打得到一到兩公分深、摸不到的肱靜脈、貴要靜脈,而打深靜脈自然會想拿長導管,所以導引方式和導管選擇在真實世界是綁在一起的。從今天起,讀這個領域的文獻,第一個要問的問題永遠是:兩組用的導管一樣嗎?"))

# ---- S17 Mechanism
S.append(("""
<div class="kicker">Mechanism</div>
<h2 class="slide-title">為什麼深靜脈 + 短導管 = 危險組合?</h2>
<div class="rule"></div>
<div class="cols" style="align-items:center">
 <div class="col-t" style="flex:1"><ul class="b" style="font-size:34px">
  <li>USG 常打 <b>1.0–2.0 cm 深</b>的靜脈;標準導管僅 <b>4.5 cm</b></li>
  <li>深度吃掉長度 → <b>血管內段(dwell ratio)不足</b> → 手臂一動,尖端就滑出血管外</li>
  <li class="warn">高壓情境(CT 顯影劑)= 放大器 → Favot 的 <b>RR 19.4</b></li>
  <li><b>對策方向</b>:深靜脈考慮 <b>≥4.78 cm 長導管</b>、確認足夠血管內長度、強化固定</li>
 </ul></div>
 <div style="flex:0 0 640px;background:#F6F8FA;border:1px solid #E3E9EF;border-radius:18px;padding:44px;font-size:30px;line-height:1.7">
  <b style="color:#0E7C86">床邊心算</b><br>皮下深度 1.5 cm ÷ 進針角 30°<br>→ 走行段 ≈ 3.0 cm<br>4.5 cm 導管 − 3.0 cm<br>→ <b style="color:#C2542D">血管內只剩 ~1.5 cm</b><br><br>手臂屈伸/軟組織位移<br>→ 尖端脫出 → 滲漏/外滲
 </div>
</div>""",
"為什麼深靜脈加短導管是危險組合?我們做個床邊心算。超音波導引常常打的是一到兩公分深的靜脈,而台灣多數單位的標準導管只有四點五公分。假設靜脈深一點五公分,以三十度進針,光是從皮膚走到血管,就要消耗大約三公分的導管長度,剩下留在血管腔內的只有一點五公分左右。手臂一屈一伸、軟組織一位移,這麼短的血管內段很容易就讓尖端退出血管外,藥物就往組織裡跑。再把場景換成電腦斷層的顯影劑高壓注射,壓力放大器一開,就是 Favot 那個十九倍外滲風險的來源。所以對策的方向很清楚:要用超音波打深靜脈,就考慮四點七八公分以上的長導管,置放時確認足夠的血管內長度,並且把固定做好。工具沒有錯,錯的是工具組合。"))

# ---- S18 GRADE
S.append(("""
<div class="kicker">Certainty of Evidence</div>
<h2 class="slide-title">GRADE:全結局 Low – Very Low</h2>
<div class="rule"></div>
<table class="t" style="font-size:31px">
 <tr><th>結局</th><th>結果</th><th>GRADE</th><th>主要降級原因</th></tr>
 <tr><td>Catheter failure</td><td>RR 1.23(1.00–1.51)</td><td>⊕⊕◯◯ Low</td><td>觀察性主導、嚴重不精確</td></tr>
 <tr><td>Dwell time</td><td>不合併(I²=91.9%)</td><td>⊕◯◯◯ Very low</td><td>嚴重不一致</td></tr>
 <tr><td>Infiltration</td><td>RR 1.30(0.82–2.05)</td><td>⊕⊕◯◯ Low</td><td>不精確、ascertainment</td></tr>
 <tr><td>Extravasation</td><td>不合併(I²=95.7%)</td><td>⊕◯◯◯ Very low</td><td>不一致、定義異質</td></tr>
</table>
<div class="note">Low/Very low ≠「沒有效果」— 而是「<b>真實效果很可能與估計值不同</b>」:留意任何方向的驚喜</div>""",
"把證據確定性總整理。用 GRADE 框架評,四個結局全部落在低到極低:導管失敗是低,主因是觀察性研究主導加上嚴重不精確;留置時間極低,因為研究間嚴重不一致;滲漏是低;外滲極低。這裡要糾正一個常見誤讀:低確定性不等於沒有效果,它的正確翻譯是:真實效果很有可能和目前的估計值不一樣,未來的研究很可能改變我們的結論,任何方向的驚喜都可能出現。所以這篇統合分析教我們的,不是超音波不好,而是在插入之後這個題目上,我們手上的證據還太薄,既不能宣稱好處,也不能宣稱等效,更不能排除傷害。"))

# ---- S19 Clinical implications
S.append(("""
<div class="kicker">Clinical Implications</div>
<h2 class="slide-title">帶回床邊的四件事</h2>
<div class="rule"></div>
<ul class="b" style="font-size:38px">
 <li><b>USG 繼續用</b> — 插入階段的價值(first-attempt success、DIVA)證據紮實,不因本篇動搖</li>
 <li class="warn">但<b>不要假設</b> USG 自動讓導管活更久、併發症更少 — 目前無此證據</li>
 <li>在乎 post-insertion 表現?焦點放在 <b>catheter selection</b>:長度、口徑、材質、目標靜脈深度</li>
 <li>深靜脈 + 高壓注射(CT 顯影)= 高風險組合 → <b>長導管 + 確認血管內長度 + 固定</b></li>
</ul>""",
"臨床啟示濃縮成四件事。第一,超音波請繼續用,它在插入階段的價值,特別是困難靜脈病人的首次成功率,證據非常紮實,今天這篇研究完全不動搖這一點。第二,但請把腦中那個自動連結拆掉:不要假設用了超音波,導管就會活得比較久、併發症比較少,目前沒有證據支持這個假設,方向甚至偏向相反。第三,如果你在乎的是插入之後的表現,把注意力從導引方式移到導管選擇:長度、口徑、材質,以及你要打的靜脈有多深。第四,一個具體的高風險組合要記牢:深靜脈置放加上顯影劑高壓注射;遇到這個組合,用長導管、置放時確認血管內段夠長、固定確實,必要時重新評估這條路是否適合打顯影劑。"))

# ---- S20 Limitations
S.append(("""
<div class="kicker">Limitations</div>
<h2 class="slide-title">研究限制(誠實面對)</h2>
<div class="rule"></div>
<ul class="b" style="font-size:35px">
 <li>證據基礎<b>小而異質</b>:僅 6 RCT + 9 cohort;族群、定義、追蹤時間各異</li>
 <li>合併結局的 k 都很小(2–4 篇);<b>&lt;10 篇無法檢驗發表偏倚</b></li>
 <li>Saltarelli 僅<b>會議摘要</b>;Varghese 僅追蹤 2 小時;Leroux 因 COVID 招募不足</li>
 <li>檢索 4 資料庫(未含 Scopus/WoS)— 已以既有 SR 與參考文獻手動補查,無新增</li>
 <li class="warn">4 篇規格混雜研究的<b>分類與排除是本篇結論的前提</b> — 我們在文中透明交代</li>
</ul>""",
"任何研究都要誠實面對限制。第一,證據基礎小而異質,只有六篇隨機試驗加九篇世代研究,族群、結局定義、追蹤長短都不一樣。第二,每個合併分析實際只有二到四篇,少於十篇也就無法正式檢驗發表偏倚。第三,個別研究各有硬傷:Saltarelli 只有會議摘要、Varghese 只追蹤兩小時、Leroux 因為疫情招募不足。第四,檢索涵蓋四個資料庫,沒有包含 Scopus 和 Web of Science,不過我們用既有系統性回顧交叉比對,並手動翻查納入研究的參考文獻,沒有找到漏網之魚。最後,也是最重要的一點:我們把四篇規格混雜的研究排除在合併之外,這個分類判斷本身就是全篇結論的前提,我們在論文裡完整透明地交代了理由,讓讀者可以自行檢驗。"))

# ---- S21 Take-home
S.append(("""
<div class="kicker">Take-Home Messages</div>
<h2 class="slide-title">三句話帶走</h2>
<div class="rule"></div>
<div class="statrow" style="flex-direction:column;gap:30px">
 <div class="stat"><div class="n" style="font-size:44px">1|插入 ≠ 插入之後</div><div class="l" style="font-size:30px">USG 的 insertion 優勢紮實;post-insertion 優勢<b>不存在一致證據</b>(failure RR 1.23, 1.00–1.51)</div></div>
 <div class="stat warn"><div class="n" style="font-size:44px">2|混雜藏在導管裡</div><div class="l" style="font-size:30px">正向研究多有<b>導管長度/規格混雜</b>;post-insertion 表現的主宰者可能是 catheter selection,不是 guidance</div></div>
 <div class="stat"><div class="n" style="font-size:44px">3|深靜脈用長導管</div><div class="l" style="font-size:30px">1–2 cm 深靜脈 + 4.5 cm 標準導管 = 血管內段不足;高壓注射情境尤其小心(extravasation 訊號)</div></div>
</div>
<div class="sub" style="font-size:26px;margin-top:26px">Lee, Wang, Lin, Chen &amp; Chen — <i>The Ultrasound Journal</i> 2026|PROSPERO CRD420261354170|謝謝聆聽,歡迎討論</div>""",
"最後,三句話帶走今天的內容。第一句:插入,不等於插入之後。超音波在插入階段的優勢證據紮實,但在插入之後,目前不存在一致的證據,導管失敗的相對風險一點二三,方向甚至稍微不利。第二句:混雜藏在導管裡。報告超音波較好的研究,多半同時換了更長更好的導管;插入之後的表現,真正的主宰者可能是導管選擇,而不是導引方式。第三句:深靜脈,請配長導管。一到兩公分深的靜脈配四點五公分標準導管,血管內段先天不足,在顯影劑高壓注射的情境尤其要小心外滲。這篇研究發表在 The Ultrasound Journal,PROSPERO 前瞻註冊,歡迎大家找原文來讀。謝謝聆聽,歡迎討論。"))

# write out
narr = {}
for i,(body,n) in enumerate(S, start=1):
    with open(os.path.join(W,"html",f"slide{i:02d}.html"),"w") as f:
        f.write(page(body, i, len(S)))
    narr[f"{i:02d}"] = n
with open(os.path.join(W,"narration.json"),"w") as f:
    json.dump(narr,f,ensure_ascii=False,indent=1)
print("slides:",len(S),"| narration chars:",sum(len(v) for v in narr.values()))
