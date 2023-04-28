from urllib.request import Request, urlopen
import urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import simplekml

# Ignorar erros de certificado SSL

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#comunicar com o site

def coletahtml(url):

    req=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req, timeout=100).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#Códigos das cidades
cidades = {'campo grande': 1, 'agua clara': 11, 'alcinopolis': 12, 'amambai': 66, 'anastacio': 55, 'anaurilandia': 191, 'angelica': 240, 'anhandui': 93, 'antonio joao': 299, 'aparecida do taboado': 136, 'aquidauana': 10, 'aral moreira': 243, 'bandeirantes': 13, 'bataguassu': 224, 'bataypora': 301, 'bela vista': 74, 'bodoquena': 56, 'bonito': 4, 'brasilandia': 59, 'caarapo': 260, 'camapua': 9, 'caracol': 127, 'cassilandia': 85, 'chapadao do sul': 94, 'cipolandia': 61, 'corguinho': 14, 'coronel sapucaia': 68, 'corumba': 15, 'costa rica': 98, 'coxim': 6, 'deodapolis': 172, 'dois irmaos do buriti': 46, 'douradina': 90, 'dourados': 22, 'eldorado': 52, 'fatima do sul': 138, 'figueirao': 21, 'gloria de dourados': 194, 'guia lopes da laguna': 101, 'iguatemi': 51, 'inocencia': 135, 'itapora': 67, 'itaquirai': 333, 'ivinhema': 280, 'japora': 334, 'jaraguari': 16, 'jardim': 40, 'jatei': 17, 'juti': 335, 'ladario': 271, 'laguna carapa': 226, 'maracaju': 53, 'miranda': 58, 'mundo novo': 79, 'navirai': 146, 'nhecolandia': 249, 'nioaque': 89, 'nova alvorada do sul': 75, 'nova andradina': 92, 'novo horizonte do sul': 337, 'palmeiras': 49, 'paraiso das aguas': 309, 'paranaiba': 73, 'paranhos': 63, 'parque das aguas': 322, 'pedro gomes': 7, 'piraputanga': 105, 'ponta pora': 47, 'porto murtinho': 50, 'ribas do rio pardo': 18, 'rio brilhante': 76, 'rio negro': 54, 'rio verde': 8, 'rio verde de mato grosso': 296, 'rochedinho': 95, 'rochedo': 19, 'santa rita do pardo': 338, 'sao gabriel do oeste': 5, 'sao joã£o': 104, 'selviria': 339, 'sete quedas': 227, 'sidrolandia': 20, 'sonora': 142, 'tacuru': 64, 'taquarussu': 340, 'terenos': 48, 'tres lagoas': 60, 'vicentina': 336}

print('##########################################')
print('\n\n   Desenvolvido por Carlos Fernandes\n\n')
print('##########################################\n')

print(u'Para usar esta aplicação, não use acentos ou cedilha!\n')

while True:
    city = input('Insira a cidade: ')
    city=city.lower()
    if city in cidades: 
        print('Cidade encontrada! Por favor aguarde enquanto coleto os elementos para você\n')
        break
    else: print(u'Cidade não encontrada!\nPor favor, verifique o nome da cidade e tente novamente.\n')

