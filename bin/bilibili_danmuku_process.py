#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0-only
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
import re
import math
from collections import defaultdict
from typing import DefaultDict
from xml.dom import minidom

# (archlinuxcn repo) sudo pacman -S python-biliass
from biliass import convert_to_ass

# https://github.com/xmcp/pakku.js/blob/9a8c59591d9d9a17dfa39595d995d2f08c781014/pakkujs/core/pinyin_dict.ts#L14
PINYIN_DICT_RAW = {
    "a": "啊阿锕",
    "ai": "埃挨哎唉哀皑癌蔼矮艾碍爱隘诶捱嗳嗌嫒瑷暧砹锿霭",
    "an": "鞍氨安俺按暗岸胺案谙埯揞犴庵桉铵鹌顸黯",
    "ang": "肮昂盎",
    "ao": "凹敖熬翱袄傲奥懊澳坳拗嗷噢岙廒遨媪骜聱螯鏊鳌鏖",
    "b_a": "芭捌扒叭吧笆八疤巴拔跋靶把耙坝霸罢爸茇菝萆捭岜灞杷钯粑鲅魃",
    "b_ai": "白柏百摆佰败拜稗薜掰鞴",
    "b_an": "斑班搬扳般颁板版扮拌伴瓣半办绊阪坂豳钣瘢癍舨",
    "b_ang": "邦帮梆榜膀绑棒磅蚌镑傍谤蒡螃",
    "b_ao": "苞胞包褒雹保堡饱宝抱报暴豹鲍爆勹葆宀孢煲鸨褓趵龅",
    "b_uo": "剥薄玻菠播拨钵波博勃搏铂箔伯帛舶脖膊渤泊驳亳蕃啵饽檗擘礴钹鹁簸跛",
    "b_ei": "杯碑悲卑北辈背贝钡倍狈备惫焙被孛陂邶埤蓓呗怫悖碚鹎褙鐾",
    "b_en": "奔苯本笨畚坌锛",
    "b_eng": "崩绷甭泵蹦迸唪嘣甏",
    "b_ee": "逼鼻比鄙笔彼碧蓖蔽毕毙毖币庇痹闭敝弊必辟壁臂避陛匕仳俾芘荜荸吡哔狴庳愎滗濞弼妣婢嬖璧贲畀铋秕裨筚箅篦舭襞跸髀",
    "b_ian": "鞭边编贬扁便变卞辨辩辫遍匾弁苄忭汴缏煸砭碥稹窆蝙笾鳊",
    "b_iao": "标彪膘表婊骠飑飙飚灬镖镳瘭裱鳔",
    "b_ie": "鳖憋别瘪蹩鳘",
    "b_in": "彬斌濒滨宾摈傧浜缤玢殡膑镔髌鬓",
    "b_ing": "兵冰柄丙秉饼炳病并禀邴摒绠枋槟燹",
    "b_u": "捕卜哺补埠不布步簿部怖拊卟逋瓿晡钚醭",
    "c_a": "擦嚓礤",
    "c_ai": "猜裁材才财睬踩采彩菜蔡",
    "c_an": "餐参蚕残惭惨灿骖璨粲黪",
    "c_ang": "苍舱仓沧藏伧",
    "c_ao": "操糙槽曹草艹嘈漕螬艚",
    "c_e": "厕策侧册测刂帻恻",
    "c_eng": "层蹭噌",
    "ch_a": "插叉茬茶查碴搽察岔差诧猹馇汊姹杈楂槎檫钗锸镲衩",
    "ch_ai": "拆柴豺侪茈瘥虿龇",
    "ch_an": "搀掺蝉馋谗缠铲产阐颤冁谄谶蒇廛忏潺澶孱羼婵嬗骣觇禅镡裣蟾躔",
    "ch_ang": "昌猖场尝常长偿肠厂敞畅唱倡伥鬯苌菖徜怅惝阊娼嫦昶氅鲳",
    "ch_ao": "超抄钞朝嘲潮巢吵炒怊绉晁耖",
    "ch_e": "车扯撤掣彻澈坼屮砗",
    "ch_en": "郴臣辰尘晨忱沉陈趁衬称谌抻嗔宸琛榇肜胂碜龀",
    "ch_eng": "撑城橙成呈乘程惩澄诚承逞骋秤埕嵊徵浈枨柽樘晟塍瞠铖裎蛏酲",
    "ch_i": "吃痴持匙池迟弛驰耻齿侈尺赤翅斥炽傺墀芪茌搋叱哧啻嗤彳饬沲媸敕胝眙眵鸱瘛褫蚩螭笞篪豉踅踟魑",
    "ch_ong": "充冲虫崇宠茺忡憧铳艟",
    "ch_ou": "抽酬畴踌稠愁筹仇绸瞅丑俦圳帱惆溴妯瘳雠鲋",
    "ch_u": "臭初出橱厨躇锄雏滁除楚础储矗搐触处亍刍憷绌杵楮樗蜍蹰黜",
    "ch_uan": "揣川穿椽传船喘串掾舛惴遄巛氚钏镩舡",
    "ch_uang": "疮窗幢床闯创怆",
    "ch_ui": "吹炊捶锤垂陲棰槌",
    "ch_un": "春椿醇唇淳纯蠢促莼沌肫朐鹑蝽",
    "ch_uo": "戳绰蔟辶辍镞踔龊",
    "c_i": "疵茨磁雌辞慈瓷词此刺赐次荠呲嵯鹚螅糍趑",
    "c_ong": "聪葱囱匆从丛偬苁淙骢琮璁枞",
    "c_u": "凑粗醋簇猝殂蹙",
    "c_uan": "蹿篡窜汆撺昕爨",
    "c_ui": "摧崔催脆瘁粹淬翠萃悴璀榱隹",
    "c_un": "村存寸磋忖皴",
    "c_uo": "撮搓措挫错厝脞锉矬痤鹾蹉躜",
    "d_a": "搭达答瘩打大耷哒嗒怛妲疸褡笪靼鞑",
    "d_ai": "呆歹傣戴带殆代贷袋待逮怠埭甙呔岱迨逯骀绐玳黛",
    "d_an": "耽担丹单郸掸胆旦氮但惮淡诞弹蛋亻儋卩萏啖澹檐殚赕眈瘅聃箪",
    "d_ang": "当挡党荡档谠凼菪宕砀铛裆",
    "d_ao": "刀捣蹈倒岛祷导到稻悼道盗叨啁忉洮氘焘忑纛",
    "d_e": "德得的锝",
    "d_eng": "蹬灯登等瞪凳邓噔嶝戥磴镫簦",
    "d_ee": "堤低滴迪敌笛狄涤翟嫡抵底地蒂第帝弟递缔氐籴诋谛邸坻莜荻嘀娣柢棣觌砥碲睇镝羝骶",
    "d_ian": "颠掂滇碘点典靛垫电佃甸店惦奠淀殿丶阽坫埝巅玷癜癫簟踮",
    "d_iao": "碉叼雕凋刁掉吊钓调轺铞蜩粜貂",
    "d_ie": "跌爹碟蝶迭谍叠佚垤堞揲喋渫轶牒瓞褶耋蹀鲽鳎",
    "d_ing": "丁盯叮钉顶鼎锭定订丢仃啶玎腚碇町铤疔耵酊",
    "d_ong": "东冬董懂动栋侗恫冻洞垌咚岽峒夂氡胨胴硐鸫",
    "d_ou": "兜抖斗陡豆逗痘蔸钭窦窬蚪篼酡",
    "d_u": "都督毒犊独读堵睹赌杜镀肚度渡妒芏嘟渎椟橐牍蠹笃髑黩",
    "d_uan": "端短锻段断缎彖椴煅簖",
    "d_ui": "堆兑队对怼憝碓",
    "d_un": "墩吨蹲敦顿囤钝盾遁炖砘礅盹镦趸",
    "d_uo": "掇哆多夺垛躲朵跺舵剁惰堕咄哚缍柁铎裰踱",
    "e": "蛾峨鹅俄额讹娥恶厄扼遏鄂饿噩谔垩垭苊莪萼呃愕屙婀轭曷腭硪锇锷鹗颚鳄",
    "en": "恩蒽摁唔嗯",
    "er": "而儿耳尔饵洱二贰迩珥铒鸸鲕",
    "f_a": "发罚筏伐乏阀法珐垡砝",
    "f_an": "藩帆番翻樊矾钒繁凡烦反返范贩犯饭泛蘩幡犭梵攵燔畈蹯",
    "f_ang": "坊芳方肪房防妨仿访纺放匚邡彷钫舫鲂",
    "f_ei": "菲非啡飞肥匪诽吠肺废沸费芾狒悱淝妃绋绯榧腓斐扉祓砩镄痱蜚篚翡霏鲱",
    "f_en": "芬酚吩氛分纷坟焚汾粉奋份忿愤粪偾瀵棼愍鲼鼢",
    "f_eng": "丰封枫蜂峰锋风疯烽逢冯缝讽奉凤俸酆葑沣砜",
    "f_u": "佛否夫敷肤孵扶拂辐幅氟符伏俘服浮涪福袱弗甫抚辅俯釜斧脯腑府腐赴副覆赋复傅付阜父腹负富讣附妇缚咐匐凫郛芙苻茯莩菔呋幞滏艴孚驸绂桴赙黻黼罘稃馥虍蚨蜉蝠蝮麸趺跗鳆",
    "g_a": "噶嘎蛤尬呷尕尜旮钆",
    "g_ai": "该改概钙盖溉丐陔垓戤赅胲",
    "g_an": "干甘杆柑竿肝赶感秆敢赣坩苷尴擀泔淦澉绀橄旰矸疳酐",
    "g_ang": "冈刚钢缸肛纲岗港戆罡颃筻",
    "g_ong": "杠工攻功恭龚供躬公宫弓巩汞拱贡共蕻廾咣珙肱蚣蛩觥",
    "g_ao": "篙皋高膏羔糕搞镐稿告睾诰郜蒿藁缟槔槁杲锆",
    "g_e": "哥歌搁戈鸽胳疙割革葛格阁隔铬个各鬲仡哿塥嗝纥搿膈硌铪镉袼颌虼舸骼髂",
    "g_ei": "给",
    "g_en": "根跟亘茛哏艮",
    "g_eng": "耕更庚羹埂耿梗哽赓鲠",
    "g_ou": "钩勾沟苟狗垢构购够佝诟岣遘媾缑觏彀鸲笱篝鞲",
    "g_u": "辜菇咕箍估沽孤姑鼓古蛊骨谷股故顾固雇嘏诂菰哌崮汩梏轱牯牿胍臌毂瞽罟钴锢瓠鸪鹄痼蛄酤觚鲴骰鹘",
    "g_ua": "刮瓜剐寡挂褂卦诖呱栝鸹",
    "g_uai": "乖拐怪哙",
    "g_uan": "棺关官冠观管馆罐惯灌贯倌莞掼涫盥鹳鳏",
    "g_uang": "光广逛犷桄胱疒",
    "g_ui": "瑰规圭硅归龟闺轨鬼诡癸桂柜跪贵刽匦刿庋宄妫桧炅晷皈簋鲑鳜",
    "g_un": "辊滚棍丨衮绲磙鲧",
    "g_uo": "锅郭国果裹过馘蠃埚掴呙囗帼崞猓椁虢锞聒蜮蜾蝈",
    "h_a": "哈",
    "h_ai": "骸孩海氦亥害骇咴嗨颏醢",
    "h_an": "酣憨邯韩含涵寒函喊罕翰撼捍旱憾悍焊汗汉邗菡撖阚瀚晗焓颔蚶鼾",
    "h_en": "夯痕很狠恨",
    "h_ang": "杭航沆绗珩桁",
    "h_ao": "壕嚎豪毫郝好耗号浩薅嗥嚆濠灏昊皓颢蚝",
    "h_e": "呵喝荷菏核禾和何合盒貉阂河涸赫褐鹤贺诃劾壑藿嗑嗬阖盍蚵翮",
    "h_ei": "嘿黑",
    "h_eng": "哼亨横衡恒訇蘅",
    "h_ong": "轰哄烘虹鸿洪宏弘红黉讧荭薨闳泓",
    "h_ou": "喉侯猴吼厚候后堠後逅瘊篌糇鲎骺",
    "h_u": "呼乎忽瑚壶葫胡蝴狐糊湖弧虎唬护互沪户冱唿囫岵猢怙惚浒滹琥槲轷觳烀煳戽扈祜鹕鹱笏醐斛",
    "h_ua": "花哗华猾滑画划化话劐浍骅桦铧稞",
    "h_uai": "槐徊怀淮坏还踝",
    "h_uan": "欢环桓缓换患唤痪豢焕涣宦幻郇奂垸擐圜洹浣漶寰逭缳锾鲩鬟",
    "h_uang": "荒慌黄磺蝗簧皇凰惶煌晃幌恍谎隍徨湟潢遑璜肓癀蟥篁鳇",
    "h_ui": "灰挥辉徽恢蛔回毁悔慧卉惠晦贿秽会烩汇讳诲绘诙茴荟蕙哕喙隳洄彗缋珲晖恚虺蟪麾",
    "h_un": "荤昏婚魂浑混诨馄阍溷缗",
    "h_uo": "豁活伙火获或惑霍货祸攉嚯夥钬锪镬耠蠖",
    "j_ee": "击圾基机畸稽积箕肌饥迹激讥鸡姬绩缉吉极棘辑籍集及急疾汲即嫉级挤几脊己蓟技冀季伎祭剂悸济寄寂计记既忌际妓继纪居丌乩剞佶佴脔墼芨芰萁蒺蕺掎叽咭哜唧岌嵴洎彐屐骥畿玑楫殛戟戢赍觊犄齑矶羁嵇稷瘠瘵虮笈笄暨跻跽霁鲚鲫髻麂",
    "j_ia": "嘉枷夹佳家加荚颊贾甲钾假稼价架驾嫁伽郏拮岬浃迦珈戛胛恝铗镓痂蛱笳袈跏",
    "j_ian": "歼监坚尖笺间煎兼肩艰奸缄茧检柬碱硷拣捡简俭剪减荐槛鉴践贱见键箭件健舰剑饯渐溅涧建僭谏谫菅蒹搛囝湔蹇謇缣枧柙楗戋戬牮犍毽腱睑锏鹣裥笕箴翦趼踺鲣鞯",
    "j_iang": "僵姜将浆江疆蒋桨奖讲匠酱降茳洚绛缰犟礓耩糨豇",
    "j_iao": "蕉椒礁焦胶交郊浇骄娇嚼搅铰矫侥脚狡角饺缴绞剿教酵轿较叫佼僬茭挢噍峤徼姣纟敫皎鹪蛟醮跤鲛",
    "j_ie": "窖揭接皆秸街阶截劫节桔杰捷睫竭洁结解姐戒藉芥界借介疥诫届偈讦诘喈嗟獬婕孑桀獒碣锴疖袷颉蚧羯鲒骱髫",
    "j_in": "巾筋斤金今津襟紧锦仅谨进靳晋禁近烬浸尽卺荩堇噤馑廑妗缙瑾槿赆觐钅锓衿矜",
    "j_ing": "劲荆兢茎睛晶鲸京惊精粳经井警景颈静境敬镜径痉靖竟竞净刭儆阱菁獍憬泾迳弪婧肼胫腈旌",
    "j_iong": "炯窘冂迥扃",
    "j_iu": "揪究纠玖韭久灸九酒厩救旧臼舅咎就疚僦啾阄柩桕鹫赳鬏",
    "j_v": "鞠拘狙疽驹菊局咀矩举沮聚拒据巨具距踞锯俱句惧炬剧倨讵苣苴莒掬遽屦琚枸椐榘榉橘犋飓钜锔窭裾趄醵踽龃雎鞫",
    "j_van": "捐鹃娟倦眷卷绢鄄狷涓桊蠲锩镌隽",
    "j_ve": "撅攫抉掘倔爵觉决诀绝厥劂谲矍蕨噘崛獗孓珏桷橛爝镢蹶觖",
    "j_vn": "均菌钧军君峻俊竣浚郡骏捃狻皲筠麇",
    "k_a": "喀咖卡佧咔胩",
    "k_e": "咯坷苛柯棵磕颗科壳咳可渴克刻客课岢恪溘骒缂珂轲氪瞌钶疴窠蝌髁",
    "k_ai": "开揩楷凯慨剀垲蒈忾恺铠锎",
    "k_an": "刊堪勘坎砍看侃凵莰莶戡龛瞰",
    "k_ang": "康慷糠扛抗亢炕坑伉闶钪",
    "k_ao": "考拷烤靠尻栲犒铐",
    "k_en": "肯啃垦恳垠裉颀",
    "k_eng": "吭忐铿",
    "k_ong": "空恐孔控倥崆箜",
    "k_ou": "抠口扣寇芤蔻叩眍筘",
    "k_u": "枯哭窟苦酷库裤刳堀喾绔骷",
    "k_ua": "夸垮挎跨胯侉",
    "k_uai": "块筷侩快蒯郐蒉狯脍",
    "k_uan": "宽款髋",
    "k_uang": "匡筐狂框矿眶旷况诓诳邝圹夼哐纩贶",
    "k_ui": "亏盔岿窥葵奎魁傀馈愧溃馗匮夔隗揆喹喟悝愦阕逵暌睽聩蝰篑臾跬",
    "k_un": "坤昆捆困悃阃琨锟醌鲲髡",
    "k_uo": "括扩廓阔蛞",
    "l_a": "垃拉喇蜡腊辣啦剌摺邋旯砬瘌",
    "l_ai": "莱来赖崃徕涞濑赉睐铼癞籁",
    "l_an": "蓝婪栏拦篮阑兰澜谰揽览懒缆烂滥啉岚懔漤榄斓罱镧褴",
    "l_ang": "琅榔狼廊郎朗浪莨蒗啷阆锒稂螂",
    "l_ao": "捞劳牢老佬姥酪烙涝唠崂栳铑铹痨醪",
    "l_e": "勒乐肋仂叻嘞泐鳓",
    "l_ei": "雷镭蕾磊累儡垒擂类泪羸诔荽咧漯嫘缧檑耒酹",
    "l_ing": "棱冷拎玲菱零龄铃伶羚凌灵陵岭领另令酃塄苓呤囹泠绫柃棂瓴聆蛉翎鲮",
    "l_eng": "楞愣",
    "l_ee": "厘梨犁黎篱狸离漓理李里鲤礼莉荔吏栗丽厉励砾历利傈例俐痢立粒沥隶力璃哩俪俚郦坜苈莅蓠藜捩呖唳喱猁溧澧逦娌嫠骊缡珞枥栎轹戾砺詈罹锂鹂疠疬蛎蜊蠡笠篥粝醴跞雳鲡鳢黧",
    "l_ian": "俩联莲连镰廉怜涟帘敛脸链恋炼练挛蔹奁潋濂娈琏楝殓臁膦裢蠊鲢",
    "l_iang": "粮凉梁粱良两辆量晾亮谅墚椋踉靓魉",
    "l_iao": "撩聊僚疗燎寥辽潦了撂镣廖料蓼尥嘹獠寮缭钌鹩耢",
    "l_ie": "列裂烈劣猎冽埒洌趔躐鬣",
    "l_in": "琳林磷霖临邻鳞淋凛赁吝蔺嶙廪遴檩辚瞵粼躏麟",
    "l_iu": "溜琉榴硫馏留刘瘤流柳六抡偻蒌泖浏遛骝绺旒熘锍镏鹨鎏",
    "l_ong": "龙聋咙笼窿隆垄拢陇弄垅茏泷珑栊胧砻癃",
    "l_ou": "楼娄搂篓漏陋喽嵝镂瘘耧蝼髅",
    "l_u": "芦卢颅庐炉掳卤虏鲁麓碌露路赂鹿潞禄录陆戮垆摅撸噜泸渌漉璐栌橹轳辂辘氇胪镥鸬鹭簏舻鲈",
    "l_v": "驴吕铝侣旅履屡缕虑氯律率滤绿捋闾榈膂稆褛",
    "l_uan": "峦孪滦卵乱栾鸾銮",
    "l_ve": "掠略锊",
    "l_un": "轮伦仑沦纶论囵",
    "l_uo": "萝螺罗逻锣箩骡裸落洛骆络倮荦摞猡泺椤脶镙瘰雒",
    "m_a": "妈麻玛码蚂马骂嘛吗唛犸嬷杩麽",
    "m_ai": "埋买麦卖迈脉劢荬咪霾",
    "m_an": "瞒馒蛮满蔓曼慢漫谩墁幔缦熳镘颟螨鳗鞔",
    "m_ang": "芒茫盲忙莽邙漭朦硭蟒",
    "m_eng": "氓萌蒙檬盟锰猛梦孟勐甍瞢懵礞虻蜢蠓艋艨黾",
    "m_iao": "猫苗描瞄藐秒渺庙妙喵邈缈缪杪淼眇鹋蜱",
    "m_ao": "茅锚毛矛铆卯茂冒帽貌贸侔袤勖茆峁瑁昴牦耄旄懋瞀蛑蝥蟊髦",
    "m_e": "么",
    "m_ei": "玫枚梅酶霉煤没眉媒镁每美昧寐妹媚坶莓嵋猸浼湄楣镅鹛袂魅",
    "m_en": "门闷们扪玟焖懑钔",
    "m_ee": "眯醚靡糜迷谜弥米秘觅泌蜜密幂芈冖谧蘼嘧猕獯汨宓弭脒敉糸縻麋",
    "m_ian": "棉眠绵冕免勉娩缅面沔湎腼眄",
    "m_ie": "蔑灭咩蠛篾",
    "m_in": "民抿皿敏悯闽苠岷闵泯珉",
    "m_ing": "明螟鸣铭名命冥茗溟暝瞑酩",
    "m_iu": "谬",
    "m_uo": "摸摹蘑模膜磨摩魔抹末莫墨默沫漠寞陌谟茉蓦馍嫫镆秣瘼耱蟆貊貘",
    "m_ou": "谋牟某厶哞婺眸鍪",
    "m_u": "拇牡亩姆母墓暮幕募慕木目睦牧穆仫苜呒沐毪钼",
    "n_a": "拿哪呐钠那娜纳内捺肭镎衲箬",
    "n_ai": "氖乃奶耐奈鼐艿萘柰",
    "n_an": "南男难囊喃囡楠腩蝻赧",
    "n_ao": "挠脑恼闹孬垴猱瑙硇铙蛲",
    "n_e": "淖呢讷",
    "n_ei": "馁",
    "n_en": "嫩能枘恁",
    "n_ee": "妮霓倪泥尼拟你匿腻逆溺伲坭猊怩滠昵旎祢慝睨铌鲵",
    "n_ian": "蔫拈年碾撵捻念廿辇黏鲇鲶",
    "n_iang": "娘酿",
    "n_iao": "鸟尿茑嬲脲袅",
    "n_ie": "捏聂孽啮镊镍涅乜陧蘖嗫肀颞臬蹑",
    "n_in": "您柠",
    "n_ing": "狞凝宁拧泞佞蓥咛甯聍",
    "n_iu": "牛扭钮纽狃忸妞蚴",
    "n_ong": "脓浓农侬",
    "n_u": "奴努怒呶帑弩胬孥驽",
    "n_v": "女恧钕衄",
    "n_uan": "暖",
    "n_ve": "虐疟",
    "n_uo": "挪懦糯诺傩搦喏锘",
    "ou": "哦欧鸥殴藕呕偶沤怄瓯耦",
    "p_a": "啪趴爬帕怕琶葩筢",
    "p_ai": "拍排牌徘湃派俳蒎",
    "p_an": "攀潘盘磐盼畔判叛爿泮袢襻蟠蹒",
    "p_ang": "乓庞旁耪胖滂逄",
    "p_ao": "抛咆刨炮袍跑泡匏狍庖脬疱",
    "p_ei": "呸胚培裴赔陪配佩沛掊辔帔淠旆锫醅霈",
    "p_en": "喷盆湓",
    "p_eng": "砰抨烹澎彭蓬棚硼篷膨朋鹏捧碰坯堋嘭怦蟛",
    "p_ee": "砒霹批披劈琵毗啤脾疲皮匹痞僻屁譬丕陴邳郫圮鼙擗噼庀媲纰枇甓睥罴铍痦癖疋蚍貔",
    "p_ian": "篇偏片骗谝骈犏胼褊翩蹁",
    "p_iao": "飘漂瓢票剽嘌嫖缥殍瞟螵",
    "p_ie": "撇瞥丿苤氕",
    "p_in": "拼频贫品聘拚姘嫔榀牝颦",
    "p_ing": "乒坪苹萍平凭瓶评屏俜娉枰鲆",
    "p_uo": "坡泼颇婆破魄迫粕叵鄱溥珀钋钷皤笸",
    "p_ou": "剖裒踣",
    "p_u": "扑铺仆莆葡菩蒲埔朴圃普浦谱曝瀑匍噗濮璞氆镤镨蹼",
    "q_ee": "期欺栖戚妻七凄漆柒沏其棋奇歧畦崎脐齐旗祈祁骑起岂乞企启契砌器气迄弃汽泣讫亟亓圻芑萋葺嘁屺岐汔淇骐绮琪琦杞桤槭欹祺憩碛蛴蜞綦綮趿蹊鳍麒",
    "q_ia": "掐恰洽葜",
    "q_ian": "牵扦钎铅千迁签仟谦乾黔钱钳前潜遣浅谴堑嵌欠歉佥阡芊芡荨掮岍悭慊骞搴褰缱椠肷愆钤虔箝",
    "q_iang": "枪呛腔羌墙蔷强抢嫱樯戗炝锖锵镪襁蜣羟跫跄",
    "q_iao": "橇锹敲悄桥瞧乔侨巧鞘撬翘峭俏窍劁诮谯荞愀憔缲樵毳硗跷鞒",
    "q_ie": "切茄且怯窃郄唼惬妾挈锲箧",
    "q_in": "钦侵亲秦琴勤芹擒禽寝沁芩蓁蕲揿吣嗪噙溱檎螓衾",
    "q_ing": "青轻氢倾卿清擎晴氰情顷请庆倩苘圊檠磬蜻罄箐謦鲭黥",
    "q_iong": "琼穷邛茕穹筇銎",
    "q_iu": "秋丘邱球求囚酋泅俅氽巯艽犰湫逑遒楸赇鸠虬蚯蝤裘糗鳅鼽",
    "q_v": "趋区蛆曲躯屈驱渠取娶龋趣去诎劬蕖蘧岖衢阒璩觑氍祛磲癯蛐蠼麴瞿黢",
    "q_van": "圈颧权醛泉全痊拳犬券劝诠荃獾悛绻辁畎铨蜷筌鬈",
    "q_ve": "缺炔瘸却鹊榷确雀阙悫",
    "q_vn": "裙群逡",
    "r_an": "然燃冉染苒髯",
    "r_ang": "瓤壤攘嚷让禳穰",
    "r_ao": "饶扰绕荛娆桡",
    "r_uo": "惹若弱",
    "r_e": "热偌",
    "r_en": "壬仁人忍韧任认刃妊纫仞荏葚饪轫稔衽",
    "r_eng": "扔仍",
    "r_i": "日",
    "r_ong": "戎茸蓉荣融熔溶容绒冗嵘狨缛榕蝾",
    "r_ou": "揉柔肉糅蹂鞣",
    "r_u": "茹蠕儒孺如辱乳汝入褥蓐薷嚅洳溽濡铷襦颥",
    "r_uan": "软阮朊",
    "r_ui": "蕊瑞锐芮蕤睿蚋",
    "r_un": "闰润",
    "s_a": "撒洒萨卅仨挲飒",
    "s_ai": "腮鳃塞赛噻",
    "s_an": "三叁伞散彡馓氵毵糁霰",
    "s_ang": "桑嗓丧搡磉颡",
    "s_ao": "搔骚扫嫂埽臊瘙鳋",
    "s_e": "瑟色涩啬铩铯穑",
    "s_en": "森",
    "s_eng": "僧",
    "sh_a": "莎砂杀刹沙纱傻啥煞脎歃痧裟霎鲨",
    "sh_ai": "筛晒酾",
    "sh_an": "珊苫杉山删煽衫闪陕擅赡膳善汕扇缮剡讪鄯埏芟潸姗骟膻钐疝蟮舢跚鳝",
    "sh_ang": "墒伤商赏晌上尚裳垧绱殇熵觞",
    "sh_ao": "梢捎稍烧芍勺韶少哨邵绍劭苕潲蛸笤筲艄",
    "sh_e": "奢赊蛇舌舍赦摄射慑涉社设厍佘猞畲麝",
    "sh_en": "砷申呻伸身深娠绅神沈审婶甚肾慎渗诜谂吲哂渖椹矧蜃",
    "sh_eng": "声生甥牲升绳省盛剩胜圣丞渑媵眚笙",
    "sh_i": "师失狮施湿诗尸虱十石拾时什食蚀实识史矢使屎驶始式示士世柿事拭誓逝势是嗜噬适仕侍释饰氏市恃室视试谥埘莳蓍弑唑饣轼耆贳炻礻铈铊螫舐筮豕鲥鲺",
    "sh_ou": "收手首守寿授售受瘦兽扌狩绶艏",
    "sh_u": "蔬枢梳殊抒输叔舒淑疏书赎孰熟薯暑曙署蜀黍鼠属术述树束戍竖墅庶数漱恕倏塾菽忄沭涑澍姝纾毹腧殳镯秫鹬",
    "sh_ua": "刷耍唰涮",
    "sh_uai": "摔衰甩帅蟀",
    "sh_uan": "栓拴闩",
    "sh_uang": "霜双爽孀",
    "sh_ui": "谁水睡税",
    "sh_un": "吮瞬顺舜恂",
    "sh_uo": "说硕朔烁蒴搠嗍濯妁槊铄",
    "s_i": "斯撕嘶思私司丝死肆寺嗣四伺似饲巳厮俟兕菥咝汜泗澌姒驷缌祀祠锶鸶耜蛳笥",
    "s_ong": "松耸怂颂送宋讼诵凇菘崧嵩忪悚淞竦",
    "s_ou": "搜艘擞嗽叟嗖嗾馊溲飕瞍锼螋",
    "s_u": "苏酥俗素速粟僳塑溯宿诉肃夙谡蔌嗉愫簌觫稣",
    "s_uan": "酸蒜算",
    "s_ui": "虽隋随绥髓碎岁穗遂隧祟蓑冫谇濉邃燧眭睢",
    "s_un": "孙损笋荪狲飧榫跣隼",
    "s_uo": "梭唆缩琐索锁所唢嗦娑桫睃羧",
    "t_a": "塌他它她塔獭挞蹋踏闼溻遢榻沓",
    "t_ai": "胎苔抬台泰酞太态汰邰薹肽炱钛跆鲐",
    "t_an": "坍摊贪瘫滩坛檀痰潭谭谈坦毯袒碳探叹炭郯蕈昙钽锬覃",
    "t_ang": "汤塘搪堂棠膛唐糖傥饧溏瑭铴镗耥螗螳羰醣倘躺淌趟烫",
    "t_ao": "掏涛滔绦萄桃逃淘陶讨套挑鼗啕韬饕",
    "t_e": "特",
    "t_eng": "藤腾疼誊滕",
    "t_ee": "梯剔踢锑提题蹄啼体替嚏惕涕剃屉荑悌逖绨缇鹈裼醍",
    "t_ian": "天添填田甜恬舔腆掭忝阗殄畋钿蚺",
    "t_iao": "条迢眺跳佻祧铫窕龆鲦",
    "t_ie": "贴铁帖萜餮",
    "t_ing": "厅听烃汀廷停亭庭挺艇莛葶婷梃蜓霆",
    "t_ong": "通桐酮瞳同铜彤童桶捅筒统痛佟僮仝茼嗵恸潼砼",
    "t_ou": "偷投头透亠",
    "t_u": "凸秃突图徒途涂屠土吐兔堍荼菟钍酴",
    "t_uan": "湍团疃",
    "t_ui": "推颓腿蜕褪退忒煺",
    "t_un": "吞屯臀饨暾豚窀",
    "t_uo": "拖托脱鸵陀驮驼椭妥拓唾乇佗坨庹沱柝砣箨舄跎鼍",
    "w_a": "挖哇蛙洼娃瓦袜佤娲腽",
    "w_ai": "歪外",
    "w_an": "豌弯湾玩顽丸烷完碗挽晚皖惋宛婉万腕剜芄苋菀纨绾琬脘畹蜿箢",
    "w_ang": "汪王亡枉网往旺望忘妄罔尢惘辋魍",
    "w_ei": "威巍微危韦违桅围唯惟为潍维苇萎委伟伪尾纬未蔚味畏胃喂魏位渭谓尉慰卫倭偎诿隈葳薇帏帷崴嵬猥猬闱沩洧涠逶娓玮韪軎炜煨熨痿艉鲔",
    "w_en": "瘟温蚊文闻纹吻稳紊问刎愠阌汶璺韫殁雯",
    "w_eng": "嗡翁瓮蓊蕹",
    "w_o": "挝蜗涡窝我斡卧握沃莴幄渥杌肟龌",
    "w_u": "巫呜钨乌污诬屋无芜梧吾吴毋武五捂午舞伍侮坞戊雾晤物勿务悟误兀仵阢邬圬芴庑怃忤浯寤迕妩骛牾焐鹉鹜蜈鋈鼯",
    "x_ee": "昔熙析西硒矽晰嘻吸锡牺稀息希悉膝夕惜熄烯溪汐犀檄袭席习媳喜铣洗系隙戏细僖兮隰郗茜葸蓰奚唏徙饩阋浠淅屣嬉玺樨曦觋欷熹禊禧钸皙穸蜥蟋舾羲粞翕醯鼷",
    "x_ia": "瞎虾匣霞辖暇峡侠狭下厦夏吓掀葭嗄狎遐瑕硖瘕罅黠",
    "x_ian": "锨先仙鲜纤咸贤衔舷闲涎弦嫌显险现献县腺馅羡宪陷限线冼藓岘猃暹娴氙祆鹇痫蚬筅籼酰跹",
    "x_iang": "相厢镶香箱襄湘乡翔祥详想响享项巷橡像向象芗葙饷庠骧缃蟓鲞飨",
    "x_iao": "萧硝霄削哮嚣销消宵淆晓小孝校肖啸笑效哓咻崤潇逍骁绡枭枵筱箫魈",
    "x_ie": "楔些歇蝎鞋协挟携邪斜胁谐写械卸蟹懈泄泻谢屑偕亵勰燮薤撷廨瀣邂绁缬榭榍歙躞",
    "x_in": "薪芯锌欣辛新忻心信衅囟馨莘歆铽鑫",
    "x_ing": "星腥猩惺兴刑型形邢行醒幸杏性姓陉荇荥擤悻硎",
    "x_iong": "兄凶胸匈汹雄熊芎",
    "x_iu": "休修羞朽嗅锈秀袖绣莠岫馐庥鸺貅髹",
    "x_v": "墟戌需虚嘘须徐许蓄酗叙旭序畜恤絮婿绪续讴诩圩蓿怵洫溆顼栩煦砉盱胥糈醑",
    "x_van": "轩喧宣悬旋玄选癣眩绚儇谖萱揎馔泫洵渲漩璇楦暄炫煊碹铉镟痃",
    "x_ve": "靴薛学穴雪血噱泶鳕谑",
    "x_vn": "勋熏循旬询寻驯巡殉汛训讯逊迅巽埙荀薰峋徇浔曛窨醺鲟",
    "y_a": "压押鸦鸭呀丫芽牙蚜崖衙涯雅哑亚讶伢揠吖岈迓娅琊桠氩砑睚痖",
    "y_an": "焉咽阉烟淹盐严研蜒岩延言颜阎炎沿奄掩眼衍演艳堰燕厌砚雁唁彦焰宴谚验厣靥赝俨偃兖讠谳郾鄢芫菸崦恹闫阏洇湮滟妍嫣琰晏胭腌焱罨筵酽魇餍鼹",
    "y_ang": "殃央鸯秧杨扬佯疡羊洋阳氧仰痒养样漾徉怏泱炀烊恙蛘鞅",
    "y_ao": "邀腰妖瑶摇尧遥窑谣姚咬舀药要耀夭爻吆崾徭瀹幺珧杳曜肴鹞窈繇鳐",
    "y_e": "椰噎耶爷野冶也页掖业叶曳腋夜液谒邺揶馀晔烨铘",
    "y_ee": "一壹医揖铱依伊衣颐夷遗移仪胰疑沂宜姨彝椅蚁倚已乙矣以艺抑易邑屹亿役臆逸肄疫亦裔意毅忆义益溢诣议谊译异翼翌绎刈劓佾诒圪圯埸懿苡薏弈奕挹弋呓咦咿噫峄嶷猗饴怿怡悒漪迤驿缢殪贻旖熠钇镒镱痍瘗癔翊衤蜴舣羿翳酏黟",
    "y_in": "茵荫因殷音阴姻吟银淫寅饮尹引隐印胤鄞堙茚喑狺夤氤铟瘾蚓霪龈",
    "y_ing": "英樱婴鹰应缨莹萤营荧蝇迎赢盈影颖硬映嬴郢茔莺萦撄嘤膺滢潆瀛瑛璎楹鹦瘿颍罂",
    "y_o": "哟唷",
    "y_ong": "拥佣臃痈庸雍踊蛹咏泳涌永恿勇用俑壅墉慵邕镛甬鳙饔",
    "y_ou": "幽优悠忧尤由邮铀犹油游酉有友右佑釉诱又幼卣攸侑莸呦囿宥柚猷牖铕疣蝣鱿黝鼬",
    "y_v": "迂淤于盂榆虞愚舆余俞逾鱼愉渝渔隅予娱雨与屿禹宇语羽玉域芋郁吁遇喻峪御愈欲狱育誉浴寓裕预豫驭禺毓伛俣谀谕萸蓣揄喁圄圉嵛狳饫庾阈妪妤纡瑜昱觎腴欤於煜燠聿钰鹆瘐瘀窳蝓竽舁雩龉",
    "y_van": "鸳渊冤元垣袁原援辕园员圆猿源缘远苑愿怨院塬沅媛瑗橼爰眢鸢螈鼋",
    "y_ve": "曰约越跃钥岳粤月悦阅龠樾刖钺",
    "y_vn": "耘云郧匀陨允运蕴酝晕韵孕郓芸狁恽纭殒昀氲",
    "z_a": "匝砸杂拶咂",
    "z_ai": "栽哉灾宰载再在咱崽甾",
    "z_an": "攒暂赞瓒昝簪糌趱錾",
    "z_ang": "赃脏葬奘戕臧",
    "z_ao": "遭糟凿藻枣早澡蚤躁噪造皂灶燥唣缫",
    "z_e": "责择则泽仄赜啧迮昃笮箦舴",
    "z_ei": "贼",
    "z_en": "怎谮",
    "z_eng": "增憎曾赠缯甑罾锃",
    "zh_a": "扎喳渣札轧铡闸眨栅榨咋乍炸诈揸吒咤哳怍砟痄蚱齄",
    "zh_ai": "摘斋宅窄债寨砦",
    "zh_an": "瞻毡詹粘沾盏斩辗崭展蘸栈占战站湛绽谵搌旃",
    "zh_ang": "樟章彰漳张掌涨杖丈帐账仗胀瘴障仉鄣幛嶂獐嫜璋蟑",
    "zh_ao": "招昭找沼赵照罩兆肇召爪诏棹钊笊",
    "zh_e": "遮折哲蛰辙者锗蔗这浙谪陬柘辄磔鹧褚蜇赭",
    "zh_en": "珍斟真甄砧臻贞针侦枕疹诊震振镇阵缜桢榛轸赈胗朕祯畛鸩",
    "zh_eng": "蒸挣睁征狰争怔整拯正政帧症郑证诤峥钲铮筝",
    "zh_i": "芝枝支吱蜘知肢脂汁之织职直植殖执值侄址指止趾只旨纸志挚掷至致置帜峙制智秩稚质炙痔滞治窒卮陟郅埴芷摭帙忮彘咫骘栉枳栀桎轵轾攴贽膣祉祗黹雉鸷痣蛭絷酯跖踬踯豸觯",
    "zh_ong": "中盅忠钟衷终种肿重仲众冢锺螽舂舯踵",
    "zh_ou": "舟周州洲诌粥轴肘帚咒皱宙昼骤啄着倜诹荮鬻纣胄碡籀舳酎鲷",
    "zh_u": "珠株蛛朱猪诸诛逐竹烛煮拄瞩嘱主著柱助蛀贮铸筑住注祝驻伫侏邾苎茱洙渚潴驺杼槠橥炷铢疰瘃蚰竺箸翥躅麈",
    "zh_ua": "抓",
    "zh_uai": "拽",
    "zh_uan": "专砖转撰赚篆抟啭颛",
    "zh_uang": "桩庄装妆撞壮状丬",
    "zh_ui": "椎锥追赘坠缀萑骓缒",
    "zh_un": "谆准",
    "zh_uo": "捉拙卓桌琢茁酌灼浊倬诼廴蕞擢啜浞涿杓焯禚斫",
    "z_i": "兹咨资姿滋淄孜紫仔籽滓子自渍字谘嵫姊孳缁梓辎赀恣眦锱秭耔笫粢觜訾鲻髭",
    "z_ong": "鬃棕踪宗综总纵腙粽",
    "z_ou": "邹走奏揍鄹鲰",
    "z_u": "租足卒族祖诅阻组俎菹啐徂驵蹴",
    "z_uan": "钻纂攥缵",
    "z_ui": "嘴醉最罪",
    "z_un": "尊遵撙樽鳟",
    "z_uo": "昨左佐柞做作坐座阝阼胙祚酢",
    "c_ou": "薮楱辏腠",
    "n_ang": "攮哝囔馕曩",
    "o": "喔",
    "d_ia": "嗲",
    "ch_uai": "嘬膪踹",
    "c_en": "岑涔",
    "d_iu": "铥",
    "n_ou": "耨",
    "f_ou": "缶",
    "b_ia": "髟",
}

