CIUDADES_ARG = ["Buenos Aires", "Rosario", "Viedma"]
CIUDADES_PERU = ["Cusco", "Lima", "Ayacucho"]
CIUDADES_BRAZ = ["Rio de Janeiro", "Belo Horizonte", "Recife"]

def calls(n, origins, destinies, durations):
    total = []
    for x in range(n):
        if origins[x] == destinies[x]:
            local_calls_price = durations[x]
            total.append(local_calls_price)
        else:
            conditions = [
                origins[x] in CIUDADES_ARG and destinies[x] in CIUDADES_ARG,
                origins[x] in CIUDADES_BRAZ and destinies[x] in CIUDADES_BRAZ,
                origins[x] in CIUDADES_PERU and destinies[x] in CIUDADES_PERU
            ]
            if any(conditions):
                if durations[x] > 60:
                    national_call_price = 10 + (durations[x] - 60)
                else:
                    national_call_price = 10
                total.append(national_call_price)
            else:
                if durations[x] >= 600:
                    international_call_price = 15 * durations[x]
                else:
                    international_call_price = 20 * durations[x]
                total.append(international_call_price)
    return total

#example1 = 1, ["Buenos Aires"], ["Buenos Aires"], [10]
#example2 = 3, ["Cusco", "Rio de Janeiro", "Viedma"], ["Cusco", "Rio de Janeiro", "Viedma"], [0, 100, 10000000]
#example3 =  2, ["Buenos Aires", "Rio de Janeiro"], ["Rosario", "Recife"], [50, 61]
print(calls(*example3))

