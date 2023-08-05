import time
from requests import post, get
import json
from random import randint

def buy_item(token, data, cookie):
  productId = data["id"]
  expectedSellerId = data["creatorTargetId"]
  expectedPrice = data["price"]
  name = data["name"]
  unitsavailable = data["unitsAvailableForConsumption"]
  if "quantityLimitPerUser" in data.keys():
    quantity = data["quantityLimitPerUser"] 
    print (data["quantityLimitPerUser"])
  else:
      quantity = 1
  bought = (0)
  if unitsavailable < 1 :
    print ("No Units Available") 
  else:
    while bought < quantity:
      #try buy item
      headers = {
      "X-CSRF-TOKEN": token,
      "content-type": "application/json; charset=UTF-8"
      }
      data = {
      "expectedCurrency": 1,
      "expectedPrice": expectedPrice,
      "expectedSellerId": expectedSellerId
      }
      dataLoad = json.dumps(data)
      buyres = post(f"https://economy.roblox.com/v1/purchases/products/{productId}",
                    headers=headers,
                    data=dataLoad,
                    cookies={".ROBLOSECURITY": cookie})
      if buyres.status_code == 200:
        print("Successfully bought:", name, bought)
        bought += 1
        time.sleep(1)
      else:
        print("Failed to buy code:", buyres.status_code)
        break
  

# opens the limiteds id file
file = open("limited_ids.txt", 'r')
IDs = file.read().split('\n')

cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_153CA2C965D2A2CF4C1D54B35417A12B5B4CEB9FAC7F117CCAC7E6D49E4CCA762636B1697B6D633EE4E899A2E29786B4714D8B3561F97B6C4B8914DF0015CCD3990F3CD07BF985F2E8F28135A36FCD5F6BC3FC334454C269C46CBB30F908248A9518EE8E9402D178ACB3B6356C66E406F1CDCE290F2855969245AF2618E8135B31067F001D5DC9D95122150894A112DD3A99598BB0061A27A846D1163A08E747E3695BA2C1AAD46671AF4F0C04C2DD59FC44429705E2482591922CB7F446D7A36D3DF3025908C426A215AF96EF8B0322DA15A87B678705A2D02848D88FD4EFA9E4B0F9A3F6F79D3AC87E07D9760BA7B4260FEF5327F2DA0328C09A51016F4C6258CAF318BBBF4A8D73B453644BC71EBFC56241479C144044DA77C7EFFE570C1A734398BF906F0AFDC7A8D4FF25700126EDF049F0B49E114A4A3B1DBE4D04C631D6D1DAFE5801B26201FDB01E825E490EDE630134056221BE7F56C5A29CA6107C008E25B86E5D29FABFCF281D6D7CA2DB541DF292CCD2EA413286DBA121BCD1A110C15C7E7C49DED093B6D5E31F12B2C8ABB7F68C"
# getting x-csrf-token
token = post("https://auth.roblox.com/v2/login", cookies={".ROBLOSECURITY": cookie}).headers['X-CSRF-TOKEN']
# goes through every id
for ID in IDs:
  print("https://www.roblox.com/catalog/"+ID+"/")

  #try to get item details
  url = 'https://catalog.roblox.com/v1/catalog/items/details'
  headers = {
      'accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRF-TOKEN': token
  }
  payload = {
      "items": [
          {
              "itemType": 1,
              "id": ID
          }
      ]
  }
  response = post(url, headers=headers, json=payload, cookies={".ROBLOSECURITY": cookie})
  print(response.status_code)
  #data = response.json()["data"][0]
  print(response.json())
  
  
  #if you succesfully get details
  if response.status_code == 200:
   data = response.json()["data"][0]
   print("DATA:", data)
   buy_item(token, data, cookie)
  else:
   print('Error: couldn\'t get item details code:', response.status_code)
      
  print("waiting before next purchase\n")
  time.sleep(randint(60, 180));

   #find what quantity for no limit