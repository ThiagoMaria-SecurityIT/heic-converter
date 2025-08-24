# HEIC to JPG/PNG Converter

![HEIC Converter](https://img.shields.io/badge/Python-3.6%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

<img width="594" height="723" alt="image" src="https://github.com/user-attachments/assets/e215c182-5e30-43f1-a4c1-9ae3b6bcb5e9" />

 HEIC Converter Interface

## Quick Start  

1. **Select HEIC files**:
   - Click "Select HEIC Files" to choose images from your iPhone/Computer folder
   - You can select multiple files at once

2. **Choose output format**:
   - Select either JPG or PNG format

3. **Select output folder** (optional):
   - Choose where to save converted images (defaults to current directory)

4. **Convert**:
   - Click "Convert" to start the conversion process
   - Progress will be shown in the status bar
   

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
   - [Option 1: Using Virtual Environment (Recommended)](#option-1-using-virtual-environment-recommended)
   - [Option 2: Global Installation (Not Recommended)](#option-2-global-installation-not-recommended)
4. [Virtual Environment Management](#virtual-environment-management)
   - [Activating the Virtual Environment](#activating-the-virtual-environment)
   - [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
   - [Updating Dependencies](#updating-dependencies)
   - [Removing the Virtual Environment](#removing-the-virtual-environment)
5. [Usage](#usage)
6. [Requirements](#requirements)
7. [Troubleshooting](#troubleshooting)
   - [Common Issues](#common-issues)
   - [Getting iPhone Photos to Your Computer](#getting-iphone-photos-to-your-computer)
8. [Technical Details](#technical-details)
9. [Contributing](#contributing)
10. [License](#license)
11. [Support](#support)
12. [Frequently Asked Questions](#frequently-asked-questions)
13. [AI Transparency](#-ai-transparency)
14. [About me](#-about-me)
15. [Contributing](#-contributing)

## Overview

iPhone cameras capture photos in the HEIC (High Efficiency Image Container) format by default, which provides excellent compression but isn't universally supported across all platforms and applications. This tool provides an easy way to convert those HEIC images to more common formats like JPG or PNG.

## Features

- **User-Friendly Interface**: Simple GUI that makes conversion easy for non-technical users
- **Batch Processing**: Convert multiple HEIC files at once
- **Format Options**: Choose between JPG or PNG output formats
- **Quality Preservation**: Maintains image quality during conversion
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Option 1: Using Virtual Environment (Recommended)

Using a virtual environment is recommended to avoid conflicts with other Python projects.

1. **Install Python** (if not already installed):
   - Download from [python.org](https://python.org)
   - Requires Python 3.6 or higher

2. **Create and activate a virtual environment**:

   **On macOS/Linux:**
   ```bash
   # Create virtual environment
   python3 -m venv heic-env
   
   # Activate the virtual environment
   source heic-env/bin/activate
   ```

   **On Windows:**
   ```bash
   # Create virtual environment
   python -m venv heic-env
   
   # Activate the virtual environment
   heic-env\Scripts\activate
   ```

3. **Download the application**:
   ```bash
   git clone https://github.com/ThiagoMaria-SecurityIT/heic-converter.git
   cd heic-converter
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Global Installation (Not Recommended)

If you prefer not to use a virtual environment:

1. **Install Python** (if not already installed):
   - Download from [python.org](https://python.org)
   - Requires Python 3.6 or higher

2. **Download the application**:
   ```bash
   git clone https://github.com/ThiagoMaria-SecurityIT/heic-converter.git
   cd heic-converter
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Virtual Environment Management

### Activating the Virtual Environment
Each time you want to use the application, you'll need to activate the virtual environment:

**macOS/Linux:**
```bash
source heic-env/bin/activate
```

**Windows:**
```bash
heic-env\Scripts\activate
```

### Deactivating the Virtual Environment
When you're done using the application, you can deactivate the virtual environment:

```bash
deactivate
```

### Updating Dependencies
If the requirements change, you can update the dependencies:

```bash
# Activate the virtual environment first
pip install -r requirements.txt --upgrade
```

### Removing the Virtual Environment
If you want to remove the virtual environment completely:

```bash
# Deactivate first if active
deactivate

# Remove the environment directory
rm -rf heic-env  # macOS/Linux
# or
rmdir /s heic-env  # Windows
```

## Usage

1. **Activate the virtual environment** (if using one):

   **On macOS/Linux:**
   ```bash
   source heic-env/bin/activate
   ```

   **On Windows:**
   ```bash
   heic-env\Scripts\activate
   ```

2. **Run the application**:
   ```bash
   python heic_converter.py
   ```

3. **Select HEIC files**:
   - Click "Select HEIC Files" to choose images from your iPhone/Computer folder
   - You can select multiple files at once

4. **Choose output format**:
   - Select either JPG or PNG format

5. **Select output folder** (optional):
   - Choose where to save converted images (defaults to current directory)

6. **Convert**:
   - Click "Convert" to start the conversion process
   - Progress will be shown in the status bar

## Requirements

The application requires the following Python packages:
- Pillow (Python Imaging Library)
- pillow-heic (HEIC format support)

These are automatically installed when you run:
```bash
pip install -r requirements.txt
```

## Troubleshooting

### Common Issues

1. **"No module named 'PIL'" error**:
   - Solution: Run `pip install -r requirements.txt` again

2. **HEIC files not recognized**:
   - Solution: Ensure you're using a recent version of pillow-heic

3. **Conversion fails for some files**:
   - Solution: Try converting files one by one to identify problematic images

4. **Virtual environment not working on Windows**:
   - **Solution**: Make sure you're using a compatible Python version (3.6+).
   - **Issue with Execution Policy**: Windows PowerShell has a security feature called an Execution Policy that restricts script execution by default to protect your system.
     - **First, check your current policy:** Open PowerShell and run:
       ```powershell
       Get-ExecutionPolicy
       ```
       If this returns `Restricted` (the default), you won't be able to run the activation script.

     - **To enable scripts for the current user only** (recommended), run:
       ```powershell
       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
       ```
       This is a safe setting as it only allows locally-created scripts or downloaded scripts from trusted publishers to run, and the change only affects your user account.

     - **After you're done**, you can revert to the more secure setting if you wish:
       ```powershell
       Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser
       ```

     - **Alternative**: Instead of changing the policy, you can always activate the virtual environment using Command Prompt (`cmd.exe`) instead of PowerShell, as it is not affected by this policy. 

### Getting iPhone Photos to Your Computer

1. **Using iCloud Photos**:
   - Enable iCloud Photos on your iPhone
   - Access photos through iCloud.com or the iCloud app on your computer

2. **Using AirDrop**:
   - Select photos on your iPhone and share via AirDrop to your computer

3. **Using a USB cable**:
   - Connect your iPhone to your computer
   - Import photos using the Photos app (macOS) or File Explorer (Windows)

## Technical Details

This application uses:
- **Pillow**: For image processing and format conversion
- **pillow-heic**: To handle HEIC format decoding
- **Tkinter**: For the graphical user interface

The conversion process:
1. Reads HEIC files using the pillow-heic library
2. Processes the image data using Pillow
3. Saves the image in the selected format (JPG/PNG)
4. Preserves the original filename while changing the extension

## Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any problems or have questions:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with details about your problem

## Frequently Asked Questions

**Q: Will converting my HEIC images reduce their quality?**
A: The conversion process is designed to preserve image quality. JPG uses lossy compression, but we use high-quality settings (95% quality). PNG uses lossless compression.

**Q: Can I convert HEIC images in bulk?**
A: Yes, you can select and convert multiple HEIC files at once.

**Q: Does this work with Live Photos?**
A: This tool converts the still image from HEIC format but doesn't preserve the motion component of Live Photos.

**Q: Is my image data secure?**
A: Yes, the conversion happens entirely on your computer. Your images are never uploaded to any server.

**Q: Why should I use a virtual environment?**
A: Virtual environments keep dependencies for different projects separate, preventing conflicts between packages required by different applications.

---

**Note**: This tool is not affiliated with or endorsed by Apple Inc.

## 🤖 AI Transparency  
This application was developed with AI assistance to generate and refine the Python code, and is designed for iPhone users who wants a quick solution to convert images to JPG or PNG.  


## 👨‍💻 About me  

**Thiago Maria - From Brazil to the World 🌎**  
*Senior Security Information Professional | Passionate Programmer | AI Developer*

With a professional background in security analysis and a deep passion for programming, I created this GitHub account to share knowledge about security information, cybersecurity, Python and AI development practices. Most of my work focuses on implementing security-first approaches at companies and developer tools while maintaining usability and productivity.

**Let's Connect:**    

👇🏽 Click on the badges below:   

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/thiago-cequeira-99202239/)  
[![Hugging Face](https://img.shields.io/badge/🤗Hugging_Face-AI_projects-yellow)](https://huggingface.co/ThiSecur)  

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a new branch
3. Submit a pull request

**Ways to Contribute:**   
Want to see more upgrades? Help me keep it updated!    
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/ThiagoMaria-SecurityIT) 
