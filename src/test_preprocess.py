from preprocess import load_signature_data, load_image_data

# Signature
sig_images, sig_labels = load_signature_data()
print("Signature:", sig_images.shape)

# Image
img_images, img_labels = load_image_data()
print("Image:", img_images.shape)