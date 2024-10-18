#codigo usando series
import pandas as pd
media = pd.Series([20,50,60,40,30,80,90,70,100,70])
ap = media[media >=70]
rp = media[media <=70]
print("medias maiores que 70")
print(ap)
print("medias menores que 70")
print(rp)
