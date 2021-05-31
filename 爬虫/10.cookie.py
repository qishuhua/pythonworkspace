#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request,error
import json


if __name__=='__main__':
    url='http://mail.ym.163.com/jy5/main.jsp?sid=406A67r8e634k9W1v2WKdBxRVIUkzV1M&hl=zh_CN#module=welcome'
    try:
        headers={
            'Cookies':'JSESSIONID=28BE7D46FEBA225C4D580318A368BF7C; _ntes_nnid=75eb7fa52c4ca1154719a8fe3d846430,1583398615966; _ntes_nuid=75eb7fa52c4ca1154719a8fe3d846430; mail_psc_fingerprint=e4f804a5e6a0d04ac772115a77bb733e; nts_mail_user=qsh2281119774@163.com:-1:1; hb_MA-BFF5-63705950A31C_source=www.baidu.com; NTES_YD_SESS=_qaVBX6NquUllU.013AK5_0DHb_iVqnvjGu9k3nDsu3ifD7CfFQYXmxR97ztD4ozJtXjp.S4olJfvF8HnFIzxsPyYvUwYYasdQMaaYzY0.8LYKBXuj1lXCAL9WhjkvOx0TJjHE5TugN67Mbor1zADR_2_Cg8rcjOBXPUH1VMhu23Ppw8tz5SktLU.riUjhIWzLdGvYnDuDFjPOQk6.HZpCx99z.hYnTzb7cHyFn6Bfo3E; NTES_YD_PASSPORT=yWWI4dfhUN.vo3kZZZY8pjO.nTtDDExVFN_OgCKHarQtZ2qhZLps8NPItqUH2YAUwH8RDxGYAnwI_yDWilh9PROGDojuMmptQ7beXVYZsBJYcVChK8Qo1pIyZY.3fKXZmFqN9iVEDpHqANqhc2D2EU9_xD6AByr4BGrz5pUELT6O2.a1FwUxD9Rahm5xc.TQ0PvM1jg9cwxVwxt73SFVa4hT9; S_INFO=1591666003|0|3&80##|19821819751; P_INFO=19821819751|1591666003|1|study|00&99|shh&1591548142&study#shh&null#10#0#0|&0|null|19821819751; NTES_hp_textlink1=old; qiye_mail_upx=up1.ym.163.com; QIYE_SESS=9Bq04t8UL7msjsSuBNJYgsyM9nC2yIB5LmV9txPtpT_MlyzQEC3kHX96TDj_y0150cifh9dzo5tJeTuTjaK1u.SisLfGgK3ircGsnS0h8n75NpatXychV5fFL8ZnXRhWXJyxIWEFg9ac.s4uTMGt5IYBJowERq2BPRIH5BdNRZC; Coremail=Onf5vHA5DgyMMOyh1pYFjcvbColdnjVYcqSRMTIDrV6SaViYA**2ZASgt*PQCm8VfoG7jhIZqDoFw61a-6z-g7oyCr-LQhdYMvRa2gAVxOeSeHGPN8*a3A0PD19BhKxyATlKYEopDCz2dtY8gLGEm*4pW0ErauJr0t8zmheHyKA|%wm-3.ym.internal; YM_WMHOST=wm-3.ym.internal; cm_last_info=rhPLolbCrkvPmi_Knk3FokTApMTxpwnydkvOr5.zaO2zaymzaynHmkzG9BzH9x2QaMTxpQOzaynEshizaynHmkzI9ADNq0iNfBbDn0iNf1eKby2QbR6SnhmNb4GTjN3Qazr9n27Sizn7jkHUjx3b7BaXb1.QehmRqxvzbxaOoNzlalmMjOHyeBvgjyzjoRDkaiOAo1PRpgON9BzH9AzIr4jMpA3G'
        }
        req=request.Request(url,headers=headers)
        rsp=request.urlopen(req)
        html =rsp.read().decode()
        with open('rsp.html','w') as a:
            a.write(html)
        print(html)
    except error.HTTPError as e:
        print('HTTPError',e.reason,'====',e)
    except error.URLError as e:
        print('URLError',e.reason,'====',e)
    except Exception as e:
        print(e)