# https://github.com/xmcp/pakku.js/blob/9a8c59591d9d9a17dfa39595d995d2f08c781014/pakkujs/core/combine_worker.ts#L14
ENDING_CHARS = set(".。,，/?？!！…~～@^、+=-_♂♀ ")
TRIM_EXTRA_SPACE_RE = re.compile(r"[  ]+")
TRIM_CJK_SPACE_RE = re.compile(
    r"([\u3000-\u9FFF\uFF00-\uFFEF]) (?=[\u3000-\u9FFF\uFF00-\uFFEF])"
)
WIDTH_TABLE = {
    " ": " ",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
    "０": "0",
    "!": "！",
    "＠": "@",
    "＃": "#",
    "＄": "$",
    "％": "%",
    "＾": "^",
    "＆": "&",
    "＊": "*",
    "（": "(",
    "）": ")",
    "－": "-",
    "＝": "=",
    "＿": "_",
    "＋": "+",
    "［": "[",
    "］": "]",
    "｛": "{",
    "｝": "}",
    ";": "；",
    "＇": "'",
    ":": "：",
    "＂": '"',
    ",": "，",
    "．": ".",
    "／": "/",
    "＜": "<",
    "＞": ">",
    "?": "？",
    "＼": "\\",
    "｜": "|",
    "｀": "`",
    "～": "~",
    "ｑ": "q",
    "ｗ": "w",
    "ｅ": "e",
    "ｒ": "r",
    "ｔ": "t",
    "ｙ": "y",
    "ｕ": "u",
    "ｉ": "i",
    "ｏ": "o",
    "ｐ": "p",
    "ａ": "a",
    "ｓ": "s",
    "ｄ": "d",
    "ｆ": "f",
    "ｇ": "g",
    "ｈ": "h",
    "ｊ": "j",
    "ｋ": "k",
    "ｌ": "l",
    "ｚ": "z",
    "ｘ": "x",
    "ｃ": "c",
    "ｖ": "v",
    "ｂ": "b",
    "ｎ": "n",
    "ｍ": "m",
    "Ｑ": "Q",
    "Ｗ": "W",
    "Ｅ": "E",
    "Ｒ": "R",
    "Ｔ": "T",
    "Ｙ": "Y",
    "Ｕ": "U",
    "Ｉ": "I",
    "Ｏ": "O",
    "Ｐ": "P",
    "Ａ": "A",
    "Ｓ": "S",
    "Ｄ": "D",
    "Ｆ": "F",
    "Ｇ": "G",
    "Ｈ": "H",
    "Ｊ": "J",
    "Ｋ": "K",
    "Ｌ": "L",
    "Ｚ": "Z",
    "Ｘ": "X",
    "Ｃ": "C",
    "Ｖ": "V",
    "Ｂ": "B",
    "Ｎ": "N",
    "Ｍ": "M",
}


