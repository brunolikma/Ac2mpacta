vicCoin = 0.00
real = 0.00

while vicCoin != -1.0:
        vicCoin = float(input())
        if vicCoin != -1.0:
            real = real + vicCoin

realtotal = real * 2.50
print(f"VC$ {real:.2f}")
print(f"R$ {realtotal:.2f}")