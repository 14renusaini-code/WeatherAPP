
# WeatherApp

A Python CLI and Jupyter-based application to fetch, analyze, and visualize weather data using the OpenWeatherMap API.

## Features
- Fetch current weather data for any city
- Save and analyze weather data
- Visualize metrics using Jupyter notebooks

## Project Structure
```
├── src/
│   ├── weather.py         # Handles API requests and weather logic
│   └── utils.py           # Utility functions (e.g., formatting, validation)
│
├── data/
│   └── sample_response.json   # Example of fetched weather data
│
├── notebooks/
│   └── weather_analysis.ipynb # Jupyter notebook for analysis/visualization
│
├── .gitignore
├── requirements.txt
├── README.md
└── main.py                # Entry point for the CLI app
```

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WeatherApp.git
   cd WeatherApp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
4. Add your API key in `src/weather.py`:
   ```python
   API_KEY = "YOUR_API_KEY"
   ```

## Usage
Run the CLI app:
```bash
python main.py
```
Enter a city name when prompted to see the weather details.

### Jupyter Notebook
Open `notebooks/weather_analysis.ipynb` to analyze and visualize weather data.

## Data
Fetched weather data is saved in `data/sample_response.json` for analysis and visualization.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.
