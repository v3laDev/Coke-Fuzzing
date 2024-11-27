# Coke Fuzzing

Welcome to the **Coke Fuzzing** tool, a powerful and efficient web fuzzing script designed to help you discover subdomains and subdirectories of a given domain. This tool is ideal for security researchers and penetration testers who need to map out the structure of a web application.

## Features

- **Subdomain Discovery**: Identify potential subdomains of a target domain.
- **Subdirectory Discovery**: Find common subdirectories within a web application.
- **Speed Modes**: Choose between low, medium, and fast modes to control the speed of your fuzzing.
- **Logging**: Save your results to a log file for further analysis.
- **Customizable**: Easily extend the list of subdomains and subdirectories to suit your needs.

## Installation

To get started with Coke Fuzzing, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/v3laDev/Coke-Fuzzing.git
   cd Coke-Fuzzing
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Your Wordlists**:
   Customize the `files/subdomains.txt` and `files/subdirectories.txt` with your desired entries.

## Usage

Run the script with the following command:
```bash
python app.py <domain> [options]
```


### Options

- `--subdomains <file>`: Specify a file containing a list of subdomains.
- `--subdirectories <file>`: Specify a file containing a list of subdirectories.
- `-all`: Search both subdomains and subdirectories.
- `--mode {low, medium, fast}`: Set the speed mode for fuzzing.
- `--logs`: Save the results to a log file.
- `-h, --help`: Show the help message and exit.

### Example Usage

```bash

python app.py example.com --subdomains files/subdomains.txt --subdirectories files/subdirectories.txt --mode fast --logs

```


## Contributing

We welcome contributions to enhance the functionality of Coke Fuzzing. Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, feel free to reach out to the repository owner at [v3laDev](https://github.com/v3laDev).

---

Thank you for using Coke Fuzzing! We hope it serves as a valuable tool in your web security arsenal.
![Example]([images/example.png](https://github.com/v3laDev/Coke-Fuzzing/blob/main/images/example.PNG))