def create_pinyin_table(pinyin_dict_raw):
    ret = {}
    symbols = {}
    symbol_idx = 0xE000

    for phonetic_raw, characters in pinyin_dict_raw.items():
        phonetics = "".join(
            symbols.setdefault(phonetic, chr(symbol_idx := symbol_idx + 1))
            for phonetic in phonetic_raw.split("_")
        )

        for c in characters:
            ret[c] = phonetics

    return ret


PINYIN_TABLE = create_pinyin_table(PINYIN_DICT_RAW)
FORCELIST = [
    (re.compile(r"^23{2,}"), "233..."),
    (re.compile(r"^6{3,}$"), "666..."),
    (re.compile(r"^[fF]+$"), "FFF..."),
    (re.compile(r"^[hH]+$"), "hhh..."),
    (re.compile(r"^[yYoO0][yYoO0\s~]+$"), "yoo..."),
]


def preprocess_str(inp: str) -> str:
    inp = re.sub(r"[\r\n\t]", "", inp)
    len_inp = len(inp)
    text = ""

    while len_inp > 0 and inp[len_inp - 1] in ENDING_CHARS:
        len_inp -= 1

    if len_inp == 0:
        len_inp = len(inp)

    for i in range(len_inp):
        c = inp[i]
        text += WIDTH_TABLE.get(c, c)

    text = re.sub(TRIM_EXTRA_SPACE_RE, " ", text)
    text = re.sub(TRIM_CJK_SPACE_RE, r"\1", text)

    for cliche in FORCELIST:
        if cliche[0].search(text):
            text = cliche[0].sub(cliche[1], text)
            return text

    return text


