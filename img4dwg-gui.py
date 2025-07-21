
import os
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageTk
from tkinter import Tk, Label, Button, filedialog, colorchooser, Scale, HORIZONTAL, StringVar, IntVar
from tkinter.ttk import Progressbar
import threading

def apply_transparency_from_luminance(image, contrast=1.0):
    gray = image.convert("L")
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(contrast)
    inverted = ImageOps.invert(gray)
    alpha = inverted
    rgba = image.convert("RGBA")
    rgba.putalpha(alpha)
    return rgba

def apply_color_overlay_with_alpha(image, color=(255, 0, 255), threshold=0):
    base = image.convert("RGBA")
    alpha = base.getchannel("A")
    gray = base.convert("L")
    inverted = ImageOps.invert(gray)
    inverted_array = np.array(inverted, dtype=np.uint8)

    if threshold > 0:
        inverted_array[inverted_array < threshold] = 0

    normalized = inverted_array / 255.0
    color_array = np.zeros((inverted_array.shape[0], inverted_array.shape[1], 4), dtype=np.uint8)
    for i in range(3):
        color_array[:, :, i] = (normalized * color[i]).astype(np.uint8)
    color_array[:, :, 3] = np.array(alpha)

    return Image.fromarray(color_array, mode="RGBA")

def process_images(folder_path, color, threshold, contrast, progress_callback, done_callback):
    output_folder = os.path.join(folder_path, "Processed")
    os.makedirs(output_folder, exist_ok=True)

    supported_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_exts)]
    total = len(image_files)

    for i, filename in enumerate(image_files):
        input_path = os.path.join(folder_path, filename)
        base_name, _ = os.path.splitext(filename)
        output_path = os.path.join(output_folder, base_name + ".png")
        try:
            image = Image.open(input_path)
            transparent_img = apply_transparency_from_luminance(image, contrast)
            result_img = apply_color_overlay_with_alpha(transparent_img, color, threshold)
            result_img.save(output_path, format="PNG")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
        progress_callback(i + 1, total)

    done_callback(total)

def start_processing():
    folder_path = folder_path_var.get()
    if not os.path.isdir(folder_path):
        status_label.config(text="Please select a valid folder.")
        return

    threshold = threshold_var.get()
    contrast = contrast_var.get() / 100.0
    color = selected_color.get()
    if not color:
        status_label.config(text="Please select a color.")
        return
    rgb = root.winfo_rgb(color)
    rgb = tuple(int(c / 256) for c in rgb)

    progress_bar["maximum"] = 100
    progress_bar["value"] = 0

    def update_progress(current, total):
        progress = int((current / total) * 100)
        progress_bar["value"] = progress
        root.update_idletasks()
        print(f"Progress: {current}/{total} ({progress}%)")

    def on_done(total_files):
        message = f"Processing complete! {total_files} files processed."
        status_label.config(text=message)
        print(message)
        close_button.config(state="normal")

    threading.Thread(target=process_images, args=(folder_path, rgb, threshold, contrast, update_progress, on_done)).start()
    status_label.config(text="Processing started...")

def choose_folder():
    path = filedialog.askdirectory()
    if path:
        folder_path_var.set(path)
        load_preview()

def choose_color():
    color_code = colorchooser.askcolor(title="Choose overlay color")
    if color_code:
        selected_color.set(color_code[1])
        load_preview()

def load_preview():
    folder_path = folder_path_var.get()
    if not os.path.isdir(folder_path):
        return

    supported_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_exts)]
    if not image_files:
        return

    first_image_path = os.path.join(folder_path, image_files[0])
    try:
        image = Image.open(first_image_path)
        threshold = threshold_var.get()
        contrast = contrast_var.get() / 100.0
        color = selected_color.get()
        if not color:
            return
        rgb = root.winfo_rgb(color)
        rgb = tuple(int(c / 256) for c in rgb)
        transparent_img = apply_transparency_from_luminance(image, contrast)
        result_img = apply_color_overlay_with_alpha(transparent_img, rgb, threshold)
        result_img.thumbnail((300, 300))
        preview_img = ImageTk.PhotoImage(result_img)
        preview_label.config(image=preview_img)
        preview_label.image = preview_img
    except Exception as e:
        print(f"Error loading preview: {e}")

def update_preview(val=None):
    load_preview()

# GUI setup
if __name__ == "__main__":
    root = Tk()
    root.title("Image Color Overlay Processor")

    folder_path_var = StringVar()
    selected_color = StringVar()
    threshold_var = IntVar(value=0)
    contrast_var = IntVar(value=100)

    Label(root, text="1. Select Folder:").pack()
    Button(root, text="Browse", command=choose_folder).pack()
    Label(root, textvariable=folder_path_var).pack()

    Label(root, text="2. Choose Overlay Color:").pack()
    Button(root, text="Pick Color", command=choose_color).pack()
    Label(root, textvariable=selected_color).pack()

    Label(root, text="3. Set Threshold:").pack()
    Scale(root, from_=0, to=255, orient=HORIZONTAL, variable=threshold_var, command=update_preview).pack()

    Label(root, text="4. Set Contrast (%):").pack()
    Scale(root, from_=50, to=300, orient=HORIZONTAL, variable=contrast_var, command=update_preview).pack()

    Button(root, text="Start Processing", command=start_processing).pack(pady=10)

    progress_bar = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
    progress_bar.pack(pady=5)

    status_label = Label(root, text="")
    status_label.pack()

    Label(root, text="Preview:").pack()
    preview_label = Label(root)
    preview_label.pack()

    close_button = Button(root, text="Close", command=root.destroy, state="disabled")
    close_button.pack(pady=10)

    root.mainloop()
