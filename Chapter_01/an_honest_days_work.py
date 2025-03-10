total_paint = int(input())
badges_per_litter = int(input())
price_per_badge = int(input())

produced_badges = int(total_paint / badges_per_litter)
leftover_paint = total_paint % badges_per_litter

total_sell = (produced_badges * price_per_badge) + (leftover_paint * 1)

print(total_sell)
