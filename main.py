import pyautogui

# TODO: Move to a separate module "itemList.py"
itemList = {
  "pumpkin": {
    "name": "pumpkin",
    "category": [1080, 1170],
    "tier": None,
    "enchantment": None,
    "quality": None,
  },
  "bread": {
    "name": "bread",
    "category": None,
    "tier": None,
    "enchantment": None,
    "quality": None,
  },
  "raw beef": {
    "name": "raw beef",
    "category": None,
    "tier": None,
    "enchantment": None,
    "quality": None,
  },
  "beef stew": {
    "name": "beef stew",
    "category": None,
    "tier": None,
    "enchantment": 0,
    "quality": None,
  },
  "scholar sandals": {
    "name": "scholar sandals",
    "category": [408, 496],
    "tier": 5,
    "enchantment": 1,
    "quality": 3,
  },
}

# TODO - DONE: Check how data client take buy and sell orders
# TODO - have info, in progress: Make shell commands for running scripts
# TODO - DONE: Record video for analysis and testing
# TODO: Create script for travel between cities
#         martlock -> martlock market,
#         martlock market -> martlock,
#         martlock -> bridgewatch,
#         bridgewatch -> bridgewatch market,
#         bridgewatch market -> bridgewatch,
#         bridgewatch -> lymhurst,
#         lymhurst -> lymhurst market,
#         lymhurst market -> lymhurst,
#         lymhurst -> fort sterling,
#         fort sterling -> fort sterling market,
#         fort sterling market -> fort sterling,
#         fort sterling -> thetford,
#         thetford -> thetford market,
# TODO: Create a list of all items in the client

def searchItemAtMarket(item):
  ySearchBar = 270
  xSearchBar = 750
  wSearchBar = 285
  wFilters = 242

  name, category, tier, enchantment, quality = dict(item).values()
  itemKeys = list(dict(item).keys())
  
  while True: # click on name input until it is focused
    pyautogui.click(xSearchBar, ySearchBar, duration=0.2) 
    img = pyautogui.locateOnScreen(
      "images/input_cursor.png", 
      confidence=0.9, 
      region=(615, 230, 740-615, 305-230)
    )
    img2 = pyautogui.locateOnScreen(
      "images/input_cursor2.png", 
      confidence=0.9, 
      region=(615, 230, 740-615, 305-230)
    )

    pyautogui.sleep(0.7)

    if img != None or img2 != None:
      print("Input is focused")
      break
        
    print(" ?---- Can't find Input cursor")
  
  pyautogui.sleep(1)
  pyautogui.write(name, interval=0.25) # type name

  # choose all of filters of item
  if category != None:
    pyautogui.click(xSearchBar + wSearchBar, ySearchBar, duration=0.2) # click on category list
    pyautogui.sleep(0.7)
    for i, y in enumerate(category): #move to needly category
      if i == 1: pyautogui.sleep(0.5)
      sublist = 225 if i == 1 else 0
      pyautogui.moveTo(xSearchBar + wSearchBar + sublist, y, duration=0.2)
    pyautogui.sleep(0.2)
    pyautogui.click() # choose category
    print("Category is chosen")

  def chooseFilter(option, filterName = "", filterNumber = 1, chooseOptionFrom = 1):
    if option != None:
      pyautogui.sleep(0.7)
      pyautogui.click( # click on filter list
        xSearchBar + wSearchBar + wFilters * filterNumber, 
        ySearchBar, 
        duration=0.2
      ) 
      pyautogui.sleep(0.7)
      pyautogui.click( # choose filter option
        xSearchBar + wSearchBar + wFilters * filterNumber, 
        ySearchBar + 45 * (option + chooseOptionFrom), 
        duration=0.2
      )
      print("{0} is chosen".format(filterName.capitalize())) 

  chooseFilter(tier, itemKeys[2])
  chooseFilter(enchantment, itemKeys[3], 2, 2)
  chooseFilter(quality, itemKeys[4], 3)


def mapMarketItems():
  for name, item in dict(itemList).items():
    print("\n -- ", name.upper())
    searchItemAtMarket(item)

    openOrdersByBuyBtn()

    spreadOrderListIfCollapsed()
    pyautogui.sleep(2)

    closeOrderList()
    pyautogui.sleep(0.7)

    resetFilter()
    pyautogui.sleep(0.7)


def resetFilter():
  while True:
    img = pyautogui.locateCenterOnScreen(
      "images/reset_btn.png", 
      confidence=0.9, 
      region=(1870, 235, 1940-1870, 305-235)
    )

    if img != None:
      print(" - Filter reset")
      pyautogui.click(*img, duration=0.2)
      break
          
    print(" ?---- Can't find Reset button")
  
  while True:
    img = pyautogui.locateCenterOnScreen(
      "images/reset_btn.png", 
      confidence=0.9, 
      region=(866, 235, 920-866, 305-235)
    )

    if img != None:
      print(" - Search value clear")
      pyautogui.click(*img, duration=0.2)
      break
    
    print(" ?---- Can't find Reset button")

