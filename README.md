# activity_system-social_worker

## 社工活動系統簡介
## 一、	源起:
## 因為製作者目前正在一間養護機構兼職擔任社工，有一天被老闆叫去問話:「為甚麼活動參加人數這麼少?」，並且被要求針對活動人數撰寫查對表，但由於目前工作人員人數稀缺，難以同時注意活動的狀況並鼓勵沒有參與活動的長者參加，加上長者們身體機能受限、居住的活動範圍受限，因此不想強迫長者參加自己不喜歡的活動(至少給予他們選擇活動的自由)，同時認為單看人數作為活動表現的指標過於武斷，應該以不同面向評估活動表現，也發現機構內有霸凌現象，所以為避免少數長者因為參與活動而被欺凌，所以寫了該系統未來讓主管可以從不同面向去看待工作人員對於活動帶領的表現。(雖然資料來源於工作人員描述，但是仍有一定參考價值)
## 二、	目的:
## 透過簡單的視覺化呈現，可以了解長者對於不同活動的參加意願，並且長期追蹤活動過程中是否有負面情緒的狀況產生。

## 三、	系統架構與模組介紹:
<a href="https://ibb.co/kGQZJPR"><img src="https://i.ibb.co/vcZ9hM7/qweqwe.png" alt="qweqwe" border="0"></a>


## 該系統內有三個模組:1.資料輸入模組2.圖表分析模組3.活動期程修改模組。接下來將一一介紹各模組功能:
## 1.	資料輸入模組:為了讓機構內工作人員能夠在紀錄活動內容時可以較為方便，所以撰寫了此模組，此模組可輸入內容為:日期、活動項目、參與人數、備註。此外，除了新增功能，還包含了修改、刪除功能，提供使用者更靈活的資料輸入方式。
## 2.	圖表分析模組:該模組內的圖表皆為互動式圖表，模組內具有三種資料呈現方式:
## (1)	各活動項目累積人數(長條圖)
## 該圖表主要功用為記錄不同活動項目間人數的比較，可以作為往後活動修改的參照，可以留下參與人數較多的活動，替換掉較少人參與的活動。
## (2)	各活動項目參與人數變化(折線圖)
## 這圖表功能較為單純，觀看各活動項目的人數變化，並且呈現備註文字可讓決策者了解活動參與細項，如:活動的氣氛、人數為何有這樣的變化..等等。
## (3)	情緒分析(正向、中立、負向、情緒分數)(折線圖)
## 會出現該圖表是因為本身在機構內有長者有欺凌他人的現象，以及有可能資料輸入的備註過多，而無法詳細呈現在參與人數變化的圖表上(圖表2)，製作者希望能夠讓決策者快速了解機構內的活動的情緒分數，並即時做出因應。本來預計圖表只會呈現情緒分數，但是可能因為資料輸入的文字量過少，而毫無波動，因此新增了正向、負向、中立字詞的總頻次，可以一定程度上在資料輸入過少的情況下，也能夠呈現活動氣氛的變化。(ANTUSD增廣意見詞詞典)
## 3.	活動期程修改模組:該模組主要功能為連接至資料輸入模組，針對活動期程的原始資料，預先填寫在資料輸入模組內，減少同樣的資料，如:
## 日期、活動項目，要一直重複鍵入，同時為因應常設活動內容的修改或是工作人員變動所造成的活動形式變換，提供彈性的修改期程方式。
## 四、	實際呈現:
## 1.資料輸入模組
<a href="https://ibb.co/Hg072Fb"><img src="https://i.ibb.co/GPX7Jx8/qweqweasd.png" alt="qweqweasd" border="0"></a>
<a href="https://ibb.co/VCvsWyN"><img src="https://i.ibb.co/dpQR09c/qweasdasd.png" alt="qweasdasd" border="0"></a>
## 2.圖表分析模組:
<a href="https://ibb.co/v1G9Bkd"><img src="https://i.ibb.co/Mn4dh71/asdzxc.png" alt="asdzxc" border="0"></a>
<a href="https://ibb.co/qnXGL15"><img src="https://i.ibb.co/0X8NpJt/ghjgh.png" alt="ghjgh" border="0"></a>
<a href="https://ibb.co/nfJ3BdD"><img src="https://i.ibb.co/zbv8F9S/fghfgh.png" alt="fghfgh" border="0"></a>
## 3.活動期程修改模組
<a href="https://ibb.co/njNwZ3f"><img src="https://i.ibb.co/YhFNYD8/qwe.png" alt="qwe" border="0"></a>


## 五、	結論與建議:
## 目前系統剛開始運作，所以資料量明顯不足，但在持續有資料紀錄的情況下，未來可以期待該系統能夠讓主管有一個方向可以進行決策，同時避免主管僅以自己短時間的所見去評斷同仁的工作能力、表現。
## 六、	製作該系統所遇到的困難:
## 1.	裝飾器的使用:
## 由於自己並沒有使用過裝飾器的經驗，所以需要花時間稍微熟悉，這樣才能夠應用在使用dash套件的回調。
## 2.	Dash 套件的回調使用:
## 之前雖有使用Dash的經驗，但是在建立資料輸入模組時，卻吃了很大的苦頭，例如:確認按鈕按下後，需要將鍵入的資料進行傳遞、儲存，但是由 於套件語法不熟悉，導致有時按鈕按下後，就一直函式重複回調、或是回調的過程中資料並未儲存，所以花了一些時間熟悉，不過也因此對資料傳遞的過程有了更深入的了解。
## 3.	資料欄位的內容、儲存的路徑名不一致:
## 該系統擁有資料輸入與資料輸出的模組，但因為自己將各模組分開寫，完成後才將所有模組合併至同一頁面，因此常常在資料輸出時，發現跟自己當初在資料輸入所定義的欄位與要輸出的變項名稱不一致，如:輸入的欄位:活動項目;輸出的欄位:活動內容，導致花了很多時間在修正欄位名稱不一致的bug上。未來將先行設計資料表所需欄位，以避免此問題。

