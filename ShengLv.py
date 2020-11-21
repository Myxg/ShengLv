import random

import requests
import csv
import json
import pandas as pd
from datetime import datetime


try:
    body = {}
    u1 = 'https://creator.zoho.com.cn/api/chunzhou.jia2/json/baobiao/view/form_ShengLv_DanDa_Report/record/delete/'
    u2 = 'https://creator.zoho.com.cn/api/chunzhou.jia2/json/baobiao/view/form_ShengLv_ZuHe_Report/record/delete/'
    params = {
        'authtoken': 'd51ecfa14f98e8f14c91ac894bf8e7d4',
        'scope': 'creatorapi',
        'raw': "true",
        'criteria': "ID != null",
    }
    req = requests.post(u1, params={**params, **body})
    req_json = req.json()
    print(req_json)
    req2 = requests.post(u2, params={**params, **body})
    req_json2 = req2.json()
    print(req_json2)
except Exception as e:
    print(e)


def time_func(date):
    return datetime.strptime(date['Date_field_CeShiRiQi'], "%d-%b-%Y")

ydy_all = []

url = 'https://creator.zoho.com.cn/api/json/badminton/view/view_YunDongYuan?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(form_DiQu.Single_Line_DiQu==("中国"))'

data = requests.get(url).text
data = data.replace(' ', '').split('0=')[1][:-1]
data = json.loads(data)['form_YunDongYuan']

urls = 'https://creator.zoho.com.cn/api/json/qiuyuan/view/form_ShuangDaZuHe_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi&criteria=(form_DiQu.Single_Line_DiQu==("中国"))'

datas = requests.get(urls).text
datas = datas.split('=')[1][:-1]
datas = json.loads(datas)['form_ShuangDaZuHe']

name_url = 'https://creator.zoho.com.cn/api/json/badminton/view/view_YunDongYuan?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi'
name_data = json.loads(requests.get(name_url).text.replace(' ','').split('0=')[1][:-1])['form_YunDongYuan']
name = {}
for i in name_data:
    name[i['Single_Line_YingWenMing']] = i['Single_Line_ZhongWenMing']

result_danda_url = 'https://creator.zoho.com.cn/api/json/saishi/view/form_BiSaiJieGuo_DanDa_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi'
rd = json.loads(requests.get(result_danda_url).text.replace(' ','').split('6=')[1][:-1])['form_BiSaiJieGuo_DanDa']
result_shuangda_url = 'https://creator.zoho.com.cn/api/json/saishi/view/form_BiSaiJieGuo_ShuangDa_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi'
rs = json.loads(requests.get(result_shuangda_url).text.split('=')[1][:-1])['form_BiSaiJieGuo_ShuangDa']

nvd_url = 'https://creator.zoho.com.cn/api/json/saishi/view/form_ShiJiePaiMing_DanDa_ZuiXin_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi'
d = json.loads(requests.get(nvd_url).text.replace(' ','').split('3=')[1][:-1])['form_ShiJiePaiMing_DanDa_ZuiXin']
s_url = 'https://creator.zoho.com.cn/api/json/saishi/view/form_ShiJiePaiMing_ShuangDa_ZuiXin_Report?authtoken=d51ecfa14f98e8f14c91ac894bf8e7d4&scope=creatorapi'
s = json.loads(requests.get(s_url).text.split('=')[1][:-1])['form_ShiJiePaiMing_ShuangDa_ZuiXin']

nvd_zg = []
nvd_wg = []
nand_zg = []
nand_wg = []
nvs_zg = []
nvs_wg = []
nans_zg = []
nans_wg = []
hs_zg = []
hs_wg = []

