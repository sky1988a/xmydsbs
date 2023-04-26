import requests, re, json, urllib3

# 抓新赚吧cookie填入下面
cookie = ['YF5f_1fc7_saltkey=PpprppGx; YF5f_1fc7_lastvisit=1669617454; YF5f_1fc7_atarget=1; YF5f_1fc7_auth=0fd9qt0ZHbn1qPeeBHqPLT5MUyoy9x9wiS%2FGbSXod0OcKOrZiC05EZ2oN%2FLH9yFApjiEDq8Ehb3uT4BXzXQobzKp4HM; YF5f_1fc7_lastcheckfeed=100979%7C1669722703; YF5f_1fc7_connect_is_bind=1; YF5f_1fc7_smile=1D1; YF5f_1fc7_sid=p4Ndcu; YF5f_1fc7_lip=221.232.107.147%2C1671609624; YF5f_2132_saltcode_36e537=MTAwOTc5IzEyYmZiYjIxNmZmOWM1OTY0ODQ1YWRlYzA0NzhjYTdh; YF5f_1fc7_member_login_status=1; YF5f_1fc7_st_p=100979%7C1671622156%7C92d67d8b9f8be4c5bb730134504cc771; YF5f_1fc7_viewid=tid_109050; YF5f_1fc7_ulastactivity=729eYxu3R%2FJbqgkrFiiKc44yCd0Y0eZuqw53sHGiP8E6fr1cttXQ; YF5f_1fc7_sendmail=1; YF5f_1fc7_lastact=1671622157%09home.php%09spacecp; YF5f_1fc7_checkpm=1; YF5f_1fc7_iswebp=1; Hm_lvt_f3eb460fa96db172aa856454146df378=1671622158; Hm_lpvt_f3eb460fa96db172aa856454146df378=1671622158','YF5f_1fc7_saltkey=EmcXqKO0; YF5f_1fc7_lastvisit=1671618616; YF5f_1fc7_sid=imwPfw; YF5f_1fc7_sendmail=1; YF5f_1fc7_iswebp=1; Hm_lvt_f3eb460fa96db172aa856454146df378=1671622217; YF5f_1fc7_ulastactivity=3436tRiYZgfE4iATMbu7ceZM3Gggiqr8wwFoEXWmdqBupIZODn4f; YF5f_1fc7_auth=0f12HhIqEn87%2FdyXpLk%2BBE4pRHho6yPpr83WyrpeeDbwqDUftQk37Xm%2BtNVG2exrjhoUptvugM07Ip0sThs6MACOJuE; YF5f_1fc7_lastcheckfeed=101301%7C1671622220; YF5f_1fc7_checkfollow=1; YF5f_1fc7_lip=221.232.107.147%2C1671609622; YF5f_2132_saltcode_36e537=MTAxMzAxIzY2MGUwZGVhMjk2NTAyMDIwMjBhMGYxZjhjYmM1OWUz; YF5f_1fc7_connect_is_bind=1; YF5f_1fc7_member_login_status=1; YF5f_1fc7_st_p=101301%7C1671622221%7Ceebbab290f9b912cecc984c3736cff29; YF5f_1fc7_viewid=tid_109050; YF5f_1fc7_lastact=1671622221%09home.php%09spacecp; YF5f_1fc7_checkpm=1; Hm_lpvt_f3eb460fa96db172aa856454146df378=1671622222','Hm_lvt_f3eb460fa96db172aa856454146df378=1671622217; YF5f_1fc7_sid=imwPfw; YF5f_1fc7_iswebp=1; YF5f_1fc7_saltkey=wdydGZ7R; YF5f_1fc7_lastvisit=1671618658; YF5f_1fc7_sendmail=1; YF5f_1fc7_ulastactivity=0bc2xaL8LHpeHaKKOxgQBRoJfZpy7kgUbYHJsZgex%2BSXS%2FOgLOOM; YF5f_1fc7_auth=0db77DalBKvApgKnH8e07Rxkv89Gjq0%2B0LtZnuE8NbH71tdwSbjPiQe206IGS8LNFyGPSN2O%2F1R9sOGXigNxduN6STQ; YF5f_1fc7_lastcheckfeed=101045%7C1671622261; YF5f_1fc7_checkfollow=1; YF5f_1fc7_lip=221.232.107.147%2C1671609626; YF5f_2132_saltcode_36e537=MTAxMDQ1IzRhM2NlOWYxYzZiOWJhNzUzNmE5YTFjNTA2NWU0ZGFl; YF5f_1fc7_connect_is_bind=1; YF5f_1fc7_member_login_status=1; YF5f_1fc7_st_p=101045%7C1671622263%7C7e7d9b9f01bc655225c1611e0a7195e7; YF5f_1fc7_viewid=tid_109050; YF5f_1fc7_lastact=1671622264%09home.php%09spacecp; YF5f_1fc7_checkpm=1; Hm_lpvt_f3eb460fa96db172aa856454146df378=1671622266']

#推送配置
# 企业微信推送参数
corpid = ''
agentid = ''
corpsecret = ''
touser = ''
# 推送加 token
plustoken = ''

def Push(contents):
    # 微信推送
    if all([corpid, agentid, corpsecret, touser]):
        token = \
        requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}').json()[
            'access_token']
        json = {"touser": touser, "msgtype": "text", "agentid": agentid, "text": {"content": "新赚吧签到\n" + contents}}
        resp = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}", json=json)
        print('微信推送成功' if resp.json()['errmsg'] == 'ok' else '微信推送失败')

    if plustoken:
        headers = {'Content-Type': 'application/json'}
        json = {"token": plustoken, 'title': '新赚吧签到', 'content': contents.replace('\n', '<br>'), "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')

urllib3.disable_warnings()
for i in range(len(cookie)):
    print('开始第'+ str(i+1) +'个帐号签到'+'\n'+'***********************')
    f_url = 'https://v1.xianbao.net/'  # 获取formhash
    url = 'https://v1.xianbao.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0'
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
        'cookie': f'{cookie[i]}',
        'Host': 'v1.xianbao.net',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://v1.xianbao.net'
    }
    f_html = requests.post(url=f_url, headers=headers, verify=False).text
    formhash = str(re.findall('name="formhash" value="(.*?)" />', f_html, re.S)).replace('[', '').replace('\'', '').replace(']', '')
    data = {
    'formhash': f'{formhash}'
    }
    html = requests.post(url=url, headers=headers, data=data, verify=False).text
    result = re.findall('<div class="c">\r\n(.*?)<a href="plugin.php?', html, re.S)
    message = "".join(result)
    url_2 = 'https://v1.xianbao.net/home.php?mod=spacecp&ac=credit&showcredit=1'
    html_2 = requests.get(url=url_2, headers=headers, verify=False).text
    info = '用户名：' + "".join(re.findall('title="访问我的空间">(.*?)</a>', html_2, re.S)) + ' 果果:' + "".join(re.findall('src="/static/images/common/guoguo.gif" /> 果果: </em>(.*?)&nbsp; <a href="home.php?', html_2, re.S))
    sign_info = message + '\n' + info
    print(sign_info)
    Push(contents=sign_info)