def trim_pinyin(text: str) -> str:
    return "".join(PINYIN_TABLE.get(c, c) for c in text.lower())


# https://github.com/xmcp/pakku.js/blob/9a8c59591d9d9a17dfa39595d995d2f08c781014/pakkujs/core/similarity.ts#L3C1-L28C2
MAX_UNICODE = 0x10FFFF
ed_a = [0] * (MAX_UNICODE + 1)
ed_b = [0] * (MAX_UNICODE + 1)
ed_counts = ed_a


# For debugging...
similar_counters = {
    "identical": 0,
    "edit-distance": 0,
    "pinyin-edit-distance": 0,
    "cosine": 0,
}


def is_similar(x: str, y: str) -> bool:
    MAX_DIST = 5
    MIN_SIZE = max(1, MAX_DIST * 2)
    MAX_COSINE = 60

    def edit_distance(x: str, y: str) -> int:
        for i in range(len(x) - 1, -1, -1):
            ed_counts[ord(x[i])] += 1
        for i in range(len(y) - 1, -1, -1):
            ed_counts[ord(y[i])] -= 1
        ans = 0

        for i in range(len(x) - 1, -1, -1):
            ans += abs(ed_counts[ord(x[i])])
            ed_counts[ord(x[i])] = 0

        for i in range(len(y) - 1, -1, -1):
            ans += abs(ed_counts[ord(y[i])])
            ed_counts[ord(y[i])] = 0

        return ans

    def gen_2gram_array(x: str) -> list[int]:
        P_length_1 = len(x)
        x += x[0]
        res = []

        clast = ord(x[0])
        for i in range(1, P_length_1 + 1):
            c = ord(x[i])
            res.append(((clast << 10) ^ c) & 1048575)
            clast = c

        return res

    def cosine_distance(Pgram: list[int], Qgram: list[int]) -> float:
        Plen = len(Pgram)
        Qlen = len(Qgram)
        for i in range(Plen):
            ed_a[Pgram[i]] += 1

        for i in range(Qlen):
            ed_b[Qgram[i]] += 1

        x = 0
        y = 0
        z = 0

        for i in range(Plen):
            h1 = Pgram[i]
            xa = ed_a[h1]
            if xa > 0:
                xb = ed_b[h1]
                y += xa * xa
                if xb > 0:
                    x += xa * xb
                    z += xb * xb
                    ed_b[h1] = 0
                ed_a[h1] = 0

        for i in range(Qlen):
            h1 = Qgram[i]
            xb = ed_b[h1]
            if xb > 0:
                z += xb * xb
                ed_b[h1] = 0

        return (x * x) / (y * z) if y != 0 and z != 0 else 0.0

    x = preprocess_str(x)
    y = preprocess_str(y)
    if x == y:
        similar_counters["identical"] += 1
        return True
    distance = edit_distance(x, y)
    if len(x) + len(y) < MIN_SIZE:
        if distance < (len(x) + len(y)) / MIN_SIZE * MAX_DIST - 1:
            similar_counters["edit-distance"] += 1
            return True
    else:
        if distance <= MAX_DIST:
            similar_counters["edit-distance"] += 1
            return True
    x_pinyin = trim_pinyin(x)
    y_pinyin = trim_pinyin(y)
    pinyin_distance = edit_distance(x_pinyin, y_pinyin)
    if len(x) + len(y) < MIN_SIZE:
        if pinyin_distance < (len(x) + len(y)) / MIN_SIZE * MAX_DIST - 1:
            similar_counters["pinyin-edit-distance"] += 1
            return True
    else:
        if pinyin_distance <= MAX_DIST:
            similar_counters["pinyin-edit-distance"] += 1
            return True
    if distance < len(x) + len(y):
        x_2gram = gen_2gram_array(x)
        y_2gram = gen_2gram_array(y)
        cos = math.floor(cosine_distance(x_2gram, y_2gram) * 100)
        if cos >= MAX_COSINE:
            similar_counters["cosine"] += 1
            return True
    return False


