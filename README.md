## AI Hackathon in Transport 2024 - Team 4 

This repository contains the work of Team 4 for the [AI Hackathon in Transport 2024](https://rsvp.withgoogle.com/events/dft-ai-hackathon-2024). Our project focuses on analysing accident data in [Greater Manchester](https://en.wikipedia.org/wiki/Greater_Manchester) from 2010 to 2021 and developing tools to provide insights to citizens and policymakers.

### Files

1. `unified_dataset.csv` 
   - Contains unified datasets of accidents, casualties and vehicles in [Greater Manchester from 2010-2021](https://www.data.gov.uk/dataset/25170a92-0736-4090-baea-bf6add82d118/gm-road-casualty-accidents-full-stats19-data)
   - Combines and cleans the raw [accident](https://odata.tfgm.com/opendata/downloads/STATS19AccDataJan2010Dec2021forGMServers.csv), [casualty](https://odata.tfgm.com/opendata/downloads/STATS19CasDataJan2010Dec2021forGMServers.csv) and [vehicle](https://odata.tfgm.com/opendata/downloads/STATS19VehDataJan2010Dec2021forGMServers.csv) CSV files 
   - Use this as the master dataset for all subsequent analysis and visualisation
- The [Jupyter Notebook](./manchester_accident_create_unified_dataset.ipynb) for creating a unified dataset is here.

2. `manchester_accident_severity1_heatmap.ipynb`
   - [Jupyter Notebook](./manchester_accident_severity1_heatmap.ipynb) generates an interactive heatmap of the severity of one accident in Greater Manchester

3. `manchester_accident_analysis.ipynb`  
   - The [Jupyter Notebook](./manchester_accident_analysis.ipynb) perform an in-depth analysis of the unified accident dataset.
   - Generates insights such as clusters of top high-risk areas and top contributing factors.
  
4. `manchester_intelligent_road_safety_hub.py`
   - [Code](./manchester_intelligent_road_safety_hub.py) for an interactive web portal presenting accident insights to citizens and policymakers
   - Built using Gradio for the frontend interface 
   - Leverages the OpenAI API to power a simple chatbot that can answer questions about Manchester accidents
   - Potential Question: What are the top three reasons for accidents in Greater Manchester with an explanation?

### Getting Started

1. Clone this repository and navigate to the project directory
2. Run the Jupyter notebooks in sequential order to generate the [unified dataset](manchester_accident_create_unified_dataset.ipynb), [generate heatmap](manchester_accident_severity1_heatmap.ipynb) and [perform analysis](manchester_accident_analysis.ipynb)
3. Install the required Python libraries: `pip install -r requirements.txt`
4. Set the environment variable OPENAI_API_KEY in the current shell session: `export OPENAI_API_KEY="your_openai_api_key"`
5. Launch the interactive portal by running: `python3 manchester_intelligent_road_safety_hub.py`

### Contributors

Ada x Amine x Harry x Finbarrs x Jill x Jamie x Hakem

> 

Thank you to our [Department for Transport](https://www.gov.uk/government/organisations/department-for-transport) (DfT), [Google](https://about.google/google-in-uk/) and [PA](https://www.paconsulting.com/) colleagues.

### License

This project is licensed under the [MIT License](./LICENSE).

### Copyright

(c) 2024 DfT - [Department for Transport](https://www.gov.uk/government/organisations/department-for-transport).
