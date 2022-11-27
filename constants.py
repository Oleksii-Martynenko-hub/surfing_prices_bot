from collections import namedtuple

Farm = namedtuple("FARM", [
  "GO_TO_FIRST_FARM_PLACE",
  "GO_TO_SECOND_FARM_PLACE",
  "GO_TO_THIRD_FARM_PLACE",
  "GO_TO_FOURTH_FARM_PLACE",
  "GO_TO_FIFTH_FARM_PLACE",
  "GO_TO_TELEPORT",
  "PUT_SEEDS",
  "TAKE_CROPS",
  "TAKE_SEEDS_FROM_INVENTORY",
  "GO_TO_NEXT_ISLAND",
  ])

FARM = Farm(**{
  "GO_TO_FIRST_FARM_PLACE": 'farm/goToFirstFarmPlace',
  "GO_TO_SECOND_FARM_PLACE": 'farm/goToSecondFarmPlace',
  "GO_TO_THIRD_FARM_PLACE": 'farm/goToThirdFarmPlace',
  "GO_TO_FOURTH_FARM_PLACE": 'farm/goToFourthFarmPlace',
  "GO_TO_FIFTH_FARM_PLACE": 'farm/goToFifthFarmPlace',
  "GO_TO_TELEPORT": 'farm/goToTeleport',
  "PUT_SEEDS": 'farm/putSeeds',
  "TAKE_CROPS": 'farm/takeCrops',
  "TAKE_SEEDS_FROM_INVENTORY": 'farm/takeSeedsFromInventory',
  "GO_TO_NEXT_ISLAND": 'farm/goToNextIsland'
})

Islands = namedtuple("ISLANDS", [
  # "OLEKSIIM",
  # "M4RTIN",
  # "PROCESS",
  "EPMTYPLAYER",
  # "FAARM1",
  # "FAARM2",
  # "FAARM3",
  # "FAARM4",
  ])

ISLANDS = Islands(**{
  # "OLEKSIIM": 'images/oleksiim_island_minimap_title.png',
  # "M4RTIN": 'images/m4rtin_island_minimap_title.png',
  # "PROCESS": 'images/process_island_minimap_title.png',
  "EPMTYPLAYER": 'images/epmtyplayer_island_minimap_title.png',
  # "FAARM1": 'images/faarm1_island_minimap_title.png',
  # "FAARM2": 'images/faarm2_island_minimap_title.png',
  # "FAARM3": 'images/faarm3_island_minimap_title.png',
  # "FAARM4": 'images/faarm4_island_minimap_title.png',
})