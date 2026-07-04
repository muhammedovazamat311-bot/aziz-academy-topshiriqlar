# Taksi park: masofasi hisobi
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
nums = [int(input()) for _ in range(4)]
total = sum(nums)
diff = max(nums) - min(nums)
avg = total // 4
print(total)
print(diff)
print(avg)