@dataclass
class DanmukuObject:
    time_ms: int
    mode: int
    fontsize: float
    color: int
    sender_hash: str
    content: str
    sendtime: int
    id: str
    pool: int
    weight: int


# https://github.com/xmcp/pakku.js/blob/9a8c59591d9d9a17dfa39595d995d2f08c781014/pakkujs/protocol/interface_xml.ts#L25C1-L58C2
def get_objects(tree: ET.ElementTree) -> tuple[list[DanmukuObject], dict[str, str]]:
    res = []
    conf = {}

    root = tree.getroot()
    if root.tag.lower() != "i":
        raise ValueError("root_elem tagname is not <i>")
    for elem in root:
        if elem.tag.lower() == "d":
            attr = elem.attrib["p"].split(",")
            str_content = elem.text if elem.text else ""

            res.append(
                DanmukuObject(
                    time_ms=int(float(attr[0]) * 1000),
                    mode=int(attr[1]),
                    fontsize=float(attr[2]),
                    color=int(attr[3]),
                    sender_hash=attr[6],
                    content=str_content,
                    sendtime=int(attr[4]),
                    id=attr[7],
                    pool=int(attr[5]),
                    weight=int(attr[8]),
                )
            )
        else:
            conf[f"xml_{elem.tag.lower()}"] = elem.text if elem.text else ""

    return res, conf