#Se a cidade for Campo Grande, a pesquisa será feita por bairro
if city == 'campo grande':
    print(u'Antes de prosseguir, verifique como está o nome do bairro no site do Infoimóveis :)\n')
    while True:
        bairro = input('Insira o bairro: ').lower()
        #Códigos dos bairros de CG
        bairros = {'aero rancho': '1399', 'altos da afonso pena': '2248', 'amambai': '44', 'amantini residence': '2500', 'arapongas': '1665', 'arnaldo estevao de figueiredo': '296', 'atlantico sul': '502', 'autonomista': '1400', 'beirute residence park': '2222', 'bela laguna': '2491', 'bom retiro': '2082', 'bosque das araras': '2157', 'bosque de avilan': '1036', 'bosque santa monica': '1186', 'bosque santa monica ii': '1052', 'buriti': '346', 'cabreuva': '75', 'cachoeirinha': '1303', 'caicara': '172', 'caranda': '1851', 'caranda bosque i': '51', 'caranda bosque ii': '95', 'caranda bosque iii': '132', 'cascudo': '1216', 'centenario': '1401', 'center park': '1799', 'centro': '3', 'chacara boa vista': '1247', 'chacara cachoeira': '19', 'chacara cachoeira ii': '1203', 'chacara das mansoes': '29', 'chacara dos coqueiros': '1304', 'chacara dos poderes': '60', 'chacara jose antonio pereira': '1767', 'chacara vendas': '152', 'cidade jardim': '65', 'clube campestre ype': '576', 'cofermat': '1217', 'cohafama': '297', 'condominio fernando sabino': '1432', 'conjunto hab. jardim anapolis': '1485', 'conjunto hab. jardim roselandia': '1492', 'conjunto oscar salazar': '1888', 'conjunto res. leon denizart conte': '1428', 'conjunto res. monte castelo': '1296', 'conjunto res. nova bahia': '22', 'conjunto res. nova olinda': '1726', 'conjunto res. novo alagoas': '565', 'conjunto res. novo amazonas': '532', 'conjunto res. novo maranhao': '666', 'conjunto res. novo minas gerais': '559', 'conjunto res. novo parana': '560', 'conjunto res. novo pernambuco': '561', 'conjunto res. novo rio grande do sul': '1364', 'conjunto res. novo sao paulo': '1365', 'conjunto res. novo sergipe': '1366', 'conjunto uniao': '353', 'coophaban': '62', 'coophafe': '52', 'coophagrande': '1297', 'coophamat': '329', 'coophamorena': '1237', 'coopharadio': '45', 'coophasul': '191', 'coophatrabalho': '158', 'coophavila': '149', 'coophavila ii': '143', 'coophavilla': '1408', 'coronel antonino': '25', 'costa verde': '1082', 'cruzeiro': '1298', 'desbarrancado': '2049', 'desm. esteban cornelas': '1414', 'eldorado': '1394', 'enseada dos passaros': '1940', 'estrela do sul': '295', 'estrela park': '1020', 'flamboyant': '14', 'giocondo orsi': '48', 'giocondo orsi ii': '131', 'golden gate park': '2489', 'granja bandeira': '1486', 'granja sao luiz': '1412', 'guanabara': '667', 'guanandi': '64', 'indubrasil': '592', 'industrial': '2402', 'iracy coelho': '144', 'itamarati': '2037', 'itanhanga park': '2', 'jacy': '1424', 'jardim 7 de setembro': '1305', 'jardim aclimacao': '582', 'jardim aeroporto': '412', 'jardim aguas vivas': '1448', 'jardim agulhas negras': '1487', 'jardim alegre': '69', 'jardim alto sao francisco': '184', 'jardim alvorada': '135', 'jardim america': '112', 'jardim ametista': '1696', 'jardim anache': '796', 'jardim anhanguera': '1766', 'jardim antares': '1198', 'jardim antartica': '398', 'jardim arco iris': '970', 'jardim aroeira': '1848', 'jardim autonomista': '139', 'jardim autonomista ii': '2492', 'jardim autonomista iii': '2493', 'jardim auxiliadora': '138', 'jardim balsamo': '1651', 'jardim barcelona': '1687', 'jardim batistao': '413', 'jardim bela vista': '15', 'jardim bonanca': '355', 'jardim botafogo': '188', 'jardim botanico': '1012', 'jardim botanico ii': '1488', 'jardim brasil': '1218', 'jardim cabral': '1417', 'jardim campina verde': '1444', 'jardim campo alto': '1066', 'jardim campo belo': '1374', 'jardim campo nobre': '660', 'jardim campo novo': '1375', 'jardim canada': '1384', 'jardim canguru': '358', 'jardim carioca': '891', 'jardim centenario': '114', 'jardim centro oeste': '714', 'jardim cidade': '1223', 'jardim cidade morena': '648', 'jardim colibri': '338', 'jardim colibri ii': '1468', 'jardim colonial': '335', 'jardim colorado': '1749', 'jardim columbia': '575', 'jardim corcovado': '354', 'jardim cristo redentor': '658', 'jardim da mooca': '2639', 'jardim das acacias': '695', 'jardim das cassias': '2528', 'jardim das cerejeiras': '661', 'jardim das hortencias i': '1030', 'jardim das hortencias ii': '1410', 'jardim das hortencias iii': '1411', 'jardim das macaubas': '1407', 'jardim das mansoes universitarias': '1489', 'jardim das meninas': '1184', 'jardim das nacoes': '150', 'jardim das paineiras': '401', 'jardim das perdizes': '408', 'jardim das reginas': '1642', 'jardim das virtudes': '1143', 'jardim de allah': '1245', 'jardim do corrego': '2033', 'jardim dos boggi': '1648', 'jardim dos estados': '1', 'jardim estrela dalva i': '332', 'jardim estrela dalva ii': '626', 'jardim estrela dalva iii': '1204', 'jardim fluminense': '617', 'jardim guaruja': '76', 'jardim ibirapuera': '53', 'jardim ima': '40', 'jardim imperial': '128', 'jardim inapolis': '1115', '1051 jardim indianapolis': '', 'jardim ipanema': '100', 'jardim italia': '1434', 'jardim itamaraca': '300', 'jardim itapema': '846', 'jardim itatiaia': '80', 'jardim jacaranda': '540', 'jardim jacy': '109', 'jardim jane': '1490', 'jardim joquei club': '66', 'jardim lagoa dourada': '556', 'jardim leblon': '68', 'jardim leonidia': '1734', 'jardim los angeles': '352', 'jardim macapa': '1469', 'jardim manaira': '1093', 'jardim mansur': '84', 'jardim maraba': '607', 'jardim marajoara': '538', 'jardim mathilde': '1948', 'jardim mato grosso': '1393', 'jardim mirasol': '1837', 'jardim moema': '1467', 'jardim monte alegre': '1155', 'jardim monte alto': '1378', 'jardim monte libano': '11', 'jardim monte verde': '591', 'jardim monterey': '1071', 'jardim montevideu': '563', 'jardim monumento': '99', 'jardim morenao': '654', 'jardim n. sra. do perpetuo socorro': '1116', 'jardim nascente do segredo': '1055', 'jardim nashiville': '362', 'jardim nhanha': '365', 'jardim noroeste': '423', 'jardim nova era': '1248', 'jardim nova jerusalem': '870', 'jardim oracilia': '434', 'jardim ouro preto': '1147', 'jardim ouro verde': '1750', 'jardim pacaembuâ€ž': '1361', 'jardim panama': '284', 'jardim paradiso': '364', 'jardim parati': '113', 'jardim parati ii': '1762', 'jardim paris': '2640', 'jardim paulista': '130', 'jardim paulo coelho machado': '373', 'jardim penfigo': '673', 'jardim petropolis': '142', 'jardim pinheiros': '1416', 'jardim piracicaba': '1238', 'jardim presidente': '391', 'jardim radialista': '1662', 'jardim roselandia': '1491', 'jardim rubiacea': '1493', 'jardim samambaia': '341', 'jardim santa catarina': '1249', 'jardim santa emilia': '500', 'jardim santa felicidade': '573', 'jardim santa ursula': '1494', 'jardim sao bento': '61', 'jardim sao conrado': '187', 'jardim sao lourenco': '54', 'jardim sao paulo': '1219', 'jardim sayonara': '1872', 'jardim seminario': '377', 'jardim serra azul': '539', 'jardim sumatra': '1845', 'jardim talisma': '343', 'jardim taruma': '327', 'jardim tijuca i': '159', 'jardim tijuca ii': '181', 'jardim tropical': '1800', 'jardim tv morena': '67', 'jardim uirapuru': '1450', 'jardim umuarama': '508', 'jardim veneza': '376', 'jardim veraneio': '185', 'jardim vicentino': '1495', 'jardim vida nova': '1053', 'jardim vila kellen': '1763', 'jardim villas lobos': '1380', 'jardim villas lobos ii': '1381', 'jardim vista alegre': '1239', 'jardim vitoria': '1631', 'jardim vitrine': '1759', 'jardim ze pereira': '176', 'jatiuca park': '79', 'joana darc': '2609', 'jose abrao': '323', 'jose tavares do couto': '2031', 'lageado': '1426', 'lagoa da cruz': '1379', 'lagoa park': '1733', 'lar do trabalhador': '90', 'lot. mul. dom antonio barbosa': '1376', 'lot. municipal alan soares': '1471', 'lot. municipal dalva de oliveira': '1893', 'loteamento abaete': '2232', 'loteamento aero rancho': '103', 'loteamento agua limpa park': '1903', 'loteamento alto da boa vista': '1447', 'loteamento bonjardim': '1748', 'loteamento bosque da esperanca': '1730', 'loteamento guanandi ii': '141', 'loteamento jose maksoud': '2695', 'loteamento nova serrana': '1427', 'loteamento paraiso do lageado': '2532', 'loteamento paulo vi': '1151', 'loteamento porto seguro': '1470', 'loteamento portobello': '1821', 'loteamento praia da urca': '1168', 'loteamento rancho alegre i': '1154', 'loteamento rancho alegre ii': '1153', 'loteamento rancho alegre iv': '2452', 'loteamento soter': '1019', 'loteamento tarsila do amaral': '1640', 'loteamento treviso': '2556', 'loteamento vida nova iii': '1714', 'maria aparecida pedrossian': '1431', 'mata do jacinto': '13', 'mata do segredo': '1406', 'monte carlo': '133', 'monte castelo': '21', 'monte verde': '1284', 'montevideu': '553', 'morada do sol': '979', 'morada do sossego': '1134', 'morada do sossego ii': '1135', 'morada dos deuses': '1905', 'morada imperial': '2046', 'morada verde': '866', 'moreninha': '1670', 'n. sra. das gracas': '37', 'n. sra. de fatima': '151', 'nasa park': '2007', 'north park': '2438', 'nova campo grande': '33', 'nova capital': '2042', 'nova jeruzalem': '2041', 'nova lima': '154', 'novos estados': '1398', 'nucleo aero rancho': '1094', 'nucleo aero rancho i': '1464', 'nucleo alves pereira': '1472', 'nucleo colibri ii': '1473', 'nucleo habitacional aero rancho': '1409', 'nucleo habitacional aero rancho i': '1459', 'nucleo habitacional aero rancho ii': '1460', 'nucleo habitacional aero rancho iii': '1461', 'nucleo habitacional aero rancho iv': '1462', 'nucleo habitacional aero rancho v': '1463', 'nucleo habitacional universitarias': '1007', 'nucleo habitacional universitarias i': '1474', 'nucleo habitacional universitarias ii': '1475', 'nucleo industrial': '1688', 'panama iii': '63', 'panorama': '202', 'parati': '1699', 'parque atlantico': '1484', 'parque dallas': '537', 'parque do lageado': '721', 'parque do sol': '1425', 'parque do trabalhador': '1476', 'parque dos ipes': '1801', 'parque dos laranjais': '153', 'parque dos poderes': '127', 'parque dos sabias': '2496', 'parque iguatemi': '2013', 'parque isabel gardens': '270', 'parque novo seculo': '173', 'parque residencial dos bancarios': '1859', 'parque rita vieira': '1765', 'petropoles': '157', 'pioneiros': '1498', 'popular': '627', 'portal caioba': '1014', 'portal caioba ii': '1138', 'portal do gramado': '1636', 'portal do panama': '567', 'portinho pache': '118', 'porto belo': '522', 'porto galo': '1982', 'pq. res. maria aparecida pedrossian': '30', 'pq. residencial azaleia': '416', 'pq. residencial bellinate': '1847', 'pq. residencial damha i': '585', 'pq. residencial damha ii': '586', 'pq. residencial damha iii': '1653', 'pq. residencial damha iv': '1932', 'pq. residencial dos girassois': '1149', 'pq. residencial lisboa': '1496', 'pq. residencial uniao': '1456', 'pq. residencial uniao ii': '1457', 'recanto das andorinhas': '1497', 'recanto das paineiras': '102', 'recanto do cerrado': '1904', 'recanto dos passaros': '85', 'recanto dos rouxinois': '344', 'recanto pantaneiro': '2093', 'regina': '1649', 'residencial alphaville': '1048', 'residencial alphaville ii': '1842', 'residencial alphaville iii': '1931', 'residencial alphaville iv': '1993', 'residencial alto tamandare': '1946', 'residencial ana maria do couto': '342', 'residencial aquarius i': '1754', 'residencial aquarius ii': '1436', 'residencial betaville': '584', 'residencial botafogo': '1499', 'residencial buzios': '1452', 'residencial carajas': '2273', 'residencial colonial': '1500', 'residencial delfos': '2501', 'residencial do lago': '1504', 'residencial eucaliptos': '1502', 'residencial figueiras do parque': '2675', 'residencial flores': '1144', 'residencial gama': '2074', 'residencial ilheus': '1477', 'residencial joao scarano': '1478', 'residencial madri': '1501', 'residencial mario covas': '1017', 'residencial nova tiradentes': '1370', 'residencial oiti': '1655', 'residencial oliveira i': '677', 'residencial oliveira ii': '664', 'residencial oliveira iii': '407', 'residencial otavio pecora': '324', 'residencial praia da enseada': '1503', 'residencial ramez tebet': '1826', 'residencial rancharia': '1132', 'residencial sagarana': '1712', 'residencial santa celina': '18', 'residencial shalom': '2199', 'residencial sirio libanes i': '1088', 'residencial sirio libanes ii': '1150', 'residencial tolentino': '2633', 'residencial via park italia': '2490', 'residencial vila olimpica': '1683', 'residencial village': '1250', 'rita vieira': '1397', 'riviera park': '2044', 'rouxinois': '642', 'royal park': '1437', 'santa carmelia': '405', 'santa fe': '27', 'santo amaro': '1483', 'santo antonio': '35', 'santos dumont': '1839', 'sao caetano': '1368', 'sao francisco': '1396', 'sao pedro': '328', 'serraville': '2299', 'setvillage i': '1950', 'setvillage ii': '1951', 'silvia regina': '523', 'sitio santa maria': '2446', 'sitiocas alvorada': '1793', 'sky residence': '2497', 'taquaral bosque': '564', 'taquarussu': '1402', 'tayama park': '336', 'terras alpha': '2688', 'terras do golfe': '2006', 'tijuca': '1433', 'tiradentes': '59', 'uniao': '1458', 'universitario': '115', 'universitario secao b': '1756', 'universitario secao d': '1479', 'vespasiano martins': '1092', 'vila abdalla': '1671', 'vila abdo': '1306', 'vila adelina': '409', 'vila aimore': '1117', 'vila aimore ii': '182', 'vila alba': '55', 'vila albuquerque': '371', 'vila almeida': '105', 'vila almeida lima': '1646', 'vila alta': '1232', 'vila alto campo de marte': '1307', 'vila alto das paineiras': '1220', 'vila alto sumare': '175', 'vila alves pereira': '1480', 'vila amapa': '1564', 'vila america': '1233', 'vila americana': '1262', 'vila anahy': '294', 'vila anfe': '1221', 'vila antonieta': '1835', 'vila antonio inacio de souza': '1246', 'vila antonio vendas': '117', 'vila antunes': '1481', 'vila aprazivel': '1222', 'vila aurora': '1272', 'vila bandeirante': '88', 'vila barao do rio branco': '1273', 'vila bartiria': '1234', 'vila bela': '595', 'vila belo horizonte': '871', 'vila benjamim': '1225', 'vila bernardo goldman': '1308', 'vila boa vista': '108', 'vila bom jardim': '797', 'vila bom jesus': '2280', 'vila bosque da saudade': '1506', 'vila capri': '1224', 'vila carlota': '87', 'vila carolina': '435', 'vila carvalho': '12', 'vila carvalho bais': '1263', 'vila castelo': '147', 'vila catarina': '1385', 'vila catarina ii': '402', 'vila celia': '17', 'vila cidade morena': '370', 'vila clelia': '1482', 'vila clementina': '1235', 'vila concordia': '1650', 'vila corumba': '496', 'vila costa lima': '1251', 'vila coutinho': '1659', 'vila cristina': '1226', 'vila da saude': '1309', 'vila dalila': '1465', 'vila danubio azul': '865', 'vila do polones': '124', 'vila dom pedrito': '566', 'vila dos ferroviarios': '574', 'vila dr. joao rosa': '1240', 'vila duque de caxias': '396', 'vila eliane': '136', 'vila espanhola': '555', 'vila esplanada': '665', 'vila esportiva': '1310', 'vila estephania': '1285', 'vila eva': '1253', 'vila feliciana carolina': '1286', 'vila fernanda': '2644', 'vila floresta': '1274', 'vila florio': '2171', 'vila fortuna': '1254', 'vila futurista': '1660', 'vila galvao': '1243', 'vila gaspar': '1255', 'vila gatao': '1241', 'vila general wolgrand': '1236', 'vila gloria': '146', 'vila gomes': '93', 'vila guaraciaba': '1311', 'vila guarani': '1294', 'vila guenka': '1275', 'vila helena': '1227', 'vila ieda': '361', 'vila ilgenfritz': '94', 'vila independencia': '1295', 'vila ipiranga': '42', 'vila isis': '1312', 'vila jardim beija-flor': '1736', 'vila jardim pioneiros': '1087', 'vila jardim sao bernardo': '1442', 'vila joselito': '89', 'vila julieta': '893', 'vila jurema': '1415', 'vila jussara': '499', 'vila leda': '430', 'vila lia': '1313', 'vila liberdade': '1256', 'vila lidia': '1228', 'vila lucinda': '190', 'vila maciel': '1181', 'vila mandeta': '1314', 'vila manoel da costa lima': '1984', 'vila manoel taveira': '404', 'vila maracaju': '1276', 'vila marcos roberto': '38', 'vila margarida': '86', 'vila maria': '1315', 'vila mariana': '1316', 'vila marisa': '1293', 'vila marly': '558', 'vila marman': '1299', 'vila miguel couto': '178', 'vila moreninha i': '494', 'vila moreninha ii': '363', 'vila moreninha iii': '1199', 'vila moreninha iv': '1200', 'vila morumbi': '56', 'vila n. sra. aparecida': '1639', 'vila n. sra. da conceicao': '1713', 'vila n. sra. das gracas': '134', 'vila n. sra. de lourdes': '1264', 'vila nascente': '140', 'vila nasser': '70', 'vila neuza': '1377', 'vila nilza': '1663', 'vila nogueira': '148', 'vila nova': '1697', 'vila nova bandeirantes': '104', 'vila nova sao bento': '1244', 'vila novo horizonte': '393', 'vila olga': '1277', 'vila olinda': '116', 'vila oliveira': '1265', 'vila onze': '1317', 'vila oracilia': '653', 'vila oriente': '183', 'vila ornelas': '1257', 'vila orpheu bais': '1278', 'vila orsi': '1788', 'vila ouro fino': '1387', 'vila palmira': '497', 'vila paraiso': '1318', 'vila paulistana': '1319', 'vila perseveranca': '1279', 'vila piratininga': '43', 'vila planalto': '36', 'vila portao de ferro': '1280', 'vila progresso': '78', 'vila quito': '1266', 'vila raquel': '1419', 'vila ravenna': '2025', 'vila rezende': '1242', 'vila rica': '72', 'vila rolim': '1320', 'vila romana': '271', 'vila rosa': '1085', 'vila rosa pires': '58', 'vila sant ana': '1321', 'vila santa barbara': '1229', 'vila santa branca': '1105', 'vila santa dorothea': '71', 'vila santa filomena': '1258', 'vila santa luiza': '1267', 'vila santa luzia': '283', 'vila santa maria': '1268', 'vila santa odete': '1322', 'vila santa rita': '1710', 'vila santa rosa': '1289', 'vila santa tereza': '1290', 'vila santerio': '1323', 'vila santo amaro': '34', 'vila santo andre': '562', 'vila santo antonio': '1281', 'vila santo eugenio': '583', 'vila santos': '1291', 'vila santos gomes': '1324', 'vila sao elias': '1325', 'vila sao francisco': '16', 'vila sao gabriel': '1326', 'vila sao joao': '1282', 'vila sao joao bosco': '1661', 'vila sao jorge': '1327', 'vila sao jorge da lagoa': '1078', 'vila sao jose': '1269', 'vila sao luis': '91', 'vila sao miguel': '1259', 'vila sao rapael': '1270', 'vila sao sebastiao': '1230', 'vila sao thome': '1231', 'vila sao vicente': '333', 'vila saraiva': '1684', 'vila sargento amaral': '1271', 'vila serradinho': '298', 'vila silvia': '1300', 'vila silvia regina': '381', 'vila soares': '1292', 'vila sobrinho': '73', 'vila sol nascente': '1260', 'vila sonia': '1420', 'vila suburbano': '1328', 'vila suica': '1301', 'vila taquari': '1386', 'vila taquarussu': '97', 'vila taveira': '1261', 'vila taveiropolis': '179', 'vila telma': '1418', 'vila tupaceretan': '1329', 'vila valparaiso': '1413', 'vila vilas boas': '57', 'vila vilma': '2615', 'vila volpe': '2665', 'vila volpe ii': '2666', 'vila warde': '1283', 'vila xv de novembro': '1330', 'vila zoe': '1770', 'villa di parma': '1252', 'villa ravena': '2113', 'villagio riviera': '2045', 'villas park residence': '2502', 'vivendas do bosque': '47', 'vivendas do parque': '433', 'zona rural': '641'}
        if bairro in bairros: 
            print('Bairro encontrado! Por favor aguarde enquanto coleto os elementos para você\n')
            break
        else: print(u'Bairro não encontrado!\nPor favor, verifique o nome do bairro e tente novamente.\n')

