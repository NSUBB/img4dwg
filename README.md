# 🖼️ Image 4 DWG

<img width="730" height="717" alt="img4dwg_icon" src="https://github.com/user-attachments/assets/06de67e5-cacb-4faa-ba93-15f12e3b83a9" />


[**img4dwg-gui.exe**](https://github.com/NSUBB/img4dwg/releases/download/v1.0.0/img4dwg-gui.exe)

A simple, standalone Windows application to batch-process images for CAD tracing.

---

## 📌 What Is It?

**Image 4 DWG** is a graphical tool designed to help architects, engineers, and drafters prepare raster images for manual tracing in CAD software like AutoCAD. When construction drawings are provided as flattened PDFs or scanned images, they often have white backgrounds that are hard to trace over in AutoCAD’s dark Model Space.

This tool allows you to apply a customizable color overlay to an entire folder of images in just a few clicks.

---

## ✅ Features

- 📁 Select a folder of images to process
- 🎨 Choose any overlay color (e.g., magenta, cyan, green)
- 🎚️ Adjust threshold and contrast for better visibility
- 🖼️ Preview changes before processing
- ⚡ Batch-processes all images in seconds
- 💾 Saves processed images in a `Processed` subfolder

<img width="681" height="682" alt="image" src="https://github.com/user-attachments/assets/bd940eb5-1113-4fa5-adf8-63a28b5e1add" />

---

## 💻 Installation (No Python Required)

1. **Download the App**
   - Go to the Releases section of this repository.
   - Download the latest version of `img4dwg-gui.exe`.

2. **Recommended Installation Folder**
   - Create a folder on your computer, e.g.:
     ```
     C:\Image4DWG\
     ```
   - Move `img4dwg-gui.exe` into that folder.

3. **(Optional) Create a Shortcut**
   - Right-click the `.exe` → **Send to** → **Desktop (create shortcut)**

---

## 🚀 How to Use

1. **Launch the App**
   - Double-click `img4dwg-gui.exe`.

2. **Select Folder**
   - Click **Browse** and choose the folder containing your images.

3. **Pick Overlay Color**
   - Click **Pick Color** and choose a color that contrasts well with AutoCAD’s dark background (e.g., magenta or cyan).

4. **Adjust Threshold & Contrast**
   - Use the sliders to fine-tune how the overlay is applied.

5. **Preview**
   - A preview of the first image will update automatically.

6. **Start Processing**
   - Click **Start Processing** to apply the overlay to all images.
   - Processed images will be saved in a subfolder called `Processed`.

7. **Done!**
   - Once complete, click **Close** to exit the app.

---

## 🖼️ Supported Image Formats

- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`

---

## 🛠️ Troubleshooting

- If the app doesn’t open, make sure your antivirus or Windows Defender isn’t blocking it.
- If you see no preview, ensure the selected folder contains supported image files.

---

## Version History

 - v2.0 Transparency added and output forced to PNG.
 - v1.0 Initial Release

---

## 📃 License
This project is open-source and free to use. See LICENSE for details.

---

## 🙌 Credits

Developed by NSUBB  
Built with Python, Tkinter, Pillow, NumPy, and PyInstaller