for i in d:
    for j in data:
        if i['Number_PaiMing'] <= 20 and i['Dropdown_BiSaiXiangMu'] == '女单' and i['form_YunDongYuan'] == j['Single_Line_YingWenMing']:
            nvd_zg.append(i['form_YunDongYuan'])
        if i['Number_PaiMing'] <= 8 and i['Dropdown_BiSaiXiangMu'] == '女单' and i['form_YunDongYuan'] not in nvd_wg:
            nvd_wg.append(i['form_YunDongYuan'])
        if i['Number_PaiMing'] <= 20 and i['Dropdown_BiSaiXiangMu'] == '男单' and i['form_YunDongYuan'] == j['Single_Line_YingWenMing']:
            nand_zg.append(i['form_YunDongYuan'])
        if i['Number_PaiMing'] <= 8 and i['Dropdown_BiSaiXiangMu'] == '男单' and i['form_YunDongYuan'] not in nand_wg:
            nand_wg.append(i['form_YunDongYuan'])
for i in s:
    for j in datas:
        if i['Number_PaiMing'] <= 20 and i['Dropdown_BiSaiXiangMu'] == '女双' and i['form_ShuangDaZuHe'] == j['Single_Line_MingCheng']:
            nvs_zg.append(i['form_ShuangDaZuHe'])
        if i['Number_PaiMing'] <= 8 and i['Dropdown_BiSaiXiangMu'] == '女双' and i['form_ShuangDaZuHe'] not in nvs_wg:
            nvs_wg.append(i['form_ShuangDaZuHe'])
        if i['Number_PaiMing'] <= 20 and i['Dropdown_BiSaiXiangMu'] == '男双' and i['form_ShuangDaZuHe'] == j['Single_Line_MingCheng']:
            nans_zg.append(i['form_ShuangDaZuHe'])
        if i['Number_PaiMing'] <= 8 and i['Dropdown_BiSaiXiangMu'] == '男双' and i['form_ShuangDaZuHe'] not in nans_wg:
            nans_wg.append(i['form_ShuangDaZuHe'])
        if i['Number_PaiMing'] <= 20 and i['Dropdown_BiSaiXiangMu'] == '混双' and i['form_ShuangDaZuHe'] == j['Single_Line_MingCheng']:
            hs_zg.append(i['form_ShuangDaZuHe'])
        if i['Number_PaiMing'] <= 8 and i['Dropdown_BiSaiXiangMu'] == '混双' and i['form_ShuangDaZuHe'] not in hs_wg:
            hs_wg.append(i['form_ShuangDaZuHe'])

for i in nvd_wg:
    if i in nvd_zg:
        nvd_wg.remove(i)
for i in nand_wg:
    if i in nand_zg:
        nand_wg.remove(i)
for i in nvs_wg:
    if i in nvs_zg:
        nvs_wg.remove(i)
for i in nans_wg:
    if i in nans_zg:
        nans_wg.remove(i)
for i in hs_wg:
    if i in hs_zg:
        hs_wg.remove(i)


dd_z = nvd_zg + nand_zg
dd_w = nvd_wg + nand_wg
dd_zs = nvs_zg + nans_zg + hs_zg
dd_ws = nvs_wg + nans_wg + hs_wg
l1 = []
l2 = []
for i in dd_z:
    li = []
    for j in dd_w:
        ll = []
        for x in rd:
            if i == x['form_YunDongYuan_A2'] and j == x['form_YunDongYuan_B1']:
                ll.append(x)
            elif j == x['form_YunDongYuan_A2'] and i == x['form_YunDongYuan_B1']:
                x['form_YunDongYuan_A2'] = i
                x['form_YunDongYuan_B1'] = j
                ll.append(x)
        if len(ll) > 0:
            li.append(ll)
    l1.append(li)
for i in dd_zs:
    li = []
    for j in dd_ws:
        ll = []
        for x in rs:
            if i == x['form_ShuangDaZuHe_A'] and j == x['form_ShuangDaZuHe_B1']:
                ll.append(x)
            elif j == x['form_ShuangDaZuHe_A'] and i == x['form_ShuangDaZuHe_B1']:
                x['form_YunDongYuan_A2'] = i
                x['form_YunDongYuan_B1'] = j
                ll.append(x)
        if len(ll) > 0:
            li.append(ll)
    l2.append(li)
