n_lattine = 6
capienza_lattina = 0.335
n_bottiglie = 1
capienza_bottiglia = 2

volume_lattine = n_lattine * capienza_lattina
volume_bottiglie = n_bottiglie * capienza_bottiglia


print("convengono le lattine" if volume_lattine > volume_bottiglie else "convengono le bottiglie")