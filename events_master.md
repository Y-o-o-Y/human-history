# 人道事件編年史（1800–2026）定量歷史學完整資料庫

> **規格遵循**：嚴格遵循 `prompt.txt` 規範、Maddison/OWID/UN 歷史人口基準、2026年當代人口等效規模換算（基準 81.5 億）、三級文獻階層與資料存取限制標籤。

**收錄事件總數**：160 筆重要歷史人道事件 (涵蓋 19 世紀至 21 世紀現代衝突，全五大分類與全球六大洲)

## 1. 核心指標對照總表 (Master Chronological Matrix)

| Event ID | 事件名稱 (中/英) | 年份 | 國碼 / 大洲 | 分類 (Taxonomy) | 死亡人數區間 (Low / Mid / High) | 2026年等效規模 | 區域衝擊率 | 共識程度 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EVT-1804-HTI-001` | 海地建國白人大屠殺<br>*1804 Haiti Massacre of the French Population* | 1804 | `HTI`<br>Americas | `Direct Physical Massacre / Genocide` | 3,000 / 4,000 / 5,000 | **32,963** | 1.0% | `High Consensus` |
| `EVT-1815-ZAF-001` | 祖魯王國擴張與「苦難動盪」浩劫<br>*Mfecane / Difaqane (Zulu Expansion and Devastation)* | 1815–1840 | `ZAF`<br>Africa | `Direct Physical Massacre / Genocide` | 500,000 / 1,000,000 / 2,000,000 | **7,996,076** | 40.0% | `Debated` |
| `EVT-1820-RUS-007` | 沙俄高加索戰爭早期卡巴爾達與達吉斯坦村落焦土清剿<br>*Yermolov's Scorched Earth Operations in the North Caucasus* | 1817–1827 | `RUS`<br>Europe | `War-Time Civilian Atrocities` | 40,000 / 60,000 / 100,000 | **477,190** | 10.0% | `High Consensus` |
| `EVT-1822-GRC-002` | 希臘獨立戰爭希俄斯島大屠殺<br>*Chios Massacre (Greek War of Independence)* | 1822 | `GRC`<br>Europe | `Direct Physical Massacre / Genocide` | 42,000 / 45,000 / 52,000 | **353,154** | 37.5% | `High Consensus` |
| `EVT-1824-AUS-001` | 澳洲黑色戰爭與原住民清剿<br>*Black War and Tasmanian Aboriginal Genocide* | 1824–1831 | `AUS`<br>Oceania | `Direct Physical Massacre / Genocide` | 900 / 1,200 / 2,000 | **9,368** | 24.0% | `High Consensus` |
| `EVT-1830-USA-001` | 北美原住民「血淚之路」強迫遷徙<br>*Trail of Tears (Indian Removal)* | 1830–1850 | `USA`<br>Americas | `Democide, Purges & Forced Labor` | 12,000 / 16,000 / 25,000 | **114,386** | 16.0% | `High Consensus` |
| `EVT-1835-NZL-001` | 查塔姆群島莫里奧里人滅絕屠殺與奴役<br>*Moriori Genocide on the Chatham Islands* | 1835–1863 | `NZL`<br>Oceania | `Direct Physical Massacre / Genocide` | 300 / 500 / 1,000 | **3,483** | 25.0% | `High Consensus` |
| `EVT-1845-IRL-001` | 愛爾蘭大饑荒<br>*Great Famine of Ireland* | 1845–1852 | `IRL`<br>Europe | `Man-made & Policy Famine` | 1,000,000 / 1,100,000 / 1,500,000 | **7,288,618** | 13.4146% | `High Consensus` |
| `EVT-1846-USA-002` | 加利福尼亞印第安原住民種族滅絕<br>*California Genocide (Act for the Government and Protection of Indians)* | 1846–1873 | `USA`<br>Americas | `Direct Physical Massacre / Genocide` | 10,000 / 16,000 / 30,000 | **105,445** | 10.6667% | `High Consensus` |
| `EVT-1847-MEX-001` | 墨西哥猶加敦階級戰爭（瑪雅起義焦土與奴役）<br>*Caste War of Yucatán (Guerra de Castas)* | 1847–1901 | `MEX`<br>Americas | `War-Time Civilian Atrocities` | 200,000 / 250,000 / 300,000 | **1,638,740** | 41.6667% | `High Consensus` |
| `EVT-1851-CHN-001` | 太平天國戰爭平民屠殺與圍城焦土<br>*Taiping Rebellion Civilian Slaughter and Sieges* | 1851–1864 | `CHN`<br>Asia | `War-Time Civilian Atrocities` | 15,000,000 / 20,000,000 / 30,000,000 | **128,346,457** | 4.878% | `Debated` |
| `EVT-1856-CHN-009` | 雲南杜文秀起義清軍鎮壓與滇西回民屠殺<br>*Panthay Rebellion Suppression and Yunnan Muslim Massacres* | 1856–1873 | `CHN`<br>Asia | `Direct Physical Massacre / Genocide` | 1,000,000 / 1,500,000 / 2,500,000 | **9,454,194** | 20.0% | `Debated` |
| `EVT-1860-NZL-002` | 紐西蘭土地戰爭毛利平民清剿與大沒收慘劇<br>*New Zealand Wars and Raupatu (Confiscation of Māori Lands)* | 1860–1872 | `NZL`<br>Oceania | `War-Time Civilian Atrocities` | 2,000 / 3,000 / 4,000 | **18,642** | 5.0% | `High Consensus` |
| `EVT-1861-CHL-002` | 智利軍事佔領阿勞卡尼亞與馬普切人暴力清洗<br>*Occupation of the Araucanía (Pacificación de la Araucanía)* | 1861–1883 | `CHL`<br>Americas | `Direct Physical Massacre / Genocide` | 10,000 / 18,000 / 30,000 | **111,461** | 12.0% | `High Consensus` |
| `EVT-1862-CHN-010` | 同治陝甘回亂族群仇殺與清軍左宗棠收復清剿<br>*Dungan Revolt Mutual Atrocities and Tso Tsung-t'ang's Cleansing* | 1862–1877 | `CHN`<br>Asia | `War-Time Civilian Atrocities` | 5,000,000 / 8,000,000 / 12,000,000 | **49,365,172** | 40.0% | `Debated` |
| `EVT-1864-PRY-001` | 三國同盟戰爭巴拉圭平民大滅絕<br>*War of the Triple Alliance – Paraguayan Population Annihilation* | 1864–1870 | `PRY`<br>Americas | `War-Time Civilian Atrocities` | 300,000 / 400,000 / 500,000 | **2,451,128** | 76.1905% | `High Consensus` |
| `EVT-1864-RUS-001` | 切爾克斯人種族滅絕與強制驅逐<br>*Circassian Genocide and Expulsion* | 1864–1867 | `RUS`<br>Europe | `Direct Physical Massacre / Genocide` | 600,000 / 800,000 / 1,500,000 | **4,902,256** | 53.3333% | `High Consensus` |
| `EVT-1864-USA-003` | 科羅拉多沙溪大屠殺<br>*Sand Creek Massacre* | 1864 | `USA`<br>Americas | `Direct Physical Massacre / Genocide` | 150 / 200 / 230 | **1,226** | 25.0% | `High Consensus` |
| `EVT-1866-AUT-001` | 奧匈帝國加利西亞貧困大饑荒<br>*Galician Poverty and Famines in Austria-Hungary* | 1866–1890 | `POL`<br>Europe | `Man-made & Policy Famine` | 500,000 / 700,000 / 1,000,000 | **4,246,898** | 11.6667% | `High Consensus` |
| `EVT-1871-FRA-001` | 巴黎公社「流血週」平民大屠殺與白色恐怖<br>*Paris Commune 'Bloody Week' (Semaine Sanglante)* | 1871 | `FRA`<br>Europe | `Democide, Purges & Forced Labor` | 10,000 / 15,000 / 20,000 | **88,801** | 0.8333% | `High Consensus` |
| `EVT-1875-TUR-003` | 鄂圖曼帝國巴爾幹危機波士尼亞與保加利亞四月起義大屠殺<br>*April Uprising Batak Massacres and Bulgarian Horrors* | 1876 | `BGR`<br>Europe | `War-Time Civilian Atrocities` | 15,000 / 20,000 / 30,000 | **115,603** | 0.8% | `High Consensus` |
| `EVT-1876-CHN-005` | 丁戊奇荒（華北大饑荒與賑災失序）<br>*Northern Chinese Famine of 1876–1879* | 1876–1879 | `CHN`<br>Asia | `Man-made & Policy Famine` | 9,500,000 / 10,000,000 / 13,000,000 | **57,801,418** | 9.2593% | `High Consensus` |
| `EVT-1876-IND-001` | 1876-1878年印度大饑荒（英印殖民政策飢荒）<br>*Great Famine of 1876–1878 (British India)* | 1876–1878 | `IND`<br>Asia | `Man-made & Policy Famine` | 5,500,000 / 7,000,000 / 10,300,000 | **40,460,993** | 3.6842% | `High Consensus` |
| `EVT-1878-ARG-002` | 阿根廷「征服沙漠」原住民清剿與強迫同化<br>*Conquest of the Desert (Conquista del Desierto)* | 1878–1885 | `ARG`<br>Americas | `Direct Physical Massacre / Genocide` | 1,500 / 2,500 / 5,000 | **14,248** | 8.3333% | `High Consensus` |
| `EVT-1880-CAN-001` | 加拿大原住民寄宿學校制度與強迫同化<br>*Canadian Indian Residential School System* | 1880–1996 | `CAN`<br>Americas | `Coercive Population Control` | 4,100 / 6,000 / 15,000 | **33,724** | 4.0% | `High Consensus` |
| `EVT-1883-VNM-002` | 法屬印度支那「勤王運動」法軍殘酷平定與焦土清鄉<br>*French Pacification of Tonkin and Can Vuong Movement Suppression* | 1885–1896 | `VNM`<br>Asia | `War-Time Civilian Atrocities` | 50,000 / 75,000 / 120,000 | **407,500** | 0.75% | `High Consensus` |
| `EVT-1885-COD-001` | 剛果自由邦暴行與橡膠強迫勞動<br>*Congo Free State Atrocities and Forced Labor* | 1885–1908 | `COD`<br>Africa | `Democide, Purges & Forced Labor` | 3,000,000 / 5,000,000 / 10,000,000 | **27,166,667** | 25.0% | `Debated` |
| `EVT-1888-ETH-004` | 衣索比亞牛瘟大饑荒（災難七年 / 基夫肯）<br>*Great Ethiopian Famine of 1888–1892 (Kifu Qen)* | 1888–1892 | `ETH`<br>Africa | `Man-made & Policy Famine` | 1,500,000 / 2,500,000 / 3,500,000 | **13,316,993** | 31.25% | `High Consensus` |
| `EVT-1890-AGO-001` | 葡屬安哥拉殖民平定戰役與強迫橡膠橡膠奴役慘劇<br>*Portuguese Pacification Campaigns in Angola and Bailundo Revolt* | 1890–1915 | `AGO`<br>Africa | `Democide, Purges & Forced Labor` | 100,000 / 150,000 / 250,000 | **788,710** | 3.75% | `High Consensus` |
| `EVT-1890-USA-004` | 傷膝河大屠殺<br>*Wounded Knee Massacre* | 1890 | `USA`<br>Americas | `Direct Physical Massacre / Genocide` | 250 / 300 / 350 | **1,577** | 75.0% | `High Consensus` |
| `EVT-1894-TUR-004` | 鄂圖曼哈米德大屠殺<br>*Hamidian Massacres of Armenians and Assyrians* | 1894–1896 | `TUR`<br>Asia | `Direct Physical Massacre / Genocide` | 100,000 / 200,000 / 300,000 | **1,025,157** | 8.0% | `High Consensus` |
| `EVT-1899-IND-003` | 1899-1900年印度大饑荒（柯松總督時期）<br>*Indian Famine of 1899–1900 (Curzon Famine)* | 1899–1900 | `IND`<br>Asia | `Man-made & Policy Famine` | 1,000,000 / 2,000,000 / 4,500,000 | **9,939,024** | 0.8% | `Debated` |
| `EVT-1899-PHL-001` | 美菲戰爭平民集中營與薩馬島焦土鎮壓<br>*Philippine-American War – Concentration Camps and Civilian Atrocities* | 1899–1902 | `PHL`<br>Asia | `War-Time Civilian Atrocities` | 200,000 / 250,000 / 600,000 | **1,242,378** | 3.5714% | `Debated` |
| `EVT-1899-ZAF-002` | 第二次波耳戰爭英國平民集中營<br>*Second Boer War British Concentration Camps* | 1899–1902 | `ZAF`<br>Africa | `War-Time Civilian Atrocities` | 42,000 / 46,000 / 48,000 | **228,598** | 15.3333% | `High Consensus` |
| `EVT-1900-PER-001` | 秘魯亞馬遜普圖馬約橡膠採集暴行<br>*Peruvian Amazon Company Putumayo Atrocities* | 1900–1912 | `PER`<br>Americas | `Democide, Purges & Forced Labor` | 30,000 / 40,000 / 50,000 | **197,576** | 80.0% | `High Consensus` |
| `EVT-1903-MDA-001` | 沙皇俄國晚期與內戰基希涅夫等反猶大屠殺<br>*Russian Empire Kishinev and Civil War Anti-Jewish Pogroms* | 1903–1921 | `MDA`<br>Europe | `Direct Physical Massacre / Genocide` | 70,000 / 120,000 / 250,000 | **579,556** | 2.4% | `High Consensus` |
| `EVT-1904-NAM-001` | 納米比亞赫雷羅與納馬人大屠殺<br>*Herero and Namaqua Genocide* | 1904–1908 | `NAM`<br>Africa | `Direct Physical Massacre / Genocide` | 45,000 / 75,000 / 100,000 | **359,559** | 75.0% | `High Consensus` |
| `EVT-1905-TZA-001` | 德屬東非馬基馬基起義焦土鎮壓與人為飢饉<br>*Maji Maji Rebellion – German Colonial Scorched Earth Famine* | 1905–1907 | `TZA`<br>Africa | `War-Time Civilian Atrocities` | 200,000 / 250,000 / 300,000 | **1,192,154** | 6.25% | `High Consensus` |
| `EVT-1909-TUR-005` | 鄂圖曼阿達納大屠殺<br>*Adana Massacre of Armenians (1909)* | 1909 | `TUR`<br>Asia | `Direct Physical Massacre / Genocide` | 20,000 / 25,000 / 30,000 | **116,732** | 5.0% | `High Consensus` |
| `EVT-1913-TUR-002` | 希臘人與亞述人種族滅絕<br>*Greek and Assyrian Genocide (Pontic Greeks, Assyrians)* | 1913–1923 | `TUR`<br>Asia | `Direct Physical Massacre / Genocide` | 500,000 / 700,000 / 900,000 | **3,201,786** | 35.0% | `High Consensus` |
| `EVT-1915-LBN-001` | 黎巴嫩山一戰大饑荒<br>*Mount Lebanon Famine (1915–1918)* | 1915–1918 | `LBN`<br>Asia | `Man-made & Policy Famine` | 100,000 / 180,000 / 200,000 | **815,000** | 43.4783% | `High Consensus` |
| `EVT-1915-TUR-001` | 亞美尼亞種族滅絕<br>*Armenian Genocide* | 1915–1917 | `TUR`<br>Asia | `Direct Physical Massacre / Genocide` | 800,000 / 1,200,000 / 1,500,000 | **5,433,333** | 60.0% | `High Consensus` |
| `EVT-1916-KGZ-001` | 沙俄中亞大起義鎮壓與柯爾克孜族大逃亡（烏爾昆浩劫）<br>*Central Asian Revolt of 1916 and Urkun Catastrophe* | 1916–1917 | `KGZ`<br>Asia | `War-Time Civilian Atrocities` | 100,000 / 150,000 / 270,000 | **672,442** | 12.5% | `High Consensus` |
| `EVT-1918-AZE-002` | 巴庫「三月事件」與「九月事件」雙向族群大屠殺<br>*March Days and September Days Massacres in Baku* | 1918 | `AZE`<br>Asia | `Direct Physical Massacre / Genocide` | 20,000 / 25,000 / 35,000 | **109,898** | 10.0% | `High Consensus` |
| `EVT-1918-FIN-001` | 芬蘭內戰白色恐怖與集中營死難<br>*Finnish Civil War White Terror and Prison Camps* | 1918 | `FIN`<br>Europe | `Democide, Purges & Forced Labor` | 20,000 / 25,000 / 30,000 | **109,898** | 0.8065% | `High Consensus` |
| `EVT-1919-RUS-002` | 蘇維埃俄國「去哥薩克化」肉體消滅運動<br>*Decossackization (Raskazachivaniye)* | 1919–1920 | `RUS`<br>Europe | `Democide, Purges & Forced Labor` | 300,000 / 500,000 / 1,000,000 | **2,176,816** | 16.6667% | `High Consensus` |
| `EVT-1920-RUS-003` | 坦波夫農民起義蘇俄軍隊毒氣鎮壓與人質營慘劇<br>*Tambov Rebellion Chemical Weapons Suppression and Hostage Camps* | 1920–1921 | `RUS`<br>Europe | `War-Time Civilian Atrocities` | 150,000 / 180,000 / 240,000 | **776,190** | 6.0% | `High Consensus` |
| `EVT-1921-RUS-004` | 蘇俄伏爾加河大饑荒<br>*Povolzhye Famine (Russian Famine of 1921–1922)* | 1921–1922 | `RUS`<br>Europe | `Man-made & Policy Famine` | 4,000,000 / 5,000,000 / 6,000,000 | **21,357,442** | 16.6667% | `High Consensus` |
| `EVT-1928-LBY-001` | 義大利法西斯平定利比亞與昔蘭尼加集中營<br>*Italian Pacification of Libya and Cyrenaica Concentration Camps* | 1928–1932 | `LBY`<br>Africa | `Democide, Purges & Forced Labor` | 60,000 / 80,000 / 100,000 | **320,551** | 35.5556% | `High Consensus` |
| `EVT-1930-KAZ-001` | 哈薩克大饑荒 (阿夏爾希里克)<br>*Kazakh Famine (Asharshylyq)* | 1930–1933 | `KAZ`<br>Asia | `Man-made & Policy Famine` | 1,300,000 / 1,500,000 / 1,750,000 | **5,905,797** | 37.5% | `High Consensus` |
| `EVT-1930-SUN-002` | 蘇聯消滅富農運動與強制流放特別定居點慘劇<br>*Soviet Dekulakization and Special Settlements Democide* | 1930–1933 | `RUS`<br>Europe | `Democide, Purges & Forced Labor` | 530,000 / 700,000 / 1,200,000 | **2,756,039** | 0.4667% | `High Consensus` |
| `EVT-1932-SLV-001` | 薩爾瓦多農民大屠殺（La Matanza）<br>*La Matanza (The 1932 Salvadoran Peasant Massacre)* | 1932 | `SLV`<br>Americas | `Democide, Purges & Forced Labor` | 10,000 / 20,000 / 30,000 | **77,619** | 1.3333% | `High Consensus` |
| `EVT-1932-UKR-001` | 蘇聯烏克蘭大饑荒 (霍洛多莫)<br>*Holodomor (Soviet Famine in Ukraine)* | 1932–1933 | `UKR`<br>Europe | `Man-made & Policy Famine` | 3,500,000 / 3,900,000 / 5,000,000 | **15,135,714** | 12.1875% | `High Consensus` |
| `EVT-1935-ETH-003` | 第二次義衣戰爭法西斯芥子毒氣戰與平民大屠殺<br>*Second Italo-Ethiopian War Mustard Gas Attacks and Yekatit 12* | 1935–1937 | `ETH`<br>Africa | `War-Time Civilian Atrocities` | 250,000 / 350,000 / 500,000 | **1,320,602** | 3.5% | `High Consensus` |
| `EVT-1936-ESP-001` | 西班牙佛朗哥白色恐怖與內戰政治清洗<br>*Spanish Civil War and Francoist White Terror Executions* | 1936–1950 | `ESP`<br>Europe | `Democide, Purges & Forced Labor` | 100,000 / 150,000 / 200,000 | **560,780** | 0.6% | `High Consensus` |
| `EVT-1937-CHN-001` | 南京大屠殺<br>*Nanjing Massacre* | 1937–1938 | `CHN`<br>Asia | `War-Time Civilian Atrocities` | 200,000 / 250,000 / 300,000 | **926,136** | 25.0% | `High Consensus` |
| `EVT-1937-DOM-001` | 多明尼加「香菜大屠殺」（海地移民種族清洗）<br>*Parsley Massacre (Haitian Massacre in Dominican Republic)* | 1937 | `DOM`<br>Americas | `Direct Physical Massacre / Genocide` | 10,000 / 17,000 / 30,000 | **62,977** | 28.3333% | `High Consensus` |
| `EVT-1937-JPN-001` | 日軍731部隊人體實驗與細菌戰<br>*Unit 731 Human Experimentation and Biological Warfare* | 1937–1945 | `CHN`<br>Asia | `War-Time Civilian Atrocities` | 200,000 / 300,000 / 400,000 | **1,111,364** | 0.6% | `High Consensus` |
| `EVT-1937-RUS-005` | 蘇聯大清洗「波蘭行動」民族大清洗<br>*Polish Operation of the NKVD (Order No. 00485)* | 1937–1938 | `RUS`<br>Europe | `Direct Physical Massacre / Genocide` | 111,091 / 120,000 / 140,000 | **444,545** | 10.0% | `High Consensus` |
| `EVT-1937-SUN-001` | 蘇聯大清洗與古拉格死亡勞役<br>*Great Purge and Gulag Fatalities* | 1937–1938 | `RUS`<br>Europe | `Democide, Purges & Forced Labor` | 950,000 / 1,200,000 / 1,600,000 | **4,445,455** | 0.7407% | `High Consensus` |
| `EVT-1937-SUN-003` | 蘇聯大清洗朝鮮族遠東強制大流放<br>*Deportation of Koreans in the Soviet Union* | 1937–1938 | `RUS`<br>Asia | `Direct Physical Massacre / Genocide` | 16,500 / 25,000 / 40,000 | **92,614** | 14.2857% | `High Consensus` |
| `EVT-1938-CHN-011` | 重慶大轟炸（日軍對平民無差別戰略轟炸）<br>*Bombing of Chongqing (Imperial Japanese Strategic Civilian Bombing)* | 1938–1943 | `CHN`<br>Asia | `War-Time Civilian Atrocities` | 24,000 / 27,000 / 32,000 | **99,122** | 2.7% | `High Consensus` |
| `EVT-1939-DEU-003` | 納粹「T4行動」強制安樂死與殘疾人滅絕計畫<br>*Nazi Aktion T4 Euthanasia Programme* | 1939–1941 | `DEU`<br>Europe | `Coercive Population Control` | 200,000 / 250,000 / 300,000 | **909,598** | 0.3125% | `High Consensus` |
| `EVT-1939-DEU-004` | 納粹羅姆人與辛提人種族滅絕（食人魔 / 吞噬）<br>*Porajmos (Romani Genocide by Nazi Germany)* | 1939–1945 | `DEU`<br>Europe | `Direct Physical Massacre / Genocide` | 220,000 / 300,000 / 500,000 | **1,091,518** | 30.0% | `High Consensus` |
| `EVT-1939-FIN-002` | 蘇芬冬季戰爭蘇聯空軍平民無差別轟炸與集束炸彈襲擊<br>*Soviet Bombing of Helsinki and Finnish Cities during the Winter War* | 1939–1940 | `FIN`<br>Europe | `War-Time Civilian Atrocities` | 1,000 / 1,500 / 2,500 | **5,458** | 0.0405% | `High Consensus` |
| `EVT-1940-POL-001` | 卡廷大屠殺（蘇聯秘密處決波蘭精英）<br>*Katyn Massacre – Soviet NKVD Execution of Polish Officers* | 1940 | `POL`<br>Europe | `Democide, Purges & Forced Labor` | 21,768 / 21,857 / 22,000 | **78,821** | 10.9285% | `High Consensus` |
| `EVT-1941-DEU-001` | 納粹猶太人大屠殺 (浩劫 / 猶太大滅絕)<br>*The Holocaust (Shoah)* | 1941–1945 | `DEU`<br>Europe | `Direct Physical Massacre / Genocide` | 5,700,000 / 5,900,000 / 6,100,000 | **21,089,912** | 62.1053% | `High Consensus` |
| `EVT-1941-DEU-002` | 納粹飢餓計畫與蘇聯戰俘/平民大滅絕<br>*Nazi Hunger Plan and Extermination of Soviet Civilians* | 1941–1944 | `BLR`<br>Europe | `Man-made & Policy Famine` | 4,200,000 / 5,000,000 / 7,000,000 | **17,872,807** | 6.6667% | `High Consensus` |
| `EVT-1941-HRV-001` | 克羅埃西亞烏斯塔沙法西斯政權種族滅絕與亞塞諾瓦茨滅絕營<br>*Ustaše Genocide against Serbs, Jews and Roma (Jasenovac Camp)* | 1941–1945 | `HRV`<br>Europe | `Direct Physical Massacre / Genocide` | 300,000 / 400,000 / 600,000 | **1,429,825** | 6.1538% | `High Consensus` |
| `EVT-1941-ROU-002` | 羅馬尼亞安東內斯庫政權敖德薩大屠殺與德涅斯特河沿岸浩劫<br>*Odessa Massacre and Transnistria Holocaust by Romania* | 1941–1944 | `ROU`<br>Europe | `Direct Physical Massacre / Genocide` | 280,000 / 300,000 / 380,000 | **1,072,368** | 75.0% | `High Consensus` |
| `EVT-1942-CHN-006` | 1942年河南大饑荒與苛稅徵糧<br>*Henan Famine of 1942–1943* | 1942–1943 | `CHN`<br>Asia | `Man-made & Policy Famine` | 1,500,000 / 2,000,000 / 3,000,000 | **7,086,957** | 6.6667% | `High Consensus` |
| `EVT-1941-POL-002` | 沃倫與東加利西亞波蘭人大屠殺<br>*Massacres of Poles in Volhynia and Eastern Galicia* | 1943–1945 | `UKR`<br>Europe | `Direct Physical Massacre / Genocide` | 60,000 / 100,000 / 120,000 | **351,293** | 6.6667% | `High Consensus` |
| `EVT-1943-DEU-005` | 盟軍對德國城市漢堡與德勒斯登平民區地毯式燃燒彈轟炸<br>*Allied Firebombing of Hamburg and Dresden (Firestorms)* | 1943–1945 | `DEU`<br>Europe | `War-Time Civilian Atrocities` | 60,000 / 75,000 / 100,000 | **263,470** | 3.75% | `High Consensus` |
| `EVT-1943-IND-001` | 1943年孟加拉大饑荒<br>*Bengal Famine of 1943* | 1943–1944 | `IND`<br>Asia | `Man-made & Policy Famine` | 2,100,000 / 3,000,000 / 3,800,000 | **10,538,793** | 4.9751% | `High Consensus` |
| `EVT-1944-POL-003` | 華沙起義納粹鎮壓與沃拉大屠殺<br>*Warsaw Uprising German Democide and Wola Massacre* | 1944 | `POL`<br>Europe | `War-Time Civilian Atrocities` | 150,000 / 180,000 / 200,000 | **623,592** | 18.0% | `High Consensus` |
| `EVT-1944-RUS-006` | 蘇聯強迫流放車臣人與印古什人（扁豆行動）<br>*Deportation of Chechens and Ingush (Operation Lentil / Aardakh)* | 1944 | `RUS`<br>Europe | `Direct Physical Massacre / Genocide` | 125,000 / 150,000 / 200,000 | **519,660** | 30.0% | `High Consensus` |
| `EVT-1944-UKR-002` | 蘇聯克里米亞韃靼人強制大流放（流亡慘劇）<br>*Deportation of Crimean Tatars (Sürgünlik)* | 1944 | `UKR`<br>Europe | `Direct Physical Massacre / Genocide` | 34,000 / 45,000 / 110,000 | **155,898** | 22.5% | `High Consensus` |
| `EVT-1944-VNM-001` | 日治越南大饑荒<br>*Vietnamese Famine of 1944–1945 (Japanese Occupation Famine)* | 1944–1945 | `VNM`<br>Asia | `Man-made & Policy Famine` | 400,000 / 1,000,000 / 2,000,000 | **3,464,400** | 10.0% | `High Consensus` |
| `EVT-1945-DEU-003` | 二戰後德裔平民大驅逐與報復性屠殺<br>*Expulsion of Germans after WWII and Associated Massacres* | 1945–1950 | `DEU`<br>Europe | `Direct Physical Massacre / Genocide` | 500,000 / 600,000 / 2,000,000 | **2,050,314** | 4.2857% | `Debated` |
| `EVT-1945-DZA-002` | 法國塞提夫與蓋勒馬平民大屠殺<br>*Sétif and Guelma Massacre (Algeria)* | 1945 | `DZA`<br>Africa | `War-Time Civilian Atrocities` | 6,000 / 20,000 / 45,000 | **68,344** | 2.0% | `Debated` |
| `EVT-1945-GRC-001` | 希臘內戰「白色恐怖」清洗與馬克羅尼索斯島集中營<br>*Greek Civil War White Terror and Makronisos Camp Internees* | 1945–1949 | `GRC`<br>Europe | `Democide, Purges & Forced Labor` | 40,000 / 50,000 / 80,000 | **170,860** | 0.6849% | `High Consensus` |
| `EVT-1945-JPN-002` | 廣島與長崎原子彈平民核爆慘劇<br>*Atomic Bombings of Hiroshima and Nagasaki* | 1945 | `JPN`<br>Asia | `War-Time Civilian Atrocities` | 129,000 / 170,000 / 226,000 | **580,922** | 28.3333% | `High Consensus` |
| `EVT-1945-PHL-002` | 馬尼拉大屠殺<br>*Manila Massacre by Imperial Japanese Forces* | 1945 | `PHL`<br>Asia | `War-Time Civilian Atrocities` | 100,000 / 100,000 / 120,000 | **341,719** | 10.0% | `High Consensus` |
| `EVT-1945-YUG-001` | 二戰後南斯拉夫布萊堡遣返屠殺與死亡行軍<br>*Bleiburg Repatriations and Post-WWII Yugoslav Death Marches* | 1945 | `YUG`<br>Europe | `Democide, Purges & Forced Labor` | 70,000 / 80,000 / 100,000 | **273,375** | 0.5333% | `Debated` |
| `EVT-1947-IND-002` | 印巴分治流血宗族大屠殺<br>*Partition of India Communal Massacres* | 1947–1948 | `IND`<br>Asia | `Direct Physical Massacre / Genocide` | 500,000 / 1,000,000 / 2,000,000 | **3,326,531** | 3.3333% | `Debated` |
| `EVT-1947-MDG-001` | 馬達加斯加起義法軍鎮壓與平民浩劫<br>*Malagasy Uprising and French Brutal Suppression* | 1947–1949 | `MDG`<br>Africa | `War-Time Civilian Atrocities` | 30,000 / 60,000 / 100,000 | **199,592** | 1.4286% | `High Consensus` |
| `EVT-1947-TWN-001` | 台灣二二八事件與白色恐怖威權清洗<br>*Taiwan 228 Incident and the White Terror* | 1947–1987 | `TWN`<br>Asia | `Democide, Purges & Forced Labor` | 18,000 / 22,000 / 32,000 | **73,184** | 0.3385% | `High Consensus` |
| `EVT-1947-IND-005` | 海得拉巴土邦併入印度「波羅行動」平民屠殺<br>*Operation Polo and Hyderabad Post-Annexation Massacres* | 1948 | `IND`<br>Asia | `War-Time Civilian Atrocities` | 27,000 / 35,000 / 40,000 | **114,367** | 0.2188% | `High Consensus` |
| `EVT-1948-COL-001` | 哥倫比亞「暴力時期」黨派屠殺與焦土清洗<br>*La Violencia in Colombia* | 1948–1958 | `COL`<br>Americas | `War-Time Civilian Atrocities` | 180,000 / 200,000 / 300,000 | **653,525** | 1.7391% | `High Consensus` |
| `EVT-1948-JPN-001` | 日本《優生保護法》強制絕育<br>*Japan Eugenic Protection Law Forced Sterilizations* | 1948–1996 | `JPN`<br>Asia | `Coercive Population Control` | 100 / 500 / 1,000 | **1,634** | 0.0006% | `High Consensus` |
| `EVT-1948-KOR-002` | 韓國濟州四三事件平民焦土清剿<br>*Jeju April 3 Incident and Civilian Massacres* | 1948–1954 | `KOR`<br>Asia | `Democide, Purges & Forced Labor` | 14,000 / 20,000 / 30,000 | **65,352** | 6.6667% | `High Consensus` |
| `EVT-1950-CHN-008` | 中國土地改革運動暴力鬥爭與鎮壓反革命運動<br>*Chinese Violent Land Reform Movement and Campaign to Suppress Counterrevolutionaries* | 1950–1953 | `CHN`<br>Asia | `Democide, Purges & Forced Labor` | 1,500,000 / 2,500,000 / 4,000,000 | **7,889,642** | 0.4545% | `Debated` |
| `EVT-1950-KOR-001` | 韓國保導聯盟大屠殺<br>*Bodo League Massacre (South Korea)* | 1950 | `KOR`<br>Asia | `Democide, Purges & Forced Labor` | 60,000 / 100,000 / 200,000 | **315,586** | 0.5% | `High Consensus` |
| `EVT-1952-KEN-001` | 肯亞茅茅起義英國酷刑集中營<br>*Kenya Mau Mau Uprising – British Detention Camps and Torture* | 1952–1960 | `KEN`<br>Africa | `Democide, Purges & Forced Labor` | 12,000 / 25,000 / 50,000 | **76,287** | 0.4167% | `High Consensus` |
| `EVT-1954-DZA-001` | 阿爾及利亞獨立戰爭法軍集中營與平民屠殺<br>*Algerian War – French Regroupement Camps and Civilian Massacres* | 1954–1962 | `DZA`<br>Africa | `War-Time Civilian Atrocities` | 300,000 / 500,000 / 1,000,000 | **1,476,895** | 5.5556% | `Debated` |
| `EVT-1955-CMR-001` | 喀麥隆獨立前夕法軍巴米累克高原焦土大清洗<br>*Cameroonian UPC Rebellion and French Scorched Earth Pacification* | 1955–1962 | `CMR`<br>Africa | `War-Time Civilian Atrocities` | 30,000 / 60,000 / 120,000 | **174,435** | 1.875% | `High Consensus` |
| `EVT-1955-SDN-003` | 第一次蘇丹內戰南部焦土平民浩劫<br>*First Sudanese Civil War and Torit Mutiny Civilian Atrocities* | 1955–1972 | `SSD`<br>Africa | `War-Time Civilian Atrocities` | 500,000 / 750,000 / 1,000,000 | **2,180,440** | 18.75% | `High Consensus` |
| `EVT-1959-CHN-002` | 中國大躍進與三年大饑荒<br>*Great Chinese Famine (Great Leap Forward)* | 1959–1961 | `CHN`<br>Asia | `Man-made & Policy Famine` | 15,000,000 / 30,000,000 / 45,000,000 | **82,046,980** | 4.5455% | `High Consensus` |
| `EVT-1960-ZAF-003` | 南非種族隔離制度沙佩維爾屠殺、索韋托起義與國家安全暗殺<br>*South African Apartheid State Murders and Massacres (Sharpeville to Soweto)* | 1960–1989 | `ZAF`<br>Africa | `Democide, Purges & Forced Labor` | 7,000 / 12,000 / 25,000 | **32,189** | 0.048% | `High Consensus` |
| `EVT-1960-IRQ-002` | 伊拉克庫德武裝起義阿拉伯化清鄉與焦土平民屠殺<br>*Iraqi Operations against Kurds and Early Arabization Campaigns* | 1961–1975 | `IRQ`<br>Asia | `War-Time Civilian Atrocities` | 60,000 / 80,000 / 110,000 | **210,549** | 3.2% | `High Consensus` |
| `EVT-1962-IDN-002` | 印尼兼併西巴布亞軍事鎮壓與原住民大清洗<br>*Indonesian Annexation of West Papua and Democide (Operation Trikora)* | 1962–1969 | `IDN`<br>Asia | `Democide, Purges & Forced Labor` | 50,000 / 100,000 / 150,000 | **258,320** | 12.5% | `High Consensus` |
| `EVT-1963-RWA-002` | 盧安達「吉康戈羅」圖西族大屠殺與流亡浩劫<br>*Gikongoro Massacres of Tutsis in Rwanda (1963)* | 1963–1964 | `RWA`<br>Africa | `Direct Physical Massacre / Genocide` | 10,000 / 15,000 / 25,000 | **38,045** | 0.5% | `High Consensus` |
| `EVT-1964-BRA-001` | 巴西軍政府威權鎮壓與亞馬遜原住民種族滅絕<br>*Brazilian Military Dictatorship and Indigenous Democide* | 1964–1985 | `BRA`<br>Americas | `Democide, Purges & Forced Labor` | 8,500 / 10,000 / 20,000 | **24,911** | 0.01% | `High Consensus` |
| `EVT-1965-IDN-001` | 印尼反共清共大屠殺<br>*Indonesian Mass Killings of 1965–1966* | 1965–1966 | `IDN`<br>Asia | `Democide, Purges & Forced Labor` | 500,000 / 750,000 / 1,200,000 | **1,835,586** | 0.7143% | `High Consensus` |
| `EVT-1966-CAF-002` | 中非帝國博卡薩獨裁政權殘暴虐殺與學生大屠殺<br>*Jean-Bédel Bokassa Regime Atrocities and Schoolchildren Massacre* | 1966–1979 | `CAF`<br>Africa | `Democide, Purges & Forced Labor` | 2,000 / 4,000 / 10,000 | **9,617** | 0.1818% | `High Consensus` |
| `EVT-1966-CHN-007` | 文化大革命政治清洗與地方大屠殺<br>*Cultural Revolution Purges, Massacres and Armed Clashes* | 1966–1976 | `CHN`<br>Asia | `Democide, Purges & Forced Labor` | 750,000 / 1,750,000 / 3,000,000 | **4,207,227** | 0.2349% | `State Suppressed` |
| `EVT-1966-GRL-001` | 格陵蘭因紐特婦女子宮節育環（螺旋環）強制置入事件<br>*Greenland Inuk Women Coil Campaign (Spiralkampagnen)* | 1966–1974 | `GRL`<br>Americas | `Coercive Population Control` | 50 / 120 / 300 | **288** | 0.3% | `High Consensus` |
| `EVT-1966-ROU-001` | 羅馬尼亞齊奧塞斯庫強制生育法令770與孤兒院人道慘劇<br>*Romanian Decree 770 Coercive Pronatalism and Orphanage Atrocities* | 1966–1989 | `ROU`<br>Europe | `Coercive Population Control` | 10,000 / 18,000 / 30,000 | **43,274** | 0.0947% | `High Consensus` |
| `EVT-1967-NGA-001` | 奈及利亞比亞法拉大饑荒與全面封鎖<br>*Biafran Famine and Starvation Blockade* | 1967–1970 | `NGA`<br>Africa | `Man-made & Policy Famine` | 1,000,000 / 1,500,000 / 3,000,000 | **3,523,055** | 11.5385% | `High Consensus` |
| `EVT-1968-GNQ-001` | 赤道幾內亞馬西埃·恩圭馬極端恐怖統治<br>*Francisco Macías Nguema Reign of Terror* | 1968–1979 | `GNQ`<br>Africa | `Democide, Purges & Forced Labor` | 50,000 / 60,000 / 80,000 | **138,038** | 20.0% | `High Consensus` |
| `EVT-1970-PRK-002` | 北韓政治犯收容所（管理所）體系死難與奴役<br>*North Korean Kwan-li-so Political Prison Camps System* | 1970–2026 | `PRK`<br>Asia | `Democide, Purges & Forced Labor` | 200,000 / 350,000 / 500,000 | **773,559** | 1.75% | `High Consensus` |
| `EVT-1971-BGD-001` | 1971年孟加拉獨立戰爭種族滅絕<br>*1971 Bangladesh Genocide* | 1971 | `BGD`<br>Asia | `Direct Physical Massacre / Genocide` | 300,000 / 1,000,000 / 3,000,000 | **2,167,553** | 1.4706% | `Debated` |
| `EVT-1971-UGA-001` | 烏干達伊迪·阿敏政權恐怖清洗與族群大屠殺<br>*Idi Amin Regime Terror, Purges and Massacres* | 1971–1979 | `UGA`<br>Africa | `Democide, Purges & Forced Labor` | 100,000 / 300,000 / 500,000 | **650,266** | 2.8571% | `High Consensus` |
| `EVT-1969-BRA-002` | 巴西軍政府阿拉瓜亞游擊隊密林大清洗與強迫失蹤<br>*Guerrilha do Araguaia Counter-Insurgency Democide* | 1972–1975 | `BRA`<br>Americas | `Democide, Purges & Forced Labor` | 70 / 90 / 120 | **191** | 0.9% | `High Consensus` |
| `EVT-1972-BDI-001` | 布隆迪選擇性種族滅絕（Ikiza 恐怖）<br>*Burundi Ikiza – Selective Genocide of Hutus* | 1972 | `BDI`<br>Africa | `Direct Physical Massacre / Genocide` | 100,000 / 150,000 / 300,000 | **318,567** | 4.1667% | `High Consensus` |
| `EVT-1972-PHL-003` | 菲律賓馬可仕戒嚴時期法外處決、酷刑與賈比達屠殺<br>*Marcos Martial Law Democide, Torture and Jabidah Massacre* | 1972–1986 | `PHL`<br>Asia | `Democide, Purges & Forced Labor` | 3,257 / 5,000 / 10,000 | **10,619** | 0.0119% | `High Consensus` |
| `EVT-1973-CHL-001` | 智利皮諾契特獨裁政權大清洗與法外處決<br>*Pinochet Dictatorship Purges and Rettig Commission Dossier* | 1973–1990 | `CHL`<br>Americas | `Democide, Purges & Forced Labor` | 3,065 / 3,225 / 4,000 | **6,714** | 0.0323% | `High Consensus` |
| `EVT-1975-IND-001` | 印度緊急狀態強制絕育運動<br>*Indian Emergency Period Forced Sterilization Campaign* | 1975–1977 | `IND`<br>Asia | `Coercive Population Control` | 1,774 / 3,387 / 5,000 | **6,782** | 0.0005% | `Debated` |
| `EVT-1975-KHM-001` | 柬埔寨紅色高棉萬人塚與種族滅絕<br>*Khmer Rouge Killing Fields and Genocide* | 1975–1979 | `KHM`<br>Asia | `Democide, Purges & Forced Labor` | 1,500,000 / 1,800,000 / 2,200,000 | **3,604,423** | 24.0% | `High Consensus` |
| `EVT-1975-TLS-001` | 東帝汶印度尼西亞佔領期屠殺與人為飢饉<br>*East Timor Genocide and Indonesian Occupation* | 1975–1999 | `TLS`<br>Asia | `Direct Physical Massacre / Genocide` | 100,000 / 150,000 / 200,000 | **300,369** | 23.0769% | `High Consensus` |
| `EVT-1976-ARG-001` | 阿根廷軍政府「骯髒戰爭」強迫失蹤與秘密處決<br>*Argentina Dirty War – Forced Disappearances and Extrajudicial Killings* | 1976–1983 | `ARG`<br>Americas | `Democide, Purges & Forced Labor` | 10,000 / 20,000 / 30,000 | **39,315** | 0.0769% | `High Consensus` |
| `EVT-1977-ETH-005` | 衣索比亞德格軍政府「紅色恐怖」政治大屠殺<br>*Ethiopian Red Terror (Qey Shibir)* | 1977–1978 | `ETH`<br>Africa | `Democide, Purges & Forced Labor` | 30,000 / 100,000 / 500,000 | **193,036** | 0.2857% | `High Consensus` |
| `EVT-1979-AFG-001` | 蘇聯阿富汗戰爭蘇軍焦土轟炸、平民屠殺與人為飢饉<br>*Soviet-Afghan War Civilian Atrocities, Depopulation and Landmines* | 1979–1989 | `AFG`<br>Asia | `War-Time Civilian Atrocities` | 560,000 / 1,000,000 / 2,000,000 | **1,863,283** | 7.6923% | `High Consensus` |
| `EVT-1980-CHN-003` | 中國一胎化強制作業與百日無孩運動<br>*Coercive Family Planning Phase & Childless Hundred Days* | 1980–1991 | `CHN`<br>Asia | `Coercive Population Control` | 20,000 / 50,000 / 100,000 | **91,573** | 0.0051% | `Debated` |
| `EVT-1980-KOR-003` | 韓國光州五一八民主化運動武力鎮壓與平民屠殺<br>*Gwangju Democratization Movement Military Massacre* | 1980 | `KOR`<br>Asia | `War-Time Civilian Atrocities` | 165 / 606 / 2,000 | **1,110** | 0.0757% | `Debated` |
| `EVT-1981-GTM-001` | 瓜地馬拉馬雅原住民大屠殺 (沉默的大屠殺)<br>*Guatemalan Maya Genocide (Silent Holocaust)* | 1981–1983 | `GTM`<br>Americas | `Direct Physical Massacre / Genocide` | 100,000 / 140,000 / 200,000 | **251,876** | 1.9444% | `High Consensus` |
| `EVT-1982-LBN-002` | 黎巴嫩薩布拉與沙提拉難民營大屠殺<br>*Sabra and Shatila Massacre in Beirut* | 1982 | `LBN`<br>Asia | `Direct Physical Massacre / Genocide` | 762 / 1,700 / 3,500 | **3,009** | 8.5% | `High Consensus` |
| `EVT-1982-SYR-002` | 敘利亞哈馬大屠殺<br>*1982 Hama Massacre by Hafez al-Assad* | 1982 | `SYR`<br>Asia | `Democide, Purges & Forced Labor` | 10,000 / 25,000 / 40,000 | **44,245** | 10.0% | `High Consensus` |
| `EVT-1983-ETH-002` | 衣索比亞德格軍政府內戰圍困與大饑荒<br>*1983–1985 Ethiopian Famine and Derg Counter-Insurgency* | 1983–1985 | `ETH`<br>Africa | `Man-made & Policy Famine` | 400,000 / 800,000 / 1,200,000 | **1,393,162** | 2.0% | `High Consensus` |
| `EVT-1983-LKA-001` | 斯里蘭卡「黑色七月」反泰米爾人大屠殺與內戰平民砲擊<br>*Black July Pogrom and Sri Lankan Civil War Civilian Shelling* | 1983–2009 | `LKA`<br>Asia | `War-Time Civilian Atrocities` | 40,000 / 70,000 / 100,000 | **121,902** | 0.3889% | `Debated` |
| `EVT-1983-SDN-002` | 第二次蘇丹內戰人為饑荒與焦土清剿<br>*Second Sudanese Civil War Famines and Depopulation* | 1983–2005 | `SSD`<br>Africa | `Man-made & Policy Famine` | 1,500,000 / 2,000,000 / 2,500,000 | **3,482,906** | 25.0% | `High Consensus` |
| `EVT-1983-ZWE-001` | 辛巴威穆加比「古庫拉胡恩迪」恩德貝勒族大屠殺<br>*Gukurahundi Massacres in Matabeleland* | 1983–1987 | `ZWE`<br>Africa | `Direct Physical Massacre / Genocide` | 10,000 / 20,000 / 30,000 | **34,829** | 0.2564% | `High Consensus` |
| `EVT-1984-IND-004` | 1984年印度反錫克教徒大屠殺<br>*1984 Anti-Sikh Pogroms* | 1984 | `IND`<br>Asia | `Direct Physical Massacre / Genocide` | 2,800 / 3,350 / 8,000 | **5,732** | 0.0004% | `High Consensus` |
| `EVT-1988-IRQ-001` | 伊拉克安法爾戰役與哈拉卜賈化武大屠殺<br>*Anfal Campaign and Halabja Chemical Attack* | 1986–1989 | `IRQ`<br>Asia | `War-Time Civilian Atrocities` | 50,000 / 100,000 / 182,000 | **165,314** | 2.8571% | `High Consensus` |
| `EVT-1988-IRN-001` | 1988年伊朗政治犯秘密大處決（死亡委員會）<br>*1988 Executions of Iranian Political Prisoners* | 1988 | `IRN`<br>Asia | `Democide, Purges & Forced Labor` | 2,800 / 5,000 / 30,000 | **7,933** | 0.0096% | `High Consensus` |
| `EVT-1989-CHN-004` | 六四天安門事件武力清場與平民屠殺<br>*Tiananmen Square Military Crackdown and Massacre* | 1989 | `CHN`<br>Asia | `Democide, Purges & Forced Labor` | 300 / 1,000 / 3,000 | **1,555** | 0.0093% | `State Suppressed` |
| `EVT-1989-LBR-001` | 賴比瑞亞與獅子山內戰肢解殘害、血鑽石奴役與童兵慘劇<br>*Liberian and Sierra Leonean Civil Wars Democide and Mutilations* | 1989–2003 | `LBR`<br>Africa | `War-Time Civilian Atrocities` | 250,000 / 300,000 / 350,000 | **466,603** | 4.2857% | `High Consensus` |
| `EVT-1991-SOM-001` | 索馬利亞內戰軍閥人為阻絕與大饑荒<br>*Somali Civil War, Warlord Predation and Famine* | 1991–1993 | `SOM`<br>Africa | `Man-made & Policy Famine` | 220,000 / 280,000 / 350,000 | **422,072** | 3.7333% | `High Consensus` |
| `EVT-1992-BIH-001` | 波士尼亞種族滅絕與雪布尼查大屠殺<br>*Bosnian Genocide and Srebrenica Massacre* | 1992–1995 | `BIH`<br>Europe | `Direct Physical Massacre / Genocide` | 65,000 / 80,000 / 100,000 | **118,761** | 1.8182% | `High Consensus` |
| `EVT-1992-TJK-001` | 塔吉克內戰族群教派清洗與克爾干秋別大屠殺<br>*Tajikistani Civil War Ethnic Cleansing and Kurgan-Tyube Massacres* | 1992–1997 | `TJK`<br>Asia | `War-Time Civilian Atrocities` | 50,000 / 60,000 / 100,000 | **89,071** | 1.0909% | `High Consensus` |
| `EVT-1994-PRK-001` | 北韓「苦難的行軍」大饑荒<br>*North Korean Famine (The Arduous March)* | 1994–1998 | `PRK`<br>Asia | `Man-made & Policy Famine` | 300,000 / 600,000 / 1,000,000 | **863,500** | 2.7273% | `Debated` |
| `EVT-1994-RWA-001` | 盧安達種族滅絕<br>*Rwandan Genocide* | 1994 | `RWA`<br>Africa | `Direct Physical Massacre / Genocide` | 500,000 / 650,000 / 800,000 | **935,458** | 8.2278% | `High Consensus` |
| `EVT-1995-PER-001` | 秘魯藤森政府強制絕育計畫<br>*Peru Fujimori Forced Sterilization Program* | 1995–2000 | `PER`<br>Americas | `Coercive Population Control` | 18 / 100 / 300 | **142** | 0.0004% | `High Consensus` |
| `EVT-1996-COD-003` | 第一次剛果戰爭胡圖族難民大清洗與密林追殺<br>*First Congo War Hutu Refugee Cleansing and Forest Massacres* | 1996–1997 | `COD`<br>Africa | `Direct Physical Massacre / Genocide` | 200,000 / 230,000 / 300,000 | **321,996** | 0.5111% | `Debated` |
| `EVT-1998-COD-002` | 第二次剛果戰爭平民人道災難與掠奪性飢饉<br>*Second Congo War Civilian Mortality and Atrocities* | 1998–2003 | `COD`<br>Africa | `War-Time Civilian Atrocities` | 2,500,000 / 3,800,000 / 5,400,000 | **5,178,930** | 7.451% | `Debated` |
| `EVT-2002-COL-002` | 哥倫比亞軍隊「偽陽性」謀殺平民冒功醜聞<br>*Colombia 'False Positives' Extrajudicial Executions Scandal* | 2002–2008 | `COL`<br>Americas | `Democide, Purges & Forced Labor` | 6,402 / 6,402 / 10,000 | **8,271** | 0.0142% | `High Consensus` |
| `EVT-2003-SDN-001` | 蘇丹達佛種族清洗與人為飢饉<br>*Darfur Genocide and Ethnic Cleansing* | 2003–2008 | `SDN`<br>Africa | `Direct Physical Massacre / Genocide` | 150,000 / 300,000 / 400,000 | **382,629** | 5.0% | `High Consensus` |
| `EVT-2009-LKA-002` | 斯里蘭卡內戰末期穆萊蒂武「無火區」平民大屠戮<br>*Sri Lankan Civil War Mullivaikkal Massacres (Final Phase)* | 2009 | `LKA`<br>Asia | `War-Time Civilian Atrocities` | 40,000 / 50,000 / 70,000 | **59,251** | 16.6667% | `High Consensus` |
| `EVT-2011-SYR-001` | 敘利亞內戰無差別轟炸、化武攻擊與平民圍城飢饉<br>*Syrian Civil War Civilian Slaughter, Chemical Attacks and Sieges* | 2011–2023 | `SYR`<br>Asia | `War-Time Civilian Atrocities` | 250,000 / 306,887 / 400,000 | **355,274** | 1.4367% | `High Consensus` |
| `EVT-2013-CAF-001` | 中非共和國族群教派清洗與人道災難<br>*Central African Republic Inter-communal Cleansing* | 2013–2016 | `CAF`<br>Africa | `Direct Physical Massacre / Genocide` | 10,000 / 15,000 / 30,000 | **16,960** | 0.3261% | `High Consensus` |
| `EVT-2013-SSD-001` | 南蘇丹內戰族群屠殺、人為封鎖與飢饉危機<br>*South Sudanese Civil War Ethnic Cleansing and Man-made Famine* | 2013–2018 | `SSD`<br>Africa | `War-Time Civilian Atrocities` | 383,000 / 383,000 / 400,000 | **433,054** | 3.4818% | `High Consensus` |
| `EVT-2014-IRQ-002` | 伊斯蘭國辛賈爾亞茲迪人種族滅絕<br>*Yazidi Genocide by ISIS in Sinjar* | 2014–2017 | `IRQ`<br>Asia | `Direct Physical Massacre / Genocide` | 3,100 / 5,000 / 10,000 | **5,588** | 1.25% | `High Consensus` |
| `EVT-2016-MMR-001` | 緬甸羅興亞人種族清洗與若開邦大屠殺<br>*Rohingya Genocide and Ethnic Cleansing in Rakhine* | 2016–2017 | `MMR`<br>Asia | `Direct Physical Massacre / Genocide` | 10,000 / 15,000 / 25,000 | **16,387** | 1.3636% | `High Consensus` |
| `EVT-2016-YEM-001` | 葉門內戰人為港口封鎖與大饑荒<br>*Yemeni Famine, Naval Blockade and Humanitarian Crisis* | 2016–2022 | `YEM`<br>Asia | `Man-made & Policy Famine` | 85,000 / 150,000 / 230,000 | **163,874** | 0.5357% | `High Consensus` |
| `EVT-2017-SSD-002` | 南蘇丹耶伊與赤道州族群大清洗與焦土清鄉<br>*Yei and Equatoria Region Ethnic Cleansing in South Sudan* | 2016–2018 | `SSD`<br>Africa | `War-Time Civilian Atrocities` | 15,000 / 20,000 / 35,000 | **21,850** | 1.3333% | `High Consensus` |
| `EVT-2020-AZE-001` | 第二次納卡衝突、人為拉欽走廊封鎖與納卡亞美尼亞人全面清空<br>*Second Nagorno-Karabakh War, Lachin Blockade and Ethnic Depopulation* | 2020–2023 | `AZE`<br>Asia | `Direct Physical Massacre / Genocide` | 6,000 / 8,000 / 12,000 | **8,370** | 5.3333% | `High Consensus` |
| `EVT-2020-ETH-001` | 衣索比亞提格雷戰爭人為封鎖與人道慘劇<br>*Tigray War Siege, Famine and Massacres* | 2020–2022 | `ETH`<br>Africa | `Man-made & Policy Famine` | 300,000 / 450,000 / 600,000 | **470,796** | 8.1818% | `Debated` |
| `EVT-2021-MMR-002` | 緬甸軍事政變全境軍事鎮壓、焦土焚村與空襲平民浩劫<br>*Myanmar Post-2021 Military Coup Nationwide Civilian Terror and Airstrikes* | 2021–2026 | `MMR`<br>Asia | `War-Time Civilian Atrocities` | 5,000 / 8,000 / 15,000 | **8,281** | 0.0148% | `High Consensus` |
| `EVT-2022-UKR-001` | 俄羅斯入侵烏克蘭平民暴行（布查大屠殺等）<br>*Russian Invasion of Ukraine – War Crimes and Civilian Atrocities* | 2022–2026 | `UKR`<br>Europe | `War-Time Civilian Atrocities` | 30,000 / 80,000 / 200,000 | **81,944** | 0.1818% | `Debated` |
| `EVT-2023-PSE-001` | 加薩走廊衝突平民傷亡與圍困人道危機<br>*Gaza Humanitarian Crisis, Civilian Casualties and Blockade* | 2023–2026 | `PSE`<br>Asia | `War-Time Civilian Atrocities` | 41,000 / 70,000 / 186,000 | **70,958** | 3.0435% | `Debated` |

---

## 2. 詳細歷史事件檔案 (Complete Event Dossiers)

### [EVT-1804-HTI-001] 海地建國白人大屠殺 (1804 Haiti Massacre of the French Population)
* **起止年份**：1804
* **地理位置**：海地全境 (Haiti) `[ISO-3: HTI / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `3,000` 人 / 中標基準 `4,000` 人 / 高標 `5,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`989,000,000` 人
  * **2026年當代等效規模**：**`32,963` 人** (放縮係數：8.24x)
  * **區域人口衝擊率**：**`1.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 海地獨立戰爭勝利後，國家領導人讓-雅克·德薩林頒布明令，下令軍隊與平民對殘留島上的全體法裔白人居民展開全面肉體清除。軍隊在太子港、海地角等市鎮逐戶搜捕白人男女及兒童實施公開處決與刺殺，僅豁免極少數波蘭逃兵軍團與德裔定居者及外科醫生，造成海地境內歐洲白人社區徹底消亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Philippe R. Girard (2011, 'The Slaves Who Defeated Napoleon', Univ of Alabama Press); Jeremy D. Popkin (2010, 'You Are All Free: The Haitian Revolution and the Abolition of Slavery'); 德薩林將軍（Jean-Jacques Dessalines）1804年官方宣告命令。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Historical Legal Decree] 德薩林於1804年4月發表正式文告公開承認並辯護該清洗行動（'我們已償還了這些食人族'）；英美各國領事檔案留存詳盡被害商人名冊。`


### [EVT-1815-ZAF-001] 祖魯王國擴張與「苦難動盪」浩劫 (Mfecane / Difaqane (Zulu Expansion and Devastation))
* **起止年份**：1815 – 1840
* **地理位置**：南部非洲（夸祖魯、納塔爾、德蘭士瓦）(Southern Africa) `[ISO-3: ZAF / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `1,000,000` 人 / 高標 `2,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,019,250,000` 人
  * **2026年當代等效規模**：**`7,996,076` 人** (放縮係數：8.0x)
  * **區域人口衝擊率**：**`40.0%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 夏卡·祖魯建立軍事集權王國推行殘酷掠奪征伐，各族群為避戰展開連鎖式毀滅遷徙（稱Mfecane或Difaqane）。祖魯軍隊與逃難部落沿途實施焦土焚村、搶奪牛群牲口並屠戮非作戰部族婦孺，引發大面積連鎖人為大饑荒與部落滅絕，使南部非洲數百萬平方公里土地化為焦土無人區。
* **學術文獻引用摘要 (`sources_summary`)**：
  Norman Etherington (2001, 'The Great Treks: The Transformation of Southern Africa'); Julian Cobbing (1988, 質疑殖民史觀之著名史學論爭); Carolyn Hamilton (1995, 'The Mfecane Aftermath'); J.D. Omer-Cooper (1966, 'The Zulu Aftermath').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 該時期南部非洲原住民未有文字記錄體系，歷史多依據早期歐洲傳教士與布爾人開拓者口述歷史回推；學界對殖民者是否誇大屠殺以合法化其搶佔土地行為（柯賓論戰）存有長期學術爭論。`


### [EVT-1820-RUS-007] 沙俄高加索戰爭早期卡巴爾達與達吉斯坦村落焦土清剿 (Yermolov's Scorched Earth Operations in the North Caucasus)
* **起止年份**：1817 – 1827
* **地理位置**：北高加索車臣、達吉斯坦、卡巴爾達 (Caucasus, Russian Empire) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `40,000` 人 / 中標基準 `60,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,024,750,000` 人
  * **2026年當代等效規模**：**`477,190` 人** (放縮係數：7.95x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 沙皇俄國高加索總督葉爾莫洛夫將軍奉行極端鐵血征服政策，宣稱'我的寬恕是殘酷的'。俄軍對不臣服的北高加索山民村落實施系統性破壞，砍光森林道路、燒光糧田莊稼、屠戮拒絕搬遷的阿烏爾（Aul，山地村寨）平民並強制將居民遷移至低地防線要塞附近監管，引發大規模飢饉與流離失所。
* **學術文獻引用摘要 (`sources_summary`)**：
  Charles King (2008, 'The Ghost of Freedom: A History of the Caucasus'); Moshe Gammer (1994, 'Muslim Resistance to the Tsar'); 阿列克謝·葉爾莫洛夫將軍（Aleksey Yermolov）作戰回憶錄與沙俄高加索軍團戰報檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Tsarist Military Reports] 葉爾莫洛夫將軍在其正式戰報中直言不諱地詳述了焚毀山寨與處死人質的軍事懲戒手段，史料極其完備。`


### [EVT-1822-GRC-002] 希臘獨立戰爭希俄斯島大屠殺 (Chios Massacre (Greek War of Independence))
* **起止年份**：1822
* **地理位置**：愛琴海希俄斯島 (Chios, Ottoman Empire / Greece) `[ISO-3: GRC / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `42,000` 人 / 中標基準 `45,000` 人 / 高標 `52,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,038,500,000` 人
  * **2026年當代等效規模**：**`353,154` 人** (放縮係數：7.85x)
  * **區域人口衝擊率**：**`37.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 鄂圖曼帝國為鎮壓希臘獨立起義，派遣大軍登陸富庶和平的希俄斯島實施示範性焦土報復。奧斯曼軍隊在全島焚毀修道院與村落，系統性處決三歲以上男性基督徒，並將逾五萬名婦女與兒童押往伊斯坦堡和開羅奴隸市場拍賣，全島十二萬人口在數週內驟降至不足兩萬人。
* **學術文獻引用摘要 (`sources_summary`)**：
  William St. Clair (2008, 'That Greece Might Still Be Free'); David Brewer (2001, 'The Greek War of Independence'); 德拉克洛瓦（Eugène Delacroix）名畫《希俄斯島的屠殺》時代檔案; 英國外交領事報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 該事件在歐洲引發強烈親希臘同情運動（Philhellenism），各國領事館留有極為詳盡的受害者與奴隸販賣贖回清冊，各方史料數字具有高度一致性。`


### [EVT-1824-AUS-001] 澳洲黑色戰爭與原住民清剿 (Black War and Tasmanian Aboriginal Genocide)
* **起止年份**：1824 – 1831
* **地理位置**：澳洲塔斯馬尼亞 (Van Diemen's Land / Tasmania, Australia) `[ISO-3: AUS / 大洲: Oceania]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `900` 人 / 中標基準 `1,200` 人 / 高標 `2,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,044,000,000` 人
  * **2026年當代等效規模**：**`9,368` 人** (放縮係數：7.81x)
  * **區域人口衝擊率**：**`24.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英國殖民當局為奪取牧羊用地，宣布戒嚴並懸賞捕殺塔斯馬尼亞原住民。殖民軍與武裝定居者發動「黑線行動」（Black Line）進行地毯式圍捕屠殺，倖存者遭強行流放至荒涼之弗林德斯島，導致塔斯馬尼亞全血統原住民社會完全滅絕。
* **學術文獻引用摘要 (`sources_summary`)**：
  Nicholas Clements (2014, 'The Black War'); Lyndall Ryan (2012, 'Tasmanian Aborigines'); Henry Reynolds (2001, 'An Indelible Stain?'); 塔斯馬尼亞殖民副總督阿瑟（George Arthur）軍事法令記錄。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 殖民早期邊境衝突缺乏官方驗屍與人口註冊體系，民間民兵游擊射殺與性暴力致死多未載入殖民政府正式公報，多數數據依靠歷史學家依據原住民部落譜系缺口推算。`


### [EVT-1830-USA-001] 北美原住民「血淚之路」強迫遷徙 (Trail of Tears (Indian Removal))
* **起止年份**：1830 – 1850
* **地理位置**：美國東南部至奧克拉荷馬 (United States) `[ISO-3: USA / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `12,000` 人 / 中標基準 `16,000` 人 / 高標 `25,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,140,000,000` 人
  * **2026年當代等效規模**：**`114,386` 人** (放縮係數：7.15x)
  * **區域人口衝擊率**：**`16.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美國聯邦政府依據1830年《印第安人遷移法案》（Indian Removal Act），出動陸軍武力強行驅逐切羅基、克里克、塞米諾爾等原住民族離開祖居地。數萬人在寒冬中缺乏口糧與醫療徒步跋涉上千英里，大量老人與幼童死於暴露、飢餓、肺炎與霍亂。
* **學術文獻引用摘要 (`sources_summary`)**：
  Russell Thornton (1984, 'Cherokee Population Losses During The Removal'); Stannard (1992, 'American Holocaust'); National Park Service (NPS) 官方歷史文獻；UCDP 非國家暴力/國家驅逐專題。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 遷徙途中軍方部隊登記制度殘缺，多數原住民死於林野行軍途中而無墓誌記錄；克里克族與塞米諾爾族死難者缺乏官方獨立審計數據。`


### [EVT-1835-NZL-001] 查塔姆群島莫里奧里人滅絕屠殺與奴役 (Moriori Genocide on the Chatham Islands)
* **起止年份**：1835 – 1863
* **地理位置**：紐西蘭查塔姆群島 (Chatham Islands / Rēkohu) `[ISO-3: NZL / 大洲: Oceania]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `300` 人 / 中標基準 `500` 人 / 高標 `1,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,170,000,000` 人
  * **2026年當代等效規模**：**`3,483` 人** (放縮係數：6.97x)
  * **區域人口衝擊率**：**`25.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 信奉極端非暴力和平信條（奴奴瓦克法則Nunuku's Law）的原住民族莫里奧里人（Moriori），遭劫持歐洲商船抵達的毛利人恩加蒂穆湯加（Ngāti Mutunga）和恩加蒂塔馬部族突襲。侵略者依傳統'兼併'習俗，將拒絕戰鬥的莫里奧里平民集體屠戮、烹食，並將倖存千餘人貶為世襲殘酷奴隸禁止通婚繁衍，使其人口在數十年間瀕臨滅絕。
* **學術文獻引用摘要 (`sources_summary`)**：
  Michael King (2000, 'Moriori: A People Rediscovered', Penguin Books); 懷唐伊法庭 (Waitangi Tribunal 2001 官方調查報告 Wai 64 認定莫里奧里人遭受掠奪與奴役); 紐西蘭國會2021年通過莫里奧里和解法案（Moriori Claims Settlement Act）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Legislative Settlement] 懷唐伊法庭進行了長達十餘年詳盡歷史勘驗，2020年紐西蘭政府與莫里奧里後裔正式簽署和解協議並正式官方道歉。`


### [EVT-1845-IRL-001] 愛爾蘭大饑荒 (Great Famine of Ireland)
* **起止年份**：1845 – 1852
* **地理位置**：愛爾蘭 (Ireland / United Kingdom) `[ISO-3: IRL / 大洲: Europe]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,000,000` 人 / 中標基準 `1,100,000` 人 / 高標 `1,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,230,000,000` 人
  * **2026年當代等效規模**：**`7,288,618` 人** (放縮係數：6.63x)
  * **區域人口衝擊率**：**`13.4146%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 馬鈴薯晚疫病爆發後，英國輝格黨政府奉行極端自由放任主義（Laissez-faire）與馬爾薩斯人口論，在全島餓殍遍野之際仍拒絕實施有效救濟，甚至持續由武裝部隊護送愛爾蘭生產之小麥、燕麥及牲畜出口至英格蘭，導致百萬貧民活活餓死。
* **學術文獻引用摘要 (`sources_summary`)**：
  Cormac Ó Gráda (1999, 'Black 47 and Beyond', Princeton Univ Press); Cecil Woodham-Smith (1962, 'The Great Hunger'); Joel Mokyr (1985, 'Why Ireland Starved'); Amartya Sen (1981, 分析英國自由放任糧食輸出政策)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 1841年與1851年愛爾蘭普查人口銳減四分之一，其中約百萬人死於飢餓與斑疹傷寒，另百餘萬人流亡海外，難民船（Coffin ships）海上病歿人數缺乏統一驗屍報告。`


### [EVT-1846-USA-002] 加利福尼亞印第安原住民種族滅絕 (California Genocide (Act for the Government and Protection of Indians))
* **起止年份**：1846 – 1873
* **地理位置**：美國加利福尼亞州 (California, United States) `[ISO-3: USA / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `16,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,236,666,666` 人
  * **2026年當代等效規模**：**`105,445` 人** (放縮係數：6.59x)
  * **區域人口衝擊率**：**`10.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 淘金熱爆發後，加州首任州長伯內特公開宣稱'一場滅絕戰爭必須打下去，直到印第安種族滅絕為止'。州政府立法通過實質奴役法案（1850年印第安人管轄法），動用州財政預算資助民間志願軍與私掠民兵，按割下的印第安頭皮發放政府賞金，直接屠殺上萬原住民，並將倖存兒童強行拍賣為無償勞工，使原住民人口銳減80%以上。
* **學術文獻引用摘要 (`sources_summary`)**：
  Benjamin Madley (2016, 'An American Genocide: The United States and the California Indian Catastrophe, 1846–1873', Yale Univ Press); 加利福尼亞州長紐森（Gavin Newsom）2019年官方道歉與行政命令認定種族滅絕; Brendan C. Lindsay (2012, 'Murder State').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Legislative Acknowledgment] 州議會撥款報銷平民民兵子彈與懸賞之收據檔案完整保存在加州州立檔案館中，耶魯大學歷史學家馬德利完成了逐一屠殺事件的法醫式證據鏈核實。`


### [EVT-1847-MEX-001] 墨西哥猶加敦階級戰爭（瑪雅起義焦土與奴役） (Caste War of Yucatán (Guerra de Castas))
* **起止年份**：1847 – 1901
* **地理位置**：墨西哥猶加敦半島 (Yucatán, Mexico) `[ISO-3: MEX / 大洲: Americas]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `250,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,243,333,333` 人
  * **2026年當代等效規模**：**`1,638,740` 人** (放縮係數：6.55x)
  * **區域人口衝擊率**：**`41.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 瑪雅原住民因不堪西裔白人地主奴役發動大規模起義，隨後演變為長達半世紀的殘酷族群滅絕內戰。起義瑪雅人對白人種植園市鎮實施圍攻屠滅，墨西哥聯邦軍隊與地方軍閥則推行野蠻的焦土反撲，焚燒整個瑪雅聚落、在熱帶密林展開長期圍剿，並將抓獲的數萬名瑪雅戰俘與婦孺直接販賣至古巴甘蔗園為終身奴隸，猶加敦半島損失近四成人口。
* **學術文獻引用摘要 (`sources_summary`)**：
  Nelson Reed (2001, 'The Caste War of Yucatán', Stanford Univ Press); Terry Rugeley (1996, 'Yucatán's Maya Peasantry and the Origins of the Caste War'); 猶加敦州政府歷史檔案館。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Archival Synthesis] 墨西哥政府與天主教會詳細記錄了叛亂初期白人平民被殺名冊，軍方對瑪雅奴隸販賣合約亦保存於哈瓦那與梅里達海關檔案中。`


### [EVT-1851-CHN-001] 太平天國戰爭平民屠殺與圍城焦土 (Taiping Rebellion Civilian Slaughter and Sieges)
* **起止年份**：1851 – 1864
* **地理位置**：中國長江中下游及江南諸省 (Qing Dynasty China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `15,000,000` 人 / 中標基準 `20,000,000` 人 / 高標 `30,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,270,000,000` 人
  * **2026年當代等效規模**：**`128,346,457` 人** (放縮係數：6.42x)
  * **區域人口衝擊率**：**`4.878%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 清軍湘軍、淮軍與太平軍在江南富庶市鎮展開長達十餘年之焦土戰與圍困戰（如天京之戰、安慶之圍）。湘軍破城後奉行有組織之屠城掠奪與縱火報復，伴隨極端糧食斷絕與難民瘟疫，造成江南精華地帶平民人口大滅絕。
* **學術文獻引用摘要 (`sources_summary`)**：
  葛劍雄主編《中國人口史》卷五；R.J. Rummel (1991, 'China's Bloody Century'); 曹樹基《中國人口史·清時期》（推算直接戰亂屠殺與飢疫致死逾2,000萬）；Matthew White (2011, 'Atrocitology')。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 太平天國期間地方基層方志與戶籍檔案悉數毀於兵燹，戰後同治年間重新編修戶口多依據耆老口述推算，屠殺與瘟疫飢饉致死之界限在統計上難以精確拆分。`


### [EVT-1856-CHN-009] 雲南杜文秀起義清軍鎮壓與滇西回民屠殺 (Panthay Rebellion Suppression and Yunnan Muslim Massacres)
* **起止年份**：1856 – 1873
* **地理位置**：中國雲南大理、昆明及滇西諸府 (Qing Dynasty China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `1,000,000` 人 / 中標基準 `1,500,000` 人 / 高標 `2,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,293,076,923` 人
  * **2026年當代等效規模**：**`9,454,194` 人** (放縮係數：6.3x)
  * **區域人口衝擊率**：**`20.0%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 清廷官員挑動漢回矛盾引發滇西回民杜文秀起義建立政權。清軍岑毓英、馬如龍等部在收復大理與昆明周邊城池後，下令嚴厲屠城報復，將投降之起義軍將領及無辜回漢平民成批屠戮，割取死者耳朵裝滿數十竹筐解送省城，戰亂疊加霍亂瘟疫導致雲南全省戶口銳減近半。
* **學術文獻引用摘要 (`sources_summary`)**：
  曹樹基《中國人口史·清時期》（統計雲南全省人口由1855年762萬暴跌至1884年442萬，非正常死亡逾300萬人）; David G. Atwill (2005, 'The Chinese Sultanate: Muslims, Ethnicity, and the State in Southwest China', Stanford Univ Press); 岑毓英奏摺與雲南各縣通志。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 清同治年間滇西基層戶籍檔案全毀，地方官員奏摺多虛報斬首具體戰果或隱匿濫殺平民，精確直接屠殺與瘟疫飢餓死亡邊界難以嚴格剝離。`


### [EVT-1860-NZL-002] 紐西蘭土地戰爭毛利平民清剿與大沒收慘劇 (New Zealand Wars and Raupatu (Confiscation of Māori Lands))
* **起止年份**：1860 – 1872
* **地理位置**：紐西蘭北島（塔拉納基、懷卡托）(New Zealand) `[ISO-3: NZL / 大洲: Oceania]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `2,000` 人 / 中標基準 `3,000` 人 / 高標 `4,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,311,538,461` 人
  * **2026年當代等效規模**：**`18,642` 人** (放縮係數：6.21x)
  * **區域人口衝擊率**：**`5.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英國殖民政府為奪取北島優質土地，出動上萬正規軍入侵懷卡托與塔拉納基。英軍在朗吉奧菲亞（Rangiaowhia）對毫無防備的毛利婦孺聚落展開拂曉突襲，縱火焚燒天主教堂並射殺逃出火海的平民，戰後殖民當局依《新西蘭定居法案》暴力沒收（Raupatu）逾300萬英畝毛利部落土地，將數萬原住民驅逐至貧瘠沼澤，造成長期貧困、飢饉與人口嚴重衰退。
* **學術文獻引用摘要 (`sources_summary`)**：
  James Belich (1986, 'The New Zealand Wars and the Victorian Interpretation of Racial Conflict', Penguin); 懷唐伊法庭 (Waitangi Tribunal 塔拉納基報告 Wai 143 認定英國軍事行為構成嚴重不公); Vincent O'Malley (2016, 'The Great War for New Zealand: Waikato 1863–64').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Formal Crown Apologies] 紐西蘭王室於1995年及後續條約和解中向懷卡托-塔伊努伊等部族正式官方道歉並支付高額賠償，歷史事實經懷唐伊法庭裁定完全確立。`


### [EVT-1861-CHL-002] 智利軍事佔領阿勞卡尼亞與馬普切人暴力清洗 (Occupation of the Araucanía (Pacificación de la Araucanía))
* **起止年份**：1861 – 1883
* **地理位置**：智利中南部阿勞卡尼亞大區 (Araucanía, Chile) `[ISO-3: CHL / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `18,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,316,153,846` 人
  * **2026年當代等效規模**：**`111,461` 人** (放縮係數：6.19x)
  * **區域人口衝擊率**：**`12.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 智利政府調動精銳軍隊以'平定'為名，對抵抗西班牙入侵達三百年的獨立馬普切王國實施最後軍事征服。薩維德拉將軍推行焦土戰術，焚毀全部馬普切莊稼糧倉、劫掠數十萬頭牲畜、屠戮部落長老，將原住民族驅逐隔離至僅佔原祖居地5%的貧瘠保留地（Reducciones），引發毀滅性大饑荒與急性傳染病，重創馬普切社會組織。
* **學術文獻引用摘要 (`sources_summary`)**：
  Jorge Pinto Rodríguez (2000, 'De la inclusión a la exclusión: la formación del estado, la nación y el pueblo mapuche'); José Bengoa (2000, 'Historia del pueblo mapuche'); 智利陸軍科內利奧·薩維德拉（Cornelio Saavedra）作戰報告檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Historical Commission Dossier] 智利'歷史真相與新協議歷史委員會'（2003年由拉戈斯總統設立）發表翔實調查報告，正式承認國家對馬普切人土地掠奪與軍事暴行的歷史責任。`


### [EVT-1862-CHN-010] 同治陝甘回亂族群仇殺與清軍左宗棠收復清剿 (Dungan Revolt Mutual Atrocities and Tso Tsung-t'ang's Cleansing)
* **起止年份**：1862 – 1877
* **地理位置**：中國陝西、甘肅、寧夏及青海 (Qing Dynasty China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `5,000,000` 人 / 中標基準 `8,000,000` 人 / 高標 `12,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,320,769,230` 人
  * **2026年當代等效規模**：**`49,365,172` 人** (放縮係數：6.17x)
  * **區域人口衝擊率**：**`40.0%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 陝西回漢民間矛盾激化爆發毀滅性宗族武裝仇殺，回民起義軍在渭南、華陰等地屠殺漢民市鎮，漢族地主團練亦展開殘酷報復。左宗棠率湘軍入陝甘鎮壓後推行焦土清剿，破金積堡、河州、肅州後皆實施屠城與集體處決，將殘存回民強行分徙至高寒貧瘠荒原（'洗回'與'善後移民'），西北數千里赤地千里。
* **學術文獻引用摘要 (`sources_summary`)**：
  曹樹基《中國人口史·清時期》（甘肅全省人口由1,946萬驟降至495萬，陝西損失近500萬）; 葛劍雄主編《中國人口史》; 金吉堂《中國回教史研究》; 左宗棠《左文襄公全集》征甘奏稿。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 該事件涉及極度敏感的跨族群仇殺歷史，清廷方志記載多帶有強烈偏見與模糊避諱；人口損失龐大但包含戰亂中大批向新疆、中亞（東干人）逃亡之流民與天花霍亂死者。`


### [EVT-1864-PRY-001] 三國同盟戰爭巴拉圭平民大滅絕 (War of the Triple Alliance – Paraguayan Population Annihilation)
* **起止年份**：1864 – 1870
* **地理位置**：巴拉圭 (Paraguay) `[ISO-3: PRY / 大洲: Americas]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `400,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,330,000,000` 人
  * **2026年當代等效規模**：**`2,451,128` 人** (放縮係數：6.13x)
  * **區域人口衝擊率**：**`76.1905%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 巴拉圭獨裁者洛佩斯（Francisco Solano López）對抗阿根廷、巴西、烏拉圭三國聯盟，奉行極端全民皆兵徵召政策，後期甚至徵調十歲男童與老人上陣，並對退卻士兵與疑似叛徒平民就地槍決。聯盟軍焦土推進、封鎖物資與全面破壞農業基礎設施，導致巴拉圭非戰鬥人口大規模死於飢餓、天花與霍亂，形成現代史上區域人口消滅比例最高之人道慘劇。
* **學術文獻引用摘要 (`sources_summary`)**：
  Vera Blinn Reber (1988, 'The Demographics of Paraguay: A Reinterpretation of the Great War', HAHR); Thomas Whigham & Barbara Potthast (1999, 'The Paraguayan Rosetta Stone: New Insights into the Demographics of the Paraguayan War', LARR); Juan Carlos Herken Krauer (1984). 學界共識：戰爭結束時巴拉圭男性人口銳減至總人口約 20–28%，整體人口損失約 60–70%（含戰亡、疫病、飢荒）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 1870年代巴拉圭政府行政體系完全崩潰，戰後人口登記極為粗疏；歷史學界對戰前人口基準（估計 52.5 萬至 100 萬人不等）至今仍有顯著爭議，學者 Reber 與 Whigham 間之論戰延續至21世紀。`


### [EVT-1864-RUS-001] 切爾克斯人種族滅絕與強制驅逐 (Circassian Genocide and Expulsion)
* **起止年份**：1864 – 1867
* **地理位置**：高加索黑海沿岸 (Russian Empire / Caucasus) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `600,000` 人 / 中標基準 `800,000` 人 / 高標 `1,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,330,000,000` 人
  * **2026年當代等效規模**：**`4,902,256` 人** (放縮係數：6.13x)
  * **區域人口衝擊率**：**`53.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 沙皇俄國為徹底兼併北高加索，在軍事征服末期下達系統性驅逐指令。俄軍焚毀原住民村落、割斷糧源，將數十萬穆斯林切爾克斯平民押送至黑海港口強行登船驅逐至鄂圖曼帝國，大批難民死於寒冬、海難、脫水與斑疹傷寒。
* **學術文獻引用摘要 (`sources_summary`)**：
  Walter Richmond (2013, 'The Circassian Genocide', Rutgers Univ Press); Charles King (2008, 'The Ghost of Freedom: A History of the Caucasus'); 喬治亞議會2011年官方種族滅絕認定文獻；沙俄高加索總督府解密檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 沙俄帝國長期將軍事行動定義為「自願遷徙（Muhajir）」，蘇聯時期相關高加索民族苦難歷史遭到意識形態壓制與刪減，直至2000年後部分軍事檔案始得重光。`


### [EVT-1864-USA-003] 科羅拉多沙溪大屠殺 (Sand Creek Massacre)
* **起止年份**：1864
* **地理位置**：美國科羅拉多領地沙溪 (Colorado, United States) `[ISO-3: USA / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `150` 人 / 中標基準 `200` 人 / 高標 `230` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,330,000,000` 人
  * **2026年當代等效規模**：**`1,226` 人** (放縮係數：6.13x)
  * **區域人口衝擊率**：**`25.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 約翰·契文頓上校（John Chivington）率領近700名科羅拉多第三志願騎兵團士兵，突襲已獲美軍安全承諾、營地高懸美國國旗與白旗的和談夏安族與阿拉帕霍族營地。美軍對營內手無寸鐵的老人、婦女與嬰兒進行無差別開槍射殺，並對死者屍體進行割取生殖器、頭皮作為戰利品誇耀遊街的野蠻殘害。
* **學術文獻引用摘要 (`sources_summary`)**：
  美國國會戰爭行為聯合調查委員會 (Joint Committee on the Conduct of the War, 1865 官方調查認定契文頓指揮官犯下殘忍野蠻行徑); Stan Hoig (1961, 'The Sand Creek Massacre'); Ari Kelman (2013, 'A Misplaced Massacre', Harvard Univ Press); 國家公園管理局 (NPS) 國家史跡地調查。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Condemnation] 塞拉斯·索爾上尉（Silas Soule）等良知軍官現場拒絕執行屠殺命令並向陸軍部長秘密舉報，隨後美國國會與陸軍法庭開展詳盡調查，使此案成為19世紀少數被美國官方機構明文譴責之屠殺暴行。`


### [EVT-1866-AUT-001] 奧匈帝國加利西亞貧困大饑荒 (Galician Poverty and Famines in Austria-Hungary)
* **起止年份**：1866 – 1890
* **地理位置**：奧匈帝國加利西亞和洛多梅里亞王國（現波蘭東南與烏克蘭西）(Austria-Hungary) `[ISO-3: POL / 大洲: Europe]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `700,000` 人 / 高標 `1,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,343,333,333` 人
  * **2026年當代等效規模**：**`4,246,898` 人** (放縮係數：6.07x)
  * **區域人口衝擊率**：**`11.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在哈布斯堡王朝保護波蘭貴族大地主利益與極端土地細碎化制度下，加利西亞數百萬烏克蘭裔與波蘭裔農民陷入制度性絕境。維也納當局實施高額農業專賣稅並禁止工業化競爭，農民每日平均熱量攝取不足生理極限之一半，在歐洲最富饒黑土邊緣爆發長達數十年的人為慢性飢荒（'加利西亞式貧窮'），引發百萬人逃亡美洲。
* **學術文獻引用摘要 (`sources_summary`)**：
  Stanisław Szczepanowski (1888, 《加利西亞的貧困》'Nędza Galicji w cyfrach' 經典量化統計，指出每年約5萬人死於極端飢餓營養不良); John-Paul Himka (1988, 'Galician Villagers and the Ukrainian National Movement'); Norman Davies (2005, 'God's Playground').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Detailed Census Records] 奧匈帝國統計局留存了精確的省級死亡率與熱量攝入調查檔案，波蘭國會議員謝帕諾夫斯基運用官方統計出版專著震撼歐洲政壇。`


### [EVT-1871-FRA-001] 巴黎公社「流血週」平民大屠殺與白色恐怖 (Paris Commune 'Bloody Week' (Semaine Sanglante))
* **起止年份**：1871
* **地理位置**：法國巴黎 (Paris, France) `[ISO-3: FRA / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `15,000` 人 / 高標 `20,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,376,666,666` 人
  * **2026年當代等效規模**：**`88,801` 人** (放縮係數：5.92x)
  * **區域人口衝擊率**：**`0.8333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 凡爾賽政府軍在阿道夫·梯也爾與麥克馬洪元帥指揮下攻入巴黎，展開代號'流血週'的殘酷大清洗。軍隊在拉雪茲神父公墓（公社社員牆）、盧森堡花園與夏特雷劇院設立即決軍事法庭，對被俘工人、國民自衛軍、女性'縱火犯'及疑似同情者進行未經審判的流水線式排隊槍決，隨後將數千人流放至新喀里多尼亞苦役營。
* **學術文獻引用摘要 (`sources_summary`)**：
  Robert Tombs (2014, 'How bloody was la Semaine Sanglante? A revision', The Historical Journal); Prosper-Olivier Lissagaray (1876, 《1871年公社史》'Histoire de la Commune de 1871'); 麥克馬洪元帥凡爾賽軍軍事法庭審判記錄; 約翰·梅里曼 (John Merriman, 2014, 'Massacre: The Life and Death of the Paris Commune').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Municipal Burial Records] 巴黎市政府衛生處與塞納省公共墓園管理局留有詳盡的埋葬收據與死體清運賬冊，現代史學家湯姆斯（Robert Tombs）經逐一比對市政檔案確立了1萬至1.5萬直接槍決死難者之基準。`


### [EVT-1875-TUR-003] 鄂圖曼帝國巴爾幹危機波士尼亞與保加利亞四月起義大屠殺 (April Uprising Batak Massacres and Bulgarian Horrors)
* **起止年份**：1876
* **地理位置**：保加利亞巴塔克、普羅夫迪夫及波士尼亞 (Bulgaria, Ottoman Empire) `[ISO-3: BGR / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `15,000` 人 / 中標基準 `20,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,410,000,000` 人
  * **2026年當代等效規模**：**`115,603` 人** (放縮係數：5.78x)
  * **區域人口衝擊率**：**`0.8%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 保加利亞民眾爆發爭取獨立的四月起義後，鄂圖曼帝國當局動用非正規穆斯林武裝'巴希波祖克'（Bashi-bazouks）實施示範性恐怖屠殺。在巴塔克鎮（Batak），起義平民避入主教堂尋求庇護，非正規軍將教堂封閉縱火並斬首全體避難婦孺，數日內屠殺五千餘名村民，引發俄土戰爭爆發與巴爾幹版圖重塑。
* **學術文獻引用摘要 (`sources_summary`)**：
  Eugene Schuyler (美國駐伊斯坦堡總領事1876官方調查報告); 尤金·麥克加漢 (Januarius MacGahan, 1876 戰地通訊震撼歐洲公眾輿論); 威廉·格萊斯頓 (William Gladstone, 1876 政治小冊子 《保加利亞的恐怖與東方問題》); 英國藍皮書檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Diplomatic Inquiry] 美國外交官斯凱勒與英國特使貝林親赴巴塔克廢墟點驗未埋葬之骸骨堆，其官方報告促成歐洲大國集體外交干涉，具有完備國際公文書記錄。`


### [EVT-1876-CHN-005] 丁戊奇荒（華北大饑荒與賑災失序） (Northern Chinese Famine of 1876–1879)
* **起止年份**：1876 – 1879
* **地理位置**：中國山西、河南、陝西、直隸、山東 (Qing Dynasty China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `9,500,000` 人 / 中標基準 `10,000,000` 人 / 高標 `13,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,410,000,000` 人
  * **2026年當代等效規模**：**`57,801,418` 人** (放縮係數：5.78x)
  * **區域人口衝擊率**：**`9.2593%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 特大旱災與鴉片種植擠佔基本糧田交織，晚清政府財政衰竭且漕運物流體系全面癱瘓。地方官僚借賑災中飽私囊，糧價暴漲數十倍，山西等地出現大規模人相食慘劇，餓讎遍野導致千萬人死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  李文海等著《近代中國災荒紀程》; Kathryn Edgerton-Tarpley (2008, 'Tears from Iron: Cultural Responses to Famine in Nineteenth-Century China'); Mike Davis (2001, 'Late Victorian Holocausts'); 晚清山西巡撫曾國荃奏摺檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 清廷戶部與地方督撫之統計折報存在瞞報與遲延，災後山西全省戶口驟降三分之一，精確因飢致死與流亡他省人口難以在原始奏摺中精準區分。`


### [EVT-1876-IND-001] 1876-1878年印度大饑荒（英印殖民政策飢荒） (Great Famine of 1876–1878 (British India))
* **起止年份**：1876 – 1878
* **地理位置**：南印度（馬德拉斯、孟買管轄區及邁索爾）(British Raj) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `5,500,000` 人 / 中標基準 `7,000,000` 人 / 高標 `10,300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,410,000,000` 人
  * **2026年當代等效規模**：**`40,460,993` 人** (放縮係數：5.78x)
  * **區域人口衝擊率**：**`3.6842%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 聖嬰現象引發乾旱後，英國總督李頓勳爵（Lord Lytton）堅持社會達爾文主義與自由市場教條，嚴禁干預糧食價格，甚至在數百萬農民瀕臨餓死之際創下向英國本土出口大米與小麥之歷史新高；飢民必須在「李頓勞動營」進行極度嚴苛苦役方可獲取低於集中營標準之卡路里配給。
* **學術文獻引用摘要 (`sources_summary`)**：
  Mike Davis (2001, 'Late Victorian Holocausts'); William Digby (1878, 'The Famine Campaign in Southern India'); Famine Commission Report of 1880 (英印殖民官方報告); Amartya Sen (1981, 糧食市場投機分析)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 英印殖民當局為掩蓋行政過失，將大量直接飢死者登記為霍亂與痢疾死亡；土邦（Princely States）之統計管理嚴重滯後，偏遠鄉村死亡難以全數登載。`


### [EVT-1878-ARG-002] 阿根廷「征服沙漠」原住民清剿與強迫同化 (Conquest of the Desert (Conquista del Desierto))
* **起止年份**：1878 – 1885
* **地理位置**：阿根廷巴塔哥尼亞及潘帕斯草原 (Patagonia, Argentina) `[ISO-3: ARG / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500` 人 / 中標基準 `2,500` 人 / 高標 `5,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,430,000,000` 人
  * **2026年當代等效規模**：**`14,248` 人** (放縮係數：5.7x)
  * **區域人口衝擊率**：**`8.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 陸軍部長胡利奧·羅卡將軍發動現代軍事遠征奪取巴塔哥尼亞肥沃土地，對馬普切人（Mapuche）與特維爾切人原住民實施系統性軍事圍剿。軍隊沿途射殺抵抗者，將抓獲的萬餘名原住民婦孺徒步押送千公里至布宜諾斯艾利斯馬丁加西亞島集中營，強行將兒童拆散送交白人家庭為奴僕，消滅原住民社會紐帶。
* **學術文獻引用摘要 (`sources_summary`)**：
  Walter Delrio et al. (2010, 'Discussing Indigenous Genocide in Argentina'); Diana Lenton (2014, 布宜諾斯艾利斯大學人類學調查); 羅卡將軍（Julio Argentino Roca）軍事遠征軍正式作戰日誌; 阿根廷歷史記憶檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 阿根廷官方歷史長年將羅卡讚頌為開拓現代國土之民族英雄（其肖像曾印製在百元比索鈔票上）；21世紀阿根廷學術界與原住民團體始全面推動將其重新定性為國家支持的種族滅絕。`


### [EVT-1880-CAN-001] 加拿大原住民寄宿學校制度與強迫同化 (Canadian Indian Residential School System)
* **起止年份**：1880 – 1996
* **地理位置**：加拿大全境 (Canada) `[ISO-3: CAN / 大洲: Americas]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `4,100` 人 / 中標基準 `6,000` 人 / 高標 `15,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,450,000,000` 人
  * **2026年當代等效規模**：**`33,724` 人** (放縮係數：5.62x)
  * **區域人口衝擊率**：**`4.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 加拿大聯邦政府與天主教會、聖公會合作，強制將超過15萬名第一民族、因紐特人和梅蒂人兒童從父母身邊帶走，集中關押於寄宿學校中，執行'殺死印第安人，拯救那個人'之強制同化政策。校內充斥系統性身體虐待、營養實驗、性侵與極端醫療疏失，數千名原住民學童因結核病、飢餓、凍斃與虐待喪生於無名墓地。
* **學術文獻引用摘要 (`sources_summary`)**：
  加拿大真相與和解委員會 (Truth and Reconciliation Commission of Canada, TRC 2015 終期報告认定為'文化種族滅絕'); John S. Milloy (1999, 'A National Crime: The Canadian Government and the Residential School System'); 國家失蹤兒童登記處 (National Student Death Register 已證實逾4,120名孩童姓名); 2021年甘露市（Kamloops）等地無標記墓塚雷達探測。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 聯邦政府印第安事務部與教會歷史檔案長期散失、部分遭銷毀或拒絕向研究人員開放；TRC報告指出大量兒童甚至未被登記姓名即埋葬，實際死亡人數普遍推算在6,000人至15,000人之間。`


### [EVT-1883-VNM-002] 法屬印度支那「勤王運動」法軍殘酷平定與焦土清鄉 (French Pacification of Tonkin and Can Vuong Movement Suppression)
* **起止年份**：1885 – 1896
* **地理位置**：越南北圻與中圻 (Tonkin & Annam, French Indochina) `[ISO-3: VNM / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `50,000` 人 / 中標基準 `75,000` 人 / 高標 `120,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,500,000,000` 人
  * **2026年當代等效規模**：**`407,500` 人** (放縮係數：5.43x)
  * **區域人口衝擊率**：**`0.75%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 咸宜帝發布《勤王詔》號召全國抗法後，法國遠征軍與外籍兵團在中圻與北圻推行殘暴的反叛亂清剿。法軍對支援義軍的農村推行連坐燒毀、在順化與河靜等地公開斬首抗法儒生與農民、截斷灌溉渠道造成地方性飢荒，迫使數十萬難民流亡高山瘴癘之地，造成大量平民死於暴力處決與熱帶傳染病。
* **學術文獻引用摘要 (`sources_summary`)**：
  David G. Marr (1971, 'Vietnamese Anticolonialism 1885–1925', Univ of California Press); Charles Fourniau (1989, 'Annam-Tonkin 1885–1896'); 法國殖民地部與海軍陸戰隊遠征軍作戰檔案（法國海外檔案中心ANOM）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Colonial Military Archives] 法國普羅旺斯艾克斯海外檔案館保存著極為詳盡的遠征軍燒村清單與斬首照片記錄，越南學者亦完成了各省勤王義軍抗法殉難名冊整理。`


### [EVT-1885-COD-001] 剛果自由邦暴行與橡膠強迫勞動 (Congo Free State Atrocities and Forced Labor)
* **起止年份**：1885 – 1908
* **地理位置**：剛果自由邦 (Congo Free State / modern DRC) `[ISO-3: COD / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `3,000,000` 人 / 中標基準 `5,000,000` 人 / 高標 `10,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,500,000,000` 人
  * **2026年當代等效規模**：**`27,166,667` 人** (放縮係數：5.43x)
  * **區域人口衝擊率**：**`25.0%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 比利時國王利奧波德二世將剛果盆地劃為私人領地，建立僱傭軍憲兵隊（Force Publique）強行榨取天然橡膠與象牙。為強制達成配額，憲兵隊普遍實施燒村、屠殺、強姦、綁架婦孺為人質及殘酷剁手酷刑，引發大規模飢荒、疾病與社會崩潰。
* **學術文獻引用摘要 (`sources_summary`)**：
  Adam Hochschild (1998, 'King Leopold's Ghost'); Casement Report (1904, 英國外交官羅傑·凱斯門特調查報告); Jan Vansina (1966, 人口學模型估算); Isidore Ndaywel è Nziem (剛果歷史學會專題研究)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 利奧波德二世在1908年被迫將統治權移交比利時政府前，下令連續焚燒剛果檔案室機密文件數日，國王親口聲稱「他們無權知道我在剛果做了什麼」；學者多依據村落人口空心化與傳教士日記回推。`


### [EVT-1888-ETH-004] 衣索比亞牛瘟大饑荒（災難七年 / 基夫肯） (Great Ethiopian Famine of 1888–1892 (Kifu Qen))
* **起止年份**：1888 – 1892
* **地理位置**：衣索比亞全境、厄利垂亞及索馬利亞 (Horn of Africa) `[ISO-3: ETH / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500,000` 人 / 中標基準 `2,500,000` 人 / 高標 `3,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,530,000,000` 人
  * **2026年當代等效規模**：**`13,316,993` 人** (放縮係數：5.33x)
  * **區域人口衝擊率**：**`31.25%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 義大利殖民軍隊為入侵非洲之角，由印度進口受感染牲畜引發牛瘟病毒首度傳入非洲大陸，境內90%耕牛與牛群在數月內死亡。在傳統農業依賴牛耕體系崩潰之際，地方軍閥爭戰與苛捐雜稅並未停止，致使全境爆發被稱為'惡毒之日'（Kifu Qen）的毀滅性大饑荒，衣索比亞總人口喪失約三分之一，野獸食人成災。
* **學術文獻引用摘要 (`sources_summary`)**：
  Richard Pankhurst (1966, 'The Great Ethiopian Famine of 1888–1892', The University College Review); Harold G. Marcus (1995, 'The Life and Times of Menelik II'); 孟尼利克二世皇帝編年史; 義大利殖民陸軍非洲遠征軍醫療報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 該時期衣索比亞處於孟尼利克二世統一前夕，除帝國編年史與阿克蘇姆教會記錄外缺乏全境人口統計普查，各省人口損失主要由皇家編年史及歐洲外交使團日記比對推估。`


### [EVT-1890-AGO-001] 葡屬安哥拉殖民平定戰役與強迫橡膠橡膠奴役慘劇 (Portuguese Pacification Campaigns in Angola and Bailundo Revolt)
* **起止年份**：1890 – 1915
* **地理位置**：葡屬西非安哥拉中央高原及南部 (Portuguese Angola) `[ISO-3: AGO / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `150,000` 人 / 高標 `250,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,550,000,000` 人
  * **2026年當代等效規模**：**`788,710` 人** (放縮係數：5.26x)
  * **區域人口衝擊率**：**`3.75%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 柏林西非會議後葡萄牙為實際佔領安哥拉內陸，對奧萬博人、姆邦杜人與拜倫多王國發動長達二十餘年的'平定戰役'。葡軍動用僱傭軍洗劫村莊、屠殺抵抗部落酋長，並實施強制勞工制度（Serviçais），將數十萬原住民強行押送至聖多美與普林西比可可種植園或內陸鐵路服苦役，工作條件形同死亡集中營，死亡率長年高達二成以上。
* **學術文獻引用摘要 (`sources_summary`)**：
  René Pélissier (1977, 'Les Guerres Grises: Résistance et Révoltes en Angola 1845–1941'); Douglas L. Wheeler & René Pélissier (1971, 'Angola', Praeger); 葡萄牙海外歷史檔案館（AHU 里斯本）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / British Foreign Office Inquiries] 英國記者亨利·內文森（Henry Nevinson）於1906年出版專著揭露'現代奴隸制'引發英美對葡屬可可的國際抵制，里斯本海事部留存詳盡強征勞工合同。`


### [EVT-1890-USA-004] 傷膝河大屠殺 (Wounded Knee Massacre)
* **起止年份**：1890
* **地理位置**：美國南達科他州傷膝河 (South Dakota, United States) `[ISO-3: USA / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `250` 人 / 中標基準 `300` 人 / 高標 `350` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,550,000,000` 人
  * **2026年當代等效規模**：**`1,577` 人** (放縮係數：5.26x)
  * **區域人口衝擊率**：**`75.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美國陸軍第七騎兵團在收繳蘇族（Lakota Sioux）大腳酋長部隊的武器時，在慌亂鳴槍後出動霍奇基斯速射機關砲（Hotchkiss guns），對包圍圈內手無寸鐵的蘇族男女與孩童近距離轟擊。士兵追殺逃跑平民達數英里，大批婦孺倒斃雪原中並遭暴風雪凍僵，事後美軍工兵將遺體草率傾倒於集體萬人塚。
* **學術文獻引用摘要 (`sources_summary`)**：
  Dee Brown (1970, 'Bury My Heart at Wounded Knee'); Jerome A. Greene (2014, 'American Carnage: Wounded Knee, 1890'); 美國國會1990年通過兩院聯合決議案對屠殺正式表示'深切悲痛與遺憾'。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Congressional Apology] 戰後美國陸軍曾荒謬地向參與屠殺的20名士兵頒發榮譽勳章（Medal of Honor）；百年後印第安人權組織持續抗爭，美國國會於1990年通過決議道歉，但涉案勳章迄今未被正式撤銷。`


### [EVT-1894-TUR-004] 鄂圖曼哈米德大屠殺 (Hamidian Massacres of Armenians and Assyrians)
* **起止年份**：1894 – 1896
* **地理位置**：鄂圖曼帝國安納托利亞各省及伊斯坦堡 (Ottoman Empire) `[ISO-3: TUR / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `200,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,590,000,000` 人
  * **2026年當代等效規模**：**`1,025,157` 人** (放縮係數：5.13x)
  * **區域人口衝擊率**：**`8.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇丹阿卜杜勒-哈米德二世（'血腥蘇丹'）為鎮壓亞美尼亞自治改革運動，組建由庫德游牧騎兵構成的'哈米迪耶輕騎兵團'（Hamidiye cavalry），對東部安納托利亞各省的亞美尼亞基督徒展開全國性屠殺。暴徒在薩孫、烏爾法大教堂（將數千名避難平民鎖入教堂活活燒死）及首都伊斯坦堡當街圍殺平民，掠奪村莊，迫使十萬人強迫改宗伊斯蘭教。
* **學術文獻引用摘要 (`sources_summary`)**：
  Vahakn N. Dadrian (1995, 'The History of the Armenian Genocide', Berghahn Books); J. Michael Fitzsimons (2013); 英國外交部藍皮書（Turkey No. 2, 1896）; 約翰尼斯·萊普修斯 (Johannes Lepsius 德國東方傳教會檔案)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Diplomatic Consular Records] 英、法、俄三國駐君士坦丁堡大使館向蘇丹發送了大量聯合抗議照會，歐洲各大國領事人員提供了極為詳盡的各省受害者統計與教堂受損名單。`


### [EVT-1899-IND-003] 1899-1900年印度大饑荒（柯松總督時期） (Indian Famine of 1899–1900 (Curzon Famine))
* **起止年份**：1899 – 1900
* **地理位置**：英屬印度（孟買管轄區、旁遮普、中央邦及德干高原）(British Raj) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,000,000` 人 / 中標基準 `2,000,000` 人 / 高標 `4,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,640,000,000` 人
  * **2026年當代等效規模**：**`9,939,024` 人** (放縮係數：4.97x)
  * **區域人口衝擊率**：**`0.8%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 柯松總督（Lord Curzon）堅持嚴格之「自力原則」（Test of Destitution），要求領受救濟之飢民通過嚴苛體力勞動測試，每日卡路里配給低於納粹達豪集中營標準。在聖嬰現象引發印度洋夏季季風全面失效之際，殖民政府同步堅持市場出口導向，拒絕直接干預糧食流通，加劇旱災引發之大規模飢荒蔓延。
* **學術文獻引用摘要 (`sources_summary`)**：
  Mike Davis (2001, 'Late Victorian Holocausts', 估算死亡逾 100 萬); William Digby (1901, 'Prosperous British India'); B.M. Bhatia (1985, 'Famines in India'); 英印殖民地《飢荒調查委員會報告》(1901); Lizzie Collingham (2011, 'The Taste of War').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 此次飢荒與1899-1902年第二次波耳戰爭同期，英國殖民行政資源分散，地方官員大量低報死亡人數以規避行政責任；學界對「直接飢饉死亡」與「因飢荒引發傳染病間接死亡」之口徑差異，導致估算範圍差距高達3.5倍。`


### [EVT-1899-PHL-001] 美菲戰爭平民集中營與薩馬島焦土鎮壓 (Philippine-American War – Concentration Camps and Civilian Atrocities)
* **起止年份**：1899 – 1902
* **地理位置**：菲律賓諸島（尤以薩馬島、巴塘加斯）(Philippines) `[ISO-3: PHL / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `250,000` 人 / 高標 `600,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,640,000,000` 人
  * **2026年當代等效規模**：**`1,242,378` 人** (放縮係數：4.97x)
  * **區域人口衝擊率**：**`3.5714%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美國拒絕承認菲律賓獨立後展開鎮壓，雅各布・史密斯（Jacob Smith）在薩馬島下達「殺光十歲以上男性」的臭名令狀；美軍在巴塘加斯等地設立「安撫區」強制集中平民，禁止農村人口外出耕作導致糧食斷絕，配合焦土清田戰術製造大規模飢荒，加以霍亂肆虐，造成數十萬農村平民在集中營及戰亂中死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Stuart Creighton Miller (1982, 'Benevolent Assimilation: The American Conquest of the Philippines'); Paul Kramer (2006, 'The Blood of Government: Race, Empire, the United States & the Philippines'); 美國參議院洛奇委員會調查報告（1902, Lodge Committee）; John Bassett Moore (戰時美軍戰略電報集)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 美國政府長年以「保護文明」之殖民敘事框架淡化平民傷亡，相關美軍戰地電報在20世紀初選擇性解密；菲律賓民族主義史學與美方正式軍史在死亡人數方面存在3倍以上差距。`


### [EVT-1899-ZAF-002] 第二次波耳戰爭英國平民集中營 (Second Boer War British Concentration Camps)
* **起止年份**：1899 – 1902
* **地理位置**：南非（川斯瓦、奧蘭治自由邦等）(South Africa) `[ISO-3: ZAF / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `42,000` 人 / 中標基準 `46,000` 人 / 高標 `48,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,640,000,000` 人
  * **2026年當代等效規模**：**`228,598` 人** (放縮係數：4.97x)
  * **區域人口衝擊率**：**`15.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英軍總司令基奇納勳爵為粉碎波耳游擊隊，下令對南非農村推行焦土政策，焚燒三萬棟農舍並將十一萬波耳白人婦孺及十餘萬黑人勞工強押進帳篷集中營。營地極度缺乏飲水、口糧與藥品，致使麻疹、斑疹傷寒失控爆發，造成約2.8萬名波耳平民（其中2.2萬為未成年兒童，佔全體波耳兒童近半數）及至少2萬名黑人平民慘死。
* **學術文獻引用摘要 (`sources_summary`)**：
  Emily Hobhouse (1901, 'The Brunt of the War and Where It Fell' 揭發集中營真相調查報告); S.B. Spies (1977, 'Methods of Barbarism?'); Elizabeth van Heyningen (2013, 'The Concentration Camps of the Anglo-Boer War', Jacana Media); 英國官方福賽特調查委員會（Fawcett Commission 1901）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 英國人道主義者艾蜜莉·霍布豪斯親赴南非調查並向英國議會公開指控'野蠻手段'（Methods of Barbarism），促成官方委員會調查；波耳人死亡名冊與營地病歷登記保存極其詳盡，黑人死者則近年透過歷史學家重新發掘補正。`


### [EVT-1900-PER-001] 秘魯亞馬遜普圖馬約橡膠採集暴行 (Peruvian Amazon Company Putumayo Atrocities)
* **起止年份**：1900 – 1912
* **地理位置**：秘魯普圖馬約盆地 (Putumayo Basin, Peru / Colombia) `[ISO-3: PER / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `30,000` 人 / 中標基準 `40,000` 人 / 高標 `50,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,650,000,000` 人
  * **2026年當代等效規模**：**`197,576` 人** (放縮係數：4.94x)
  * **區域人口衝擊率**：**`80.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 秘魯亞馬遜公司（PAC）由英國資本支撐，委派武裝監工對普圖馬約河流域之惠托托（Huitoto）等印第安原住民實施橡膠配額制度。凡無法完成指定採膠量之村落，監工即以鞭打（鱷魚皮抽打直至骨現）、斬首、活焚及強姦等酷刑懲罰，並將目標村落夷平；人口因直接屠殺、強迫勞役、疾病及逃亡損失估計高達 80–90%。
* **學術文獻引用摘要 (`sources_summary`)**：
  Roger Casement (1912, Putumayo Report, 英國外交官調查報告向國會呈交); Wade Davis (1996, 'One River'); Colin Tatz & Winton Higgins (2016, 'The Magnitude of Genocide'); 英國下議院藍皮書（Blue Book on Putumayo, 1913）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 秘魯司法對涉案英國股東及秘魯本地監工皆未能成功追訴，現場記錄主要依賴凱斯門特爵士（Sir Roger Casement）秘密訪查與原住民倖存者證詞；Casement 本人後因愛爾蘭獨立案被英國處決，部分相關文件流散。`


### [EVT-1903-MDA-001] 沙皇俄國晚期與內戰基希涅夫等反猶大屠殺 (Russian Empire Kishinev and Civil War Anti-Jewish Pogroms)
* **起止年份**：1903 – 1921
* **地理位置**：俄羅斯帝國猶太人定居界（摩爾多瓦、烏克蘭等）(Russian Empire) `[ISO-3: MDA / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `70,000` 人 / 中標基準 `120,000` 人 / 高標 `250,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,687,500,000` 人
  * **2026年當代等效規模**：**`579,556` 人** (放縮係數：4.83x)
  * **區域人口衝擊率**：**`2.4%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在沙皇專制暗中縱容及極右翼'黑色百人團'挑唆下，復活節期間在基希涅夫爆發駭人反猶血腥暴動。此後在俄國內戰期間（1918-1921），烏克蘭民族軍、白軍哥薩克與各派綠軍武裝對猶太市鎮（Shtetl）展開超過一千場系統性暴動與屠戮，數萬名猶太人遭割喉、強姦與整村滅絕，被史學界視為納粹屠猶之前奏。
* **學術文獻引用摘要 (`sources_summary`)**：
  Steven J. Zipperstein (2018, 'Pogrom: Kishinev and the Making of the Modern Jewish World'); Jeffrey Veidlinger (2021, 'In the Midst of Civilized Europe: The Pogroms of 1918–1921 and the Onset of the Holocaust'); Monty Noam Penkower (2004); 亨利·斯利奧茲伯格司法調查報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 內戰混亂期大批偏遠猶太村莊完全被毀無倖存者登記，各派軍閥均否認官方責任；紅十字會與猶太援助委員會在戰後依據難民登記核實出至少十餘萬死者姓名。`


### [EVT-1904-NAM-001] 納米比亞赫雷羅與納馬人大屠殺 (Herero and Namaqua Genocide)
* **起止年份**：1904 – 1908
* **地理位置**：德屬西南非洲 (modern Namibia) `[ISO-3: NAM / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `45,000` 人 / 中標基準 `75,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,700,000,000` 人
  * **2026年當代等效規模**：**`359,559` 人** (放縮係數：4.79x)
  * **區域人口衝擊率**：**`75.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 德意志帝國殖民軍總司令洛塔爾·馮·特羅塔（Lothar von Trotha）發布明文「滅絕令」（Vernichtungsbefehl），下令射殺境內所有赫雷羅人。德軍將逃亡之原住民婦孺逼入奧馬海凱沙漠並封鎖所有水井，倖存者被押送至鯊魚島集中營進行致死勞動與人體醫學試驗，赫雷羅族人口銳減約80%。
* **學術文獻引用摘要 (`sources_summary`)**：
  Jürgen Zimmerer & Joachim Zeller (2003, 'Genocide in German South-West Africa'); 德國聯邦政府2021年官方道歉文獻；聯合國惠特克報告 (Whitaker Report, 1985) 認定為20世紀首場種族滅絕；德軍特羅塔將軍滅絕令檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 集中營受害者遺骸曾遭德軍大量送往柏林作種族優生學研究，沙漠死亡者多化為白骨；至2021年德德雙方政府簽署協議時始確認大部歷史賠償框架。`


### [EVT-1905-TZA-001] 德屬東非馬基馬基起義焦土鎮壓與人為飢饉 (Maji Maji Rebellion – German Colonial Scorched Earth Famine)
* **起止年份**：1905 – 1907
* **地理位置**：德屬東非（現坦尚尼亞南部）(German East Africa / Tanzania) `[ISO-3: TZA / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `250,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,709,090,909` 人
  * **2026年當代等效規模**：**`1,192,154` 人** (放縮係數：4.77x)
  * **區域人口衝擊率**：**`6.25%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 面對多族群武裝起義，德意志帝國殖民軍隊採取系統性焦土政策，摧毀坦尚尼亞南部（馬特加斯等地區）所有農村糧倉、焚燒農田並屠殺農業勞動力，造成長達兩年之人為大饑荒。殖民地政府有意識地以飢餓作為戰略武器，導致非戰鬥平民死於飢餓的人數遠超直接戰鬥傷亡，重創了南部坦尚尼亞整整一個世代的人口基礎。
* **學術文獻引用摘要 (`sources_summary`)**：
  John Iliffe (1979, 'A Modern History of Tanganyika', Cambridge Univ Press); James Giblin & Jamie Monson (2010, 'Maji Maji: Lifting the Fog of War'); Marcia Wright (1968); 德屬東非殖民政府鎮壓報告（德國聯邦檔案館）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 德屬殖民地行政崩潰後德國敗於一戰，大批地方農業與人口損失記錄未能完整保存；德國聯邦檔案館中殖民時期文件保存散亂，坦尚尼亞國家檔案館的口述歷史研究為主要補充史料。`


### [EVT-1909-TUR-005] 鄂圖曼阿達納大屠殺 (Adana Massacre of Armenians (1909))
* **起止年份**：1909
* **地理位置**：鄂圖曼帝國奇里乞亞阿達納省 (Adana, Ottoman Empire) `[ISO-3: TUR / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `20,000` 人 / 中標基準 `25,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,745,454,545` 人
  * **2026年當代等效規模**：**`116,732` 人** (放縮係數：4.67x)
  * **區域人口衝擊率**：**`5.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在伊斯坦堡反青年土耳其黨的反革命政變騷亂期間，極端反動暴民與地方駐軍在阿達納省對亞美尼亞基督徒展開大規模屠戮。暴民洗劫焚毀了阿達納全城的亞美尼亞人聚居區、學校與教堂，屠殺蔓延至全省農村，造成兩萬餘名亞美尼亞平民慘遭殺害，數千名孤兒流離失所，被學界確認為1915年全面種族滅絕的直接前奏預演。
* **學術文獻引用摘要 (`sources_summary`)**：
  Raymond Kévorkian (2011, 'The Armenian Genocide: A Complete History', I.B. Tauris); 青年土耳其黨政府議會調查委員會報告 (哈戈普·巴巴吉安代表發布); 英國外交領事道格蒂-懷利報告; 美國外交檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Ottoman Parliamentary Investigation] 當時青年土耳其黨中央政府派出的議會調查團向議會提交了確認死傷的正式報告，涉案阿達納省長與部分軍官一度遭軍事法庭免職審判。`


### [EVT-1913-TUR-002] 希臘人與亞述人種族滅絕 (Greek and Assyrian Genocide (Pontic Greeks, Assyrians))
* **起止年份**：1913 – 1923
* **地理位置**：鄂圖曼帝國及其後繼土耳其共和國 (Ottoman Empire / Modern Turkey) `[ISO-3: TUR / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `700,000` 人 / 高標 `900,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,781,818,181` 人
  * **2026年當代等效規模**：**`3,201,786` 人** (放縮係數：4.57x)
  * **區域人口衝擊率**：**`35.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 與亞美尼亞種族滅絕同步展開，鄂圖曼青年土耳其黨政府對本都希臘人（Pontic Greeks）、愛奧尼亞希臘人及亞述基督徒實施死亡行軍、驅逐、強制勞役兵團（Amele Taburlari）死亡及黑海沿岸屠殺等手段；凱末爾政府成立後1919-1923年對倖存希臘平民進行最後清洗，構成完整的人口清除意圖與系統性執行。
* **學術文獻引用摘要 (`sources_summary`)**：
  Taner Akçam (2012, 'The Young Turks' Crime Against Humanity', Princeton Univ Press); David Gaunt (2006, 'Massacres, Resistance, Protectors: Muslim-Christian Relations in Eastern Anatolia during WWI'); 國際種族滅絕研究學會 (IAGS) 決議認定；希臘議會種族滅絕認定法案（1994）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 同亞美尼亞案例，土耳其官方否認種族滅絕性質，相關奧圖曼帝國晚期政府文件遭選擇性封存或銷毀；本都希臘社群及亞述流亡組織之口述歷史為主要史料來源，考古遺址多在現代土耳其境內至今未獲系統性發掘。`


### [EVT-1915-LBN-001] 黎巴嫩山一戰大饑荒 (Mount Lebanon Famine (1915–1918))
* **起止年份**：1915 – 1918
* **地理位置**：鄂圖曼黎巴嫩山省 (Mount Lebanon, Ottoman Syria) `[ISO-3: LBN / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `180,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,800,000,000` 人
  * **2026年當代等效規模**：**`815,000` 人** (放縮係數：4.53x)
  * **區域人口衝擊率**：**`43.4783%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 一戰期間，英法地中海艦隊對敘利亞沿岸實施嚴密封鎖，切斷所有糧食進口；鄂圖曼帝國軍方同步大規模強行徵收黎巴嫩山地區的農產物資供應軍隊。雙重打擊下，加以蝗災肆虐，黎巴嫩山基督教與德魯茲族混居社區在短短三年內餓死總人口約四至五成，城市街頭餓死屍體遍佈之景象，被目擊傳教士詳細留下書面紀錄。
* **學術文獻引用摘要 (`sources_summary`)**：
  Linda Schilcher (1992, 'The Famine of 1915–1918 in Greater Syria', in 'Problems of the Middle East in Historical Perspective'); Melanie Schulze Tanielian (2018, 'The Charity of War: Famine, Humanitarian Aid, and World War I in the Middle East', Stanford Univ Press); Ottoman archival records （解密鄂圖曼徵糧令文件）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 黎巴嫩山彼時處於多國軍事佔領的法律真空地帶，鄂圖曼、英法與地方宗教社區檔案分散保存於不同國家，人口死亡登記殘缺；學界主要依靠1921年法國委任統治政府的人口普查回推損失。`


### [EVT-1915-TUR-001] 亞美尼亞種族滅絕 (Armenian Genocide)
* **起止年份**：1915 – 1917
* **地理位置**：鄂圖曼帝國安納托利亞至敘利亞沙漠 (Ottoman Empire) `[ISO-3: TUR / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `800,000` 人 / 中標基準 `1,200,000` 人 / 高標 `1,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,800,000,000` 人
  * **2026年當代等效規模**：**`5,433,333` 人** (放縮係數：4.53x)
  * **區域人口衝擊率**：**`60.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 鄂圖曼青年土耳其黨三巨頭政權利用第一次世界大戰掩護，下達《特希爾法》（Tehcir Law），首先清洗亞美尼亞知識分子與士兵，隨後將全體亞美尼亞平民有組織地押往敘利亞代爾祖爾沙漠進行「死亡行軍」。特種組織（Teşkilât-ı Mahsusa）沿途執行系統性屠殺、搶劫與強姦。
* **學術文獻引用摘要 (`sources_summary`)**：
  Taner Akçam (2012, 'The Young Turks' Crime Against Humanity', Princeton Univ Press); Raymond Kévorkian (2011, 'The Armenian Genocide'); International Association of Genocide Scholars (IAGS); 亨利·摩根索大使（Henry Morgenthau）回憶錄。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 土耳其共和國歷任政府官方嚴詞否認種族滅絕性質，將檔案局涉案文件長期列為機密或有選擇性銷毀，並將公開稱其為種族滅絕者依《土耳其刑法典第301條》起訴，具強烈官方審查屬性。`


### [EVT-1916-KGZ-001] 沙俄中亞大起義鎮壓與柯爾克孜族大逃亡（烏爾昆浩劫） (Central Asian Revolt of 1916 and Urkun Catastrophe)
* **起止年份**：1916 – 1917
* **地理位置**：沙皇俄國突厥斯坦總督區（七河州、吉爾吉斯、哈薩克）(Russian Turkestan) `[ISO-3: KGZ / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `150,000` 人 / 高標 `270,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,818,000,000` 人
  * **2026年當代等效規模**：**`672,442` 人** (放縮係數：4.48x)
  * **區域人口衝擊率**：**`12.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 一戰期間沙皇尼古拉二世下達動員中亞穆斯林充當後方軍事苦力的詔令，引發哈薩克與吉爾吉斯牧民爆發廣泛起義。沙俄庫羅帕特金總督調動配備機關槍的哥薩克騎兵部隊展開殘酷焦土鎮壓，焚燒數百座遊牧氈帳，迫使三十萬柯爾克孜平民在嚴冬中攜家帶口翻越天山別迭里山口逃往中國新疆，逾十萬人在雪崩、飢寒與追兵射殺中倒斃雪原。
* **學術文獻引用摘要 (`sources_summary`)**：
  Alexander Morrison (2020, 'The Russian Empire and the First World War: Central Asian Uprising', Oxford Univ Press); 吉爾吉斯共和國議會2016年決議將烏爾昆認定為種族滅絕; 庫羅帕特金總督（Aleksey Kuropatkin）鎮壓戰報; 俄羅斯國家軍事檔案館。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Century Centennial Memorial] 吉爾吉斯斯坦於2016年百年祭舉行國家哀悼，歷史學家在天山山口沿線收集到大量未安葬之受難者白骨遺骸；俄羅斯歷史學界亦完全解密庫羅帕特金鎮壓電報。`


### [EVT-1918-AZE-002] 巴庫「三月事件」與「九月事件」雙向族群大屠殺 (March Days and September Days Massacres in Baku)
* **起止年份**：1918
* **地理位置**：亞塞拜然巴庫及周邊 (Transcaucasia / Azerbaijan) `[ISO-3: AZE / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `20,000` 人 / 中標基準 `25,000` 人 / 高標 `35,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,854,000,000` 人
  * **2026年當代等效規模**：**`109,898` 人** (放縮係數：4.4x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 俄羅斯帝國崩潰之際，巴庫蘇維埃布爾什維克與亞美尼亞達什納克軍隊聯手，在3月對巴庫的亞塞拜然穆斯林居民發動殘暴屠殺（三月事件，約1.2萬人遇害）；同年9月鄂圖曼高加索伊斯蘭軍與亞塞拜然部隊反攻巴庫後，隨即對城內的亞美尼亞平民實施對等的殘酷報復大屠殺（九月事件，約1.5萬名亞美尼亞人被殺）。
* **學術文獻引用摘要 (`sources_summary`)**：
  Firuz Kazemzadeh (1951, 'The Struggle for Transcaucasia, 1917–1921'); Michael G. Smith (2001, 'Anatomy of a Rumour: Murder Scandal, the Musavat Party and Narratives of the Russian Revolution in Baku'); 亞塞拜然官方調查委員會檔案; 亞美尼亞革命聯盟檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Contested Memory] 該事件為亞美尼亞與亞塞拜然現代世紀世仇之核心原爆點，兩國各自建立紀念碑並指控對方犯下種族滅絕，中立史學界確認雙向大屠殺之歷史客觀性。`


### [EVT-1918-FIN-001] 芬蘭內戰白色恐怖與集中營死難 (Finnish Civil War White Terror and Prison Camps)
* **起止年份**：1918
* **地理位置**：芬蘭全境（坦佩雷、維堡、亨努拉等集中營）(Finland) `[ISO-3: FIN / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `20,000` 人 / 中標基準 `25,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,854,000,000` 人
  * **2026年當代等效規模**：**`109,898` 人** (放縮係數：4.4x)
  * **區域人口衝擊率**：**`0.8065%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 芬蘭獨立爆發紅白內戰後，曼納海姆將軍指揮的白衛軍在德軍支援下擊潰紅衛軍，隨後展開殘酷的'白色恐怖'清算。白軍在維堡等地展開即決槍決（包含大量俄羅斯平民與婦女），並將八萬名赤衛軍戰俘與左翼平民（包含哺乳母親）關押在條件極度非人的集中營中，在數月內因故意飢餓與痢疾折磨導致逾萬人慘死。
* **學術文獻引用摘要 (`sources_summary`)**：
  芬蘭國家檔案館 (War Victims of Finland 1914–1922 官方數據庫，精確核實 36,640 名總內戰死者中，白軍即決槍決約 7,370 人，營地飢病死亡 11,652 人); Marko Tikka (2006, 'Terrorin aika'); Jaakko Paavolainen 經典三部曲研究。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Memorial Database] 芬蘭政府在1998–2003年啟動國家級歷史調查項目，為1918年內戰中每一位死難者建立了包含姓名、死因與埋葬地的全數字化公開檔案庫。`


### [EVT-1919-RUS-002] 蘇維埃俄國「去哥薩克化」肉體消滅運動 (Decossackization (Raskazachivaniye))
* **起止年份**：1919 – 1920
* **地理位置**：俄羅斯頓河、庫班、捷列克哥薩克地區 (Soviet Russia) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `500,000` 人 / 高標 `1,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,872,000,000` 人
  * **2026年當代等效規模**：**`2,176,816` 人** (放縮係數：4.35x)
  * **區域人口衝擊率**：**`16.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 俄共中央簽署秘密通令，將哥薩克族群定性為'反革命階級'，下令實施全面肉體消滅。布爾什維克契卡部隊推進頓河地區，就地集體處決所有曾服役哥薩克軍官與男性，焚毀數百座哥薩克村落（Stanitsa），沒收全部糧食引發飢荒並強迫剩餘婦孺流放，致使頓河哥薩克人口直接消亡三分之一以上。
* **學術文獻引用摘要 (`sources_summary`)**：
  Nicolas Werth (1999, 《共產主義黑皮書》); Peter Holquist (1997, 'Conduct Merciless Mass Terror': Decossackization on the Don, 1919, Cahiers du Monde russe); 俄共（布）中央組織局1919年1月24日絕密秘密通令（斯維爾德洛夫簽署：'對全體哥薩克上層實施無情的大規模恐怖'）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯時期該秘密指令被列為最高機密，相關批判直至1990年代俄羅斯聯邦最高蘇維埃通過《關於平反哥薩克法》始正式解密與官方承認過失。`


### [EVT-1920-RUS-003] 坦波夫農民起義蘇俄軍隊毒氣鎮壓與人質營慘劇 (Tambov Rebellion Chemical Weapons Suppression and Hostage Camps)
* **起止年份**：1920 – 1921
* **地理位置**：蘇俄坦波夫省及伏爾加河下游 (Tambov Governorate, Soviet Russia) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `150,000` 人 / 中標基準 `180,000` 人 / 高標 `240,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,890,000,000` 人
  * **2026年當代等效規模**：**`776,190` 人** (放縮係數：4.31x)
  * **區域人口衝擊率**：**`6.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 為抵抗戰時共產主義糧食強徵餘糧徵集制，坦波夫數萬農民爆發起義。紅軍指揮官圖哈切夫斯基調動十萬重兵、裝甲車及炮兵，在人類歷史上首次由國家正規軍對本國平民使用化學毒氣（氯氣砲彈）攻擊森林隱蔽區；同時建立七所大型集中營，將起義農民全家（含哺乳期嬰兒）作為人質關押，成批公開槍決人質並縱火焚毀數十個村莊。
* **學術文獻引用摘要 (`sources_summary`)**：
  Richard Pipes (1994, 'Russia Under the Bolshevik Regime'); 圖哈切夫斯基與安東諾夫-奧夫謝延科1921年6月12日第0116號全權委員會作戰命令（明文下令使用氯氣彈'徹底清洗森林'）; 俄羅斯國家軍事檔案館（RGVA）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯歷史學長年將其抹黑為'安東諾夫富農叛亂'並徹底抹除使用化學武器之記錄；1990年代解密之圖哈切夫斯基簽署的毒氣作戰命令原件目前陳列於莫斯科歷史展覽中。`


### [EVT-1921-RUS-004] 蘇俄伏爾加河大饑荒 (Povolzhye Famine (Russian Famine of 1921–1922))
* **起止年份**：1921 – 1922
* **地理位置**：蘇俄伏爾加河沿岸、烏拉爾及烏克蘭東部 (Soviet Russia) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `4,000,000` 人 / 中標基準 `5,000,000` 人 / 高標 `6,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`1,908,000,000` 人
  * **2026年當代等效規模**：**`21,357,442` 人** (放縮係數：4.27x)
  * **區域人口衝擊率**：**`16.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 內戰期間列寧政權實施嚴厲的'餘糧徵集制'，徵糧隊強行搜繳農民所有口糧與來年播種種子，徹底破壞了農民生產積極性。乾旱來臨時，農村毫無儲備糧食，伏爾加河流域三千萬人陷入毀滅性飢荒，出現極端人相食現象；若非赫伯特·胡佛領導之美國救濟總署（ARA）緊急運送物資挽救上千萬人，死亡規模將成倍擴大。
* **學術文獻引用摘要 (`sources_summary`)**：
  Bertrand M. Patenaude (2002, 'The Big Show in Bololand: The American Relief Expedition to Soviet Russia in the Famine of 1921', Stanford Univ Press); 赫伯特·胡佛美國救濟總署 (ARA 檔案); 馬克西姆·高爾基公開求援信; 蘇俄中央全權委員會報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 列寧罕見地允許高爾基向資本主義世界公開求援，外國記者與ARA救濟隊留下了大量死者照片、醫療救濟登記冊與口述調查，具有極高透明度與學術共識。`


### [EVT-1928-LBY-001] 義大利法西斯平定利比亞與昔蘭尼加集中營 (Italian Pacification of Libya and Cyrenaica Concentration Camps)
* **起止年份**：1928 – 1932
* **地理位置**：義屬利比亞昔蘭尼加高原至沙漠 (Cyrenaica, Italian Libya) `[ISO-3: LBY / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `60,000` 人 / 中標基準 `80,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,034,000,000` 人
  * **2026年當代等效規模**：**`320,551` 人** (放縮係數：4.01x)
  * **區域人口衝擊率**：**`35.5556%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 墨索里尼指派格拉齊亞尼元帥鎮壓奧馬爾·穆赫塔爾領導的抵抗運動，對昔蘭尼加游牧民族推行系統性人口清除。法西斯軍隊修築數百公里鐵絲網封鎖埃及邊境，屠宰全境逾九成牲畜，並將十一萬貝都因平民強制驅趕進索盧格（Soluch）等十六座沙漠集中營，高達半數營地平民死於飢餓、傷寒與處決。
* **學術文獻引用摘要 (`sources_summary`)**：
  Angelo Del Boca (1986, 'Gli italiani in Libia'); Ali Abdullatif Ahmida (2020, 'Genocide in Libya: Shar, a Hidden Colonial History', Routledge); 魯道夫·格拉齊亞尼元帥軍事報告; 義大利外交部解密檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 戰後義大利政府長期宣傳'義大利好人'（Italiani brava gente）的神話，刻意抹除法西斯在非洲殖民地之暴行；格拉齊亞尼回憶錄亦刪除集中營死亡統計，直至2008年義大利總理貝魯斯柯尼始向利比亞正式道歉並簽署賠償條約。`


### [EVT-1930-KAZ-001] 哈薩克大饑荒 (阿夏爾希里克) (Kazakh Famine (Asharshylyq))
* **起止年份**：1930 – 1933
* **地理位置**：哈薩克蘇維埃社會主義自治共和國 (Soviet Union) `[ISO-3: KAZ / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,300,000` 人 / 中標基準 `1,500,000` 人 / 高標 `1,750,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,070,000,000` 人
  * **2026年當代等效規模**：**`5,905,797` 人** (放縮係數：3.94x)
  * **區域人口衝擊率**：**`37.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林政權指派戈洛謝金（Filipp Goloshchyokin）強行推行遊牧民強制定居化與牲畜集體化徵收。短短兩年間境內八成牲畜遭強徵或屠宰，游牧民族賴以生存的生計徹底斷絕，哈薩克族人口銳減逾三分之一，為蘇聯集體化時期人口比例損失最高之民族。
* **學術文獻引用摘要 (`sources_summary`)**：
  Sarah Cameron (2018, 'The Hungry Steppe: Famine, Violence, and the Making of Soviet Kazakhstan', Cornell Univ Press); Niccolò Pianciola (2001); 蘇聯政治局哈薩克定居化絕密檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯官方長年對哈薩克草原大饑荒保持完全沉默；哈薩克獨立後始解密國家檔案，惟大批越境逃往中國新疆或中亞其他地區途中死難者無完整統計。`


### [EVT-1930-SUN-002] 蘇聯消滅富農運動與強制流放特別定居點慘劇 (Soviet Dekulakization and Special Settlements Democide)
* **起止年份**：1930 – 1933
* **地理位置**：蘇聯全境（西伯利亞、烏拉爾、哈薩克及北方邊區）(Soviet Union) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `530,000` 人 / 中標基準 `700,000` 人 / 高標 `1,200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,070,000,000` 人
  * **2026年當代等效規模**：**`2,756,039` 人** (放縮係數：3.94x)
  * **區域人口衝擊率**：**`0.4667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林發起'作為階級消滅富農'的運動，將超過180萬名被劃為'富農'（Kulak）的農民及其家眷剝奪全部財產，用悶罐火車強行流放至西伯利亞原始森林、北極凍原及哈薩克荒漠的'特別定居點'。在毫無口糧、住房與保暖工具的極端環境下強制拓荒（如臭名昭著的納濟諾島食人慘劇Nazino tragedy），導致數十萬婦女、兒童與老人死於凍餓、壞血病與傷寒。
* **學術文獻引用摘要 (`sources_summary`)**：
  Lynne Viola (2007, 'The Unknown Gulag: The Lost World of Stalin's Special Settlements', Oxford Univ Press); Nicolas Werth (2006, 'Cannibal Island: Fatal Death in a Siberian Gulag'); 俄羅斯解密國家檔案館 (GARF) 與內務部OGPU特別定居點秘密月報; 紀念學會 (Memorial)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯時期特別定居點死亡率統計被列為絕密國家檔案；蘇聯解體後俄羅斯國家檔案館解密了OGPU內部統計（已確認登記入冊的死亡人數達38.9萬人），學界考量運送途中死亡與未登載黑數普遍認定死亡在50萬至120萬人之間。`


### [EVT-1932-SLV-001] 薩爾瓦多農民大屠殺（La Matanza） (La Matanza (The 1932 Salvadoran Peasant Massacre))
* **起止年份**：1932
* **地理位置**：薩爾瓦多西部伊薩爾科、松索納特 (El Salvador) `[ISO-3: SLV / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `20,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,100,000,000` 人
  * **2026年當代等效規模**：**`77,619` 人** (放縮係數：3.88x)
  * **區域人口衝擊率**：**`1.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在咖啡價格崩盤引發原住民共產黨農民起義後，獨裁將軍馬丁內斯（Maximiliano Hernández Martínez）派遣軍隊與大地主民兵實施徹底的種族與政治滅絕。軍隊在西部各城鎮將所有穿著原住民傳統服裝（皮皮爾族Pipil）、攜帶柴刀或具原住民外貌特徵的男性平民成批用卡車運至墓地機槍掃射，導致皮皮爾原住民語言與服飾文化在數年內被迫徹底消亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Thomas Anderson (1971, 'Matanza: El Salvador's Communist Revolt of 1932'); Jeffrey L. Gould & Aldo Lauria-Santiago (2008, 'To Rise in Darkness: Revolution, Repression, and Memory in El Salvador', Duke Univ Press); 薩爾瓦多國防部鎮壓日誌。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Cultural Extinction Dossier] 屠殺後倖存原住民為求保命完全放棄母語納瓦特語並丟棄傳統服飾改說西班牙語；薩爾瓦多總統毛里西奧·富內斯於2010年代表國家正式向原住民社群道歉。`


### [EVT-1932-UKR-001] 蘇聯烏克蘭大饑荒 (霍洛多莫) (Holodomor (Soviet Famine in Ukraine))
* **起止年份**：1932 – 1933
* **地理位置**：烏克蘭蘇維埃社會主義共和國及庫班地區 (Soviet Union) `[ISO-3: UKR / 大洲: Europe]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `3,500,000` 人 / 中標基準 `3,900,000` 人 / 高標 `5,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,100,000,000` 人
  * **2026年當代等效規模**：**`15,135,714` 人** (放縮係數：3.88x)
  * **區域人口衝擊率**：**`12.1875%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林政權為加速農業集體化與粉碎烏克蘭民族主義自主意識，在歉收背景下強行制定不可完成的糧食徵收配額。當局頒布「五支麥穗法」槍決私藏穀物之飢民，並出動國家安全部隊（OGPU）徹底封鎖村落邊界，禁止飢民外出逃荒，導致數百萬農民慘遭活活餓死。
* **學術文獻引用摘要 (`sources_summary`)**：
  Robert Conquest (1986, 'The Harvest of Sorrow'); Timothy Snyder (2010, 'Bloodlands: Europe Between Hitler and Stalin'); Anne Applebaum (2017, 'Red Famine'); 烏克蘭國家科學院人口統計學會 (Demographic Institute of NASU, 2015 專題報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯政府嚴格禁止在任何公開出版物中使用「飢荒」字眼，1937年蘇聯人口普查因揭露烏克蘭人口大規模銳減而遭史達林下令銷毀並處決統計局專家，直至蘇聯解體後烏克蘭安全局（SBU）解密克格勃檔案方告水落石出。`


### [EVT-1935-ETH-003] 第二次義衣戰爭法西斯芥子毒氣戰與平民大屠殺 (Second Italo-Ethiopian War Mustard Gas Attacks and Yekatit 12)
* **起止年份**：1935 – 1937
* **地理位置**：衣索比亞全境（阿迪斯阿貝巴、德布雷利巴諾斯修道院等）(Ethiopia) `[ISO-3: ETH / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `250,000` 人 / 中標基準 `350,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,160,000,000` 人
  * **2026年當代等效規模**：**`1,320,602` 人** (放縮係數：3.77x)
  * **區域人口衝擊率**：**`3.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 巴多格里奧與格拉齊亞尼元帥獲墨索里尼明令授權，動用數百噸劇毒芥子氣（Mustard Gas）由空軍進行大面積噴灑，摧毀村莊河流農田並毒殺無防護之平民。1937年格拉齊亞尼遇刺未遂後發動'葉卡蒂特12'（Yekatit 12）報復大屠殺，黑衫軍在首都三天內屠殺三萬平民，並在德布雷利巴諾斯將數百名修士與神學生集體處決。
* **學術文獻引用摘要 (`sources_summary`)**：
  Ian Campbell (2017, 'The Addis Ababa Massacre: Italy's National Shame'); Angelo Del Boca (2005, 'I gas di Mussolini'); 國際聯盟（League of Nations 1936 化學武器調查委員會記錄）; 海爾·塞拉西一世向國聯之著名抗告演講。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / International Inaction] 儘管國際聯盟完整記錄了化武照片與受害者潰爛傷情，但英法等國出於對德地緣政治考量拒絕對義實施石油禁運與軍事制裁；戰後無任何義大利軍事將領因此戰爭罪行受到審判。`


### [EVT-1936-ESP-001] 西班牙佛朗哥白色恐怖與內戰政治清洗 (Spanish Civil War and Francoist White Terror Executions)
* **起止年份**：1936 – 1950
* **地理位置**：西班牙 (Spain) `[ISO-3: ESP / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `150,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,180,000,000` 人
  * **2026年當代等效規模**：**`560,780` 人** (放縮係數：3.74x)
  * **區域人口衝擊率**：**`0.6%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 佛朗哥叛軍在內戰期間及取得政權後，對共和派支持者、無政府主義者、社會主義者、巴斯克及加泰隆尼亞分離主義者展開長達十餘年的系統性政治清洗，在路邊、教堂後院、牧場以秘密審判或無審判方式就地處決，遺體棄入路邊壕溝或萬人坑（Fosas Comunes）；超過30萬西班牙人被強制徵調至法西斯勞改營（Batallones de Trabajadores）服勞役。
* **學術文獻引用摘要 (`sources_summary`)**：
  Paul Preston (2012, 'The Spanish Holocaust: Inquisition and Extermination in Twentieth-Century Spain', W.W. Norton); 西班牙歷史記憶法（2007年）及ARMH協會墓葬發掘報告; 胡立奧・羅德里戈（Julio Rodrigo）量化研究（估算法西斯派直接處決約13萬人）; 聯合國工作組強迫失蹤報告（西班牙存有全球第二多之強迫失蹤案例，次於柬埔寨）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 佛朗哥獨裁長達36年期間所有相關討論被嚴格禁止；1977年《遺忘法》（Ley de Amnistía）事實上封存了對法西斯暴行的司法追訴，2023年「民主記憶法」始重開部分墓葬調查；聯合國人權機制多次批評西班牙對二戰後執政期清洗記錄的持續掩蓋。`


### [EVT-1937-CHN-001] 南京大屠殺 (Nanjing Massacre)
* **起止年份**：1937 – 1938
* **地理位置**：中國南京及其周邊 (Republic of China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `250,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`926,136` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`25.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 侵華日軍第6師團、第16師團等部隊攻佔中華民國首都南京後，在松井石根等指揮下，展開長達六週之組織性暴行。日軍對解除武裝之戰俘進行集體機槍掃射與活埋，並在市內挨家挨戶搜捕平民實施無差別屠殺、大規模強姦（估計2-8萬名女性受害）與縱火毀城。
* **學術文獻引用摘要 (`sources_summary`)**：
  遠東國際軍事法庭（IMTFE）判決書（認定死者逾20萬人）；南京審判戰犯軍事法庭（認定死者達30萬人）；約翰·拉貝（John Rabe）日記；松井石根與日本軍方陣中日記；笠原十九司（日本現代史研究會）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 日本軍部在戰敗投降前下達「徹底燒毀所有涉暴檔案」之軍令；戰後日本右翼政客與歷史修正主義學者長期否認大屠殺事實或將死傷人數壓低至數千人，中日學術界在統計口徑上存在長期論戰。`


### [EVT-1937-DOM-001] 多明尼加「香菜大屠殺」（海地移民種族清洗） (Parsley Massacre (Haitian Massacre in Dominican Republic))
* **起止年份**：1937
* **地理位置**：多明尼加共和國北部邊境 (Dominican Republic) `[ISO-3: DOM / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `17,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`62,977` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`28.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 獨裁者特魯希略（Rafael Trujillo）下令多明尼加軍隊與平民民兵，在3至5日內以砍刀與槍枝屠殺聚居於多明尼加北部邊境之海地移民與多世代混血農民。士兵以受害者能否正確發音西班牙語「香菜」（perejil）作為即地判決族裔歸屬的生死測試，其種族清洗性質得到廣泛學術認定。
* **學術文獻引用摘要 (`sources_summary`)**：
  Lauren Derby (1994, 'Haitians, Magic, and Money', Comparative Studies in Society and History); Richard Turits (2002, 'A World Destroyed, A Nation Imposed', HAHR); Michele Wucker (1999, 'Why the Cocks Fight'); 海地政府與多明尼加政府1938年外交協議文件（多明尼加支付 72.5 萬美元「賠償」海地）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 特魯希略政府事後否認屠殺之系統性國家性質，對外稱係「自發民眾衝突」；多明尼加官方檔案在後續獨裁統治數十年間遭到人為管控，確切死亡人數至今因缺乏獨立法醫記錄而存在爭議。`


### [EVT-1937-JPN-001] 日軍731部隊人體實驗與細菌戰 (Unit 731 Human Experimentation and Biological Warfare)
* **起止年份**：1937 – 1945
* **地理位置**：中國哈爾濱平房及華中、浙贛地區 (Manchukuo & Occupied China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `300,000` 人 / 高標 `400,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`1,111,364` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`0.6%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 石井四郎指揮的關東軍第731部隊在平房基地以「圓木」（Maruta）為代號，對中、蘇、朝平民及戰俘實施活體解剖、凍傷試驗、毒氣試驗及鼠疫/霍亂感染等極限反人類暴行；日軍更在浙贛、常德等地投擲染疫跳蚤實施細菌戰，引發沿線平民大規模鼠疫流行死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Sheldon H. Harris (1994, 'Factories of Death'); 伯力審判（Khabarovsk War Crime Trials 1949 庭審紀錄）; 金成民等《侵華日軍第七三一部隊罪證集》; 美國解密德特里克堡（Fort Detrick）希爾報告（Hill Report）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 戰後美國麥克阿瑟總部為獲取細菌戰軍事數據，與石井四郎等戰犯達成免予起訴之秘密交易；日本政府在撤退前炸毀基地並焚燒全部實驗名冊，長年對731部隊罪證消極應對。`


### [EVT-1937-RUS-005] 蘇聯大清洗「波蘭行動」民族大清洗 (Polish Operation of the NKVD (Order No. 00485))
* **起止年份**：1937 – 1938
* **地理位置**：蘇聯全境（白俄羅斯、烏克蘭、列寧格勒等）(Soviet Union) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `111,091` 人 / 中標基準 `120,000` 人 / 高標 `140,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`444,545` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 內務人民委員部葉若夫簽署第00485號命令，指控蘇聯境內波蘭裔居民均為'波蘭軍事組織'（POW）間諜。NKVD透過電話簿與戶籍名冊搜捕所有具波蘭姓氏者，由'雙人小組'（Dvoika）進行流水線式缺席審判，短短一年內判處近14萬人，其中高達八成（111,091人）直接後腦開槍處決，為大清洗中致死率最高的單一族裔屠殺。
* **學術文獻引用摘要 (`sources_summary`)**：
  NKVD第00485號絕密行動命令檔案; Terry Martin (2001, 'The Affirmative Action Empire', 稱其為現代史上首場國家針對特定族裔的大規模清洗); 紀念學會 (Memorial 核實111,091名死者姓名處決冊); Timothy Snyder (2010, 'Bloodlands').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 俄羅斯與烏克蘭國家安全檔案館解密了完整的審判名冊與行刑隊打卡簽字記錄，Memorial學會將每一位受害者個體生卒年全數建檔公佈於網絡。`


### [EVT-1937-SUN-001] 蘇聯大清洗與古拉格死亡勞役 (Great Purge and Gulag Fatalities)
* **起止年份**：1937 – 1938
* **地理位置**：蘇聯全境 (Soviet Union) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `950,000` 人 / 中標基準 `1,200,000` 人 / 高標 `1,600,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`4,445,455` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`0.7407%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林與內務人民委員部（NKVD）首腦葉若夫簽署第00447號命令，向蘇聯各加盟國、省份強制下達「反革命分子與富農」之處決與流放硬性指標。在「大恐怖」高峰期，國家安全機構未經正當審判秘密處決約70萬人，數十萬人因極寒、飢餓與繁重苦役死於古拉格集中營與轉運途中。
* **學術文獻引用摘要 (`sources_summary`)**：
  Memorial 人權組織（'紀念'學會解密行刑清單）；J. Arch Getty (1993, 'Victims of the Soviet Penal System'); Nicolas Werth (1999, 'The Black Book of Communism'); 俄聯邦安全局（FSB）解密NKVD第00447號命令。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 處決記錄在蘇聯時期長年被冠以「判處十年監禁且不准通信」之官方謊言隱瞞親屬；紀念學會（Memorial）於俄羅斯解密大量檔案後，近年在俄烏局勢下該組織遭俄官方撤銷登記並再度面臨檔案查閱緊縮。`


### [EVT-1937-SUN-003] 蘇聯大清洗朝鮮族遠東強制大流放 (Deportation of Koreans in the Soviet Union)
* **起止年份**：1937 – 1938
* **地理位置**：蘇聯遠東濱海邊疆區至哈薩克與烏茲別克荒漠 (Soviet Union) `[ISO-3: RUS / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `16,500` 人 / 中標基準 `25,000` 人 / 高標 `40,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,200,000,000` 人
  * **2026年當代等效規模**：**`92,614` 人** (放縮係數：3.7x)
  * **區域人口衝擊率**：**`14.2857%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林以防範日本間諜滲透為莫須有罪名，發動蘇聯歷史上首場針對整個族裔的集體全面清洗。NKVD在數週內將居住於遠東邊疆區的17.2萬名高麗人（Koryo-saram）強行塞入嚴冬的貨運火車，橫跨西伯利亞流放至哈薩克與烏茲別克未開發之鹽鹼荒地，流放途中與抵達第一年因缺乏口糧、棚屋與極端嚴寒，造成近四分之一兒童與老人悲慘死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  蘇聯人民委員會與聯共（布）中央1937年8月21日第1428-326號絕密決議（莫洛托夫與史達林簽署：'關於將朝鮮族人口從遠東邊疆區邊境地區遷出'）; German Kim (2004, 'The Deportation of 1937 as a Logical Result of Tsarist and Soviet National Policy'); 紀念學會 (Memorial); 俄羅斯解密國家檔案館 (GARF)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Declassified Stalin Decrees] 1993年俄羅斯聯邦最高蘇維埃正式通過決議平反被流放的俄羅斯高麗人；哈薩克與烏茲別克檔案館公開了鐵路專列死亡交接清單。`


### [EVT-1938-CHN-011] 重慶大轟炸（日軍對平民無差別戰略轟炸） (Bombing of Chongqing (Imperial Japanese Strategic Civilian Bombing))
* **起止年份**：1938 – 1943
* **地理位置**：中國戰時陪都重慶及成都、合川 (Chongqing, China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `24,000` 人 / 中標基準 `27,000` 人 / 高標 `32,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,220,000,000` 人
  * **2026年當代等效規模**：**`99,122` 人** (放縮係數：3.67x)
  * **區域人口衝擊率**：**`2.7%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 侵華日軍發動代號'百號作戰'等長期戰略轟炸，以徹底摧毀中國抗戰民意士氣為目標，對無有效防空武裝的重慶平民市區實施長達五年半的地毯式無差別轟炸。日軍動用燃燒彈製造市中心大火風暴（如五三、五四大轟炸），在較場口防空大隧道引發數千名躲避空襲平民窒息踐踏慘死，造成逾三萬名非戰鬥平民直接死傷。
* **學術文獻引用摘要 (`sources_summary`)**：
  重慶市大轟炸民間對日索賠團統計檔案; 中華民國戰時首都防空司令部傷亡統計呈報; 前田哲男（2006, 《戰略轟炸的始祖：重慶大轟炸》）; 侵華日軍大本營海軍航空兵作戰日誌。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Claims Dossier] 中日兩國學者與律師團聯合赴日本東京地方法院進行了長達十餘年的重慶大轟炸國家賠償訴訟，日方法院判決正式認證了日軍實施無差別轟炸平民之歷史事實。`


### [EVT-1939-DEU-003] 納粹「T4行動」強制安樂死與殘疾人滅絕計畫 (Nazi Aktion T4 Euthanasia Programme)
* **起止年份**：1939 – 1941
* **地理位置**：納粹德國及奧地利（哈特海姆、格拉芬內克等六大中心）(Nazi Germany) `[ISO-3: DEU / 大洲: Europe]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `250,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,240,000,000` 人
  * **2026年當代等效規模**：**`909,598` 人** (放縮係數：3.64x)
  * **區域人口衝擊率**：**`0.3125%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 希特勒簽署秘密授權令，由帝國總理府與醫學專家在柏林蒂爾加滕街4號（Tiergartenstraße 4）設立指揮部，對精神障礙者、癲癇患者、先天殘疾兒童及長期住院病患等'不值得活的生命'（Lebensunwertes Leben）進行系統性肉體消滅。納粹首次研發一氧化碳毒氣室與人體焚屍爐，此套工業化殺人技術與醫療人員隨後全套移植至奧斯威辛等猶太滅絕營。
* **學術文獻引用摘要 (`sources_summary`)**：
  Götz Aly (2013, 'Die Belasteten: Euthanasie 1939–1945'); Ernst Klee (1983, 'Euthanasie im NS-Staat'); 德國聯邦檔案館 (Bundesarchiv, 柏林蒂爾加滕街4號指揮中樞原始解密檔案); 紐倫堡審判醫生案件判決書; 柏林T4行動紀念館。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 因明斯特大主教馮·加倫（Clemens August Graf von Galen）等公開佈道強烈抗議，希特勒於1941年下令暫停官方公開行動，但隨後轉為更加隱蔽的'分散性安樂死'（以飢餓飲食與致死注射處死病患直至1945年戰敗），受害者病例名冊經戰後紐倫堡審判與現代德奧歷史學界完整核實。`


### [EVT-1939-DEU-004] 納粹羅姆人與辛提人種族滅絕（食人魔 / 吞噬） (Porajmos (Romani Genocide by Nazi Germany))
* **起止年份**：1939 – 1945
* **地理位置**：歐洲納粹佔領區（德國、波蘭、烏克蘭等）(Nazi-occupied Europe) `[ISO-3: DEU / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `220,000` 人 / 中標基準 `300,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,240,000,000` 人
  * **2026年當代等效規模**：**`1,091,518` 人** (放縮係數：3.64x)
  * **區域人口衝擊率**：**`30.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 納粹政權將羅姆人（吉普賽人）定性為'外來劣等種族'與反社會分子，依據紐倫堡種族法實施強制絕育與系統性圍剿。別動隊在蘇聯西部將整個羅姆大篷車營地集體就地槍殺，數萬家庭被押送至奧斯威辛比克瑙集中營'吉普賽家族營'進行門格勒殘酷雙胞胎醫學實驗並全部送入毒氣室滅絕，歐洲羅姆人口損失四分之一至一半。
* **學術文獻引用摘要 (`sources_summary`)**：
  Donald Kenrick & Grattan Puxon (1995, 'Gypsies Under the Swastika'); Guenter Lewy (2000, 'The Nazi Persecution of the Gypsies', Oxford Univ Press); 美國大屠殺紀念館 (USHMM); 德國聯邦政府1982年由總理施密特正式官方承認該種族滅絕責任。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 戰後紐倫堡審判甚至未傳召羅姆人證人，西德法庭在戰後初期拒絕向倖存者賠償並謊稱其係因治安犯罪被捕；羅姆人社群缺乏書面檔案與文字機構，使得死者名冊重建極度困難。`


### [EVT-1939-FIN-002] 蘇芬冬季戰爭蘇聯空軍平民無差別轟炸與集束炸彈襲擊 (Soviet Bombing of Helsinki and Finnish Cities during the Winter War)
* **起止年份**：1939 – 1940
* **地理位置**：芬蘭赫爾辛基、維堡、圖爾庫等主要城市 (Finland) `[ISO-3: FIN / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `1,000` 人 / 中標基準 `1,500` 人 / 高標 `2,500` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,240,000,000` 人
  * **2026年當代等效規模**：**`5,458` 人** (放縮係數：3.64x)
  * **區域人口衝擊率**：**`0.0405%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇聯紅軍未宣而戰入侵芬蘭首日，蘇聯空軍即對首都赫爾辛基無防備之平民居民區、醫院與學校投擲大量燃燒彈與早期集束炸彈（RRAB-3，蘇聯外長莫洛托夫諷刺稱其為向飢民投送的'莫洛托夫麵包籃'）。戰爭期間蘇聯轟炸機空襲芬蘭城鎮逾兩千次，直接造成上千名平民死傷、近五十萬卡累利阿平民被迫背井離鄉永久撤離家園。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際聯盟（League of Nations 1939年12月14日歷史性決議：因蘇聯侵略與轟炸平民將蘇聯開除出國際聯盟）; Carl-Fredrik Geust (2004, 'Red Stars over the Winter War'); 芬蘭國家防空司令部傷亡檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Expulsion from League of Nations] 該轟炸直接導致國際聯盟啟動公約將蘇聯正式除名，赫爾辛基市消防與警察局詳細記錄了逐一炸彈落點與死難者身份。`


### [EVT-1940-POL-001] 卡廷大屠殺（蘇聯秘密處決波蘭精英） (Katyn Massacre – Soviet NKVD Execution of Polish Officers)
* **起止年份**：1940
* **地理位置**：蘇聯（卡廷森林、加里寧、哈爾科夫等地）(Soviet Union) `[ISO-3: POL / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `21,768` 人 / 中標基準 `21,857` 人 / 高標 `22,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,260,000,000` 人
  * **2026年當代等效規模**：**`78,821` 人** (放縮係數：3.61x)
  * **區域人口衝擊率**：**`10.9285%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 1940年3至5月，依據史達林與貝利亞之NKVD指令，蘇聯秘密警察以逐一後腦射擊方式，在卡廷森林、加里寧（今特維爾）及哈爾科夫系統性處決了21,857名被俘波蘭軍官、警察、知識分子、神職人員與地主，意圖一舉斬斷波蘭未來復國之精英脊梁。此為現代最有完整記錄（含確切姓名冊）之精英種族滅絕事件之一。
* **學術文獻引用摘要 (`sources_summary`)**：
  俄羅斯聯邦1992年解密文件（葉爾欽移交波蘭政府之完整NKVD處決名單，含21,857人確切姓名）; 波蘭-蘇聯聯合歷史委員會; Anna Cienciała, Natalia Lebedeva & Wojciech Materski eds. (2007, 'Katyn: A Crime Without Punishment'); 歐洲人權法院Janowiec訴俄羅斯案判決（2013）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇聯當局長達半世紀將此案歸咎於納粹德國，於1990年由戈巴契夫首度官方承認蘇聯責任；俄羅斯至今拒絕以「種族滅絕」定性，並於2004年中止對相關肇事者之正式刑事調查，部分完整NKVD行刑命令文件仍列機密。`


### [EVT-1941-DEU-001] 納粹猶太人大屠殺 (浩劫 / 猶太大滅絕) (The Holocaust (Shoah))
* **起止年份**：1941 – 1945
* **地理位置**：歐洲納粹佔領區（德國、波蘭、蘇聯西部等）(Nazi Occupied Europe) `[ISO-3: DEU / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `5,700,000` 人 / 中標基準 `5,900,000` 人 / 高標 `6,100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,280,000,000` 人
  * **2026年當代等效規模**：**`21,089,912` 人** (放縮係數：3.57x)
  * **區域人口衝擊率**：**`62.1053%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 納粹德國在希特勒、希姆萊主導及萬湖會議部署下，動員全部國家行政、鐵路與工業機器執行「最終解決方案」（Endlösung）。納粹建立奧斯威辛、特雷布林卡等工業化滅絕營，使用齊克隆B毒氣、大規模槍決（別動隊）及奴役性飢餓，系統性消滅了全歐洲近三分之二的猶太人口。
* **學術文獻引用摘要 (`sources_summary`)**：
  Raul Hilberg (1961/1985, 'The Destruction of the European Jews'); United States Holocaust Memorial Museum (USHMM); 以色列猶太大屠殺紀念館 (Yad Vashem Database of Shoah Victims); Wolfgang Benz (1991, 'Dimension des Völkermords').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 納粹屠猶是全球記錄最詳盡的滅絕事件之一，萬湖會議紀要、集中營進出冊與紐倫堡審判證詞構成完整證據鏈；少數東歐邊境槍決死者（Holocaust by Bullets）近年由雅哈德-伊恩·烏納姆組織（Yahad-In Unum）實地挖掘核實。`


### [EVT-1941-DEU-002] 納粹飢餓計畫與蘇聯戰俘/平民大滅絕 (Nazi Hunger Plan and Extermination of Soviet Civilians)
* **起止年份**：1941 – 1944
* **地理位置**：蘇聯西部佔領區（白俄羅斯、烏克蘭及俄羅斯西部）(Nazi Occupied USSR) `[ISO-3: BLR / 大洲: Europe]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `4,200,000` 人 / 中標基準 `5,000,000` 人 / 高標 `7,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,280,000,000` 人
  * **2026年當代等效規模**：**`17,872,807` 人** (放縮係數：3.57x)
  * **區域人口衝擊率**：**`6.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 納粹糧食部長赫伯特·巴克制訂「飢餓計畫」（Der Hungerplan），明文規劃截留烏克蘭與白俄羅斯之所有農產以供應德軍本土，預定消滅東歐數千萬「多餘的斯拉夫人口」。納粹有系統地在戰俘營與包圍圈中斷絕食物，導致逾300萬蘇聯戰俘與數百萬圍城平民（如列寧格勒圍城）悲慘餓斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  Timothy Snyder (2010, 'Bloodlands'); Christian Gerlach (1998, 'Kalkulierte Morde'); Alex J. Kay (2006, 'Exploitation, Resettlement, Mass Murder'); 赫伯特·巴克（Herbert Backe）飢餓計畫國家檔案備忘錄。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 蘇聯東部前線交戰極度殘烈，大量戰俘露天圈禁於鐵絲網泥地中凍餓致死，死亡登記殘缺不全；戰後紐倫堡審判將其定性為戰爭罪核心組成部分。`


### [EVT-1941-HRV-001] 克羅埃西亞烏斯塔沙法西斯政權種族滅絕與亞塞諾瓦茨滅絕營 (Ustaše Genocide against Serbs, Jews and Roma (Jasenovac Camp))
* **起止年份**：1941 – 1945
* **地理位置**：克羅埃西亞獨立國（亞塞諾瓦茨滅絕營、波士尼亞等）(NDH / Yugoslavia) `[ISO-3: HRV / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `400,000` 人 / 高標 `600,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,280,000,000` 人
  * **2026年當代等效規模**：**`1,429,825` 人** (放縮係數：3.57x)
  * **區域人口衝擊率**：**`6.1538%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 軸心國傀儡'克羅埃西亞獨立國'元首安特·帕維里奇推行'三分之一驅逐、三分之一強迫改宗、三分之一徹底屠殺'的塞爾維亞人清洗政策。烏斯塔沙武裝在亞塞諾瓦茨建立唯一非由納粹德國親自經營的滅絕營，使用特製屠夫彎刀（'Srbosjek'割塞刀）、大鐵錘與直接拋入薩瓦河等野蠻手段，殘酷處決數十萬塞爾維亞人、猶太人、羅姆人與反法西斯克羅埃西亞人。
* **學術文獻引用摘要 (`sources_summary`)**：
  亞塞諾瓦茨紀念館官方名冊 (Jasenovac Memorial Site 核實 83,145 名個體遇害者名錄); Jozo Tomasevich (2001, 'War and Revolution in Yugoslavia: Occupation and Collaboration'); Rory Yeomans (2013, 'Visions of Annihilation', Univ of Pittsburgh Press); 美國大屠殺紀念館 (USHMM)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Contested Casualty Numbers] 戰後狄托政權曾宣稱營區死難達70萬人以爭取德國戰爭賠款，現代塞爾維亞與克羅埃西亞獨立人口學家運用微觀檔案剔除重複計算後，確立亞塞諾瓦茨營地約10萬人、全境滅絕逾40萬人之學術共識。`


### [EVT-1941-ROU-002] 羅馬尼亞安東內斯庫政權敖德薩大屠殺與德涅斯特河沿岸浩劫 (Odessa Massacre and Transnistria Holocaust by Romania)
* **起止年份**：1941 – 1944
* **地理位置**：烏克蘭敖德薩及德涅斯特河沿岸管區 (Transnistria, Romanian-occupied USSR) `[ISO-3: ROU / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `280,000` 人 / 中標基準 `300,000` 人 / 高標 `380,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,280,000,000` 人
  * **2026年當代等效規模**：**`1,072,368` 人** (放縮係數：3.57x)
  * **區域人口衝擊率**：**`75.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 羅馬尼亞獨裁者揚·安東內斯庫元帥聯手納粹入侵蘇聯後，在羅軍佔領管區德涅斯特河沿岸實施由羅馬尼亞國家獨立主導的大屠殺。在敖德薩總督府遭炸毀後，安東內斯庫下令實施恐怖報復，羅軍在港口炸藥倉庫將兩萬多名猶太人鎖入庫房淋上汽油活活燒死，並在博格達諾夫卡集中營（Bogdanovka）將四萬多名猶太難民集體射殺並焚屍除跡。
* **學術文獻引用摘要 (`sources_summary`)**：
  埃利·威瑟爾國際委員會羅馬尼亞大屠殺研究報告 (Wiesel Commission Report, 2004 官方調查確認羅馬尼亞政府消滅了28萬至38萬猶太人與羅姆人); Jean Ancel (2011, 'The History of the Holocaust in Romania', Univ of Nebraska Press); 羅馬尼亞軍事檔案館解密檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Wiesel Commission] 戰後共產黨羅馬尼亞長期將大屠殺罪責全數推給納粹德國；2004年由諾貝爾獎得主威瑟爾主持的國際歷史委員會發表權威報告，羅馬尼亞政府正式接受責任並設立國家大屠殺紀念日。`


### [EVT-1942-CHN-006] 1942年河南大饑荒與苛稅徵糧 (Henan Famine of 1942–1943)
* **起止年份**：1942 – 1943
* **地理位置**：中國河南省 (Republic of China / Henan) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500,000` 人 / 中標基準 `2,000,000` 人 / 高標 `3,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,300,000,000` 人
  * **2026年當代等效規模**：**`7,086,957` 人** (放縮係數：3.54x)
  * **區域人口衝擊率**：**`6.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在旱災蝗災疊加背景下，國民政府軍事第一戰區與地方政府為維持部隊給養，實施嚴厲之田賦徵實徵購，甚至向飢民逼索軍糧草料。軍政當局封鎖新聞並拒絕及時開倉放糧與調撥平漢鐵路疏運，導致數百萬難民在隴海鐵路沿線凍餓倒斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  白修德 (Theodore H. White, 1943 時代雜誌專題報導); 宋致新《1942：河南大饑荒》; 中華民國國史館戰時徵實徵購檔案; 曹樹基人口估算。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 國民政府戰時新聞檢查處查封刊登河南災情的《大公報》並停刊三日；白修德直接覲見蔣介石展示野狗啃食餓死災民照片後，賑災救濟始勉強啟動。`


### [EVT-1941-POL-002] 沃倫與東加利西亞波蘭人大屠殺 (Massacres of Poles in Volhynia and Eastern Galicia)
* **起止年份**：1943 – 1945
* **地理位置**：烏克蘭西部沃倫與東加利西亞 (Nazi-occupied Poland/Ukraine) `[ISO-3: UKR / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `60,000` 人 / 中標基準 `100,000` 人 / 高標 `120,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,320,000,000` 人
  * **2026年當代等效規模**：**`351,293` 人** (放縮係數：3.51x)
  * **區域人口衝擊率**：**`6.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在德軍佔領烏克蘭西部背景下，斯捷潘·班傑拉派烏克蘭起義軍（UPA）為確保戰後邊界人口純粹性，發動針對境內波蘭少數社群的種族清洗。UPA武裝在1943年7月'血腥星期天'同步突襲近百個波蘭村莊天主教堂，以斧頭、鐮刀、長鋸等農具對男女老幼進行殘暴砍殺並放火燒村，波蘭家鄉軍（AK）亦展開報復性反屠殺（造成2-3萬烏克蘭平民死亡）。
* **學術文獻引用摘要 (`sources_summary`)**：
  波蘭國家記憶研究院 (IPN 官方專題研究認定具有種族滅絕特徵); Grzegorz Motyka (2011, 'Od rzezi wołyńskiej do akcji Wisła'); Timothy Snyder (2003, 'The Reconstruction of Nations', Yale Univ Press); 波蘭議會2016年決議將7月11日定為烏克蘭民族主義者所犯種族滅絕罪行國家紀念日。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Deep Polish-Ukrainian Historiographical Tensions] 波蘭IPN建立了詳盡的遇害村莊與死者資料庫；烏克蘭獨立後將UPA視為反抗蘇聯之民族英雄，雙方政府與歷史學家就事件性質定性（種族滅絕 vs 雙向內戰悲劇）持續進行外交爭端。`


### [EVT-1943-DEU-005] 盟軍對德國城市漢堡與德勒斯登平民區地毯式燃燒彈轟炸 (Allied Firebombing of Hamburg and Dresden (Firestorms))
* **起止年份**：1943 – 1945
* **地理位置**：德國漢堡、德勒斯登 (Nazi Germany) `[ISO-3: DEU / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `60,000` 人 / 中標基準 `75,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,320,000,000` 人
  * **2026年當代等效規模**：**`263,470` 人** (放縮係數：3.51x)
  * **區域人口衝擊率**：**`3.75%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英國皇家空軍轟炸機司令部指揮官哈里斯（'轟炸機哈里斯'）推行'區域轟炸'政策，以削弱平民士氣為戰略目標，故意對市中心密集木造民宅區投擲大量高爆炸彈揭開屋頂、隨後密集投擲燃燒彈製造人工火焰風暴（Firestorm）。漢堡（蛾摩拉行動）與德勒斯登防空洞內數萬名非作戰婦孺在攝氏千度高溫下窒息融化或遭烈焰焚斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  Frederick Taylor (2004, 'Dresden: Tuesday, 13 February 1945'); 德勒斯登歷史學家委員會 (Dresden Historians' Commission, 2010 官方調查核實德勒斯登死亡約2.5萬人); Keith Lowe (2007, 'Inferno: The Devastation of Hamburg, 1943'); 英國皇家空軍轟炸機司令部作戰日誌。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 該事件在戰後西方倫理與軍事史學引發極大道德爭論；冷戰期間蘇聯與納粹餘孽曾誇大德勒斯登死亡為20萬人，2010年由各國歷史學家組成的獨立委員會調閱全部墳場與警察登記確認為2.5萬人（漢堡約4.2萬人）。`


### [EVT-1943-IND-001] 1943年孟加拉大饑荒 (Bengal Famine of 1943)
* **起止年份**：1943 – 1944
* **地理位置**：英屬印度孟加拉省 (British Raj / Bengal) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `2,100,000` 人 / 中標基準 `3,000,000` 人 / 高標 `3,800,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,320,000,000` 人
  * **2026年當代等效規模**：**`10,538,793` 人** (放縮係數：3.51x)
  * **區域人口衝擊率**：**`4.9751%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 日軍佔領緬甸切斷大米進口後，英國戰時內閣（首相邱吉爾主導）實施焦土「抗戰物資拒止政策」（Denial Policy），強行徵收摧毀沿海數萬艘船隻與庫存糧食。戰時軍事優先政策挪用所有航運船舶儲備歐洲物資，並拒絕調撥澳洲小麥救濟孟加拉，引發城市街頭數百萬難民活活餓死與瘟疫肆虐。
* **學術文獻引用摘要 (`sources_summary`)**：
  Amartya Sen (1981, 'Poverty and Famines: An Essay on Entitlement and Deprivation'); Madhusree Mukerjee (2010, 'Churchill's Secret War'); Cormac Ó Gráda (2009, 'Famine: A Short History'); 英國殖民官方《飢荒調查委員會報告》（Woodhead Commission, 1945）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 英國戰時新聞審查機構嚴禁印度報刊刊登餓死者橫屍街頭照片，《政治家報》（The Statesman）主編伊恩·史蒂芬斯（Ian Stephens）頂住吊銷執照壓力刊發照片始震撼國際；邱吉爾戰時內閣部分拒絕救援會議紀錄直至半世紀後始解密。`


### [EVT-1944-POL-003] 華沙起義納粹鎮壓與沃拉大屠殺 (Warsaw Uprising German Democide and Wola Massacre)
* **起止年份**：1944
* **地理位置**：波蘭華沙市（沃拉區、奧霍塔區等）(Warsaw, Occupied Poland) `[ISO-3: POL / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `150,000` 人 / 中標基準 `180,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,352,500,000` 人
  * **2026年當代等效規模**：**`623,592` 人** (放縮係數：3.46x)
  * **區域人口衝擊率**：**`18.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 波蘭家鄉軍在華沙發動起義後，希特勒與希姆萊下達徹底毀滅城市的軍令：'所有居民必須被處決，不得留俘虜，華沙必須被夷為平地'。黨衛軍親衛隊動用惡名昭彰的重刑犯組成的狄爾勒旺格爾旅與卡明斯基旅進駐市中心，在沃拉區（Wola Massacre）逐街逐戶槍殺4萬至5萬名醫院病患、醫生、婦女與嬰兒，隨後以工兵噴火器有系統地摧毀了華沙85%以上的建築物。
* **學術文獻引用摘要 (`sources_summary`)**：
  Norman Davies (2003, 'Rising '44: The Battle for Warsaw'); 波蘭國家記憶研究院 (IPN 沃拉大屠殺專題調查); Alexandra Richie (2013, 'Warsaw 1944: Hitler, Himmler, and the Warsaw Uprising'); 狄爾勒旺格爾旅與卡明斯基旅作戰日誌。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Urban Reconstruction Archives] 華沙起義博物館與波蘭IPN完整核實了逐一街區集體處決坑的死難名冊，蘇聯紅軍隔維斯瓦河岸觀望坐視起義遭鎮壓之政治冷血亦被史學界完整記錄。`


### [EVT-1944-RUS-006] 蘇聯強迫流放車臣人與印古什人（扁豆行動） (Deportation of Chechens and Ingush (Operation Lentil / Aardakh))
* **起止年份**：1944
* **地理位置**：俄羅斯北高加索至哈薩克、吉爾吉斯 (Soviet Union) `[ISO-3: RUS / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `125,000` 人 / 中標基準 `150,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,352,500,000` 人
  * **2026年當代等效規模**：**`519,660` 人** (放縮係數：3.46x)
  * **區域人口衝擊率**：**`30.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 史達林與貝利亞以通敵為莫須有罪名，動用10萬軍警在短短七天內將全體車臣與印古什族人（近50萬人）包圍押入嚴冬中的無暖氣貨運悶罐車流放中亞荒漠。在海巴赫村（Khaibakh），因大雪封山無法轉運，NKVD將700多名老人幼童鎖入馬廄直接放火活活燒死；流放途中與抵達初期四分之一至三分之一人口死於嚴寒、飢餓與斑疹傷寒。
* **學術文獻引用摘要 (`sources_summary`)**：
  歐洲議會2004年決議將該流放認定為種族滅絕; Pavel Polian (2004, 'Against Their Will: The History and Geography of Forced Migrations in the USSR'); NKVD貝利亞呈報史達林之流放執行電報檔案; 俄羅斯國家檔案館 (GARF)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / State Archives] 蘇聯解體後俄羅斯與哈薩克檔案館公開了NKVD專列死亡每日匯報電文；歐洲議會於2004年正式認定其構成1948年聯合國公約定義之種族滅絕罪。`


### [EVT-1944-UKR-002] 蘇聯克里米亞韃靼人強制大流放（流亡慘劇） (Deportation of Crimean Tatars (Sürgünlik))
* **起止年份**：1944
* **地理位置**：克里米亞至烏茲別克及烏拉爾 (Soviet Union) `[ISO-3: UKR / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `34,000` 人 / 中標基準 `45,000` 人 / 高標 `110,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,352,500,000` 人
  * **2026年當代等效規模**：**`155,898` 人** (放縮係數：3.46x)
  * **區域人口衝擊率**：**`22.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 二戰德軍撤離克里米亞後，史達林下令將島上全體克里米亞韃靼人（近二十萬人，多為婦女、兒童與傷殘老兵）在三日內驅逐出祖居地。受害者被鎖於悶罐車內長達數週穿越歐亞大陸，不給水糧，棄屍鐵道旁；流放到烏茲別克棉田與採礦特別定居點後，因惡劣生活條件導致超過20%至46%的人口在最初數年內非正常死亡，全島韃靼地名與古蹟遭抹除韃靼痕跡。
* **學術文獻引用摘要 (`sources_summary`)**：
  烏克蘭最高拉達2015年立法認定為種族滅絕; Greta Uehling (2004, 'Beyond Memory: The Crimean Tatars' Deportation and Return', Palgrave); 烏茲別克特別定居點解密檔案; 克里米亞韃靼人民族運動檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Parliamentary Resolutions] 蘇聯政府於1989年宣布該驅逐為非法犯罪，烏克蘭、拉脫維亞、立陶宛及加拿大國會已先後立法正式認定其為種族滅絕。`


### [EVT-1944-VNM-001] 日治越南大饑荒 (Vietnamese Famine of 1944–1945 (Japanese Occupation Famine))
* **起止年份**：1944 – 1945
* **地理位置**：法屬印度支那北越（東京及安南北部）(French Indochina / Vietnam) `[ISO-3: VNM / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `400,000` 人 / 中標基準 `1,000,000` 人 / 高標 `2,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,352,500,000` 人
  * **2026年當代等效規模**：**`3,464,400` 人** (放縮係數：3.46x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 日本佔領當局強制要求北越農民將稻田改種黃麻、棉花等軍事工業作物，同步實施嚴厲糧食強徵配給制；法屬殖民行政機構同期以儲備應付日軍需求，兩層剝奪下導致1944年冬至1945年春「連座糧食缺口」形成。加以盟軍轟炸破壞鐵路運輸，北越糧食無法南調，數百萬農民在短短數月內慘死街頭，屍體遍野。
* **學術文獻引用摘要 (`sources_summary`)**：
  Nola Cooke, Tana Li & James A. Anderson eds. (2011, 'The Mekong's Past and Present'); Van Nguyen-Marshall (2008); 胡志明（Ho Chi Minh 1945年宣布獨立演講引述「兩百萬人餓死」）; 法國殖民當局稻米徵購令檔案（解密）; UCDP 非戰鬥人員死亡資料庫。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 日占與法殖民雙重行政體系下，北越無完整人口死亡登記；戰後胡志明政府以「200萬」為象徵性政治數字，學術界一般依據1943–1946年人口普查差額採用40-200萬之廣闊區間，精確死亡數目至今未能取得跨國學術共識。`


### [EVT-1945-DEU-003] 二戰後德裔平民大驅逐與報復性屠殺 (Expulsion of Germans after WWII and Associated Massacres)
* **起止年份**：1945 – 1950
* **地理位置**：波蘭、捷克斯洛伐克、匈牙利、南斯拉夫等東歐諸國 (Eastern Europe) `[ISO-3: DEU / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `600,000` 人 / 高標 `2,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`2,050,314` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`4.2857%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 依據1945年《波茨坦協定》，波蘭、捷克（蘇台德）等東歐國家在蘇聯軍事掌控下，對境內14-16百萬德裔（Volksdeutsche）實施大規模強制驅逐。驅逐過程中伴隨有組織的報復性屠殺（如布爾諾死亡行軍、科赫廷事件）、搶劫、強姦及嚴冬徒步驅離等暴行，造成大批老弱婦孺在轉移途中因凍餓、疾病及直接暴力死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Rüdiger Overmans (德國歷史學家，估算驅逐及相關死亡 50–60 萬); Matthias Beer (2011, Bundeszentrale für politische Bildung); Alfred de Zayas (1994, 'A Terrible Revenge'); Detlef Brandes (2001); 德意志聯邦共和國《東德問題聯邦大臣辦公室報告》(1950s 西德官方調查報告，聲稱逾200萬人死亡，現代史學家多認為高估)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 此事件政治敏感性極高，德國與東歐各國間歷史賠償與領土爭議使客觀記錄長期受政治因素干擾；1950年代西德官方報告之200萬死亡數字為後世學術界廣泛質疑高估，現代人口學研究將超額死亡數縮減至50-60萬區間。`


### [EVT-1945-DZA-002] 法國塞提夫與蓋勒馬平民大屠殺 (Sétif and Guelma Massacre (Algeria))
* **起止年份**：1945
* **地理位置**：阿爾及利亞塞提夫、蓋勒馬及海拉塔 (French Algeria) `[ISO-3: DZA / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `6,000` 人 / 中標基準 `20,000` 人 / 高標 `45,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`68,344` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`2.0%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 1945年5月8日歐戰勝利紀念日當天，阿爾及利亞塞提夫爆發和平遊行要求獨立，法國憲兵向展示阿爾及利亞旗幟的示威者開槍引發騷亂。法國殖民當局與歐洲定居者武裝隨後展開報復性大屠殺，調動巡洋艦艦砲轟擊沿海村莊、空軍戰機俯衝掃射平民聚落，並使用石灰窯集體焚化死難者遺體掩蓋暴行，點燃了阿爾及利亞獨立戰爭之烈火。
* **學術文獻引用摘要 (`sources_summary`)**：
  Jean-Louis Planche (2006, 'Sétif 1945: histoire d'un massacre annoncé'); 法國駐阿爾及利亞大使圖巴爾（Bernard Bajolet）2008年官方承認'不可原諒的悲劇'; 圖比埃將軍（Général Tubert）官方調查報告; 阿爾及利亞官方採信4.5萬人數字。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 法國當局在事後數十年嚴密封鎖軍方作戰與死傷檔案，長年將死亡人數壓低至千餘人；法國駐阿大使直至2008年始公開定性為'集體屠殺'，但法國官方迄今拒絕作出全面國家賠償。`


### [EVT-1945-GRC-001] 希臘內戰「白色恐怖」清洗與馬克羅尼索斯島集中營 (Greek Civil War White Terror and Makronisos Camp Internees)
* **起止年份**：1945 – 1949
* **地理位置**：希臘全境（馬克羅尼索斯島、伯羅奔尼撒等）(Greece) `[ISO-3: GRC / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `40,000` 人 / 中標基準 `50,000` 人 / 高標 `80,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`170,860` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`0.6849%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 二戰軸心國佔領結束與《瓦爾基扎協定》簽署後，英美支持的希臘保皇派政府與極右翼民兵（X組織等）對前抵抗武裝民族解放陣線（EAM/ELAS）成員及左翼平民發動大規模'白色恐怖'清算。軍政府在荒涼的馬克羅尼索斯島（Makronisos）等地設立'再教育集中營'，實施系統性水刑、連續數日站立酷刑與強迫簽署'悔過書'，導致數萬名政治犯與平民遭非審判處決、折磨致死或流放。
* **學術文獻引用摘要 (`sources_summary`)**：
  Mark Mazower (2000, 'After the War Was Over: Reconstructing the Family, Nation, and State in Greece, 1943–1960', Princeton Univ Press); Polymeris Voglis (2002, 'Becoming a Subject: Political Prisoners during the Greek Civil War', Berghahn Books); David H. Close (1995, 'The Origins of the Greek Civil War'); 國際紅十字會 (ICRC 馬克羅尼索斯島探視報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 希臘戰後歷任保守派政府長年將內戰定義為單方面的'匪幫戰爭'（Symmoritopolemos），警方將數萬名左翼家庭列入'社會信念證書'（Pistopoiitiko Koinonikon Fronimaton）黑名單剝奪就業權；直至1989年希臘議會始正式通過立法承認內戰雙方歷史並下令焚毀數百萬份國家安全政治檔案。`


### [EVT-1945-JPN-002] 廣島與長崎原子彈平民核爆慘劇 (Atomic Bombings of Hiroshima and Nagasaki)
* **起止年份**：1945
* **地理位置**：日本廣島市、長崎市 (Japan) `[ISO-3: JPN / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `129,000` 人 / 中標基準 `170,000` 人 / 高標 `226,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`580,922` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`28.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美軍B-29轟炸機在廣島與長崎投下'小男孩'鈾彈與'胖子'鈈彈。原子彈在人口稠密市中心千米高空爆炸，數千度超高溫熱輻射、極端衝擊波與致命急性核輻射瞬間將十萬以上非戰鬥平民氣化或碳化，其後黑雨與急性放射病、白血病奪去數以萬計倖存婦孺之生命，成為人類歷史上唯一在實戰中遭受核毀滅之平民慘劇。
* **學術文獻引用摘要 (`sources_summary`)**：
  理化學研究所與廣島市/長崎市官方原爆死沒者名冊; 放射線影響研究所 (RERF 流行病學長期追蹤報告); Richard B. Frank (1999, 'Downfall: The End of the Imperial Japanese Empire'); 聯合國裁軍事務廳報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 廣島與長崎市和平紀念館每年更新核實原爆受害者名冊，日美兩國放射醫學會建立了世界最詳盡的核輻射受害者終身醫療追蹤數據庫。`


### [EVT-1945-PHL-002] 馬尼拉大屠殺 (Manila Massacre by Imperial Japanese Forces)
* **起止年份**：1945
* **地理位置**：菲律賓馬尼拉市（聖托馬斯大學、市中市等）(Philippines) `[ISO-3: PHL / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `100,000` 人 / 高標 `120,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`341,719` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美軍反攻馬尼拉期間，日本海軍陸戰隊指揮官岩淵三次少將率部退守市中心歷史城區（Intramuros），奉行焦土決死令，對市內平民實施長達一個月的有組織瘋狂屠殺。日軍在醫院、教堂（如聖保祿修道院）將醫生、護士、修女與難民用刺刀挑死、用手榴彈炸死，將嬰兒拋起用刺刀刺穿，並實施普遍強姦，超過十萬菲律賓平民在城區焦土中遭屠戮。
* **學術文獻引用摘要 (`sources_summary`)**：
  遠東國際軍事法庭 (IMTFE 山下奉文與岩淵三次審判判決書); James M. Scott (2018, 'Rampage: MacArthur, Yamashita, and the Battle of Manila'); 馬尼拉紀念碑基金會 (Memorare Manila 1945); 美軍第六軍法醫調查報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Post-War Judicial Scrutiny] 馬尼拉審判為戰後首場重要戰犯審判，確立了軍事指揮責任原則（山下原則）；美軍法醫與倖存者證詞完備，死者紀念碑銘刻於馬尼拉市中心。`


### [EVT-1945-YUG-001] 二戰後南斯拉夫布萊堡遣返屠殺與死亡行軍 (Bleiburg Repatriations and Post-WWII Yugoslav Death Marches)
* **起止年份**：1945
* **地理位置**：奧地利邊境布萊堡至南斯拉夫斯洛維尼亞、克羅埃西亞全境 (Yugoslavia) `[ISO-3: YUG / 大洲: Europe]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `70,000` 人 / 中標基準 `80,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,385,000,000` 人
  * **2026年當代等效規模**：**`273,375` 人** (放縮係數：3.42x)
  * **區域人口衝擊率**：**`0.5333%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 歐洲戰事結束之際，數十萬向奧地利英軍投降的克羅埃西亞烏斯塔沙部隊、斯洛維尼亞國土防衛軍、塞爾維亞切特尼克士兵及其隨行平民家屬，遭英軍依協議強行遣返交予狄托領導的南斯拉夫游擊隊。游擊隊在未經審判的情況下，對遣返人員實施長達數百公里的死亡行軍，並在斯洛維尼亞的深坑、石灰岩洞與廢棄礦井（如芭芭拉礦坑）進行大規模機槍掃射、活埋與毒氣封死屠殺。
* **學術文獻引用摘要 (`sources_summary`)**：
  Mitja Ferenc (斯洛維尼亞隱蔽萬人坑政府調查委員會主編，核查出斯洛維尼亞境內近600處戰後集體萬人坑); Jozo Tomasevich (2001, 'War and Revolution in Yugoslavia, 1941–1945'); Ivo Goldstein (2008); 斯洛維尼亞胡達亞馬礦坑（Huda Jama）遺骸法醫挖掘報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 南斯拉夫共產黨政權統治四十五年間將布萊堡事件列為絕對歷史禁忌，任何公開討論皆被視為反革命罪行；南斯拉夫解體後斯洛維尼亞展開全面法醫開挖，但受害者中武裝通敵士兵與純平民家屬之比例在巴爾幹各國學界仍具強烈政治爭端。`


### [EVT-1947-IND-002] 印巴分治流血宗族大屠殺 (Partition of India Communal Massacres)
* **起止年份**：1947 – 1948
* **地理位置**：印度與巴基斯坦旁遮普、孟加拉邊境地區 (India / Pakistan) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `1,000,000` 人 / 高標 `2,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,450,000,000` 人
  * **2026年當代等效規模**：**`3,326,531` 人** (放縮係數：3.33x)
  * **區域人口衝擊率**：**`3.3333%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英國匆促劃定雷德克里夫線（Radcliffe Line）撤出印度後，伴隨逾1,400萬人跨越邊界的非自願大遷徙，印度教徒、穆斯林與錫克教徒民兵展開滅絕式宗族仇殺。火車裝載滿車被屠戮平民屍體跨越邊境，數萬名婦女遭有組織綁架、強姦與強迫毀容殉節。
* **學術文獻引用摘要 (`sources_summary`)**：
  Penderel Moon (1961, 'Divide and Quit'); Ian Talbot & Gurharpal Singh (2009, 'The Partition of India'); Urvashi Butalia (1998, 'The Other Side of Silence'); Paul Brass (2003, 'The Partition of India and Retributive Genocide').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 兩國獨立初期行政體系完全瓦解，難民潮與邊界流血衝突無法進行法醫屍檢與民事登記；多數遇害平民直接遭拋入運河或就地焚化，官方數字僅能依靠兩國人口普查差額粗略推算。`


### [EVT-1947-MDG-001] 馬達加斯加起義法軍鎮壓與平民浩劫 (Malagasy Uprising and French Brutal Suppression)
* **起止年份**：1947 – 1949
* **地理位置**：馬達加斯加全境（東部沿海森林）(French Madagascar) `[ISO-3: MDG / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `30,000` 人 / 中標基準 `60,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,450,000,000` 人
  * **2026年當代等效規模**：**`199,592` 人** (放縮係數：3.33x)
  * **區域人口衝擊率**：**`1.4286%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 馬達加斯加爆發反法獨立起義後，法國第四共和國派遣外籍兵團與塞內加爾步兵實施焦土反叛亂平定。法軍動用'飛行縱隊'（colonnes volantes）焚毀數百個村莊、實施公開處決與飛機空投活人示眾，數十萬平民逃入東部熱帶雨林，因封鎖缺乏口糧而大批死於飢荒、瘧疾與營養不良。
* **學術文獻引用摘要 (`sources_summary`)**：
  Jean Fremigacci (1999, 'La vérité sur le massacre de Madagascar', L'Histoire 估算直接與間接死亡約3至4萬人); 官方殖民總督德舍維涅（Pierre de Chevigné）報告（曾估算高達8.9萬人）; Françoise Raison-Jourde (2002); 馬達加斯加獨立後官方採信8.9萬人。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 死亡多數發生在熱帶叢林避難期間而無現場法醫登記，法國軍事當局事後為掩飾失職刻意模糊死亡統計，學界在3萬至8.9萬之間存在評估差異。`


### [EVT-1947-TWN-001] 台灣二二八事件與白色恐怖威權清洗 (Taiwan 228 Incident and the White Terror)
* **起止年份**：1947 – 1987
* **地理位置**：台灣全境及澎湖 (Taiwan) `[ISO-3: TWN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `18,000` 人 / 中標基準 `22,000` 人 / 高標 `32,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,450,000,000` 人
  * **2026年當代等效規模**：**`73,184` 人** (放縮係數：3.33x)
  * **區域人口衝擊率**：**`0.3385%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 專賣局緝菸血案引發全台反貪腐抗議後，陳儀請調國民革命軍整編第21師在基隆、高雄等地登陸實施流血鎮壓與地毯式'清鄉'。軍警有預謀地搜捕處決地方精英、律師、記者、醫師與學生領袖，隨後進入長達38年的戒嚴白色恐怖時期，警總等情治單位濫用叛亂罪名實施保密局黑獄酷刑與綠島政治犯集中營勞改，數萬家庭破碎。
* **學術文獻引用摘要 (`sources_summary`)**：
  行政院《二二八事件研究報告》（1992 官方調查報告，推估遇害人數約1.8萬至2.8萬人）; 國家人權博物館與促進轉型正義委員會 (促轉會) 檔案; 李喬等人口學回推研究; 國史館解密保密局與戒嚴司令部審訊檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Transitional Justice] 台灣民主轉型後透過官方賠償條例、成立促轉會與平反司法不法，開放全部國家檔案，死者名冊與補償補貼檔案完整公佈於國家人權資料庫。`


### [EVT-1947-IND-005] 海得拉巴土邦併入印度「波羅行動」平民屠殺 (Operation Polo and Hyderabad Post-Annexation Massacres)
* **起止年份**：1948
* **地理位置**：印度海得拉巴土邦（現泰倫加納、馬哈拉施特拉）(Hyderabad State, India) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `27,000` 人 / 中標基準 `35,000` 人 / 高標 `40,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,494,166,666` 人
  * **2026年當代等效規模**：**`114,367` 人** (放縮係數：3.27x)
  * **區域人口衝擊率**：**`0.2188%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 印度陸軍為吞併拒絕加入印度的穆斯林統治海得拉巴土邦，發動代號'波羅行動'（Operation Polo）軍事佔領。軍隊擊潰非正規拉扎卡爾民兵（Razakars）後，印度軍隊與進駐部隊在馬哈拉施特拉與奧斯馬納巴德等地默許甚至參與對穆斯林少數平民的大規模報復性屠殺、洗劫與普遍性暴力，造成數萬無武裝平民喪生。
* **學術文獻引用摘要 (`sources_summary`)**：
  桑德拉爾調查委員會報告 (Sunderlal Committee Report, 1948 尼赫魯政府委託之官方調查報告，長年封存至2013年解密); A.G. Noorani (2014, 'The Destruction of Hyderabad'); Sunil Purushotham (2015, Modern Asian Studies); 印度國防部作戰檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 尼赫魯總理在收到桑德拉爾法官撰寫的極具毀滅性之調查報告後，出於防範全國性印度教-穆斯林騷亂考量，將該官方報告列為絕對國家機密永久封存，直至2013年印度內政部始被迫在信息自由法訴訟下解密檔案。`


### [EVT-1948-COL-001] 哥倫比亞「暴力時期」黨派屠殺與焦土清洗 (La Violencia in Colombia)
* **起止年份**：1948 – 1958
* **地理位置**：哥倫比亞全境 (Colombia) `[ISO-3: COL / 大洲: Americas]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `180,000` 人 / 中標基準 `200,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,494,166,666` 人
  * **2026年當代等效規模**：**`653,525` 人** (放縮係數：3.27x)
  * **區域人口衝擊率**：**`1.7391%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 自由黨領袖蓋坦遇刺（波哥大暴動Bogotazo）後，保守黨政府軍警、武裝警察（Chulavitas）與自由黨游擊隊在農村展開極端殘暴的階級與黨派報復屠殺。暴徒實施駭人聽聞的身體殘割（如'哥倫比亞領帶'頸部剖割法）、整村燒戮、強姦婦女並迫使兩百萬農民背井離鄉流離失所。
* **學術文獻引用摘要 (`sources_summary`)**：
  Paul Oquist (1980, 'Violence, Conflict, and Politics in Colombia', Academic Press); Marco Palacios (2006, 'Between Legitimacy and Violence'); 哥倫比亞國家歷史記憶中心 (CNMH); Germán Guzmán Campos et al. (1962, 《La Violencia en Colombia》經典奠基調查)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 農村偏遠山區法治完全真空，地方民事登記徹底瓦解，數以萬計的無名死者遭棄置於考卡河等河流漂流；歷任軍政府與兩黨全國陣線（National Front）特赦妥協協議淡化了責任追究。`


### [EVT-1948-JPN-001] 日本《優生保護法》強制絕育 (Japan Eugenic Protection Law Forced Sterilizations)
* **起止年份**：1948 – 1996
* **地理位置**：日本全境 (Japan) `[ISO-3: JPN / 大洲: Asia]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `100` 人 / 中標基準 `500` 人 / 高標 `1,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,494,166,666` 人
  * **2026年當代等效規模**：**`1,634` 人** (放縮係數：3.27x)
  * **區域人口衝擊率**：**`0.0006%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 日本《優生保護法》（1948年制定）授權對「遺傳性疾病」、精神障礙、麻瘋病（漢生病）患者及部落民（Burakumin）實施未經本人同意之強制不孕手術。醫生、公衛人員與都道府縣優生保護審查委員會可在當事人毫不知情或明確拒絕的情況下，秘密核准並實施輸精管切除或卵巢摘除手術，受害者多為未成年人與院所收容者。
* **學術文獻引用摘要 (`sources_summary`)**：
  日本政府2019年優生保護法調查報告（正式承認16,475件強制手術及支付補償）; 辻岡靖仁等《旭川事件》(2001); 內閣府優生手術記錄數據庫; Sabine Frühstück (2003, 'Colonizing Sex: Sexology and Social Control in Modern Japan')。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 日本政府長達半世紀否認強制性質，直至2019年6月通過《舊優生保護法基礎上手術受害者補償法》，始首度正式道歉；大量地方衛生機構記錄在1990年代法律修訂前遭銷毀，估計強制施術總數（官方核認16,475件，推估達25,000件以上）仍存統計缺口。`


### [EVT-1948-KOR-002] 韓國濟州四三事件平民焦土清剿 (Jeju April 3 Incident and Civilian Massacres)
* **起止年份**：1948 – 1954
* **地理位置**：韓國濟州島 (Jeju Island, South Korea) `[ISO-3: KOR / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `14,000` 人 / 中標基準 `20,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,494,166,666` 人
  * **2026年當代等效規模**：**`65,352` 人** (放縮係數：3.27x)
  * **區域人口衝擊率**：**`6.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 反對美軍政廳單獨舉行南韓選舉之抗議爆發後，李承晚政權頒布戒嚴令，將濟州島海岸線5公里以外山區劃為敵對交戰區，命令射殺一切進入該區之平民。政府軍警與極右翼極端組織'西北青年會'推行徹底焦土政策，焚燒山區95%以上的村落，在北村里等地將全體村民不分老幼集中於小學操場用機槍屠殺，全島十分之一人口喪生。
* **學術文獻引用摘要 (`sources_summary`)**：
  韓國國務總理下屬濟州四三事件真相查明和名譽恢復委員會 (2003 官方綜合報告，核實確切遇害者名單逾1.4萬人); John Merrill (1989, 'Korea: The Peninsular Origins of the War'); 盧武鉉總統2003年代表韓國政府正式向濟州人民道歉; 濟州四三和平財團檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Apology] 獨裁統治期間該事件被列為反共叛亂禁忌話題達半世紀，家屬遭連坐法迫害；2000年韓國國會通過特別法後全面完成真相平反，建立和平公園並逐一鑑定萬人坑遺骸。`


### [EVT-1950-CHN-008] 中國土地改革運動暴力鬥爭與鎮壓反革命運動 (Chinese Violent Land Reform Movement and Campaign to Suppress Counterrevolutionaries)
* **起止年份**：1950 – 1953
* **地理位置**：中國全境 (People's Republic of China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500,000` 人 / 中標基準 `2,500,000` 人 / 高標 `4,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,582,500,000` 人
  * **2026年當代等效規模**：**`7,889,642` 人** (放縮係數：3.16x)
  * **區域人口衝擊率**：**`0.4545%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 中共建國初期為重塑農村社會權力結構並鞏固政權，發動暴力土地改革與鎮壓反革命運動。當局組織群眾鬥爭大會，由工作隊動員貧下中農對地主、富農及其家屬實施殘酷公審、棍棒圍毆致死；在鎮反運動中，中央按人口比例下達處決硬性定額指標，大批前民國軍政公教人員、宗教人士未經正規司法程序被判處死刑槍決。
* **學術文獻引用摘要 (`sources_summary`)**：
  Frank Dikötter (2013, 'The Tragedy of Liberation: A History of the Chinese Revolution 1945–1957'); R.J. Rummel (1991, 'China's Bloody Century'); 毛澤東選集及中央檔案館（毛親自制定'殺人指標'，要求各地按千分之一至千分之二比例處決反革命）; 楊奎松《中華人民共和國建國史研究》卷一（詳證建國初期鎮反處決逾71萬人）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 官方檔案中涉及土改致死地主富農（包含逼迫自殺、沒收口糧餓死）之總數據從未公開，基層各縣公安局檔案長期列為絕密；學界對土改與鎮反之直接處決及被逼自殺總人數在150萬至400萬間存在長期史學論爭。`


### [EVT-1950-KOR-001] 韓國保導聯盟大屠殺 (Bodo League Massacre (South Korea))
* **起止年份**：1950
* **地理位置**：韓國全境（大田、清州、慶州等地）(Republic of Korea) `[ISO-3: KOR / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `60,000` 人 / 中標基準 `100,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,582,500,000` 人
  * **2026年當代等效規模**：**`315,586` 人** (放縮係數：3.16x)
  * **區域人口衝擊率**：**`0.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 韓戰爆發後，李承晚政府以「防止通敵」為名，對「保導聯盟」（Bodo League）──即此前被強制登記為改過自新前左翼嫌疑人的數十萬平民──展開預防性大規模處決。韓國警察與軍隊在幾天之內將各地被拘押的聯盟成員（多為普通農民、教師及地方人士）以集體槍決方式處死並推入路邊沙坑，其中包括大量毫無政治活動的家屬連坐者。
* **學術文獻引用摘要 (`sources_summary`)**：
  韓國「真相與和解委員會」(Truth and Reconciliation Commission of Korea, TRCK 2009–2010 系列調查報告，確認至少 3,400 個個案); Kim Dong-choon (2000, 'War and Society', 估算10-20萬人); 美國解密軍事顧問檔案（NARA，顯示美軍駐韓顧問目擊並記錄部分屠殺）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 南韓政府在軍事獨裁時期（尤其朴正熙與全斗煥政府）將此事件列為最高國家機密，家屬數十年來被禁止祭悼，真相委員會相關報告於2010年後遭李明博政府縮減預算並事實上中止調查，許多萬人坑尚未全面完成法醫發掘。`


### [EVT-1952-KEN-001] 肯亞茅茅起義英國酷刑集中營 (Kenya Mau Mau Uprising – British Detention Camps and Torture)
* **起止年份**：1952 – 1960
* **地理位置**：英屬肯亞 (British Kenya) `[ISO-3: KEN / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `12,000` 人 / 中標基準 `25,000` 人 / 高標 `50,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,670,833,333` 人
  * **2026年當代等效規模**：**`76,287` 人** (放縮係數：3.05x)
  * **區域人口衝擊率**：**`0.4167%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英國殖民政府宣布緊急狀態後，建立龐大的「管理村」（Pipeline）拘留體系，超過150萬吉庫尤族（Kikuyu）平民被強制圍困於由鐵絲網包圍的管制區。殖民警察與「鑑別軍官」（Screening Officers）系統性實施電擊、強制閹割、以玻璃瓶及竹棒插入肛門及陰道等性酷刑、強制勞役及故意餓死手段，以「鑑別」茅茅同情者。
* **學術文獻引用摘要 (`sources_summary`)**：
  Caroline Elkins (2005, 'Imperial Reckoning: The Untold Story of Britain's Gulag in Kenya', Pulitzer Prize獲獎著作); David Anderson (2005, 'Histories of the Hanged'); 英國2013年外交部承認酷刑並支付賠償（Leigh Day法律事務所訴訟記錄）; 英國高等法院2011年裁定案受害者具有訴訟資格。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 英國殖民政府在撤離前秘密銷毀或運走大批「遷移文件」（Migrated Archive），英國外交部至2012年始承認數萬份肯亞殖民時期敏感文件曾被系統性秘密轉移；2013年英國外交大臣官方道歉並支付1995萬英鎊賠償金予5,228名倖存受害者。`


### [EVT-1954-DZA-001] 阿爾及利亞獨立戰爭法軍集中營與平民屠殺 (Algerian War – French Regroupement Camps and Civilian Massacres)
* **起止年份**：1954 – 1962
* **地理位置**：阿爾及利亞 (Algeria, French Union) `[ISO-3: DZA / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `500,000` 人 / 高標 `1,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,759,166,666` 人
  * **2026年當代等效規模**：**`1,476,895` 人** (放縮係數：2.95x)
  * **區域人口衝擊率**：**`5.5556%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 法軍為鎮壓民族解放陣線（FLN），在阿爾及利亞實施「重新安置」（Regroupement）政策，將超過200萬農村平民強制遷入可控集中營區，造成大規模飢饉與傳染病死亡；法國空降兵部隊對懷疑通敵之村落進行報復性集體屠殺（如麥勒茲村Melouza屠殺）、系統性電刑虐待與水刑審訊，造成大量平民非正常死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Benjamin Stora (2001, 'Algeria, 1830–2000'); Alistair Horne (1977, 'A Savage War of Peace: Algeria 1954–1962'); Raphaëlle Branche (2001, 'La Torture et L'Armée Pendant La Guerre d'Algérie'); 法國國防部解密檔案（2001年後部分開放）；阿爾及利亞官方宣稱死亡逾150萬人。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 法國政府直至2018年始首度官方承認殖民時期對阿爾及利亞平民的系統性酷刑行為（馬克宏聲明），相關軍事調查法庭與反恐審訊檔案至今大部分仍處於法國國防部保密狀態；學界死亡估算差距高達3倍以上。`


### [EVT-1955-CMR-001] 喀麥隆獨立前夕法軍巴米累克高原焦土大清洗 (Cameroonian UPC Rebellion and French Scorched Earth Pacification)
* **起止年份**：1955 – 1962
* **地理位置**：喀麥隆西部巴米累克高原與薩納加-海洋省 (French Cameroun) `[ISO-3: CMR / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `30,000` 人 / 中標基準 `60,000` 人 / 高標 `120,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,803,333,333` 人
  * **2026年當代等效規模**：**`174,435` 人** (放縮係數：2.91x)
  * **區域人口衝擊率**：**`1.875%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 為剷除左翼獨立政黨喀麥隆人民聯盟（UPC）並扶植親法阿希喬政權，法國殖民軍隊調動曾參與印支與阿爾及利亞作戰的特種部隊，在巴米累克高原展開極度殘酷的隱密反叛亂平定。法軍動用直升機與轟炸機投放凝固汽油彈燒村、推行強迫搬遷集中營管制農民，並公開斬首游擊隊員與支持平民懸首市集示眾，引發大規模平民死傷。
* **學術文獻引用摘要 (`sources_summary`)**：
  Thomas Deltombe, Manuel Domergue & Jacob Tatsitsa (2011, 'Kamerun ! Une guerre cachée aux origines de la Françafrique', La Découverte); 法國總統馬克宏2022年訪問喀麥隆時宣布委託兩國歷史學家聯合委員會調查該歷史慘劇; 法國國防部解密軍事通報。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 該衝突被法國殖民史學界長期封存抹煞，稱其為'隱密戰爭'；2023年法喀兩國正式成立歷史真相委員會解密軍事檔案以還原真相。`


### [EVT-1955-SDN-003] 第一次蘇丹內戰南部焦土平民浩劫 (First Sudanese Civil War and Torit Mutiny Civilian Atrocities)
* **起止年份**：1955 – 1972
* **地理位置**：蘇丹南部各省（現南蘇丹）(Southern Sudan) `[ISO-3: SSD / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `750,000` 人 / 高標 `1,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,803,333,333` 人
  * **2026年當代等效規模**：**`2,180,440` 人** (放縮係數：2.91x)
  * **區域人口衝擊率**：**`18.75%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇丹獨立前夕托里特南部駐軍譁變，揭開南北長達17年流血內戰。北部喀土穆阿拉伯伊斯蘭中央政府為鎮壓阿尼亞-尼亞（Anya-Nya）南部黑人反抗軍，對南部非阿拉伯村莊實施全面焦土清剿，有組織地槍決南部知識分子與神職人員、焚毀糧田牲口並阻斷醫療物資，導致南部總人口五分之一死於戰爭屠殺、人為飢荒與霍亂。
* **學術文獻引用摘要 (`sources_summary`)**：
  Douglas H. Johnson (2003, 'The Root Causes of Sudan's Civil Wars', Indiana Univ Press); Edgar O'Ballance (1977, 'The Secret War in the Sudan: 1955–1972'); 亞的斯亞貝巴和平協定歷史文件; 國際特赦組織檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 該衝突發生於非洲非殖民化動盪期，交戰各方長年處於熱帶叢林游擊戰狀態，無任何完整民事死亡登記機構，死傷規模全賴戰後亞的斯亞貝巴協定簽署時人口學家對南北人口普查虧空推估。`


### [EVT-1959-CHN-002] 中國大躍進與三年大饑荒 (Great Chinese Famine (Great Leap Forward))
* **起止年份**：1959 – 1961
* **地理位置**：中國全境（尤以河南、四川、安徽、甘肅最烈）(People's Republic of China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `15,000,000` 人 / 中標基準 `30,000,000` 人 / 高標 `45,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`2,980,000,000` 人
  * **2026年當代等效規模**：**`82,046,980` 人** (放縮係數：2.73x)
  * **區域人口衝擊率**：**`4.5455%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 毛澤東推行「大躍進」與「人民公社化運動」，基層官員嚴重浮誇虛報糧食產量，導致國家按虛假產量進行高比例強行徵購。在農村糧倉見底之際，當局嚴厲打擊「反瞞產」、封閉公共食堂並嚴格禁止飢民外出逃荒，糧食庫存封存優先用於外銷換取工業設備與外匯，造成歷史上死亡人數最多之人道悲劇。
* **學術文獻引用摘要 (`sources_summary`)**：
  楊繼繩 (2008, 《墓碑：中國六十年代大饑荒紀實》, 估算非正常死亡3,600萬); Frank Dikötter (2010, 'Mao's Great Famine', 估算4,500萬); 曹樹基 (2005, 《大饑荒：1959-1961年的中國人口》, 估算3,250萬); 高華；彭德懷信件與中共七千人大會檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 中共官方長期將災難歸咎為「三年自然災害」或「蘇聯逼債」；各省公安廳非正常死亡秘密統計資料長年列為絕密檔案，信陽、通渭等重災區基層檔案多處於封閉狀態，相關歷史研究在中國境內遭到嚴格出版審查。`


### [EVT-1960-ZAF-003] 南非種族隔離制度沙佩維爾屠殺、索韋托起義與國家安全暗殺 (South African Apartheid State Murders and Massacres (Sharpeville to Soweto))
* **起止年份**：1960 – 1989
* **地理位置**：南非全境（沙佩維爾、索韋托、克魯克斯多普等）(South Africa) `[ISO-3: ZAF / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `7,000` 人 / 中標基準 `12,000` 人 / 高標 `25,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,038,333,333` 人
  * **2026年當代等效規模**：**`32,189` 人** (放縮係數：2.68x)
  * **區域人口衝擊率**：**`0.048%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 南非白人少數政權推行全面種族隔離體制（Apartheid），剝奪黑人公民權並將其強制驅逐至貧瘠的'班圖斯坦'（黑人家園）。警察部隊在沙佩維爾對反通行證和平示威開槍射殺69人（背部中彈居多），在1976年索韋托起義中實彈射殺數百名抗議強制使用阿非利卡語教學的黑人中學生，並由軍警秘密行動暗殺隊（Vlakplaas，如尤金·德科克）秘密刑求與處決無數反種族隔離領袖（如史蒂夫·比科）。
* **學術文獻引用摘要 (`sources_summary`)**：
  南非真相與和解委員會 (TRC 1998 終期報告，大主教屠圖主編); 聯合國大會將種族隔離定性為危害人類罪（反種族隔離國際公約）; 國際特赦組織檔案; 美國國務院人權報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / TRC Judicial Records] 曼德拉當選後成立之真相與和解委員會（TRC）創立了全球轉型正義之典範模式，加害者以坦白真相換取特赦，完整記錄並公佈了國家安全機構的暗殺與酷刑網絡檔案。`


### [EVT-1960-IRQ-002] 伊拉克庫德武裝起義阿拉伯化清鄉與焦土平民屠殺 (Iraqi Operations against Kurds and Early Arabization Campaigns)
* **起止年份**：1961 – 1975
* **地理位置**：伊拉克北部庫德斯坦（基爾庫克、埃爾比勒等）(Iraqi Kurdistan) `[ISO-3: IRQ / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `60,000` 人 / 中標基準 `80,000` 人 / 高標 `110,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,096,666,666` 人
  * **2026年當代等效規模**：**`210,549` 人** (放縮係數：2.63x)
  * **區域人口衝擊率**：**`3.2%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在穆斯塔法·巴爾扎尼領導庫德起義期間，伊拉克歷任軍政府與復興黨早期政權推行'阿拉伯化政策'（Ta'rib）。巴格達空軍對庫德山區村落投擲凝固汽油彈，陸軍推平數百座庫德與亞述村莊，將數十萬原住庫德平民強行驅離富饒石油重鎮基爾庫克，移居中南部荒漠集中拘留營，製造大規模飢饉與難民凍斃死難。
* **學術文獻引用摘要 (`sources_summary`)**：
  David McDowall (2004, 'A Modern History of the Kurds', I.B. Tauris); 人權觀察 (Human Rights Watch, 1993 庫德問題背景研究); Ofra Bengio (2012, 'The Kurds of Iraq'); 復興黨革命指揮委員會解密命令。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 海珊政權垮台前庫德地區所有歷史檔案遭到嚴密保密管控；2003年美軍進入巴格達後繳獲數百萬份復興黨情報檔案，確立了阿拉伯化驅逐與平民處決的官方政策脈絡。`


### [EVT-1962-IDN-002] 印尼兼併西巴布亞軍事鎮壓與原住民大清洗 (Indonesian Annexation of West Papua and Democide (Operation Trikora))
* **起止年份**：1962 – 1969
* **地理位置**：西巴布亞 / 西新幾內亞 (West Papua, Indonesia) `[ISO-3: IDN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `50,000` 人 / 中標基準 `100,000` 人 / 高標 `150,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,155,000,000` 人
  * **2026年當代等效規模**：**`258,320` 人** (放縮係數：2.58x)
  * **區域人口衝擊率**：**`12.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 印尼蘇卡諾與蘇哈托軍隊為吞併前荷屬西新幾內亞，對美拉尼西亞原住民巴布亞人展開長達數年的軍事清洗。印尼軍警空襲高地村落、強制將部落遷往沿海管制區，並在1969年所謂'自由選擇法案'中，以槍枝威脅強迫指派的1025名長老一致投票加入印尼，其後十年間軍隊對任何爭取自決的原住民社群實施秘密處決與焦土掃蕩，造成數萬原住民喪生。
* **學術文獻引用摘要 (`sources_summary`)**：
  耶魯大學法學院人權診所報告 (Allard K. Lowenstein International Human Rights Clinic, 2004 'Genocide in West Papua?'); 澳洲雪梨大學和平與衝突研究中心報告 (2005); 自由巴布亞運動 (OPM) 檔案; 聯合國第2504號決議歷史檢視。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 印尼政府數十年來嚴禁外國記者、外交官與國際特赦組織等獨立人權團體進入西巴布亞省實地考察，實施嚴厲新聞審查；所有死難名冊主要依靠海外巴布亞流亡團體與教會秘密記錄收集。`


### [EVT-1963-RWA-002] 盧安達「吉康戈羅」圖西族大屠殺與流亡浩劫 (Gikongoro Massacres of Tutsis in Rwanda (1963))
* **起止年份**：1963 – 1964
* **地理位置**：盧安達吉康戈羅省及全境 (Rwanda) `[ISO-3: RWA / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `15,000` 人 / 高標 `25,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,213,333,333` 人
  * **2026年當代等效規模**：**`38,045` 人** (放縮係數：2.54x)
  * **區域人口衝擊率**：**`0.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 流亡布隆迪的圖西族君主派發動微弱越境突襲後，盧安達首任胡圖族總統卡伊班達政權借機發動全境報復清洗。內政部發動地方行政官員組建民兵，在吉康戈羅等地有預謀地屠殺平民圖西族知識分子、教師及農民，甚至按名冊殺光所有被拘留圖西政治人物，造成十五萬人逃亡鄰國，為三十年後的1994年大滅絕埋下仇恨根基。
* **學術文獻引用摘要 (`sources_summary`)**：
  René Lemarchand (1970, 'Rwanda and Burundi', Praeger); Gérard Prunier (1995, 'The Rwanda Crisis'); 聯合國秘書長吳丹特別代表報告; 伯特蘭·羅素 (Bertrand Russell, 1964 發表公開聲明稱其為'自滅絕猶太人以來最可怕的大屠殺').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / International Eyewitnesses] 瑞士與比利時天主教傳教士留下了詳盡的屠殺日記與現場遺骸照片；著名哲學家羅素公開向聯合國呼籲干預，歷史證據充分。`


### [EVT-1964-BRA-001] 巴西軍政府威權鎮壓與亞馬遜原住民種族滅絕 (Brazilian Military Dictatorship and Indigenous Democide)
* **起止年份**：1964 – 1985
* **地理位置**：巴西亞馬遜盆地及各大城市 (Brazil) `[ISO-3: BRA / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `8,500` 人 / 中標基準 `10,000` 人 / 高標 `20,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,271,666,666` 人
  * **2026年當代等效規模**：**`24,911` 人** (放縮係數：2.49x)
  * **區域人口衝擊率**：**`0.01%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 1964年政變後之巴西軍事獨裁政權推行跨亞馬遜公路等國家開發計畫，指派印第安人保護局（SPI）軍官殘暴對待原住民部落（如Waimiri-Atroari族）。官方默許甚至主導空軍投擲凝固汽油彈轟炸部落村莊、引進天花病菌實施細菌感染、毒化水源，並將數百名左翼游擊隊與知識分子在秘密監獄酷刑處決與強迫失蹤。
* **學術文獻引用摘要 (`sources_summary`)**：
  巴西國家真相委員會 (Comissão Nacional da Verdade, CNV 2014 官方終期報告認定軍政府造成至少8,350名原住民被殺害); 菲格雷多報告 (Relatório Figueiredo, 1967年一度失蹤後重光的7000頁軍政時期原住民虐殺原始調查報告); 人權觀察報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Truth Commission Report] 曾被軍方宣稱在火災中燒毀之《菲格雷多報告》於2013年在庫里奇巴印第安人博物館地下室重光，詳細記錄了軍方蓄意引進天花疫苗空針與投毒屠殺的原始供詞，促成CNV正式定罪國家責任。`


### [EVT-1965-IDN-001] 印尼反共清共大屠殺 (Indonesian Mass Killings of 1965–1966)
* **起止年份**：1965 – 1966
* **地理位置**：印尼爪哇島、峇里島及蘇門答臘 (Indonesia) `[ISO-3: IDN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `750,000` 人 / 高標 `1,200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,330,000,000` 人
  * **2026年當代等效規模**：**`1,835,586` 人** (放縮係數：2.45x)
  * **區域人口衝擊率**：**`0.7143%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 「九三〇事件」後，蘇哈托將軍奪取權力，指控印尼共產黨（PKI）策動政變。在印尼軍方主導與伊斯蘭青年民兵配合下，展開全國性地毯式血腥大清洗，針對共產黨員、左翼同情者、工會工農及華裔少數族群實施就地斬首、溺斃與活埋。
* **學術文獻引用摘要 (`sources_summary`)**：
  Robert Cribb (1990, 'The Indonesian Killings of 1965–1966'); 印尼國家人權委員會 (Komnas HAM, 2012 調查報告認定為嚴重危害人類罪); Geoffrey Robinson (2018, 'The Killing Season', Princeton Univ Press); 美國解密國務院電報 (National Security Archive).
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇哈托「新秩序」統治三十年間嚴禁公開調查與討論屠殺，被害者遺屬遭剝奪公民權益；直至2010年後紀錄片《殺人一舉》（The Act of Killing）上映引發國際關注，官方仍拒絕正式道歉與全面開棺驗屍。`


### [EVT-1966-CAF-002] 中非帝國博卡薩獨裁政權殘暴虐殺與學生大屠殺 (Jean-Bédel Bokassa Regime Atrocities and Schoolchildren Massacre)
* **起止年份**：1966 – 1979
* **地理位置**：中非共和國 / 中非帝國 (Central African Republic / Empire) `[ISO-3: CAF / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `2,000` 人 / 中標基準 `4,000` 人 / 高標 `10,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,390,000,000` 人
  * **2026年當代等效規模**：**`9,617` 人** (放縮係數：2.4x)
  * **區域人口衝擊率**：**`0.1818%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 獨裁者讓-貝德爾·博卡薩自立為皇帝揮霍國庫，建立恐怖秘密警察網絡對政治反對者實施殘酷私刑折磨、投餵鱷魚及獅子。1979年4月，因中小學生抗議被迫購買印有其肖像的昂貴指定校服，帝國禁衛軍搜捕百餘名年僅8至16歲的學童關入納揚加巴監獄（Ngaragba），博卡薩親臨監獄指揮衛兵用皮鞭、木棍活活將約百名幼童毆打折磨致死，直接促成法國發動軍事政變推翻其政權。
* **學術文獻引用摘要 (`sources_summary`)**：
  非洲司法調查委員會 (African Judicial Commission, 1979 由盧安達、賴比瑞亞、塞內加爾、象牙海岸法官組成之國際調查團認定博卡薩親自參與屠殺學生); 國際特赦組織 (Amnesty International 1979 報告); 中非班基高等法院1980年對博卡薩缺席死刑審判判決書; Brian Titley (1997, 'Dark Age: The Political Odyssey of Emperor Bokassa', McGill-Queen's Univ Press).
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Judicial Investigation] 非洲五國法官組成的獨立調查團親赴班基監獄挖掘法醫骸骨並訊問看守，確鑿證實了兒童屠殺事件；1986年博卡薩返國後接受公開司法審判，被判處謀殺罪成立。`


### [EVT-1966-CHN-007] 文化大革命政治清洗與地方大屠殺 (Cultural Revolution Purges, Massacres and Armed Clashes)
* **起止年份**：1966 – 1976
* **地理位置**：中國全境（廣西、湖南道縣、北京大興、內蒙古等最烈）(People's Republic of China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `750,000` 人 / 中標基準 `1,750,000` 人 / 高標 `3,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,390,000,000` 人
  * **2026年當代等效規模**：**`4,207,227` 人** (放縮係數：2.4x)
  * **區域人口衝擊率**：**`0.2349%`**
* **學界共識度**：`State Suppressed`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 毛澤東發動「無產階級文化大革命」摧毀既有黨政體制，動員紅衛兵與造反派進行狂熱意識形態清洗。運動迅速演變為全國性殘酷批鬥、抄家、逼供信虐殺及各派武裝割據之動態「武鬥」；地方革委會與軍警更主導針對「黑五類」階級敵人的系統性群體滅絕（如廣西屠殺吃人狂潮、湖南道縣大屠殺、北京大興屠殺及內人黨冤案），造成逾百萬平民非正常慘死與數千萬人受迫害殘疾。
* **學術文獻引用摘要 (`sources_summary`)**：
  宋永毅主編 (2002, 《文革大屠殺》及《中國文化大革命數據庫》); Andrew G. Walder & Su Yang (2003, 'The Cultural Revolution in the Countryside: Scope, Timing and Human Casualties', American Sociological Review 依據縣志抽樣估算非正常死亡 75-150 萬); Roderick MacFarquhar & Michael Schoenhals (2006, 'Mao's Last Revolution', Harvard Univ Press); R.J. Rummel (1991, 'China's Bloody Century'); 中共中央1981年《關於建國以來黨的若干歷史問題的決議》（定性為全局性內亂浩劫）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 儘管中共十一屆六中全會將文革定性為嚴重災難，但官方對非正常死亡總數長年秘而不宣，各地公安局、革委會與地方檔案館之原始卷宗列為絕密；宋永毅等學者之歷史檔案庫在境內遭封禁，廣西文革機密檔案亦僅極少數流向海外，精確總體遇難名冊仍處於官方審查封閉狀態。`


### [EVT-1966-GRL-001] 格陵蘭因紐特婦女子宮節育環（螺旋環）強制置入事件 (Greenland Inuk Women Coil Campaign (Spiralkampagnen))
* **起止年份**：1966 – 1974
* **地理位置**：格陵蘭 (Greenland / Denmark) `[ISO-3: GRL / 大洲: Americas]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `50` 人 / 中標基準 `120` 人 / 高標 `300` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,390,000,000` 人
  * **2026年當代等效規模**：**`288` 人** (放縮係數：2.4x)
  * **區域人口衝擊率**：**`0.3%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 丹麥殖民當局為縮減對格陵蘭島的原住民社會福利支出與人口增長率，在學校體檢時由丹麥醫師對數千名年僅12-16歲的因紐特女童強制或瞞騙植入過大的宮內節育環（IUD）。粗暴手術引發大規模子宮穿孔、盆腔嚴重感染、終身不孕與敗血性併發症致死，使格陵蘭島生育率在數年內暴跌近50%。
* **學術文獻引用摘要 (`sources_summary`)**：
  丹麥廣播公司 (DR 2022 調查播客 'Spiralkampagnen'); 丹麥與格陵蘭聯合歷史調查委員會（2022年正式啟動兩國調查）; 聯合國原住民族權利特別報告員通報 (2023); 格陵蘭人權委員會檔案（證實全島13至17歲半數育齡因紐特少女約4,500人遭未經知情同意植入）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 丹麥官方將此醫療控制計畫列為機密檔案逾半個世紀，受害女性大多在2022年媒體披露檔案後始知身體創傷之真相；丹麥政府於2023年面臨受害者跨國集體訴訟索賠。`


### [EVT-1966-ROU-001] 羅馬尼亞齊奧塞斯庫強制生育法令770與孤兒院人道慘劇 (Romanian Decree 770 Coercive Pronatalism and Orphanage Atrocities)
* **起止年份**：1966 – 1989
* **地理位置**：羅馬尼亞社會主義共和國 (Socialist Republic of Romania) `[ISO-3: ROU / 大洲: Europe]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `18,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,390,000,000` 人
  * **2026年當代等效規模**：**`43,274` 人** (放縮係數：2.4x)
  * **區域人口衝擊率**：**`0.0947%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 齊奧塞斯庫政權頒布第770號法令，全面禁止墮胎與避孕工具，動用秘密警察「安全局」派遣婦科醫生常駐工廠實施強制例行驗孕（被稱為月經警察）。無數女性因自製工具秘密墮胎死於敗血症與大出血，數十萬被遺棄之「法令兒童」（Decree 770 children）被關入非人道的國家精神病態孤兒院，在捆綁、缺乏食物與污穢中大批非正常死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  Gail Kligman (1998, 'The Politics of Duplicity: Controlling Reproduction in Ceausescu's Romania', Univ of California Press); 聯合國兒童基金會 (UNICEF 1990 年羅馬尼亞孤兒院調查); 羅馬尼亞衛生部解密產婦死亡率登記檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 齊奧塞斯庫統治期間嚴禁公布因非法墮胎死亡之產婦與孤兒院幼童夭折統計，醫院被命令將死因偽造為急性肺炎或先天殘疾；1989年革命政權倒台後，國際電視台揭發殘暴孤兒院現況震撼全球。`


### [EVT-1967-NGA-001] 奈及利亞比亞法拉大饑荒與全面封鎖 (Biafran Famine and Starvation Blockade)
* **起止年份**：1967 – 1970
* **地理位置**：奈及利亞東南部比亞法拉共和國 (Biafra, Nigeria) `[ISO-3: NGA / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,000,000` 人 / 中標基準 `1,500,000` 人 / 高標 `3,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,470,000,000` 人
  * **2026年當代等效規模**：**`3,523,055` 人** (放縮係數：2.35x)
  * **區域人口衝擊率**：**`11.5385%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 奈及利亞聯邦軍對宣布獨立之伊博族（Igbo）比亞法拉實施全面陸海空封鎖。聯邦政府要員公開聲稱「飢餓也是一種合法的戰爭武器」，嚴厲攔截紅十字會之人道糧食與奶粉飛機，導致上百萬兒童罹患極端惡性營養不良（紅孩症Kwashiorkor）並活活餓斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  Chinua Achebe (2012, 'There Was a Country: A Personal History of Biafra'); John de St. Jorre (1972, 'The Nigerian Civil War'); 國際紅十字會 (ICRC 空運救援記錄); 無國界醫生 (MSF 創立之歷史起源檔案)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 比亞法拉政權在戰爭後期政府架構完全崩毀，數百萬飢民分散在叢林難民營中死亡；法國紅十字會志願醫生因不滿官方封鎖真相，憤而退會並創立「無國界醫生」（MSF）。`


### [EVT-1968-GNQ-001] 赤道幾內亞馬西埃·恩圭馬極端恐怖統治 (Francisco Macías Nguema Reign of Terror)
* **起止年份**：1968 – 1979
* **地理位置**：赤道幾內亞 (Equatorial Guinea) `[ISO-3: GNQ / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `50,000` 人 / 中標基準 `60,000` 人 / 高標 `80,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,542,500,000` 人
  * **2026年當代等效規模**：**`138,038` 人** (放縮係數：2.3x)
  * **區域人口衝擊率**：**`20.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 獨裁者弗朗西斯科·馬西埃·恩圭馬建立被稱為'非洲達豪集中營'的極端恐怖體制。他自封'唯一奇蹟'，宣布關閉全國所有學校與醫院，禁止使用'知識分子'一詞並處決所有戴眼鏡及受過教育的公民；政權下令屠殺布比族（Bubi）少數民族精英，全島三分之一人口逃亡海外，數萬人死於馬拉博黑灘監獄的私刑折磨與強制可可種植園奴隸勞動。
* **學術文獻引用摘要 (`sources_summary`)**：
  Randall Fegley (1989, 'Equatorial Guinea: An African Tragedy'); 國際法學家委員會 (ICJ 1978 特殊人權報告); Max Liniger-Goumaz (1988, 'Small is Not Beautiful: The Case of Equatorial Guinea'); 聯合國人權委員會調查報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 該國在馬西埃統治期間實施完全的封閉鎖國，禁止外國記者入境並驅逐聯合國代表；馬西埃於1979年被其侄子奧比昂政變推翻並槍決，但奧比昂政權延續至今，歷史檔案仍未全面開放。`


### [EVT-1970-PRK-002] 北韓政治犯收容所（管理所）體系死難與奴役 (North Korean Kwan-li-so Political Prison Camps System)
* **起止年份**：1970 – 2026
* **地理位置**：朝鮮民主主義人民共和國（耀德15號、價川14號、會寧22號管理所等）(North Korea) `[ISO-3: PRK / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `350,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,687,500,000` 人
  * **2026年當代等效規模**：**`773,559` 人** (放縮係數：2.21x)
  * **區域人口衝擊率**：**`1.75%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 金氏世襲極權政權依據'出身成分'制度與'連坐法'（牽連三代），將疑似政治異見者、宗派分子及脫北失敗者秘密送往封閉山區的管理所（Kwan-li-so）。在耀德、價川等地，收容者終身無釋放可能，在極限熱量飢餓下於煤礦及重工業設施強制苦役，營內警衛享有隨意處決、公開絞刑及性侵女犯的絕對特權，數十萬人非正常死亡於此現代古拉格群島中。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國朝鮮人權狀況調查委員會報告 (UN COI Report, 2014 認定其體系構成危害人類罪); 美國北韓人權委員會 (HRNK 系列衛星圖像與營地調查); 國際特赦組織 (Amnesty International); 脫北者姜哲煥（《平壤水族館》）與申東赫證詞。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 朝鮮官方完全否認政治犯收容所存在，稱其為帝國主義捏造宣傳；聯合國COI委員會依據高解析商人造衛星圖像、逃亡前守衛證詞及前囚犯繪製的地圖交叉核驗，建立了無可置疑的法律證據鏈。`


### [EVT-1971-BGD-001] 1971年孟加拉獨立戰爭種族滅絕 (1971 Bangladesh Genocide)
* **起止年份**：1971
* **地理位置**：東巴基斯坦 (modern Bangladesh) `[ISO-3: BGD / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `1,000,000` 人 / 高標 `3,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,760,000,000` 人
  * **2026年當代等效規模**：**`2,167,553` 人** (放縮係數：2.17x)
  * **區域人口衝擊率**：**`1.4706%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 西巴基斯坦軍事獨裁政權為阻止人民聯盟組閣，啟動「探照燈行動」（Operation Searchlight）。巴基斯坦陸軍部隊與極端宗教民兵（拉扎卡爾Razakars）在達卡大學等重鎮有預謀地處決孟加拉知識分子、學生與少數印度教徒，並實施系統性大規模強姦（估計20-40萬婦女受害），致使千萬難民逃亡印度。
* **學術文獻引用摘要 (`sources_summary`)**：
  R.J. Rummel (1994, 'Death by Government'); Gary Bass (2013, 'The Blood Telegram: Nixon, Kissinger, and a Forgotten Genocide'); 孟加拉官方調查委員會（宣稱300萬人遇害）；Hamoodur Rahman Commission Report（巴基斯坦官方調查，採信極低死傷）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 巴基斯坦政府迄今拒絕承認軍隊犯下種族滅絕罪行，尼克森與季辛吉時期的美國外交電報（如阿徹·布拉德總領事之《血電報》）曾長年列為機密以維護對巴外交聯盟。`


### [EVT-1971-UGA-001] 烏干達伊迪·阿敏政權恐怖清洗與族群大屠殺 (Idi Amin Regime Terror, Purges and Massacres)
* **起止年份**：1971 – 1979
* **地理位置**：烏干達全境 (Uganda) `[ISO-3: UGA / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `300,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,760,000,000` 人
  * **2026年當代等效規模**：**`650,266` 人** (放縮係數：2.17x)
  * **區域人口衝擊率**：**`2.8571%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 獨裁者伊迪·阿敏發動政變奪權後，建立國家研究局（SRB）與公共安全股（PSU）等恐怖秘密警察機構，對阿喬利族（Acholi）和蘭戈族（Lango）軍人及平民實施滅絕性清洗。阿敏更下令驅逐8萬名亞裔公民沒收其財產，並公開處決最高法院首席大法官、坎帕拉大主教及無數知識分子，受害者遺體被大規模拋入尼羅河餵食鱷魚。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際法學家委員會 (International Commission of Jurists, ICJ 1977 年報告指控阿敏犯下危害人類罪); 國際特赦組織 (Amnesty International 系列調查); Alicia C. Decker (2014, 'In Idi Amin's Shadow', Ohio Univ Press); Phares Mutibwa (1992, 'Uganda Since Independence').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 阿敏政權統治時期完全不留書面司法處決審判記錄，逮捕直接等同於秘密私刑處決；1979年坦尚尼亞軍隊攻克坎帕拉時多數酷刑中心已人去樓空，確切罹難人數主要由國際法學家委員會與難民口述統計。`


### [EVT-1969-BRA-002] 巴西軍政府阿拉瓜亞游擊隊密林大清洗與強迫失蹤 (Guerrilha do Araguaia Counter-Insurgency Democide)
* **起止年份**：1972 – 1975
* **地理位置**：巴西托坎廷斯州、帕拉州阿拉瓜亞河流域 (Araguaia, Brazil) `[ISO-3: BRA / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `70` 人 / 中標基準 `90` 人 / 高標 `120` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,837,500,000` 人
  * **2026年當代等效規模**：**`191` 人** (放縮係數：2.12x)
  * **區域人口衝擊率**：**`0.9%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 巴西軍政府調動近萬名特種部隊與空軍直升機，對亞馬遜叢林中數十名巴西共產黨反對派青年展開代號'清理行動'的毀滅性圍剿。軍方下達'不留活口'秘密命令，對受傷被俘的青年學生實施殘酷肉體酷刑、斬首、將遺體藏於秘密軍事基地或用直升機運往無人雨林深處掩埋，並嚴厲刑求當地無辜原住民農民以逼供。
* **學術文獻引用摘要 (`sources_summary`)**：
  美洲人權法院 (IACHR, 2010 'Gomes Lund et al. v. Brazil' 歷史性判決認定巴西軍隊犯下強迫失蹤與危害人類罪); 巴西國家真相委員會 (CNV 2014); Taís Morais & Eumano Silva (2005, 'Operação Araguaia').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / IACHR International Judgment] 美洲人權法院裁定巴西1979年大赦法違反國際人權公約無效，下令巴西政府追查遺骸；巴西軍隊至今以'檔案已銷毀'為由拒絕交出埋屍坐標，此案成為巴西轉型正義指標性案件。`


### [EVT-1972-BDI-001] 布隆迪選擇性種族滅絕（Ikiza 恐怖） (Burundi Ikiza – Selective Genocide of Hutus)
* **起止年份**：1972
* **地理位置**：布隆迪 (Burundi) `[ISO-3: BDI / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `150,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,837,500,000` 人
  * **2026年當代等效規模**：**`318,567` 人** (放縮係數：2.12x)
  * **區域人口衝擊率**：**`4.1667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 圖西族軍政府米孔貝羅（Michel Micombero）在鎮壓胡圖族起義後，展開蓄意針對胡圖族（Hutu）受教育精英之選擇性屠殺：系統性搜捕所有具備讀寫能力、擁有政府職位或接受過教育的胡圖族男性，包括小學生、技師、神職人員，以軍卡逐村逮捕後集體槍決，旨在從結構上消滅胡圖族未來的政治領導層。
* **學術文獻引用摘要 (`sources_summary`)**：
  René Lemarchand (1974, 'Selective Genocide in Burundi', Minority Rights Group Report); Michael Bowen, Gary Freeman & Kay Miller (1973, 'Passing By: The United States and Genocide in Burundi', Carnegie Endowment for International Peace); 聯合國大會第3074號決議; Christian Scherrer (2002)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 當時國際社會與新聞媒體對此事件保持近乎完全的沉默（美國卡內基國際和平基金會研究題目即為「一場被忽略的種族滅絕」）；布隆迪軍政府管控所有媒體，聯合國未採取任何實質行動，大量原始檔案已不可尋。`


### [EVT-1972-PHL-003] 菲律賓馬可仕戒嚴時期法外處決、酷刑與賈比達屠殺 (Marcos Martial Law Democide, Torture and Jabidah Massacre)
* **起止年份**：1972 – 1986
* **地理位置**：菲律賓全境（馬尼拉、棉蘭老島、科雷希多島）(Philippines) `[ISO-3: PHL / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `3,257` 人 / 中標基準 `5,000` 人 / 高標 `10,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,837,500,000` 人
  * **2026年當代等效規模**：**`10,619` 人** (放縮係數：2.12x)
  * **區域人口衝擊率**：**`0.0119%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 費迪南德·馬可仕宣布全境戒嚴以維持獨裁統治，軍警安全部門推行'搜戮'（Salvaging，即法外處決俚語），在路旁拋屍處決學生運動家、工會組織者與記者。1968年軍方更在科雷希多島秘密集體槍決受訓拒絕滲透沙巴的數十名穆斯林新兵（賈比達屠殺Jabidah Massacre），引發南部棉蘭老島摩洛民族解放陣線長達數十年的流血內戰。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際特赦組織 (1976/1981 系列戒嚴報告，記錄3,257起法外處決、35,000名酷刑受害者、70,000人被拘留); Alfred W. McCoy (1999, 'Closer than Brothers: Manhood at the Philippine Military Academy'); 菲律賓人權受害者索賠委員會 (HRVCB 2018 官方認證報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] 1995年美國夏威夷聯邦地方法院依外國人侵權法判決馬可仕遺產向近萬名菲律賓人權受害者賠償近20億美元；2013年菲律賓國會立法設立索賠委員會，逐一核發補償。`


### [EVT-1973-CHL-001] 智利皮諾契特獨裁政權大清洗與法外處決 (Pinochet Dictatorship Purges and Rettig Commission Dossier)
* **起止年份**：1973 – 1990
* **地理位置**：智利 (Chile) `[ISO-3: CHL / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `3,065` 人 / 中標基準 `3,225` 人 / 高標 `4,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`3,915,000,000` 人
  * **2026年當代等效規模**：**`6,714` 人** (放縮係數：2.08x)
  * **區域人口衝擊率**：**`0.0323%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 陸軍總司令皮諾契特發動政變推翻民選總統阿葉德後，建立國家情報局（DINA）在國家體育館等場所實施大規模秘密逮捕、酷刑與即決處決。軍方啟動'死亡大篷車'（Caravan of Death）赴各省清洗左翼政治犯，並聯手南美軍政府實施跨國獵殺異議人士的'禿鷹行動'（Operation Condor）。
* **學術文獻引用摘要 (`sources_summary`)**：
  雷蒂格委員會 (Rettig Commission, 1991 智利真相與和解國家委員會官方報告，正式核實 3,197 名被殺害與強迫失蹤者); 法萊奇委員會 (Valech Report, 2004/2011 記錄 38,254 名酷刑倖存者); 美國國家安全檔案館解密CIA智利檔案; Steve J. Stern (2006, 'Battling for Hearts and Minds').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] 智利在民主轉型後透過官方真相委員會完整建立了個體檔案與DNA資料庫，軍方秘密銷毀的直升機'死亡飛行'（將犯人綁鐵軌投入太平洋）死難名冊近年透過前軍官供詞逐一重建。`


### [EVT-1975-IND-001] 印度緊急狀態強制絕育運動 (Indian Emergency Period Forced Sterilization Campaign)
* **起止年份**：1975 – 1977
* **地理位置**：印度全境 (India) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `1,774` 人 / 中標基準 `3,387` 人 / 高標 `5,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,070,000,000` 人
  * **2026年當代等效規模**：**`6,782` 人** (放縮係數：2.0x)
  * **區域人口衝擊率**：**`0.0005%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 在甘地總理宣布的全國緊急狀態期間，政府推行極端人口控制政策，將公務員薪資、房屋配給及教師考核與絕育配額嚴格掛鉤。地方官員與警方以突襲與斷糧威脅將底層貧民強押至簡陋帳篷進行批量輸精管切除手術，導致大規模術後感染、破傷風及警民衝突（如突克曼門事件）致死慘劇。
* **學術文獻引用摘要 (`sources_summary`)**：
  Shah Commission of Inquiry (1978 官方調查委員會第三期暨最終報告) 記錄 1,774 起絕育直接致死撫卹案；Matthew Connelly (2008, 'Fatal Misconception', Harvard Univ Press) 與 Marika Vicziany (1982, 'Coercion in a Soft State')；全期遭強制絕育人數逾 830 萬人。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 緊急狀態期間實施嚴格新聞檢查與紀錄封鎖，大批地方流動營地之術後死亡、嚴重感染截肢與抗爭鎮壓死傷遭隱匿或登記為普通急病。沙阿委員會報告於國大黨重返執政後曾遭官方低調回收封存，致使全國性完整死亡與殘疾總數難以全面解密歸檔。`


### [EVT-1975-KHM-001] 柬埔寨紅色高棉萬人塚與種族滅絕 (Khmer Rouge Killing Fields and Genocide)
* **起止年份**：1975 – 1979
* **地理位置**：民主柬埔寨 (Democratic Kampuchea / Cambodia) `[ISO-3: KHM / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500,000` 人 / 中標基準 `1,800,000` 人 / 高標 `2,200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,070,000,000` 人
  * **2026年當代等效規模**：**`3,604,423` 人** (放縮係數：2.0x)
  * **區域人口衝擊率**：**`24.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 波布率領的紅色高棉奪取政權後，強行在48小時內清空首都金邊等所有城市人口，將全體國民驅逐至農村公社。政權推行極端原始共產主義與階級清洗，系統性肉體消滅前公務員、教師、醫生、華裔、占族穆斯林及戴眼鏡等「知識階層」，逾五分之一人口死於S-21酷刑中心、田間勞役折磨與飢饉。
* **學術文獻引用摘要 (`sources_summary`)**：
  Ben Kiernan (1996, 'The Pol Pot Regime: Race, Power, and Genocide in Cambodia under the Khmer Rouge'); David Chandler (1999, 'Voices from S-21'); 柬埔寨法院特別法庭 (ECCC, 聯合國支持國際法庭判決書); Documentation Center of Cambodia (DC-Cam 萬人坑製圖計畫)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Scrutiny] 柬埔寨文獻中心（DC-Cam）繪製了全境近兩萬個萬人坑（Killing Fields）之GPS座標，ECCC法庭正式裁定其對占族與越南裔犯下種族滅絕罪，歷史證據具高度法律與學術權威性。`


### [EVT-1975-TLS-001] 東帝汶印度尼西亞佔領期屠殺與人為飢饉 (East Timor Genocide and Indonesian Occupation)
* **起止年份**：1975 – 1999
* **地理位置**：東帝汶 (East Timor / Timor-Leste) `[ISO-3: TLS / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `150,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,070,000,000` 人
  * **2026年當代等效規模**：**`300,369` 人** (放縮係數：2.0x)
  * **區域人口衝擊率**：**`23.0769%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 印尼蘇哈托軍隊在美澳默許下入侵剛脫離葡萄牙獨立的東帝汶，執行代號「蓮花行動」。印尼軍隊對抵抗平民展開焦土掃蕩，實施強制重新定居營地、摧毀農田並斷絕糧藥供應，導致全境近三分之一的原住民人口因屠殺、飢荒與肺結核滅絕。
* **學術文獻引用摘要 (`sources_summary`)**：
  東帝汶接待、真相與和解委員會 (CAVR 官方報告 'Chega!', 2005); John Taylor (1991, 'Indonesia's Forgotten War'); Ben Kiernan (2007, 'Blood and Soil'); 聯合國人權理事會報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 印尼軍方完全封鎖東帝汶達十餘年，禁止外國記者與人權組織入境；1991年聖克魯斯公墓屠殺（Santa Cruz Massacre）被英國記者偷偷錄影帶出境後，真相始公諸於世。`


### [EVT-1976-ARG-001] 阿根廷軍政府「骯髒戰爭」強迫失蹤與秘密處決 (Argentina Dirty War – Forced Disappearances and Extrajudicial Killings)
* **起止年份**：1976 – 1983
* **地理位置**：阿根廷 (Argentina) `[ISO-3: ARG / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `20,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,146,000,000` 人
  * **2026年當代等效規模**：**`39,315` 人** (放縮係數：1.97x)
  * **區域人口衝擊率**：**`0.0769%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 豬灣軍政府（1976年3月政變後）啟動代號「過程」（El Proceso）之系統性鎮壓，設立如海軍機械學校（ESMA）等約340所秘密拘留酷刑中心，將政治異見人士（Desaparecidos，即「消失者」）在未經司法程序下秘密逮捕、系統性虐殺後沉屍河海或空中投入拉布拉他河，並竊奪受害者孕婦所生嬰兒重新安置給軍方親信。
* **學術文獻引用摘要 (`sources_summary`)**：
  CONADEP（阿根廷國家失蹤人口調查委員會, 1984,《永不再犯》報告，記錄確認 8,960 人，估算總數 30,000 人）; Marguerite Feitlowitz (1998, 'A Lexicon of Terror'); 法庭判決書（前總統魏地拉、馬塞拉等軍事領袖的國家恐怖主義罪定罪）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] CONADEP報告、後續多次審判及阿根廷法醫人類學小組（EAAF）DNA鑑定構成高度詳盡的文獻體系；確切總死亡數因許多遺體永久沉於海底而無法精確確認。`


### [EVT-1977-ETH-005] 衣索比亞德格軍政府「紅色恐怖」政治大屠殺 (Ethiopian Red Terror (Qey Shibir))
* **起止年份**：1977 – 1978
* **地理位置**：衣索比亞阿迪斯阿貝巴及主要城市 (Ethiopia) `[ISO-3: ETH / 大洲: Africa]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `30,000` 人 / 中標基準 `100,000` 人 / 高標 `500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,222,000,000` 人
  * **2026年當代等效規模**：**`193,036` 人** (放縮係數：1.93x)
  * **區域人口衝擊率**：**`0.2857%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 門格斯圖在革命廣場摔碎盛滿紅墨水的瓶子宣布啟動'紅色恐怖'，以消滅衣索比亞人民革命黨（EPRP）等異議團體。軍警與'凱貝萊'（Kebele）民兵在街頭隨意逮捕青年學生與工會領袖，在監獄實施倒吊毆打、水刑處決，並將數以萬計的死刑犯屍體棄置街頭，家屬甚至必須向軍警支付'贖子彈費'方能領回親人遺體。
* **學術文獻引用摘要 (`sources_summary`)**：
  人權觀察 (Human Rights Watch, 1991, 'Evil Days'); 衣索比亞特別檢察官辦公室 (SPO 2006 歷史性審判判定門格斯圖種族滅絕與危害人類罪成立); 國際特赦組織 (1978 報告指控數萬青年被處決); Babile Tola (1989, 'To Kill a Generation').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] 1991年德格政權垮台後，衣索比亞特別檢察官歷經十二年公開審判，動用數噸軍政府簽署之處決公文定罪門格斯圖與數百名前高官，在首都建立了'紅色恐怖烈士紀念博物館'。`


### [EVT-1979-AFG-001] 蘇聯阿富汗戰爭蘇軍焦土轟炸、平民屠殺與人為飢饉 (Soviet-Afghan War Civilian Atrocities, Depopulation and Landmines)
* **起止年份**：1979 – 1989
* **地理位置**：阿富汗全境（帕克蒂亞、楠格哈爾、潘傑希爾等）(Afghanistan) `[ISO-3: AFG / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `560,000` 人 / 中標基準 `1,000,000` 人 / 高標 `2,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,374,000,000` 人
  * **2026年當代等效規模**：**`1,863,283` 人** (放縮係數：1.86x)
  * **區域人口衝擊率**：**`7.6923%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇聯出兵佔領阿富汗後，為粉碎游擊隊實施'去人口化焦土戰略'（Depopulation）。蘇軍戰機對阿富汗農村實施地毯式轟炸、摧毀古老地下坎兒井灌溉系統以製造人為飢饉、投擲數百萬枚偽裝成玩具的蝴蝶地雷（PFM-1）致殘無數平民兒童，並在拉格曼省、庫納爾省等地實施整村集體槍決，造成阿富汗三分之一人口流亡巴基斯坦與伊朗，上百萬平民非正常死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  M. Hasan Kakar (1995, 'Afghanistan: The Soviet Invasion and the Afghan Response, 1979–1982', Univ of California Press 認定構成國家恐怖主義與種族滅絕); 聯合國人權委員會菲利克斯·埃馬科拉調查報告 (Felix Ermacora 1985); Noor Ahmad Khalidi (1991, UN Population Studies); 國際特赦組織檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / UN Special Rapporteur Records] 聯合國大會連續十年通過決議譴責蘇聯侵略，埃馬科拉特使深入難民營取得了極為詳盡的空襲傷亡法醫數據；蘇聯解體後俄羅斯國會亦正式通過決議譴責出兵阿富汗為嚴重政治錯誤。`


### [EVT-1980-CHN-003] 中國一胎化強制作業與百日無孩運動 (Coercive Family Planning Phase & Childless Hundred Days)
* **起止年份**：1980 – 1991
* **地理位置**：中國全境（山東冠縣、莘縣等重點試驗區）(People's Republic of China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `20,000` 人 / 中標基準 `50,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,450,000,000` 人
  * **2026年當代等效規模**：**`91,573` 人** (放縮係數：1.83x)
  * **區域人口衝擊率**：**`0.0051%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 中共自1980年代起將計劃生育定為基本國策，實行幹部一票否決制。在1991年山東冠縣與莘縣發起的「百日無孩」運動中，地方官員為消除超生指標，下令在百日內全縣不得有嬰兒出生，對所有孕婦實施強制大月份引產、強制結紮，導致大量新生兒直接遭溺殺遺棄及產婦因粗暴手術致死致殘。
* **學術文獻引用摘要 (`sources_summary`)**：
  Kay Ann Johnson (2016, 'China's Hidden Children', Univ of Chicago Press); 梁中堂 (前國家計生委專家委員會委員專題論著); 國際特赦組織 (Amnesty International 1990年代人權報告); 山東冠縣地方縣誌記載之「百日無孩」運動口述史。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 涉及強制大月份引產之具體母嬰致死傷亡人數在官方統計中完全隱匿，相關計生檔案、大月份引產手術記錄與被遺棄女嬰名單均為國家保密範疇，多數數據僅能透過地方官員口述回憶與人口普查性別比異常回推。`


### [EVT-1980-KOR-003] 韓國光州五一八民主化運動武力鎮壓與平民屠殺 (Gwangju Democratization Movement Military Massacre)
* **起止年份**：1980
* **地理位置**：韓國全羅南道光州市 (Gwangju, South Korea) `[ISO-3: KOR / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `165` 人 / 中標基準 `606` 人 / 高標 `2,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,450,000,000` 人
  * **2026年當代等效規模**：**`1,110` 人** (放縮係數：1.83x)
  * **區域人口衝擊率**：**`0.0757%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 雙十二政變奪權的新軍部首腦全斗煥下達全境戒嚴令，派遣陸軍特戰空降旅（第七、第十一空輸旅）進駐光州。空降兵部隊使用帶刺刀步槍、M16實彈及催淚瓦斯，對和平示威學生及路過市民進行無差別刺殺、脫衣毆打與坦克碾壓；全斗煥隨後指派軍隊封鎖全市，對佔領全羅南道道廳之市民軍發動代號'尚武忠正作戰'血腥清剿。
* **學術文獻引用摘要 (`sources_summary`)**：
  韓國國立5·18民主墓地官方核實死傷者名錄; 5·18民衆抗爭戒嚴司令部解密作戰日誌; 尤爾根·辛茲佩特（Jürgen Hinzpeter）德國記者目擊影像檔案; 首爾高等法院1996年審判全斗煥、盧泰愚內亂罪判決書。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] 新軍部在事後十餘年間嚴格管控新聞出版並將死難者遺體秘密埋葬於望月洞荒墳；1996年韓國最高法院裁定全斗煥犯下內亂首魁罪與軍事叛亂罪並判處死刑（後特赦），光州檔案已列入聯合國教科文組織世界記憶遺產。`


### [EVT-1981-GTM-001] 瓜地馬拉馬雅原住民大屠殺 (沉默的大屠殺) (Guatemalan Maya Genocide (Silent Holocaust))
* **起止年份**：1981 – 1983
* **地理位置**：瓜地馬拉奎切省及西部高地 (Guatemala) `[ISO-3: GTM / 大洲: Americas]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `100,000` 人 / 中標基準 `140,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,530,000,000` 人
  * **2026年當代等效規模**：**`251,876` 人** (放縮係數：1.8x)
  * **區域人口衝擊率**：**`1.9444%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 美軍支持的埃弗拉因·里奧斯·蒙特軍事獨裁政權推行「焦土政策」，宣稱「為消滅游擊隊之魚，必須抽乾馬雅人這池水」。政府軍與民間自衛巡邏隊夷平了626個馬雅原住民村莊，將孕婦剖腹、將嬰兒撞死在樹幹上，並對馬雅伊西爾族（Ixil Maya）實施種族滅絕式屠戮。
* **學術文獻引用摘要 (`sources_summary`)**：
  瓜地馬拉歷史澄清委員會 (CEH 聯合國支持真相委員會報告 'Guatemala: Memory of Silence', 1999 認定構成種族滅絕); 里奧斯·蒙特（Efraín Ríos Montt）種族滅絕審判判決書; 美國國家安全檔案館解密CIA情報。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Conviction] 2013年瓜地馬拉法院正式判決前獨裁者蒙特種族滅絕罪名成立（雖隨後遭保守派憲法法庭阻撓技術性撤銷），法醫人類學基金會（FAFG）藉由DNA比對完成了上百處萬人坑遺骸挖掘與身分判定。`


### [EVT-1982-LBN-002] 黎巴嫩薩布拉與沙提拉難民營大屠殺 (Sabra and Shatila Massacre in Beirut)
* **起止年份**：1982
* **地理位置**：黎巴嫩貝魯特南部薩布拉與沙提拉巴勒斯坦難民營 (Beirut, Lebanon) `[ISO-3: LBN / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `762` 人 / 中標基準 `1,700` 人 / 高標 `3,500` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,605,000,000` 人
  * **2026年當代等效規模**：**`3,009` 人** (放縮係數：1.77x)
  * **區域人口衝擊率**：**`8.5%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 以色列軍隊包圍西貝魯特後，國防部長艾里爾·沙龍批准黎巴嫩基督教長槍黨民兵（Phalangists）進入無武裝的薩布拉與沙提拉難民營清剿巴解組織殘餘。長槍黨民兵在營內展開連續四十小時的滅門屠殺，以色列軍隊在營外發射照明彈照亮街道並封鎖出口阻止難民逃生，大批巴勒斯坦婦女遭強姦後處決、幼童與嬰兒在睡夢中遭劈死。
* **學術文獻引用摘要 (`sources_summary`)**：
  以色列官方卡漢調查委員會 (Kahan Commission 1983 報告，認定國防部長沙龍負有個人間接責任); 聯合國大會第37/123號決議（定性為種族滅絕行為）; 國際紅十字會 (ICRC) 現場點驗名冊; Bayan Nuwayhed al-Hout (2004, 'Sabra and Shatila: September 1982').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Official Commission Report] 屠殺引發以色列國內四十萬人抗議集會，促成以色列政府設立司法卡漢委員會；涉案的黎巴嫩長槍黨軍閥隨後在黎巴嫩內戰大赦法案下未受起訴，確切死難總數因大量遺體被推土機掩埋於無名集體墓塚而存在區間差距。`


### [EVT-1982-SYR-002] 敘利亞哈馬大屠殺 (1982 Hama Massacre by Hafez al-Assad)
* **起止年份**：1982
* **地理位置**：敘利亞哈馬市 (Hama, Syria) `[ISO-3: SYR / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `25,000` 人 / 高標 `40,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,605,000,000` 人
  * **2026年當代等效規模**：**`44,245` 人** (放縮係數：1.77x)
  * **區域人口衝擊率**：**`10.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 敘利亞總統哈菲茲·阿薩德（現總統巴夏爾之父）為徹底粉碎穆斯林兄弟會起義，指派其胞弟里法特·阿薩德指揮國防特遣隊包圍第四大城市哈馬。軍隊動用T-72重型坦克、火砲與重型空襲地毯式轟炸老城區達三個星期，隨後派遣突擊隊逐戶搜捕處決全部男性居民，三分之一的歷史城區被推土機徹底夷為平地。
* **學術文獻引用摘要 (`sources_summary`)**：
  人權觀察 (Human Rights Watch, 1996, 'Syria's Tadmor Prison'); Patrick Seale (1988, 'Asad of Syria: The Struggle for the Middle East'); 美國國防情報局 (DIA 1982 解密評估報告估算約2萬人死亡); 國際特赦組織報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 阿薩德家族政權在國內實施極端新聞封鎖，數十年間在敘利亞境內提及'哈馬'事件即面臨叛國罪長期監禁；廢墟之上被政府直接興建為新市鎮與停車場以湮滅地表罪證。`


### [EVT-1983-ETH-002] 衣索比亞德格軍政府內戰圍困與大饑荒 (1983–1985 Ethiopian Famine and Derg Counter-Insurgency)
* **起止年份**：1983 – 1985
* **地理位置**：衣索比亞沃洛、提格雷及厄利垂亞 (Ethiopia) `[ISO-3: ETH / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `400,000` 人 / 中標基準 `800,000` 人 / 高標 `1,200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,680,000,000` 人
  * **2026年當代等效規模**：**`1,393,162` 人** (放縮係數：1.74x)
  * **區域人口衝擊率**：**`2.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 門格斯圖領導的親蘇馬克思主義'德格'（Derg）軍政府為鎮壓北部叛亂，在乾旱來臨時將國際人道糧食援助作為軍事武器，刻意阻絕物資進入反叛區域。軍政府耗資上億美元在首都大肆慶祝政權十週年而封鎖災情，並強行實施殘酷的'強制重新安置'（Resettlement）政策，將數十萬北方農民用軍卡與飛機強押至南部叢林，導致數十萬人在遷徙營地與途中飢病倒斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  人權觀察 (Human Rights Watch, 1991, 'Evil Days: Thirty Years of War and Famine in Ethiopia', Alex de Waal 深入分析證明軍事反叛亂政策加劇了致命性); Amartya Sen (1981); Dawit Wolde Giorgis (前衣索比亞救濟與康復委員會主席回憶錄 'Red Tears', 1989); 聯合國非洲應急行動辦公室 (OEOA)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Archives] 該災難透過BBC記者邁克爾·布爾克（Michael Buerk）鏡頭曝光震撼世界並催生'Live Aid'慈善演唱會；1991年德格政權倒台後，衣索比亞特別檢察官辦公室以種族滅絕與危害人類罪對門格斯圖等人進行了缺席審判。`


### [EVT-1983-LKA-001] 斯里蘭卡「黑色七月」反泰米爾人大屠殺與內戰平民砲擊 (Black July Pogrom and Sri Lankan Civil War Civilian Shelling)
* **起止年份**：1983 – 2009
* **地理位置**：斯里蘭卡全境（可倫坡、賈夫納半島、穆萊蒂武）(Sri Lanka) `[ISO-3: LKA / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `40,000` 人 / 中標基準 `70,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,680,000,000` 人
  * **2026年當代等效規模**：**`121,902` 人** (放縮係數：1.74x)
  * **區域人口衝擊率**：**`0.3889%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 1983年7月，僧伽羅極端暴民持有政府選民名冊，在首都可倫坡對泰米爾少數民族展開焚掠屠殺，警方坐視不管，引發全面內戰。2009年內戰決戰階段，政府軍將數十萬泰米爾平民逼入極狹窄的'無火區'（No Fire Zone），並動用重砲、集群火箭與空襲對野戰醫院與難民帳篷實施無差別轟炸，泰米爾猛虎組織亦扣押平民作為人肉盾牌，引發慘絕人寰的平民人道災難。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國秘書長斯里蘭卡問責問題專家小組報告 (Darusman Report, 2011 認定2009年最後戰役幾個月內多達4萬名平民死亡); 斯里蘭卡官方桑薩尼調查委員會 (Sansi Commission); 人權觀察 (HRW 2009); Gordon Weiss (2011, 'The Cage: The Fight for Sri Lanka and the Last Days of the Tamil Tigers').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 斯里蘭卡政府在2009年最後階段完全驅逐所有國際媒體、聯合國救援人員與非政府組織，對交戰區實施完全信息黑箱；戰後歷屆政府拒絕接受任何獨立的聯合國國際戰爭罪調查。`


### [EVT-1983-SDN-002] 第二次蘇丹內戰人為饑荒與焦土清剿 (Second Sudanese Civil War Famines and Depopulation)
* **起止年份**：1983 – 2005
* **地理位置**：南蘇丹巴哈爾加札爾及努巴山脈 (Sudan / modern South Sudan) `[ISO-3: SSD / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `1,500,000` 人 / 中標基準 `2,000,000` 人 / 高標 `2,500,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,680,000,000` 人
  * **2026年當代等效規模**：**`3,482,906` 人** (放縮係數：1.74x)
  * **區域人口衝擊率**：**`25.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 喀土穆伊斯蘭軍政府為掠奪南部油田與鎮壓南蘇丹反政府武裝，武裝北方的「穆拉哈林」（Murahaleen）阿拉伯民兵對丁卡族等原住民村落進行焦土突襲。民兵搶劫牛群、摧毀穀物、綁架婦孺為奴，並多次阻斷聯合國OLS救援飛機降落，導致1988年與1998年連續爆發兩場造成數十萬人飢斃的人為慘劇。
* **學術文獻引用摘要 (`sources_summary`)**：
  美國和平研究所 (USIP 專題報告); 亞歷克斯·德瓦爾 (Alex de Waal, 1997, 'Famine Crimes'); Human Rights Watch (1998, 'Famine in Sudan, 1998'); 聯合國終身生命線行動 (Operation Lifeline Sudan, OLS)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 跨越22年的內戰導致南蘇丹完全失去道路、通信與行政機構，數百萬流亡兒童（蘇丹失散男孩Lost Boys）穿過沙漠逃亡衣索比亞與肯亞，實際死亡人數多依據跨期人口損失模型估算。`


### [EVT-1983-ZWE-001] 辛巴威穆加比「古庫拉胡恩迪」恩德貝勒族大屠殺 (Gukurahundi Massacres in Matabeleland)
* **起止年份**：1983 – 1987
* **地理位置**：辛巴威馬塔貝萊蘭及米德蘭茲 (Matabeleland, Zimbabwe) `[ISO-3: ZWE / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `20,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,680,000,000` 人
  * **2026年當代等效規模**：**`34,829` 人** (放縮係數：1.74x)
  * **區域人口衝擊率**：**`0.2564%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 穆加比總理調動由北韓軍事教官單獨訓練的辛巴威國防軍第五旅（Fifth Brigade），以清剿'反叛分子'為名，對少數民族恩德貝勒族（Ndebele）聚居區實施地毯式殘酷清洗。第五旅將整個村莊的村民鎖在草屋中活活燒死、強迫受害者自挖萬人坑後集體處決，並實施禁糧封鎖導致數萬平民餓斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  辛巴威天主教正義與和平委員會 (CCJP) 與法律資源基金會 (LRF 1997 聯合調查報告 《Breaking the Silence: Building True Peace》); Jocelyn Alexander et al. (2000, 'Violence and Memory: One Hundred Years in the 'Dark Forests' of Matabeleland'); 查帕姆巴拉委員會 (Chihambakwe Commission) 遭政府封存之官方報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 辛巴威政府將官方調查報告（查帕姆巴拉調查）列為最高機密永久封存，穆加比生前僅稱其為'瘋狂時期'而拒絕正式道歉與法律調查；在辛巴威境內公開紀念古庫拉胡恩迪死難者常年遭警方騷擾與鎮壓。`


### [EVT-1984-IND-004] 1984年印度反錫克教徒大屠殺 (1984 Anti-Sikh Pogroms)
* **起止年份**：1984
* **地理位置**：印度德里及旁遮普邦周邊 (Delhi, India) `[ISO-3: IND / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `2,800` 人 / 中標基準 `3,350` 人 / 高標 `8,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,763,333,333` 人
  * **2026年當代等效規模**：**`5,732` 人** (放縮係數：1.71x)
  * **區域人口衝擊率**：**`0.0004%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 英迪拉·甘地總理遭其錫克教保鑣刺殺後，執政的國大黨激進政客與暴民組織利用選民名冊，在首都德里等地對錫克教徒展開長達四天的有組織血腥暴動。暴徒配備鐵棒、煤油與輪胎，將錫克男性套上輪胎點火焚燒（胎刑頸輪Necklacing）、洗劫焚毀錫克教廟宇與商業店鋪，警方受命收繳錫克自衛武器並放任暴民屠殺。
* **學術文獻引用摘要 (`sources_summary`)**：
  納納瓦蒂司法調查委員會 (Nanavati Commission 2005 官方調查報告，認定執政國大黨高層涉案並批評警方蓄意不作為); 米斯拉委員會 (Misra Commission 1986); 人民自由聯盟 (PUCL) 與公民民主權利委員會 (PUDR 1984 《Who Are The Guilty?》即時調查); 德里高等法院2018年定罪前國大黨議員庫馬爾（Sajjan Kumar）終身監禁判決書。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 歷屆印度政府歷經十餘個司法調查委員會反覆拖延與包庇，多數關鍵涉案政治人物長年逃脫法律追究；德里警方曾系統性拒絕為受害者立案（FIR）或銷毀報警電話記錄，直至案發三十餘年後始有少數政客獲罪。`


### [EVT-1988-IRQ-001] 伊拉克安法爾戰役與哈拉卜賈化武大屠殺 (Anfal Campaign and Halabja Chemical Attack)
* **起止年份**：1986 – 1989
* **地理位置**：伊拉克北部庫德斯坦 (Iraqi Kurdistan) `[ISO-3: IRQ / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `50,000` 人 / 中標基準 `100,000` 人 / 高標 `182,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`4,930,000,000` 人
  * **2026年當代等效規模**：**`165,314` 人** (放縮係數：1.65x)
  * **區域人口衝擊率**：**`2.8571%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 海珊政權委派其表弟「化學阿里」馬吉德指揮安法爾行動，針對伊拉克北部庫德族展開系統性焦土清剿。政府軍對庫德村落動用芥子毒氣、沙林等化學武器（如哈拉卜賈毒氣襲擊），並將抓獲之數萬名非戰鬥人員（包括老弱婦孺）押送至南部荒漠進行集中處決與萬人坑掩埋。
* **學術文獻引用摘要 (`sources_summary`)**：
  Human Rights Watch (1993, 'Genocide in Iraq: The Anfal Campaign Against the Kurds'); 伊拉克特別法庭 (Iraqi High Tribunal 2007 年審判阿里·哈桑·馬吉德判決書); Joost Hiltermann (2007, 'A Poisonous Affair').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Post-War Judicial Records] 美軍攻佔巴格達後繳獲數噸復興黨絕密內部錄音與軍令公文，完整記錄了馬吉德下達毒氣攻擊與人口清除之指令，審判中多個大型萬人坑完成法醫開棺鑑定。`


### [EVT-1988-IRN-001] 1988年伊朗政治犯秘密大處決（死亡委員會） (1988 Executions of Iranian Political Prisoners)
* **起止年份**：1988
* **地理位置**：伊朗全境（埃溫監獄、戈哈達什特監獄等）(Iran) `[ISO-3: IRN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `2,800` 人 / 中標基準 `5,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,136,666,666` 人
  * **2026年當代等效規模**：**`7,933` 人** (放縮係數：1.59x)
  * **區域人口衝擊率**：**`0.0096%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 兩伊戰爭結束前夕，最高領袖霍梅尼頒布秘密宗教裁判法令，成立由四人組成的'死亡委員會'（Death Commissions，現任總統萊希曾為成員之一）。委員會在埃溫與戈哈達什特監獄對已服刑數年的數千名左翼政治犯與人民聖戰者組織（MEK）成員進行每人僅數分鐘的宗教效忠盤問，凡拒絕誓死效忠者直接被成批押往刑場絞死，屍體被冷藏卡車秘密運往德黑蘭卡瓦朗等無名集體墓地掩埋。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際特赦組織 (Amnesty International 2018 專題調查報告 《Blood-soaked Secrets: Why Iran's 1988 prison massacres are ongoing crimes against humanity》); 聯合國伊朗人權特別報告員報告; 蒙塔澤里大阿亞圖拉（Ayatollah Montazeri 1988內部秘密錄音指責'這是伊斯蘭共和國犯下的最大罪行'）; 瑞典斯德哥爾摩地方法院2022年依普遍管轄權判處涉案伊朗官員哈米德·努里（Hamid Noury）終身監禁。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 伊朗伊斯蘭共和國嚴禁家屬公開祭奠與追查遺體，卡瓦朗萬人坑遭水泥推平掩蓋；伊朗當局在各級國際場合對處決人數完全否認並封鎖死因證明，聯合國特別報告員長年被拒絕入境實地調查。`


### [EVT-1989-CHN-004] 六四天安門事件武力清場與平民屠殺 (Tiananmen Square Military Crackdown and Massacre)
* **起止年份**：1989
* **地理位置**：中國北京天安門廣場及長安街 (Beijing, China) `[ISO-3: CHN / 大洲: Asia]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `300` 人 / 中標基準 `1,000` 人 / 高標 `3,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,240,000,000` 人
  * **2026年當代等效規模**：**`1,555` 人** (放縮係數：1.56x)
  * **區域人口衝擊率**：**`0.0093%`**
* **學界共識度**：`State Suppressed`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 中共中央調動20餘萬戒嚴部隊配備裝甲車與步槍，對北京和平示威之大學生與市民進行流血武力清場。部隊在木樨地、西單及長安街沿途對手無寸鐵之平民展開實彈密集掃射並以坦克推進，造成大量學生與市民死傷。
* **學術文獻引用摘要 (`sources_summary`)**：
  天安門母親群體 (丁子霖主持之確鑿遇難者名冊，核實202人); 英國解密外交檔案 (大使唐納德爵士電報稱估計2,700-3,400人); 美國解密國務院電報 (估計數百至數千人); 中國國務院發言人袁木官方通報 (稱死近300人含軍人); Timothy Brook (1998, 'Quelling the People').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 中共當局將事件嚴密封鎖三十餘年，嚴禁家屬公開祭奠與任何獨立司法調查，醫院病歷與火葬場登記資料遭軍警強行沒收管制；精確死難總數因國家全面抹除痕跡而無法取得統一公認數字。`


### [EVT-1989-LBR-001] 賴比瑞亞與獅子山內戰肢解殘害、血鑽石奴役與童兵慘劇 (Liberian and Sierra Leonean Civil Wars Democide and Mutilations)
* **起止年份**：1989 – 2003
* **地理位置**：賴比瑞亞與獅子山 (Liberia & Sierra Leone) `[ISO-3: LBR / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `250,000` 人 / 中標基準 `300,000` 人 / 高標 `350,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,240,000,000` 人
  * **2026年當代等效規模**：**`466,603` 人** (放縮係數：1.56x)
  * **區域人口衝擊率**：**`4.2857%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 查爾斯·泰勒領導的全國愛國陣線與福迪·桑科的革命聯合陣線（RUF）為爭奪血鑽石礦區，在西非發動極度野蠻的內戰。叛軍大量給予毒品強征幼童組成童兵部隊，系統性對數以萬計的平民農民砍斷雙手手腕（'留短袖或長袖'肢解暴行），實施普遍食人、強姦與整村屠殺，使兩國社會結構完全瓦解崩潰。
* **學術文獻引用摘要 (`sources_summary`)**：
  獅子山問題特別法庭 (SCSL 判處查爾斯·泰勒50年監禁判決書); 賴比瑞亞真相與和解委員會 (TRC 2009 終期報告); 人權觀察與國際特赦組織系列報告; Paul Richards (1996, 'Fighting for the Rain Forest').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / International Judicial Conviction] 聯合國支持的海牙獅子山特別法庭歷史性判定前國家元首查爾斯·泰勒危害人類罪成立，兩國真相委員會詳細記錄了數萬名肢殘受害者與前童兵的證詞。`


### [EVT-1991-SOM-001] 索馬利亞內戰軍閥人為阻絕與大饑荒 (Somali Civil War, Warlord Predation and Famine)
* **起止年份**：1991 – 1993
* **地理位置**：索馬利亞中南部（摩加迪休、拜多亞'死亡之城'）(Somalia) `[ISO-3: SOM / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `220,000` 人 / 中標基準 `280,000` 人 / 高標 `350,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,406,666,666` 人
  * **2026年當代等效規模**：**`422,072` 人** (放縮係數：1.51x)
  * **區域人口衝擊率**：**`3.7333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 獨裁者巴雷倒台後國家全面崩解，法拉赫·艾迪德等敵對氏族軍閥為爭奪港口與農田，有系統地洗劫中南部農業重鎮（如拜多亞）。各派民兵掠奪紅十字會與世界糧食計劃署的運糧車隊並將口糧作為招募童兵的軍餉，故意封鎖糧食進入敵對氏族區域，直接催生了造成近30萬人死亡之毀滅性人為飢荒，引發聯合國UNOSOM軍事干預行動。
* **學術文獻引用摘要 (`sources_summary`)**：
  美國疾病管制與預防中心 (CDC 1993 流行病學死亡率調查報告); 聯合國人道事務部 (UN DHA); Alex de Waal (1997, 'Famine Crimes: Politics & the Disaster Relief Industry in Africa'); 西亞德·巴雷倒台後之各派武裝掠奪報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 索馬利亞中央政府完全瓦解，全國陷入無政府狀態達數十年，醫院與戶籍檔案不復存在；死亡數據全賴CDC、無國界醫生（MSF）與國際紅十字會在各難民營之超額死亡率抽樣模型建立。`


### [EVT-1992-BIH-001] 波士尼亞種族滅絕與雪布尼查大屠殺 (Bosnian Genocide and Srebrenica Massacre)
* **起止年份**：1992 – 1995
* **地理位置**：波士尼亞與赫塞哥維納 (Bosnia and Herzegovina) `[ISO-3: BIH / 大洲: Europe]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `65,000` 人 / 中標基準 `80,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,490,000,000` 人
  * **2026年當代等效規模**：**`118,761` 人** (放縮係數：1.48x)
  * **區域人口衝擊率**：**`1.8182%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 塞族共和國軍在拉特科·姆拉迪奇指揮下，對波士尼亞穆斯林（波士尼亞克人）展開系統性種族清洗。在長達三年的薩拉熱窩圍城中持續砲擊平民，並於1995年7月攻陷聯合國宣布之「安全區」雪布尼查後，有組織地處決並以挖掘機掩埋了超過8,000名無武裝男子與男童。
* **學術文獻引用摘要 (`sources_summary`)**：
  前南斯拉夫問題國際刑事法庭 (ICTY 判決書，判定塞族軍隊犯下種族滅絕); 薩拉熱窩研究與記錄中心 (RDC / Mirsad Tokača, 2012 人口普查核實97,207名死者); 國際失蹤人口委員會 (ICMP DNA匹配報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / DNA Verified Archives] 塞族軍隊曾多次動用推土機將原始萬人坑遺體移至「次級坑」試圖毀屍滅跡；國際失蹤人口委員會（ICMP）透過先進法醫DNA技術，已精確識別出近7,000名雪布尼查個體遺骸。`


### [EVT-1992-TJK-001] 塔吉克內戰族群教派清洗與克爾干秋別大屠殺 (Tajikistani Civil War Ethnic Cleansing and Kurgan-Tyube Massacres)
* **起止年份**：1992 – 1997
* **地理位置**：塔吉克南部瓦赫什谷地、克爾干秋別、杜尚別 (Tajikistan) `[ISO-3: TJK / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `50,000` 人 / 中標基準 `60,000` 人 / 高標 `100,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,490,000,000` 人
  * **2026年當代等效規模**：**`89,071` 人** (放縮係數：1.48x)
  * **區域人口衝擊率**：**`1.0909%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇聯解體後塔吉克爆發劇烈內戰，列寧納巴德與庫洛布親政府民兵同加爾姆（Gharm）與帕米爾（Pamiri）反對派展開殘酷的地域族群清洗。民兵在克爾干秋別棉花農莊攔截平民巴士，按身份證出生地將加爾姆人就地拉下車用刀槍屠殺拋屍瓦赫什河，數萬平民在酷寒中越過阿富汗邊界逃亡時遭射殺溺斃，全國百萬人淪為難民。
* **學術文獻引用摘要 (`sources_summary`)**：
  人權觀察 (Human Rights Watch, 1993, 'Human Rights in Tajikistan on the Incomplete Transition'); 國際特赦組織系列報告; Shirin Akiner (2001, 'Tajikistan: Disintegration or Reconciliation?'); 俄羅斯與聯合國調解和平協定檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 內戰初期中央政權幾乎不復存在，南部農村死難者多數直接草草埋葬於棉花田與渠溝中；1997年和解協議後拉赫蒙政權對內戰傷亡採取政治噤聲以維持統治穩定。`


### [EVT-1994-PRK-001] 北韓「苦難的行軍」大饑荒 (North Korean Famine (The Arduous March))
* **起止年份**：1994 – 1998
* **地理位置**：朝鮮民主主義人民共和國 (North Korea) `[ISO-3: PRK / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `600,000` 人 / 高標 `1,000,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,663,000,000` 人
  * **2026年當代等效規模**：**`863,500` 人** (放縮係數：1.44x)
  * **區域人口衝擊率**：**`2.7273%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇聯解體切斷補貼與極端氣候爆發後，金日成與金正日政權堅持「先軍政治」，拒絕改革僵化之國家配給體系（PDS）。在糧食產量驟降之際，國家配給優先保障平壤菁英與百萬人民軍，並封鎖邊界阻止平民自發進行黑市交易與逃荒，導致東北部工業重鎮（如咸鏡道）平民出現大規模餓死與幼童營養發育障礙。
* **學術文獻引用摘要 (`sources_summary`)**：
  Marcus Noland, Sherman Robinson & Tao Wang (2001, 'Famine in North Korea', Institute for International Economics); Daniel Goodkind & Loraine West (2001, 美國人口普查局模型推算60-100萬); 韓國統一部與世界糧食計劃署 (WFP) 調查; Andrew Natsios (2001, 'The Great North Korean Famine').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 朝鮮政府長年實施完全極權封鎖，嚴禁任何國際機構進行自由隨機人口普查，境內饑饉數據被列為最高國家機密；所有學術估算均依靠脫北者訪談、人造衛星夜間燈光及邊界秘密調研推算。`


### [EVT-1994-RWA-001] 盧安達種族滅絕 (Rwandan Genocide)
* **起止年份**：1994
* **地理位置**：盧安達 (Rwanda) `[ISO-3: RWA / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `500,000` 人 / 中標基準 `650,000` 人 / 高標 `800,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,663,000,000` 人
  * **2026年當代等效規模**：**`935,458` 人** (放縮係數：1.44x)
  * **區域人口衝擊率**：**`8.2278%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 1994年盧安達極端胡圖族政權、武裝部隊（FAR）與聯隊民兵（Interahamwe）在總統座機失事後，啟動預先籌備之系統性國家滅絕計畫。透過廣播電台（RTLM）煽動並動員基層行政網絡，在約100天內以砍刀與槍枝有組織地屠殺約75%的圖西族少數群體及溫和派胡圖族平民。
* **學術文獻引用摘要 (`sources_summary`)**：
  Alison Des Forges / Human Rights Watch (1999, 'Leave None to Tell the Story') 估算約 50 萬圖西人遇害；Gérard Prunier (1995, 'The Rwanda Crisis') 估算約 80 萬人；聯合國獨立調查委員會報告 (Carlsson Report, 1999) 採認約 80 萬；UCDP/PRIO 衝突數據庫記錄。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 混亂期間大量受害者遭拋入尼亞巴隆哥河或掩埋於無名萬人坑，缺乏戶口與生還記錄，精確名冊難以完全統計。盧安達政府戰後官方普查稱遇害者達 107 萬人，學界普遍認為該數據包含間接戰亂死亡，國際學術界普遍採用 50 萬至 80 萬之區間。`


### [EVT-1995-PER-001] 秘魯藤森政府強制絕育計畫 (Peru Fujimori Forced Sterilization Program)
* **起止年份**：1995 – 2000
* **地理位置**：秘魯 (Peru) `[ISO-3: PER / 大洲: Americas]`
* **核心分類**：`Coercive Population Control`
* **傷亡估算 (Raw Death Toll)**：低標 `18` 人 / 中標基準 `100` 人 / 高標 `300` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,742,250,000` 人
  * **2026年當代等效規模**：**`142` 人** (放縮係數：1.42x)
  * **區域人口衝擊率**：**`0.0004%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 藤森政府「家庭計劃」（Programa Nacional de Salud Reproductiva）設定輸卵管結紮配額並連結衛生工作者績效考核，基層官員在安第斯山區與亞馬遜叢林之克丘亞族（Quechua）與高地原住民婦女農村社區，以糧食救濟品、種子包或承諾醫療服務作為誘使，在極端衛生條件下強行實施大規模結紮手術，導致數十名婦女術後感染死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  秘魯國會調查委員會（2002 強制絕育調查報告，確認272,028名婦女遭未經同意手術）; Amnesty International (2006, 'Peru: The Truth and Reconciliation Commission – A First Step Towards a Country Without Injustice'); Human Rights Watch (1998, 'Peru: Government Program Threatens Women's Rights')。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 藤森政府否認強制性質，將計畫定性為自願家庭計劃；相關衛生部手術記錄在政府倒台前已有選擇性銷毀，受害婦女因語言障礙（克丘亞語）及地理偏遠，長年無力進行法律追訴；藤森至今（截至2026年）尚未就此罪行在秘魯司法體系中受到正式定罪。`


### [EVT-1996-COD-003] 第一次剛果戰爭胡圖族難民大清洗與密林追殺 (First Congo War Hutu Refugee Cleansing and Forest Massacres)
* **起止年份**：1996 – 1997
* **地理位置**：剛果民主共和國東部密林至基桑加尼 (DR Congo / Zaire) `[ISO-3: COD / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `200,000` 人 / 中標基準 `230,000` 人 / 高標 `300,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,821,500,000` 人
  * **2026年當代等效規模**：**`321,996` 人** (放縮係數：1.4x)
  * **區域人口衝擊率**：**`0.5111%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 保羅·卡加梅領導的盧安達愛國軍（RPA）聯手洛朗·卡比拉叛軍攻入薩伊東部，摧毀高馬等巨型難民營。盧安達軍隊隨後對向剛果西南部原始密林徒步逃亡的數十萬胡圖族難民（包括婦孺老弱）展開長達上千公里的圍追堵截，在廷基廷基（Tingi-Tingi）難民營與赤道森林深處以重武器和砍刀實施系統性屠殺，數十萬人橫死密林或餓斃於沼澤。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國剛果民主共和國地圖繪製報告 (UN Mapping Exercise Report, 2010 官方調查指出卡加梅軍隊之行為'若經主管法庭審判可被定性為種族滅絕罪行'); 諾貝爾和平獎得主穆克維格醫生證詞; 人權觀察與無國界醫生 (MSF 難民追蹤報告); Gérard Prunier (2009, 'Africa's World War').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Blocked Prosecution] 聯合國2010年發表具法律震懾力之Mapping報告後，盧安達政府以威脅撤出維和部隊強烈抗議，國際社會出於對1994年屠猶內疚長年對卡加梅涉案責任消極應對，至今無任何法庭正式起訴。`


### [EVT-1998-COD-002] 第二次剛果戰爭平民人道災難與掠奪性飢饉 (Second Congo War Civilian Mortality and Atrocities)
* **起止年份**：1998 – 2003
* **地理位置**：剛果民主共和國 (Democratic Republic of the Congo) `[ISO-3: COD / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `2,500,000` 人 / 中標基準 `3,800,000` 人 / 高標 `5,400,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`5,980,000,000` 人
  * **2026年當代等效規模**：**`5,178,930` 人** (放縮係數：1.36x)
  * **區域人口衝擊率**：**`7.451%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 九個非洲國家與數十個武裝派系捲入這場被稱為「非洲世界大戰」之衝突。各方軍閥為爭奪釷鉭、黃金與鑽石礦區，有系統地破壞農村生計體系，實施普遍之大規模強姦（作為戰爭武器）、奴役與屠殺平民，導致醫療衛生徹底崩潰，數百萬平民因可預防之飢餓、瘧疾與痢疾死亡。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際救援委員會 (International Rescue Committee, IRC 2000-2008 系列人口普查調查報告); 聯合國剛果民主共和國地圖繪製報告 (UN Mapping Exercise Report, 2010); Human Rights Watch (2002, 'The War Within The War'); 世衛組織 (WHO) 流行病調查。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 剛果東部叢林遼闊且長年缺乏公路交通與基礎行政戶籍，IRC 採用之流行病學流行率死亡抽樣模型曾遭部分人口統計學者質疑高估，但學界一致確認其為二戰以來死亡人數最高之平民人道慘劇。`


### [EVT-2002-COL-002] 哥倫比亞軍隊「偽陽性」謀殺平民冒功醜聞 (Colombia 'False Positives' Extrajudicial Executions Scandal)
* **起止年份**：2002 – 2008
* **地理位置**：哥倫比亞全境（索阿查、安蒂奧基亞、塞薩爾等）(Colombia) `[ISO-3: COL / 大洲: Americas]`
* **核心分類**：`Democide, Purges & Forced Labor`
* **傷亡估算 (Raw Death Toll)**：低標 `6,402` 人 / 中標基準 `6,402` 人 / 高標 `10,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`6,308,000,000` 人
  * **2026年當代等效規模**：**`8,271` 人** (放縮係數：1.29x)
  * **區域人口衝擊率**：**`0.0142%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 哥倫比亞陸軍在烏里韋政府'民主安全政策'高壓指標與獎金帶薪假期獎勵誘使下，系統性誘騙貧困失業平民青年至偏遠戰區殺害。軍人隨後為平民遺體穿上游擊隊迷彩服並擺放武器，偽造為'在戰鬥中擊斃的FARC叛軍'（即偽陽性），以此領取政府殺敵獎金與軍階晉升，形成國家軍隊制度性冷血獵殺本國公民之極端醜聞。
* **學術文獻引用摘要 (`sources_summary`)**：
  哥倫比亞和平特別司法管轄區 (Jurisdicción Especial para la Paz, JEP 2021 官方裁定：阿爾瓦羅·烏里韋總統執政期間陸軍犯下至少 6,402 起法外處決平民偽造為游擊隊員案件); 國際刑事法院 (ICC); 索阿查母親協會 (Madres de Soacha) 司法指控檔案。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Transitional Justice Confessions] JEP特別法庭透過召集上百名前將軍、上校與士兵公開認罪聽證會，由軍人親口承認作案細節並指出埋屍萬人塚坐標，此案已由司法定讞建立了毫無爭議的確切6,402名受害人名冊。`


### [EVT-2003-SDN-001] 蘇丹達佛種族清洗與人為飢饉 (Darfur Genocide and Ethnic Cleansing)
* **起止年份**：2003 – 2008
* **地理位置**：蘇丹西部達佛地區 (Darfur, Sudan) `[ISO-3: SDN / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `150,000` 人 / 中標基準 `300,000` 人 / 高標 `400,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`6,390,000,000` 人
  * **2026年當代等效規模**：**`382,629` 人** (放縮係數：1.28x)
  * **區域人口衝擊率**：**`5.0%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 蘇丹總統巴席爾政權出動政府軍空軍轟炸，並武裝阿拉伯游牧民兵「金戈威德」（Janjaweed），針對達佛地區非阿拉伯裔富爾人、馬薩利特人及扎加瓦人展開焦土清除。民兵摧毀村莊水井、毒化水源、焚毀糧倉並對婦女進行集體性暴力，造成數百萬難民流離失所並在沙漠中大規模餓斃。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際刑事法院 (ICC 對蘇丹總統奧馬爾·巴席爾發布種族滅絕逮捕令); 聯合國人道事務協調廳 (UN OCHA); 國際特赦組織與人權觀察系列報告; Eric Reeves (2007, 'A Long Day's Dying: Critical Moments in the Darfur Genocide').
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 蘇丹政府驅逐國際非政府救援組織，封鎖達佛地區新聞採訪，並多次拒絕配合海牙國際刑事法院之引渡與法醫現場調查。`


### [EVT-2009-LKA-002] 斯里蘭卡內戰末期穆萊蒂武「無火區」平民大屠戮 (Sri Lankan Civil War Mullivaikkal Massacres (Final Phase))
* **起止年份**：2009
* **地理位置**：斯里蘭卡東北部穆萊蒂武海灘 (Mullivaikkal, Sri Lanka) `[ISO-3: LKA / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `40,000` 人 / 中標基準 `50,000` 人 / 高標 `70,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`6,877,500,000` 人
  * **2026年當代等效規模**：**`59,251` 人** (放縮係數：1.19x)
  * **區域人口衝擊率**：**`16.6667%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 斯里蘭卡政府軍發動最後攻勢，將三十萬泰米爾平民驅趕至狹窄沙洲穆萊蒂武海灘並設立官方'無火區'。政府軍隨後違反國際人道法，動用重型榴彈砲、集束火箭和多管火箭連續數月向擠滿平民帳篷的無火區實施地毯式轟擊，有預謀地轟炸全部野戰臨時醫院與紅十字會運糧船，傷兵被就地處決，數萬平民在海灘焦土中慘死。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國秘書長問責內部審查小組報告 (Petrie Report, 2012 嚴厲批評聯合國在保護平民方面'制度性失職'); 英國第四台 (Channel 4 紀錄片 《斯里蘭卡殺戮戰場》'Sri Lanka's Killing Fields'); 國際特赦組織與人權觀察調查; 聯合國人權事務高級專員辦事處 (OHCHR 2015 綜合調查報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Unpunished War Crimes] 斯里蘭卡軍方指派官員事後推平現場並建立軍事度假村以掩蓋罪證；聯合國人權理事會多次通過決議要求國際刑事調查，但歷屆斯里蘭卡政府皆堅決拒絕配合外部司法調查。`


### [EVT-2011-SYR-001] 敘利亞內戰無差別轟炸、化武攻擊與平民圍城飢饉 (Syrian Civil War Civilian Slaughter, Chemical Attacks and Sieges)
* **起止年份**：2011 – 2023
* **地理位置**：敘利亞 (Syria) `[ISO-3: SYR / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `250,000` 人 / 中標基準 `306,887` 人 / 高標 `400,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,040,000,000` 人
  * **2026年當代等效規模**：**`355,274` 人** (放縮係數：1.16x)
  * **區域人口衝擊率**：**`1.4367%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 阿薩德政權在俄羅斯與伊朗支持下，以平民區為打擊目標維持統治。政權動員直升機投擲裝填TNT與廢鐵之桶裝炸彈（Barrel Bombs），在古塔等地使用沙林化武，並對東阿勒頗、馬達亞等反對派城鎮實施「跪下或挨餓」（Kneel or Starve）圍城政策，封鎖醫療與麵粉供應，殘酷折磨非戰鬥平民。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國人權事務高級專員辦事處 (OHCHR 2022 年官方統計核實 306,887 名直接死於衝突平民); 敘利亞人權觀察組織 (SOHR); 禁止化學武器組織 (OPCW 判定敘政府使用沙林與氯氣報告); 凱撒法案（Caesar Photographs）證實拘留所系統性酷刑處決。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 敘利亞軍事情報局（凱撒照片揭發之Saydnaya軍事監獄等）將上萬平民秘密虐殺並登載為假性心臟病；官方完全封鎖獨立聯合國調查團入境，數據由民間白頭盔志願者與海外人權核查網絡共同蒐證。`


### [EVT-2013-CAF-001] 中非共和國族群教派清洗與人道災難 (Central African Republic Inter-communal Cleansing)
* **起止年份**：2013 – 2016
* **地理位置**：中非共和國全境（班基等）(Central African Republic) `[ISO-3: CAF / 大洲: Africa]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `15,000` 人 / 高標 `30,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,208,000,000` 人
  * **2026年當代等效規模**：**`16,960` 人** (放縮係數：1.13x)
  * **區域人口衝擊率**：**`0.3261%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 穆斯林為主的塞雷卡（Séléka）反叛武裝推翻政權引發流血洗劫後，主要由基督教農民組成的'反巴拉卡'（Anti-balaka）武裝展開大規模族群清洗。民兵手持砍刀在首都班基及西部各城鎮對穆斯林平民實施逐街屠戮、斬首、私刑焚燒與清真寺破壞，迫使全國80%以上的穆斯林居民在一日內逃離家園流亡查德與喀麥隆。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國中非共和國調查委員會 (UN International Commission of Inquiry, 2014 報告); 國際刑事法院 (ICC 對反巴拉卡民兵領導人審判); 人權觀察 (HRW 2014 報告 《They Came to Kill》); 國際特赦組織報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 國家警察與司法體系在衝突初期全面崩潰，偏遠森林小鎮的屠殺缺乏完整法醫記錄；死難數據主要依據聯合國駐中非穩定團（MINUSCA）與國際人道組織核查。`


### [EVT-2013-SSD-001] 南蘇丹內戰族群屠殺、人為封鎖與飢饉危機 (South Sudanese Civil War Ethnic Cleansing and Man-made Famine)
* **起止年份**：2013 – 2018
* **地理位置**：南蘇丹全境（朱巴、本提烏、馬拉卡勒）(South Sudan) `[ISO-3: SSD / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `383,000` 人 / 中標基準 `383,000` 人 / 高標 `400,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,208,000,000` 人
  * **2026年當代等效規模**：**`433,054` 人** (放縮係數：1.13x)
  * **區域人口衝擊率**：**`3.4818%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 基爾總統（丁卡族）與副總統馬查爾（努爾族）政治決裂，迅速演化為全境毀滅性的部族報復屠殺。政府軍與叛軍在醫院與聯合國庇護所屠殺平民，推行焦土洗劫農田牛群，故意封鎖聯合國運糧車隊與人道空投，並在團結州等地普遍實施作為戰爭武器的殘酷輪姦，導致四百萬人流離失所並在富饒尼羅河盆地催生完全人為的災難性大飢荒。
* **學術文獻引用摘要 (`sources_summary`)**：
  倫敦衛生與熱帶醫學院流行病學團隊 (LSHTM 2018 流行病學超額死亡率專題研究，核實至少38.3萬人超額死亡); 聯合國人權理事會南蘇丹人權委員會 (UN CHRSS 報告); 非洲聯盟南蘇丹調查委員會 (AUCISS 奧巴桑喬前總統報告)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Epidemiological Study] 倫敦大學研究團隊運用衛星燈光變化、難民營戶口普查與死亡率統計模型建立了目前非洲內戰最精確的超額死亡量化分析報告。`


### [EVT-2014-IRQ-002] 伊斯蘭國辛賈爾亞茲迪人種族滅絕 (Yazidi Genocide by ISIS in Sinjar)
* **起止年份**：2014 – 2017
* **地理位置**：伊拉克北部辛賈爾及尼尼微省 (Sinjar, Iraq) `[ISO-3: IRQ / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `3,100` 人 / 中標基準 `5,000` 人 / 高標 `10,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,292,000,000` 人
  * **2026年當代等效規模**：**`5,588` 人** (放縮係數：1.12x)
  * **區域人口衝擊率**：**`1.25%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 恐怖組織'伊斯蘭國'（ISIS）攻佔辛賈爾地區後，指控信奉古代一神教的亞茲迪人（Yazidi）為'魔鬼崇拜者'，發動滅絕性聖戰。武裝分子就地集體槍決拒絕改宗的成年與老年男性，設立現代奴隸市場綁架、轉賣並系統性性奴役超過6,400名亞茲迪婦女與女童，並強迫男童洗腦為自殺炸彈客，造成整個古代宗教社群的毀滅性瓦解。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國調查推進伊斯蘭國追責小組 (UNITAD); 聯合國人權理事會 (UN HRC 2016 認定ISIS犯下種族滅絕罪行); 諾貝爾和平獎得主娜迪亞·穆拉德 (Nadia Murad 證詞); 德國法蘭克福高等法院2021年全球首例判定ISIS成員對亞茲迪人犯下種族滅絕罪判決書; Valeria Cetorelli et al. (2017, PLoS Medicine 人口抽樣研究)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Judicial Records] 辛賈爾山周邊已發現超過80個萬人坑，UNITAD小組運用現代DNA技術核驗骸骨；但仍有超過2,700名被綁架婦女與孩童下落不明，部分失蹤者至今生死未卜。`


### [EVT-2016-MMR-001] 緬甸羅興亞人種族清洗與若開邦大屠殺 (Rohingya Genocide and Ethnic Cleansing in Rakhine)
* **起止年份**：2016 – 2017
* **地理位置**：緬甸若開邦北部 (Rakhine State, Myanmar) `[ISO-3: MMR / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `10,000` 人 / 中標基準 `15,000` 人 / 高標 `25,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,460,000,000` 人
  * **2026年當代等效規模**：**`16,387` 人** (放縮係數：1.09x)
  * **區域人口衝擊率**：**`1.3636%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 緬甸國防軍（Tatmadaw）在若開邦啟動所謂「清剿行動」（Clearance Operations）。軍隊聯手地方極端民兵包圍羅興亞村落（如因丁村屠殺、圖拉托利屠殺），近距離槍殺幼童、集體強姦婦女並以火箭彈和焚燒夷平數百個村莊，迫使逾74萬平民在數週內冒死渡河逃亡孟加拉考克斯巴扎爾難民營。
* **學術文獻引用摘要 (`sources_summary`)**：
  無國界醫生 (MSF 2017 實地難民抽樣調查，估算首月內直接死於暴力逾 6,700 人); 聯合國獨立國際實況調查團 (UN Fact-Finding Mission on Myanmar, 2018 認定具有種族滅絕意圖); 國際法院 (ICJ 岡比亞控訴緬甸案臨時措施令)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 緬甸軍政權完全封鎖若開邦北部，逮捕揭發因丁村屠殺之路透社記者；軍方官方調查報告宣稱無平民受害，極力掩蓋萬人坑與毀滅村落之衛星痕跡。`


### [EVT-2016-YEM-001] 葉門內戰人為港口封鎖與大饑荒 (Yemeni Famine, Naval Blockade and Humanitarian Crisis)
* **起止年份**：2016 – 2022
* **地理位置**：葉門 (Yemen) `[ISO-3: YEM / 大洲: Asia]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `85,000` 人 / 中標基準 `150,000` 人 / 高標 `230,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,460,000,000` 人
  * **2026年當代等效規模**：**`163,874` 人** (放縮係數：1.09x)
  * **區域人口衝擊率**：**`0.5357%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 沙烏地領導的多國聯軍為封鎖青年運動（胡塞武裝），對葉門紅海關鍵生命線荷台達港實施海空封鎖，扣押糧食、藥品與燃油輪船；胡塞武裝亦在塔伊茲等城市布設地雷並阻撓國際物資分發。基礎設施遭空襲摧毀導致現代歷史上最嚴重的霍亂爆發，造成數十萬平民與嬰幼兒死於極端急性營養不良。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國開發計劃署 (UNDP 2021 年報告指出因飢餓與缺乏醫療間接死亡人數逾 150,000 人，總衝突死亡逾 37.7 萬); 救助兒童會 (Save the Children 2018 估算逾 85,000 名五歲以下幼童活活餓死); ACLED 衝突事件庫; 聯合國人權專家組 (UN GEE)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 葉門全境醫療機構八成陷入癱瘓，大量偏遠山區村落嬰幼兒在未送醫前即在家中餓斃或染疫身亡，未能登入中央醫院死亡名冊，數據主要依靠聯合國機構之超額死亡率推估。`


### [EVT-2017-SSD-002] 南蘇丹耶伊與赤道州族群大清洗與焦土清鄉 (Yei and Equatoria Region Ethnic Cleansing in South Sudan)
* **起止年份**：2016 – 2018
* **地理位置**：南蘇丹大赤道州（耶伊、卡約卡吉）(Equatoria, South Sudan) `[ISO-3: SSD / 大洲: Africa]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `15,000` 人 / 中標基準 `20,000` 人 / 高標 `35,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,460,000,000` 人
  * **2026年當代等效規模**：**`21,850` 人** (放縮係數：1.09x)
  * **區域人口衝擊率**：**`1.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 南蘇丹政府軍（SPLA）將戰火擴大至原本和平富庶的農業大省赤道州，指控當地少數民族支持叛軍。軍隊進駐耶伊市及周邊農村推行殘暴焦土政策，以砍刀和槍決屠殺農民、將老弱鎖入民宅活活燒死、系統性實施殘暴輪姦以摧毀社群心理防線，並摧毀糧食庫存與診所，迫使全州人口大半流亡烏干達比迪比迪（Bidi Bidi）巨型難民營。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國南蘇丹人權委員會 (UN CHRSS 2017 特別調查報告指出存在種族清洗); 聯合國難民署 (UNHCR 記錄超過一百萬赤道州難民逃往烏干達); 人權觀察 (HRW 2017 報告 《Soldiers Who Rape》); 國際特赦組織。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / UN Commission On-Site Verification] 聯合國人權專員與聯合國駐南蘇丹特派團（UNMISS）多次親臨耶伊實地核驗無人死城現狀，並發表了極具國際法律效力的調查報告。`


### [EVT-2020-AZE-001] 第二次納卡衝突、人為拉欽走廊封鎖與納卡亞美尼亞人全面清空 (Second Nagorno-Karabakh War, Lachin Blockade and Ethnic Depopulation)
* **起止年份**：2020 – 2023
* **地理位置**：納戈爾諾-卡拉巴赫（阿爾察赫地區）(Nagorno-Karabakh / Azerbaijan) `[ISO-3: AZE / 大洲: Asia]`
* **核心分類**：`Direct Physical Massacre / Genocide`
* **傷亡估算 (Raw Death Toll)**：低標 `6,000` 人 / 中標基準 `8,000` 人 / 高標 `12,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,790,000,000` 人
  * **2026年當代等效規模**：**`8,370` 人** (放縮係數：1.05x)
  * **區域人口衝擊率**：**`5.3333%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 2020年衝突後，亞塞拜然於2022年12月起非法封鎖連接納卡的唯一通道拉欽走廊長達九個月，切斷12萬平民全部食物、藥品、電力及天然氣供應，製造極端人為飢饉與醫療絕境。2023年9月亞塞拜然發動閃電軍事進攻後，原居於該地數千年的逾十萬名亞美尼亞原住民在極端恐懼下全數被迫逃離家園，使該古老社區人口面臨徹底清空。
* **學術文獻引用摘要 (`sources_summary`)**：
  國際法院 (ICJ 2023 臨時措施令，命令亞塞拜然解除拉欽走廊封鎖); 國際刑事法院首任檢察官莫雷諾-奧坎波 (Luis Moreno Ocampo 2023 專家報告認定封鎖構成種族滅絕); 歐洲議會2023年決議強烈譴責亞塞拜然暴力清空納卡; 聯合國難民署 (UNHCR 登記10.4萬名難民在一週內湧入亞美尼亞)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Exhaustive Contemporary Documentation] 現代高解析度衛星、人權組織與聯合國難民署在一週內完整記錄了100,514名登記難民出逃車龍與無人城區；國際法院已正式受理亞美尼亞控訴亞塞拜然消除一切形式種族歧視公約案。`


### [EVT-2020-ETH-001] 衣索比亞提格雷戰爭人為封鎖與人道慘劇 (Tigray War Siege, Famine and Massacres)
* **起止年份**：2020 – 2022
* **地理位置**：衣索比亞北部提格雷州 (Tigray Region, Ethiopia) `[ISO-3: ETH / 大洲: Africa]`
* **核心分類**：`Man-made & Policy Famine`
* **傷亡估算 (Raw Death Toll)**：低標 `300,000` 人 / 中標基準 `450,000` 人 / 高標 `600,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,790,000,000` 人
  * **2026年當代等效規模**：**`470,796` 人** (放縮係數：1.05x)
  * **區域人口衝擊率**：**`8.1818%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 衣索比亞聯邦政府與厄利垂亞軍隊在圍困提格雷人民解放陣線（TPLF）期間，對提格雷全州切斷電力、電信、銀行及人道卡車運輸達兩年之久。聯軍洗劫醫院與農田穀倉，厄利垂亞軍隊在阿克蘇姆等地屠殺平民並實施殘酷性暴力，極端封鎖引發全面性人為人道饑荒。
* **學術文獻引用摘要 (`sources_summary`)**：
  根特大學提格雷研究小組 (Ghent University Every Casualty Worldwide, Jan Nyssen 團隊統計估算30-60萬平民因飢荒、缺乏藥品與屠殺死亡); 聯合國國際人權專家委員會 (ICHREE 2022 報告指控將飢餓作為戰爭手段); 國際特赦組織關於阿克蘇姆屠殺之報告。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 衣索比亞政府實施全面電訊黑箱與新聞驅逐，嚴禁記者進入提格雷，阻撓聯合國獨立調查團實地勘驗，學者與醫護人員必須依靠走私衛星電話與難民回憶錄統計死難者。`


### [EVT-2021-MMR-002] 緬甸軍事政變全境軍事鎮壓、焦土焚村與空襲平民浩劫 (Myanmar Post-2021 Military Coup Nationwide Civilian Terror and Airstrikes)
* **起止年份**：2021 – 2026
* **地理位置**：緬甸實皆省、馬圭省、克倫邦、欽邦等全境 (Myanmar) `[ISO-3: MMR / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `5,000` 人 / 中標基準 `8,000` 人 / 高標 `15,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,873,333,333` 人
  * **2026年當代等效規模**：**`8,281` 人** (放縮係數：1.04x)
  * **區域人口衝擊率**：**`0.0148%`**
* **學界共識度**：`High Consensus`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 敏昂萊軍政權發動政變推翻民選政府後，對全境和平抗議平民展開狙擊槍爆頭實彈鎮壓。在面對全民防衛軍（PDF）抵抗後，軍方推行'四斷政策'，派遣戰鬥機與武裝直升機頻繁轟炸村莊學校、教堂與寺廟，並在實皆省地毯式縱火焚毀逾七萬棟平民住宅，故意切斷災區醫藥與糧食供應，迫使近三百萬人流離失所。
* **學術文獻引用摘要 (`sources_summary`)**：
  政治犯援助協會 (AAPP 官方核實直接遭軍警射殺與酷刑致死平民逾 5,000 人); 聯合國緬甸人權狀況特別報告員湯姆·安德魯斯 (Tom Andrews) 2023–2024 年度報告; ACLED 衝突事件庫; 帕濟基村（Pazigyi）空襲大屠殺調查報告（單次空襲屠殺逾160名平民婦孺）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[High Consensus / Ongoing Documentation] AAPP與聯合國駐地機構逐日建立每位遇害者照片、年齡與死因數據庫；軍政府切斷網絡通訊並逮捕記者，但衛星遙感與民間密拍影像已在海牙聯合國調查機構（IIMM）完整建檔。`


### [EVT-2022-UKR-001] 俄羅斯入侵烏克蘭平民暴行（布查大屠殺等） (Russian Invasion of Ukraine – War Crimes and Civilian Atrocities)
* **起止年份**：2022 – 2026
* **地理位置**：烏克蘭全境（尤以基輔州布查、赫爾松、馬里烏波爾）(Ukraine) `[ISO-3: UKR / 大洲: Europe]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `30,000` 人 / 中標基準 `80,000` 人 / 高標 `200,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`7,956,666,666` 人
  * **2026年當代等效規模**：**`81,944` 人** (放縮係數：1.02x)
  * **區域人口衝擊率**：**`0.1818%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 2022年2月俄羅斯全面入侵後，俄軍在多地實施被廣泛記錄的戰爭罪行，包括布查（Bucha）平民後腦射擊、就地棄置的遇害市民、馬里烏波爾亞速鋼鐵廠平民圍困、巴赫穆特等城市地毯式砲轟平民居住區，及強迫驅送烏克蘭兒童進行「再教育」（已記錄逾16,000名兒童被強制移送俄羅斯）。
* **學術文獻引用摘要 (`sources_summary`)**：
  聯合國烏克蘭人權監察團（UN Human Rights Monitoring Mission, OHCHR 報告，截至2024年核實平民死亡逾11,000人，實際數字遠高於此）; ACLED衝突事件庫; 國際刑事法院（ICC，2023年對普廷簽發逮捕令）; 醫學期刊《刺胳針》（The Lancet, 2023年超額死亡率估算）。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[Archival Gap / Historical Chaos] 衝突仍在進行中（截至2026年），大規模戰場及後方佔領區平民死亡仍無法獨立全面記錄；俄羅斯方面拒絕合作任何國際司法調查，佔領區死亡數據處於嚴重資訊黑洞，死亡總數估算持續修正。`


### [EVT-2023-PSE-001] 加薩走廊衝突平民傷亡與圍困人道危機 (Gaza Humanitarian Crisis, Civilian Casualties and Blockade)
* **起止年份**：2023 – 2026
* **地理位置**：巴勒斯坦加薩走廊 (Gaza Strip, Palestine) `[ISO-3: PSE / 大洲: Asia]`
* **核心分類**：`War-Time Civilian Atrocities`
* **傷亡估算 (Raw Death Toll)**：低標 `41,000` 人 / 中標基準 `70,000` 人 / 高標 `186,000` 人
* **人口標準化換算**：
  * 當時全球人口基準：`8,040,000,000` 人
  * **2026年當代等效規模**：**`70,958` 人** (放縮係數：1.01x)
  * **區域人口衝擊率**：**`3.0435%`**
* **學界共識度**：`Debated`
* **慘劇機制質性描述 (`qualitative_description`)**：
  > 2023年10月7日哈瑪斯突襲以色列平民（造成約1,200人死亡）後，以色列國防軍對狹小密集之加薩走廊展開高強度轟炸與全面地面圍攻，並對水電、燃料與國際糧食援助卡車實施極限嚴苛准入控制。大面積住宅區、學校與醫院化為廢墟，導致兩百萬人流離失所，婦孺傷亡比例高達近六成，引發極端人為飢荒與公共衛生崩潰。
* **學術文獻引用摘要 (`sources_summary`)**：
  加薩衛生部 (MOH 核實直接死亡名冊逾4.1萬人); 柳葉刀醫學期刊 (The Lancet, 2024 研究估算計入飢餓、缺乏醫療及廢墟掩埋之間接非正常死亡可能高達18.6萬人); 聯合國人道事務協調廳 (UN OCHA); 綜合食品安全階段分類 (IPC 宣布加薩面臨人為災難性飢荒臨界)。
* **數據存取與缺失標記 (`data_access_note`)**：
  `[State Suppression / Censorship] 以色列政府禁止外國獨立記者單獨進入加薩走廊，並對加薩衛生部之統計公信力提出質疑，但聯合國與世衛組織（WHO）歷次戰事核查表明衛生部名冊具高度真實性；數萬名被掩埋於鋼筋混凝土瓦礫下失蹤人口尚無法開挖登記。`

