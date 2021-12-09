
area_kuvert = 0.229 * 0.324 *2 #dubbla arean då det är 2 sidor 
area_affisch = 0.297 * 0.42 * 2 # 2 affischer
area_infoblad = 0.21 * 0.297

vikt = 0

ytvikt_kuvert = int(input("Kuvert ? "))
ytvikt_affisch = int(input("Affisch ? "))
ytvikt_blad = int(input("Blad ? "))

vikt = ytvikt_kuvert * area_kuvert + ytvikt_affisch * area_affisch + ytvikt_blad * area_infoblad

print(vikt)