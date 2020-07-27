from person import Person
import random

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show



def create_graph_calculate(steps, person, times_try):
    distances = []
    graph = figure(title=f"Distancia Recorrida con {steps} pasos", x_axis_label="eje x", y_axis_label="eje y")
    for _ in range(times_try):
        x, y, final_x, final_y = person.create_path(steps, 0.01)
        total_distance = abs((final_x**2 - final_y **2 )**0.5)
        distances.append(round(total_distance, 2))
        random_color = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
        graph.line(x, y, color=random_color)
    
    max_distance = max(distances)
    min_distance = min(distances)
    average_distance = round(sum(distances) / times_try, 3)
    print(f"CON {steps} PASOS:\n============================================================\nDistancia maxima recorrida {max_distance}\n Distancia Minima Recorrida {min_distance}\n Distancia Promedio {average_distance}")
    show(graph)


def main():
    times_try = 100
    distances_walk = [10, 100, 1000, 10000]
    person = Person("alejandro", 0, 0)
    for steps in distances_walk:
        create_graph_calculate(steps, person, times_try)
    
  
    

    # print(f"{x}\n{y}")

    # person.create_path(100)
    # person.create_path(1000)
    



    



if __name__ == "__main__":
    main()