
🕵️‍♂️ Steganography Tool – Hide Messages in Images

A Python-based steganography tool to hide and extract secret messages inside image files using Least Significant Bit (LSB) technique.



📌 Features

- 🔐 Encode text messages into images (PNG)
- 🔓 Decode hidden messages from stego images
- 🖼️ Supports clean and lossless LSB steganography
- 🛠️ Command-line interface for quick use
- 🔒 (Optional) Message encryption support
- 💡 Easy to extend with audio or GUI features



🧠 How It Works

This tool uses LSB (Least Significant Bit) steganography to embed secret messages into the pixel data of image files. Since LSB changes are visually unnoticeable, it allows hiding data without altering image appearance.



🛠️ Tech Stack

- Language: Python 3.x
- Libraries:
  - [`Pillow`](https://pillow.readthedocs.io/) – Image manipulation
  - `argparse` – Command-line argument parsing
  - `wave` – *(Optional)* for future audio support
  - `cryptography` – *(Optional)* for message encryption



📁 Project Structure

```
steganography-tool/
├── steg_tool.py
├── requirements.txt
├── README.md
├── input/
│   └── sample.png
└── output/
    └── stego_image.png
```



🚀 Usage

▶️ Encode a message into an image

bash
python steg_tool.py encode -i input/sample.png -o output/stego_image.png -m "Top Secret Message"


🔍 Decode a message from an image

bash
python steg_tool.py decode -i output/stego_image.png
```



📦 Installation

1. Clone the repo:

bash
git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool
```

2. Install dependencies:

bash
pip install -r requirements.txt
```
 🧪 Example

Original Image:

![input](input/sample.png)

After Encoding:

![output](output/stego_image.png)

(Visually identical — but contains your hidden message!)



🔒 Future Enhancements

- 🧠 Add support for **audio steganography (WAV)**
- 🧩 Build a **GUI version** using Tkinter/PyQt
- 🔐 Encrypt message before embedding
- 🌐 Web-based interface (Flask/Streamlit)



👨‍💻 Author

Dharmik Rajani
Cybersecurity Enthusiast | Ethical Hacking | Malware Analysis | AI in Security  
🔗 [LinkedIn](https://linkedin.com/in/dharmikrajani01)  
📧 dharmikrajani01@gmail.com

 📜 License

This project is licensed under the MIT License. Feel free to use and modify with credit.