@dataclass
class ClusteredDanmuku:
    peers: list[DanmukuObject]
    contents: str


def combine(objects: list[DanmukuObject]) -> list[ClusteredDanmuku]:
    THRESHOLD_MS = 20 * 1000

    clusters: list[ClusteredDanmuku] = []

    def select_median_length(s: list[str]) -> str:
        if not s:
            return ""
        s.sort(key=len)
        return s[len(s) // 2]

    def apply_cluster(dms: list[DanmukuObject]) -> None:
        if len(dms) == 1:
            clusters.append(ClusteredDanmuku(peers=dms, contents=dms[0].content))
        else:
            text_cnts: DefaultDict[str, int] = defaultdict(int)
            most_texts = []
            most_cnt = 0

            for dm in dms:
                text = dm.content
                text_cnts[text] += 1
                cnt = text_cnts[text]

                if cnt > most_cnt:
                    most_texts = [text]
                    most_cnt = cnt
                elif cnt == most_cnt:
                    most_texts.append(text)

            most_text = select_median_length(most_texts)

            clusters.append(ClusteredDanmuku(peers=dms, contents=most_text))

    nearby_dms: list[list[DanmukuObject]] = []
    for dm in objects:
        while nearby_dms and dm.time_ms - nearby_dms[0][0].time_ms > THRESHOLD_MS:
            apply_cluster(nearby_dms.pop(0))

        sim = False
        for candidate in nearby_dms:
            dm0 = candidate[0]

            sim = is_similar(dm.content, dm0.content)
            if sim:
                candidate.append(dm)
                break

        if sim is False:
            nearby_dms.append([dm])

    while nearby_dms:
        apply_cluster(nearby_dms.pop(0))

    return clusters


# https://github.com/xmcp/pakku.js/blob/9a8c59591d9d9a17dfa39595d995d2f08c781014/pakkujs/core/post_combine.ts#L37
SUBSCRIPT_CHARS = [chr(0x2080 + x) for x in range(10)]


def to_subscript(x: int) -> str:
    ret = SUBSCRIPT_CHARS[x % 10]
    while x >= 10:
        x //= 10
        ret = SUBSCRIPT_CHARS[x % 10] + ret
    return ret


def post_combine(clusters: list[ClusteredDanmuku]) -> list[DanmukuObject]:
    def calc_enlarge_rate(cnt: int) -> float:
        return 1 if cnt < 5 else math.log(cnt, 5)

    def build_text(cluster: ClusteredDanmuku, s: str) -> str:
        MARK_THRESHOLD = 1
        cnt = len(cluster.peers)
        if cnt > MARK_THRESHOLD:
            return f"₍{to_subscript(cnt)}₎" + s
        return s

    res = []
    for cluster in clusters:
        if len(cluster.peers) == 0:
            continue  # though this should not happen...
        rep_dm = cluster.peers[0]
        max_dm_size = rep_dm.fontsize
        max_mode = rep_dm.mode
        for peer in cluster.peers:
            if peer.fontsize < 30:
                max_dm_size = max(max_dm_size, peer.fontsize)
            if peer.mode == 4:
                max_mode = 4
            elif peer.mode == 5 and max_mode != 4:
                max_mode = 5
        rep_dm.mode = max_mode
        rep_dm.fontsize = math.ceil(
            rep_dm.fontsize * calc_enlarge_rate(len(cluster.peers))
        )
        rep_dm.content = build_text(cluster, rep_dm.content)
        res.append(rep_dm)
    return res


def construct_xml(dms: list[DanmukuObject], header: dict[str, str]) -> str:
    # Create the root <i> element
    i_elem = ET.Element("i")

    # Add the static fields as sub-elements
    ET.SubElement(i_elem, "chatserver").text = "chat.bilibili.com"
    ET.SubElement(i_elem, "chatid").text = str(header.get("xml_chatid", 0))
    ET.SubElement(i_elem, "mission").text = "0"
    ET.SubElement(i_elem, "maxlimit").text = str(
        header.get("xml_maxlimit", len(dms) + 1)
    )
    ET.SubElement(i_elem, "state").text = "0"
    ET.SubElement(i_elem, "real_name").text = "0"

    # Loop through the danmu objects and create <d> elements
    for d in dms:
        elem = ET.Element("d")
        # The <d> element has only text content and a 'p' attribute
        elem.text = d.content
        attr = [
            d.time_ms / 1000,  # 0
            d.mode,  # 1
            d.fontsize,  # 2
            d.color,  # 3
            d.sendtime,  # 4
            d.pool,  # 5
            d.sender_hash,  # 6
            d.id,  # 7
            d.weight,  # 8
        ]
        elem.set("p", ",".join(map(str, attr)))
        i_elem.append(elem)

    # Convert the ElementTree to a string
    xml_str = ET.tostring(i_elem, encoding="unicode")

    # Prettify the XML by using minidom
    dom = minidom.parseString(xml_str)
    pretty_xml_as_str = dom.toprettyxml(indent="  ")

    # Further format to match the requested formatting from the JavaScript version
    # Removing extra new lines introduced by minidom (it introduces too many new lines)
    formatted_str = "".join(
        [line for line in pretty_xml_as_str.splitlines() if line.strip()]
    )

    # Replace <d p=...> to have new lines as in the JS version
    return formatted_str.replace("<d p=", "\n  <d p=").replace("</i>", "\n</i>")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} [XMLFILE] [WIDTH] [HEIGHT]")
        sys.exit(1)
    tree = ET.parse(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    objects, header = get_objects(tree)
    objects.sort(key=lambda obj: obj.time_ms)
    clustered = combine(objects)
    final_dms = post_combine(clustered)
    result_xml = construct_xml(final_dms, header)
    print(convert_to_ass(result_xml, width, height, font_size=50, duration_marquee=15, duration_still=10, text_opacity=0.8, reduce_comments=False))
