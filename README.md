# Check-Kodam

Check-Kodam is a Python and Flask-based web application that uses face detection to assign a random name to the user. The app utilizes OpenCV and MediaPipe to detect faces through a camera.

## Features

- **Face Detection**: Uses the camera to detect the user's face.
- **Random Name Assignment**: Once a face is detected, the app assigns a random name from a predefined list.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Mahklvk/Check-Kodam.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Check-Kodam
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:

   ```bash
   python app.py
   ```

6. **Access the application**:

   Open your browser and visit `http://localhost:5000`.

## Usage

- **Camera Access**: Make sure to grant camera access when using the application.
- **Face Detection**: The app will automatically detect your face through the camera.
- **Random Name Display**: Once a face is detected, the app will display a random name chosen from a predefined list.

## Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request for improvements or new features.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.
