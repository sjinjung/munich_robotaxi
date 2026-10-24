# Network Heatmap Comparison of Robotaxi Pick-up and Drop-off Behaviors in Munich: A Spatial Analysis of Grid vs. Radial Topologies

> **Status:** Work in Progress (Data integration and scenario modeling phase)

## 1. Project Overview
This project investigates the impact of urban road network topologies on traffic congestion induced by autonomous Robotaxi pick-up and drop-off (PUDO) operations. Focusing on downtown Munich, Germany, the study establishes a comparative analysis between two distinct network structures: the grid topology of Maxvorstadt and the radial topology of the Old City (Altstadt). 

By leveraging the Simulation of Urban MObility (SUMO) framework, this research visualizes spatial vehicle density and bottleneck formations through high-resolution heatmaps. The primary objective is to quantify the structural vulnerabilities and resilience of different urban layouts in response to emerging micro-transit behaviors.
<img width="2000" height="800" alt="before" src="https://github.com/user-attachments/assets/32210af1-bdea-4109-8058-d4d7e5a3c3ae" />

## 2. Methodology & Key Features
- **Base Scenario Modeling:** Utilizes the [TUMFTM/munich-sumo-scenario](https://github.com/TUMFTM/munich-sumo-scenario) as the foundational microscopic traffic simulation environment.
- **Empirical Data Integration:** Incorporates General Transit Feed Specification (GTFS, https://www.mvg.de/static/gtfs/google_transit.zip) data to synthesize realistic public transit demand and model empirical Robotaxi routing algorithms.
- **Spatial-Temporal Analysis:** Quantifies the localized traffic perturbations caused by PUDO events, utilizing a 10m x 10m grid-based density heatmap to evaluate congestion propagation.

## 3. Simulation Results & Topological Comparison
*(Note: Simulations and data extraction are currently in progress. Empirical heatmaps will be appended upon the completion of computational experiments.)*

### 3.1. Grid Network Topology (Maxvorstadt)
Analyzes the traffic dispersion capacity and detour routing efficiency within a grid structure during high-frequency PUDO operations.


### 3.2. Radial Network Topology (Old City / Altstadt)
Evaluates the centralization of traffic flow and the exacerbation of bottleneck phenomena in a radial structure constrained by limited alternative routing.


## 4. Project Progress
- [x] Establish and validate the baseline microscopic traffic scenario (TUMFTM Munich).
- [x] Develop a Python-based pipeline for spatial heatmap visualization utilizing SUMO Floating Car Data (FCD).
- [ ] Synthesize Robotaxi demand distributions and routing models derived from empirical GTFS transit data.
- [ ] Execute comparative PUDO simulations across the Maxvorstadt and Old City topologies.
- [ ] Conduct quantitative comparative analysis and update spatial visualizations.

## 5. Replication & Usage
```bash
# 1. Clone the repository
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

# 2. Install required dependencies
pip install pandas seaborn matplotlib

# 3. Execute the simulation and generate spatial heatmaps
python run_simulation_and_heatmap.py
