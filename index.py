from appliances import DishWasher
from appliances import CoffeeMaker
from appliances import Dryer
from appliances import Washer
from appliances import Refrigerator
from appliances import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_washer.wash_clothes("delicates")

samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes("high")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

open_can = CanOpener("green")
open_can.open_can()