# Coletar todas as anchor tags da pg de pesquisa
links = []
for page in range(1,6):
    if city == 'campo grande':
        url = 'https://www.infoimoveis.com.br/busca.php?finalidade=2&tipos%5B%5D=4&uf=1&cidade=1&bairros%5B%5D='+str(bairros[bairro])+'&valorde=&valorate=&pagina='+str(page)
    else:
        url = 'https://www.infoimoveis.com.br/busca.php?finalidade=2&tipos%5B%5D=4&uf=1&cidade='+str(cidades[city])+'&valorde=&valorate=&pagina='+str(page)
    soup = coletahtml(url)
    hrefs = soup('a')
 
    #Filtrar apenas as tags com link de venda de terreno
    for tag in hrefs:
        if 'venda-terreno' in tag.get('href', None):
            if tag.get('href', None) not in links:
                links.append(tag.get('href', None))

if links != []:
    dados = {'Area (m2)': [], 'Valor':[], 'Localizacao':[], 'Link':[]} #Criando o DF
    print('Coletando terrenos em '+city.title()+'. Por favor, aguarde...\n')
        
        #Aqui coletaremos a localização dos links extraídos
    for l in links:
        url = l
        tags = coletahtml(url).find_all('button')
        loc = None
        for i in tags:
            if i.get('onclick') == None: continue
            if 'posiciona' in i.get('onclick'):
                loc = i.get('onclick').split('(')[1]
                loc = loc[:len(loc)-1]
                break
        if loc == None: #Se não tiver localizacao
            continue
        dados['Link'].append(url)
        dados['Localizacao'].append(loc)

            #Aqui coletaremos a area
        if loc != None:
            infoimovel = coletahtml(url).find_all('td')
            for i in infoimovel:
                i=str(i)
                if ' m²' in i:
                    area = i.lstrip('<td>').rstrip(' m²</td>')
                    break
            dados['Area (m2)'].append(area)
        
            #Aqui coletaremos o valor
        if loc != None:
            infoimovel = coletahtml(url).find_all('span')
            for i in infoimovel:
                i=str(i)
                if i != None and 'R$' in i:
                    valor = i.lstrip('<span class="valor">').rstrip('</span>')
                    break
            dados['Valor'].append(valor)

        #Criando o dataframe e salvando como .xlsx        
    df = pd.DataFrame(dados)
    df.index += 1
    if city == 'campo grande': df.to_excel('Elementos '+bairro.title()+'.xlsx',index_label='#')
    else: df.to_excel('Elementos '+city.title()+'.xlsx',index_label='#')
        
        #Criando o arquivo KML
    index = 1
    kml=simplekml.Kml()
    for item in dados['Localizacao']:
        item=item.split(',')
        lat=item[0]
        lon = item[1]
        kml.newpoint(name=index, coords=[(lon,lat)])
        index +=1
        
    if city == 'campo grande': kml.save('Elementos '+bairro.title()+'.kml')
    else: kml.save('Elementos '+city.title()+'.kml')

    print('Elementos coletados\nArquivos EXCEL e KML salvos na pasta\nObrigado!\n')

else: print(u'Poxa! Não há elementos para coleta nesse lugar. Boa sorte =/.')
    
while True:
    if input('Pressione Enter para sair') != None : break #Finalização