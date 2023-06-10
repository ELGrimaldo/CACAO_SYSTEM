# Cacao Fermentation Dashboard

## Introduction
---

The Cacao Fermentation Dashboard is a web-based application designed to monitor and analyze the fermentation process of cacao beans. This dashboard provides real-time insights and visualizations to help cacao producers optimize their fermentation processes and ensure high-quality chocolate production. Additionally real-time classification of fermentation degree is incorporated using TensorFlow. 

## Features
The Cacao Fermentation Dashboard offers the following features:

1. Real-time Data Monitoring: The dashboard displays real-time data on temperature, pH levels, and MQ-sensors data. Users can track the progress of fermentation and identify any deviations from the desired conditions.

2. Visualizations: The dashboard provides interactive charts and graphs to visualize the fermentation data over time. 

3. Alerts and Notifications: The dashboard can be configured to send alerts and notifications when specific thresholds or conditions are met. This feature helps users identify critical issues or anomalies in the fermentation process promptly.

4. Real-time Classification of Cacao Beans Fermentation Degree: Users will be able to see if the cacao is already fermented based on the AI that used previous data.

## Installation:
To install and set up the Cacao Fermentation Dashboard, follow these steps:

1. Clone the repository from github:
    >  `git clone https://github.com/ELGrimaldo/CACAO_SYSTEM.git` 

2. Install virtual environment in the project root directory:
    > `python -m venv env`

    `env` is a variable

3. Activate virtual environtment. Make sure that you are in the root directory
    > `env\Scripts\activate`

4. Once the virtual environment is activated, run the server using the following command:
    > `python manage.py runserver`

## Technology Used

The Cacao Fermentation Dashboard is built using the following technologies:
- Front-end
    - HTML, CSS, and JavaScript
    - Chart.js for Data Visualization
- Back-end:
    - Python
- Framework
    - Django

## Contributors
The Cacao Fermentation Dashboard was developed by the following contributors:

- [James Grimaldo](https://github.com/ELGrimaldo)
- [Meliza Parcon](https://github.com/Mel1030)
- [Rikiya Yamamoto](https://github.com/Boopya)

## Project Tasks
The Cacao Fermentation Dashboard is currently under development with the following unfinished features:
- Front-End:
    - [ ] Dashboard Interface
    - [ ] Dashboard graph data using Chart.js
    - [ ] Boxes Interace
    - [ ] Boxes graph data using Chart.js
    - [ ] Connection Interface

- Back-end and Data connection
    - [ ] Create a server for recieving data from ESP32
    - [ ] Create class that will handle recieved data
    - [ ] Create class that will manage the data including request from the interface.
    - [ ] Create class that will handle server client connection.
