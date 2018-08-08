# total coins
coins_found = 3978
new_coins = coins_found / 5
stolen_coins = 4

days = 365

# total coin for a year
total_coins = days * new_coins + coins_found
print ("Total Coins ", total_coins)

month1 = 6 
weeks = days * month1 / 7
total_stolen_cs = weeks * stolen_coins
print("Total stolen coins ",total_stolen_cs)

remaining_coins = total_coins - total_stolen_cs
print("remaining coins ",remaining_coins)
