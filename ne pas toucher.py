import os
import pickle

os.chdir("d://programmes/python/plan de cuve")

stockParDefaulft = 0

conf_canister1 = {"viso":7,\
    "0":{"x":250,"y":250,"color":"red","name":"alex","stock":stockParDefaulft,"num":"10","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":250,"y":125,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":375,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":375,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":250,"y":375,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":125,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":125,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}

conf_canister2 = {"viso":7,\
    "0":{"x":250,"y":250,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":250,"y":125,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":375,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":375,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":250,"y":375,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":125,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":125,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}

conf_canister3 = {"viso":7,\
    "0":{"x":250,"y":250,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":250,"y":125,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":375,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":375,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":250,"y":375,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":125,"y":332,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":125,"y":166,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}

conf_canister4 = {"viso":12,\
    "0":{"x":250,"y":60,"color":"blue","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":350,"y":100,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":420,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":410,"y":310,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":350,"y":400,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":225,"y":430,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":100,"y":350,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "7":{"x":80,"y":220,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "8":{"x":140,"y":110,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "9":{"x":200,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "10":{"x":300,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "11":{"x":250,"y":300,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}

conf_canister5 = {"viso":12,\
    "0":{"x":250,"y":60,"color":"blue","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":350,"y":100,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":420,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":410,"y":310,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":350,"y":400,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":225,"y":430,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":100,"y":350,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "7":{"x":80,"y":220,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "8":{"x":140,"y":110,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "9":{"x":200,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "10":{"x":300,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "11":{"x":250,"y":300,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}

conf_canister6 = {"viso":12,\
    "0":{"x":250,"y":60,"color":"blue","name":"t","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "1":{"x":350,"y":100,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "2":{"x":420,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "3":{"x":410,"y":310,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "4":{"x":350,"y":400,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "5":{"x":225,"y":430,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "6":{"x":100,"y":350,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "7":{"x":80,"y":220,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "8":{"x":140,"y":110,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "9":{"x":200,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "10":{"x":300,"y":200,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0},\
    "11":{"x":250,"y":300,"color":"red","name":"","stock":stockParDefaulft,"num":"","lait":0,"TP":0,"TB":0,"impl":0,"long":0,"vitess":0,"tempera":0,"loco":0}}


fichier = open("data","wb")

pickle.dump(conf_canister1,fichier)
pickle.dump(conf_canister2,fichier)
pickle.dump(conf_canister3,fichier)
pickle.dump(conf_canister4,fichier)
pickle.dump(conf_canister5,fichier)
pickle.dump(conf_canister6,fichier)

fichier.close()