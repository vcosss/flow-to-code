from tqdm import tqdm
import os
import subprocess
import time


def py_to_flowchart(name):

    # making file addresses
    code = f"./codes/{name}.py"
    flowchart = f"./flowchart/{name}.flowchart"

    # converting code to flowchart file
    os.system(f'python3 -m pyflowchart --no-simplify "{code}" > "{flowchart}"')
    # --conds-align

def edit_flowchart(name):

    # # editing the flowchart file
    fun_name = "function"

    flowchart = f"./flowchart/{name}.flowchart"
    flow_file = open(flowchart,'r')
    lines = flow_file.readlines()
    flow_file.close()

    for i in range(len(lines)):
        if f"start {fun_name}" in lines[i]:
            lines[i] = lines[i].replace(f"start {fun_name}", "start")
        if (f"end {fun_name} return" in lines[i]) or (f"end {fun_name}" in lines[i]):
            lines[i] = lines[i].replace(f"end {fun_name} return", "end")
            lines[i] = lines[i].replace(f"end {fun_name}", "end")

    with open(flowchart,'w') as file:
        for lin in lines:
            file.write(lin)

def flowchart_to_svg(name):
    
    # making file addresses
    flowchart = f"./flowchart/{name}.flowchart"
    svg = f"./svg/{name}.svg"

    # converting the flowchart file to svg
    os.system(f'diagrams flowchart "{flowchart}" "{svg}"')

def edit_svg(name):
    # editing the svg file
    svg = f"./svg/{name}.svg"
    svg_file = open(svg,'r')
    data = svg_file.read()
    svg_file.close()

    left, height, right = data.split(sep='"', maxsplit=2)
    height = str(0.7 * float(height))

    svg_file = open(svg,'w')
    svg_file.write(f'{left}"{height}"{right}')
    svg_file.close()

def svg_to_png(name):

     # making file addresses
    svg = f"./svg/{name}.svg"
    png = f"./png/{name}.png"

    # converting the svg file to png file
    os.system(f'svgexport "{svg}" "{png}" 5x '+'"svg{background:white;}" > /dev/null')



if __name__ == '__main__':

    # MAKING THE DIRECTORIES
    print("making directories...")
    os.system("rm -rf flowchart")
    os.system("rm -rf svg")
    os.system("rm -rf png")
    os.makedirs("flowchart",exist_ok=True)
    os.makedirs("svg",exist_ok=True)
    os.makedirs("png",exist_ok=True)
    print("\n-------------------------DONE MAKING DIRECTORIES----------------------------\n")


    # CODE TO FLOWCHART
    print("converting codes to flowcharts...")
    code_names = [i[:-3] for i in os.listdir('./codes') if i.endswith('.py')]
    for name in tqdm(code_names, desc="code to flowchart"):
        py_to_flowchart(name)
        # edit_flowchart(name)
    print("\n-------------------DONE CONVERTING CODES TO FLOWCHARTS----------------------\n")


    # FLOWCHART TO SVG
    print("converting flowcharts to svg...")
    flow_names = [i[:-10] for i in os.listdir('./flowchart') if i.endswith('.flowchart')]
    pid = []
    for i in tqdm(range(len(flow_names)-1,-1,-1), desc="flowchart to svg"):
        name = flow_names[i]

        # with popen
        # pid.append(subprocess.Popen(
        #     ["diagrams", "flowchart", f"./flowchart/{name}.flowchart", f"./svg/{name}.svg"],
        #     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        # ))
        # if ((i+1)%10==0):
        #     time.sleep(5)
        #     for p in pid:
        #         p.kill()
        #     pid = []

        # with run
        try:
            result = subprocess.run(
                ["diagrams", "flowchart", f"./flowchart/{name}.flowchart", f"./svg/{name}.svg"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10
            )
            if (result.returncode != 0):
                print(f"Some error in {name}")
        except subprocess.TimeoutExpired:
            print(f"Timeout for {name}")
    print("\n-----------------DONE CONVERTING FLOWCHARTS TO SVG--------------------\n")

        
    # EDITING THE SVGS
    print("editing the svgs...")
    svg_names = [i[:-4] for i in os.listdir('./svg') if i.endswith('.svg')]
    for name in tqdm(svg_names, desc="editing the svg"):
        edit_svg(name)
    print("\n----------------------DONE EDITING THE SVGS-------------------------\n")


    # SVG TO PNG
    print("converting svg to png...")
    svg_names = [i[:-4] for i in os.listdir('./svg') if i.endswith('.svg')]
    for name in tqdm(svg_names, desc="svg to png"):
        svg_to_png(name)
    print("\n--------------------DONE CONVERTING SVG TO PNG-----------------------\n")


    # STORING THE RESULTS
    print("storing the results...")
    png_names = [i[:-4] for i in os.listdir('./png') if i.endswith('.png')]

    os.system("rm -rf results")
    os.makedirs("results",exist_ok=True)
    os.makedirs("results/codes",exist_ok=True)
    os.makedirs("results/flowchart",exist_ok=True)
    os.makedirs("results/svg",exist_ok=True)
    os.makedirs("results/png",exist_ok=True)

    for name in tqdm(png_names, desc="storing final results"):
        results = subprocess.run(
            ["cp",f"./codes/{name}.py",f"./results/codes/{name}.py"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        results = subprocess.run(
            ["cp",f"./flowchart/{name}.flowchart",f"./results/flowchart/{name}.flowchart"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        results = subprocess.run(
            ["cp",f"./svg/{name}.svg",f"./results/svg/{name}.svg"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        results = subprocess.run(
            ["cp",f"./png/{name}.png",f"./results/png/{name}.png"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
    print("\n--------------------DONE STORING THE RESULTS------------------------\n")
