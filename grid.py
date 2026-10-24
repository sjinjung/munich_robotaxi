import os
import subprocess
import xml.etree.ElementTree as ET
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 0. SUMO 시뮬레이션 자동 실행 (fcd_data.xml 생성)
sumo_command = [
    "sumo", 
    "-c", "munich_robotaxi.sumocfg", 
    "--fcd-output", "fcd_data.xml", 
    "--begin", "21000", 
    "--end", "28200", 
    "--step-length", "1"
]

print("Running SUMO simulation from 21000 to 28200 (This may take a while)")
try:
    # 명령어 실행이 끝날 때까지 파이썬 스크립트가 대기합니다.
    subprocess.run(sumo_command, check=True)
    print("✅ SUMO simulation completed successfully.\n")
except subprocess.CalledProcessError as e:
    print(f"❌ SUMO execution failed: {e}")
    exit(1)
except FileNotFoundError:
    print("❌ 'sumo' command not found. Please ensure SUMO is installed and added to your system PATH.")
    exit(1)

# ---------------------------------------------------------
# 기존 데이터 처리 및 시각화 코드 시작
# ---------------------------------------------------------
file_path = 'fcd_data.xml' 

# 1. identify file path and size
if not os.path.exists(file_path):
    raise FileNotFoundError(f"'{file_path}' not a valid file path. Please check the file path and try again.")

file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
if file_size_mb == 0:
    raise ValueError("File size is 0 bytes. SUMO failed to execute the simulation properly.")

print(f"✅ File confirmed: {file_path} (Size: {file_size_mb:.2f} MB)")

# 2. XML data parsing
data = []
print("Reading data... (This may take several seconds depending on file size)...")

try:
    for event, elem in ET.iterparse(file_path, events=('end',)):
        if elem.tag == 'vehicle':
            data.append({
                'x': float(elem.attrib['x']),
                'y': float(elem.attrib['y'])
            })
            elem.clear()
except ET.ParseError as e:
    print(f" XML parsing error occurred: {e}")

# 3. parsing results
if not data:
    print("File was read successfully but no 'vehicle' data found. No vehicles were generated in the scenario.")
else:
    print(f"Parsing completed! Successfully retrieved {len(data):,} vehicle trajectory positions.")
    
    # Heatmap generation (10m x 10m grid)
    df = pd.DataFrame(data)
    GRID_SIZE = 10
    df['grid_x'] = (df['x'] // GRID_SIZE) * GRID_SIZE
    df['grid_y'] = (df['y'] // GRID_SIZE) * GRID_SIZE
    
    grid_density = df.groupby(['grid_x', 'grid_y']).size().reset_index(name='density')
    heatmap_matrix = grid_density.pivot(index='grid_y', columns='grid_x', values='density').fillna(0)
    heatmap_matrix.sort_index(ascending=False, inplace=True)
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(
    heatmap_matrix, 
    cmap="inferno", 
    xticklabels=50, 
    yticklabels=50, 
    robust=True
)
    plt.title("Munich Scenario: 10m x 10m Vehicle Density Heatmap")
    plt.show()