d_list = []
ds_list = []
for i in l1:
    for j in i:
        list1 = []
        if len(j) < 2:
            data = j[0]
            A = data['form_YunDongYuan_A2']
            B = data['form_YunDongYuan_B1']
            a = name[data['form_YunDongYuan_A2']]
            b = name[data['form_YunDongYuan_B1']]
            zongchangci = 1
            if data['form_YunDongYuan_HuoSheng'] == A:
                sheng = 1
                fu = 0
            else:
                sheng = 0
                fu = 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            list1.append('')
            list1.append(a)
            list1.append(b)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)

        if len(j) == 2:
            data = j[0]
            d2 = j[1]
            A = data['form_YunDongYuan_A2']
            B = data['form_YunDongYuan_B1']
            a = name[data['form_YunDongYuan_A2']]
            b = name[data['form_YunDongYuan_B1']]
            zongchangci = 2
            if data['form_YunDongYuan_HuoSheng'] == A:
                sheng = 1
                fu = 0
                if d2['form_YunDongYuan_HuoSheng'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                if d2['form_YunDongYuan_HuoSheng'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
            if data['form_YunDongYuan_HuoSheng'] == B:
                sheng = 0
                fu = 1
                if d2['form_YunDongYuan_HuoSheng'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                if d2['form_YunDongYuan_HuoSheng'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            s2 = d2['form_SaiShi']
            z2 = d2['Dropdown_BiSaiJieGuo']
            b2 = d2['Single_Line_BiFen']
            u2 = d2['form_ShiPin']
            list1.append('')
            list1.append(a)
            list1.append(b)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)
            list1.append(s2)
            list1.append(b2)
            list1.append(u2)
        if len(j) > 3:
            # print(j)
            data = j[0]
            d2 = j[1]
            d3 = j[2]
            A = data['form_YunDongYuan_A2']
            B = data['form_YunDongYuan_B1']
            a = name[data['form_YunDongYuan_A2']]
            b = name[data['form_YunDongYuan_B1']]
            zongchangci = 3
            if data['form_YunDongYuan_HuoSheng'] == A:
                sheng = 1
                fu = 0
                if d2['form_YunDongYuan_HuoSheng'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
                if d2['form_YunDongYuan_HuoSheng'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
                    if d3['form_YunDongYuan_HuoSheng'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
            if data['form_YunDongYuan_HuoSheng'] == B:
                sheng = 0
                fu = 1
                if d2['form_YunDongYuan_HuoSheng'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
                if d2['form_YunDongYuan_HuoSheng'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
                    if d3['form_YunDongYuan_HuoSheng'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_YunDongYuan_HuoSheng'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            s2 = d2['form_SaiShi']
            z2 = d2['Dropdown_BiSaiJieGuo']
            b2 = d2['Single_Line_BiFen']
            u2 = d2['form_ShiPin']
            s3 = d3['form_SaiShi']
            z3 = d3['Dropdown_BiSaiJieGuo']
            b3 = d3['Single_Line_BiFen']
            u3 = d3['form_ShiPin']
            list1.append('')
            list1.append(a)
            list1.append(b)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)
            list1.append(s2)
            list1.append(b2)
            list1.append(u2)
            list1.append(s3)
            list1.append(b3)
            list1.append(u3)
        if len(list1) > 0:
            zongchangci = len(j)
            sheng = 0
            fu = 0

            for h in j:
                if h['form_YunDongYuan_A2'] == h['form_YunDongYuan_HuoSheng']:
                    sheng += 1
                elif h['form_YunDongYuan_B1'] == h['form_YunDongYuan_HuoSheng']:
                    fu += 1
            shenglv = round((sheng / zongchangci) * 100, 2)
            list1[3] = zongchangci
            list1[4] = sheng
            list1[5] = fu
            list1[6] = shenglv

        d_list.append(list1)

for i in l2:
    for j in i:
        # print(j)
        list1 = []
        if len(j) < 2:
            data = j[0]
            A = data['form_ShuangDaZuHe_A']
            B = data['form_ShuangDaZuHe_B1']
            zongchangci = 1
            if data['form_ShuangDaZuHe_ShengLi'] == A:
                sheng = 1
                fu = 0
            else:
                sheng = 0
                fu = 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            list1.append('')
            list1.append(A)
            list1.append(B)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)

        if len(j) == 2:
            data = j[0]
            d2 = j[1]
            A = data['form_ShuangDaZuHe_A']
            B = data['form_ShuangDaZuHe_B1']
            # a = name[data['form_YunDongYuan_A2']]
            # b = name[data['form_YunDongYuan_B1']]
            zongchangci = 2
            if data['form_ShuangDaZuHe_ShengLi'] == A:
                sheng = 1
                fu = 0
                if d2['form_ShuangDaZuHe_ShengLi'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                if d2['form_ShuangDaZuHe_ShengLi'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
            if data['form_ShuangDaZuHe_ShengLi'] == B:
                sheng = 0
                fu = 1
                if d2['form_ShuangDaZuHe_ShengLi'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                if d2['form_ShuangDaZuHe_ShengLi'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            s2 = d2['form_SaiShi']
            z2 = d2['Dropdown_BiSaiJieGuo']
            b2 = d2['Single_Line_BiFen']
            u2 = d2['form_ShiPin']
            list1.append('')
            list1.append(A)
            list1.append(B)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)
            list1.append(s2)
            list1.append(b2)
            list1.append(u2)

        if len(j) == 3:
            data = j[0]
            d2 = j[1]
            d3 = j[2]
            A = data['form_ShuangDaZuHe_A']
            B = data['form_ShuangDaZuHe_B1']
            # a = name[data['form_YunDongYuan_A2']]
            # b = name[data['form_YunDongYuan_B1']]
            zongchangci = 3
            if data['form_ShuangDaZuHe_ShengLi'] == A:
                sheng = 1
                fu = 0
                if d2['form_ShuangDaZuHe_ShengLi'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
                if d2['form_ShuangDaZuHe_ShengLi'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
                    if d3['form_ShuangDaZuHe_ShengLi'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
            if data['form_ShuangDaZuHe_ShengLi'] == B:
                sheng = 0
                fu = 1
                if d2['form_ShuangDaZuHe_ShengLi'] == A:
                    sheng = sheng + 1
                    fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
                if d2['form_ShuangDaZuHe_ShengLi'] == B:
                    sheng = sheng + 0
                    fu = fu + 1
                    if d3['form_ShuangDaZuHe_ShengLi'] == A:
                        sheng = sheng + 1
                        fu = fu + 0
                    if d3['form_ShuangDaZuHe_ShengLi'] == B:
                        sheng = sheng + 0
                        fu = fu + 1
            shenglv = round((sheng/zongchangci)*100, 2)
            saishi = data['form_SaiShi']
            zongbifen = data['Dropdown_BiSaiJieGuo']
            bifen = data['Single_Line_BiFen']
            url = data['form_ShiPin']
            s2 = d2['form_SaiShi']
            z2 = d2['Dropdown_BiSaiJieGuo']
            b2 = d2['Single_Line_BiFen']
            u2 = d2['form_ShiPin']
            s3 = d3['form_SaiShi']
            z3 = d3['Dropdown_BiSaiJieGuo']
            b3 = d3['Single_Line_BiFen']
            u3 = d3['form_ShiPin']
            list1.append('')
            list1.append(A)
            list1.append(B)
            list1.append(zongchangci)
            list1.append(sheng)
            list1.append(fu)
            list1.append(shenglv)
            list1.append(saishi)
            list1.append(url)
            list1.append(bifen)
            list1.append(s2)
            list1.append(b2)
            list1.append(u2)
            list1.append(s3)
            list1.append(b3)
            list1.append(u3)

        if len(list1) > 0:
            zongchangci = len(j)
            sheng = 0
            fu = 0

            for h in j:
                if h['form_ShuangDaZuHe_A'] == h['form_ShuangDaZuHe_ShengLi']:
                    sheng += 1
                elif h['form_ShuangDaZuHe_B1'] == h['form_ShuangDaZuHe_ShengLi']:
                    fu += 1
            shenglv = round((sheng / zongchangci) * 100, 2)
            list1[3] = zongchangci
            list1[4] = sheng
            list1[5] = fu
            list1[6] = shenglv
        ds_list.append(list1)
for i in d_list:
    # print(i)
    l1 = i
    try:
        if len(i) == 0:
            body = {}
        elif len(i) == 10:
            body = {
                'form_YunDongYuan': l1[1],
                'form_YunDongYuan_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'Single_Line_BiFen_1': l1[9],
                'URL_1': l1[8],
            }
        elif len(i) == 13:
            body = {
                'form_YunDongYuan': l1[1],
                'form_YunDongYuan_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'form_SaiShi_2': l1[10],
                'Single_Line_BiFen_1': l1[9],
                'Single_Line_BiFen_2': l1[11],
                'URL_1': l1[8],
                'URL_2': l1[12],
            }
        elif len(i) == 16:
            body = {
                'form_YunDongYuan': l1[1],
                'form_YunDongYuan_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'form_SaiShi_2': l1[10],
                'form_SaiShi_3': l1[13],
                'Single_Line_BiFen_1': l1[9],
                'Single_Line_BiFen_2': l1[11],
                'Single_Line_BiFen_3': l1[14],
                'URL_1': l1[8],
                'URL_2': l1[12],
                'URL_3': l1[15],
            }

        u1 = 'https://creator.zoho.com.cn/api/chunzhou.jia2/json/baobiao/form/form_ShengLv_DanDa/record/add/'
        params = {
            'authtoken': 'd51ecfa14f98e8f14c91ac894bf8e7d4',
            'scope': 'creatorapi',
            'raw': "true",
        }
        req = requests.post(u1, params={**params, **body})
        req_json = req.json()
        print(req_json)
    except Exception as e:
        print(e)
for i in ds_list:
    # print(i)
    l1 = i
    try:
        if len(i) == 0:
            body = {}

        elif len(i) == 10:
            body = {
                'form_ShuangDaZuHe_ZhongGuo': l1[1],
                'form_ShuangDaZuHe_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'Single_Line_BiFen_1': l1[9],
                'URL_1': l1[8],
            }
        elif len(i) == 13:
            body = {
                'form_ShuangDaZuHe_ZhongGuo': l1[1],
                'form_ShuangDaZuHe_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'form_SaiShi_2': l1[10],
                'Single_Line_BiFen_1': l1[9],
                'Single_Line_BiFen_2': l1[11],
                'URL_1': l1[8],
                'URL_2': l1[12],
            }
        elif len(i) == 16:
            body = {
                'form_ShuangDaZuHe_ZhongGuo': l1[1],
                'form_ShuangDaZuHe_8': l1[2],
                'Number_ZongChangCi': l1[3],
                'Number_Ying': l1[4],
                'Number_Shu': l1[5],
                'Percent_ShengLv': l1[6],
                'form_SaiShi_1': l1[7],
                'form_SaiShi_2': l1[10],
                'form_SaiShi_3': l1[13],
                'Single_Line_BiFen_1': l1[9],
                'Single_Line_BiFen_2': l1[11],
                'Single_Line_BiFen_3': l1[14],
                'URL_1': l1[8],
                'URL_2': l1[12],
                'URL_3': l1[15],
            }

        u1 = 'https://creator.zoho.com.cn/api/chunzhou.jia2/json/baobiao/form/form_ShengLv_ZuHe/record/add/'
        params = {
            'authtoken': 'd51ecfa14f98e8f14c91ac894bf8e7d4',
            'scope': 'creatorapi',
            'raw': "true",
        }
        req = requests.post(u1, params={**params, **body})
        req_json = req.json()
        print(req_json)
    except Exception as e:
        print(e)