def openOrdersByBuyBtn():
  while True:
    img = pyautogui.locateCenterOnScreen(
      "images/buy_btn.png", 
      confidence=0.9, 
      region=(1690, 480, 1940-1690, 590-480)
    )

    if img != None:
      print("Open orders by Buy button")
      pyautogui.click(*img, duration=0.2)
      break
      
    print(" ?---- Can't find Buy button")

def spreadOrderListIfCollapsed():
  while True:
    buyOrdersTitle = pyautogui.locateCenterOnScreen(
      "images/buy_orders_title.png", 
      confidence=0.9, 
      region=(1715, 325, 1890-1715, 455-325)
    )

    if buyOrdersTitle != None:
      print("Order list was spread")
      return
    
    print(" ?---- Can't find Order list")

    collapseOrdersBtn = pyautogui.locateCenterOnScreen(
      "images/collapse_orders_btn.png", 
      confidence=0.9, 
      region=(1710, 315, 1820-1710, 405-315)
    )

    if collapseOrdersBtn != None:
      print("Order list has been spread")
      pyautogui.click(*collapseOrdersBtn, duration=0.2)
      break

    print(" ?---- Can't find Collapse button")

def closeOrderList():
  while True:
    closeBtn = pyautogui.locateCenterOnScreen(
      "images/close_btn.png", 
      confidence=0.9, 
      region=(1190, 290, 1290-1190, 380-290)
    )

    if closeBtn != None:
      print("Orders has been closed")
      pyautogui.click(*closeBtn, duration=0.2)
      break

    print(" ?---- Can't find close button")

def closeMarketWindow():
  while True:
    closeBtn = pyautogui.locateCenterOnScreen(
      "images/close_btn.png", 
      confidence=0.9, 
      region=(1880, 80, 1980-1880, 160-80)
    )

    if closeBtn != None:
      print("\n ---- Market has been closed")
      pyautogui.click(*closeBtn, duration=0.2)
      break

    print(" ?---- Can't find close button")

def isMarketWindowOpened():
  while True:
    img = pyautogui.locateCenterOnScreen(
      "images/market_portrait.png", 
      confidence=0.9, 
      region=(590, 70, 880-590, 290-70)
    )

    if img != None:
      print("\n ---- Market has been opened")
      pyautogui.click(*img, duration=0.2)
      break
    
    if img == None:
      print(" ?---- Can't find Market window")
      pyautogui.click(1780, 320, duration=0.2)

# TODO: Change search and activation methods of window
def isAlbionWindowActive():
  while True:
    x, y = pyautogui.position()
    img = pyautogui.locateCenterOnScreen("images/cursor.png", confidence=0.9, region=(x-20, y-10, 60, 60))

    if img != None:
      print("Albion window is active")
      pyautogui.move(20,0, duration=0.2)
      pyautogui.move(-20,0, duration=0.2)
      break
  
  return True

def run():
  print("\n ------ START ------")

  pyautogui.countdown(3)

  isMarketWindowOpened()

  resetFilter()
  pyautogui.sleep(0.7)

  mapMarketItems()

  closeMarketWindow()

  print("\n ------ DONE ------")

run()




def takeScreenshot(takePosition = 1):
  left, top, right, bottom = 645, 253, 680, 287

  if takePosition == 1:
    pyautogui.countdown(5)
    left, top = pyautogui.position()
    pyautogui.countdown(5)
    right, bottom = pyautogui.position()
    pyautogui.countdown(5)

  print([left, top, right, bottom])
  # for i in range(5): # for blinking things
  pyautogui.screenshot("images/t.png", region=(left, top, right - left, bottom - top))

# takeScreenshot(0)


# for checking color values, in this case check if input text are selected
def checkColorInRange(
  left: int,
  top: int,
  color: tuple,
  right: int = None,
  bottom: int = None,
  tolerance: int = 10
):
  foundColorCounter = []

  for x in range(left, right or left+1): # range for x coordinate
    for y in range(top, bottom or top+1): # range for y coordinate
      isColorFound = pyautogui.pixelMatchesColor(x, y, color, tolerance)
      
      if isColorFound: foundColorCounter.append(isColorFound)
      
      print(isColorFound, "-----" if isColorFound else "", x, " - ", y)

  print("input selected" if len(foundColorCounter) > 6 else "input blured")

# checkColorInRange(left=661, top=277, right=666, bottom=281, color=(248, 213, 128))
