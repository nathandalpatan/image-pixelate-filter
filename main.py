from PIL import Image

#3x3 matrix of the surrounding pixels
#find the average colour of the surrounding pixels
#change every pixel in 3x3 matrix to the average colour


def main():
    image_path = "dog-guitar.jpg"
    width, height = Image.open(image_path).size
    k = 21
    if k > width // 9 or k > height // 9 or k % 2 == 0:
        print("Error: k is too large for the image dimensions OR k is not odd.")
        return

    pixel_matrix = get_2d_array(image_path)
    loop_through_pixels(pixel_matrix, width, height, k)
    pixel_array = [pixel for row in pixel_matrix for pixel in row]
    new_img = Image.new("RGB", (width, height))
    new_img.putdata(pixel_array)
    new_img.save("output_image.jpg")


def loop_through_pixels(pixel_matrix, width, height, k):
    neighbors = []
    half = k // 2

    for m in range(0 - half , half + 1):
        for n in range(0 - half , half + 1):
            neighbors.append((m, n))

    for i in range(1, height - 3, k):
        for j in range(1, width - 3, k):
            r_total, g_total, b_total = 0, 0, 0
            count = 0
            for dx, dy in neighbors:
                x, y = i + dx, j + dy

                r, g, b = pixel_matrix[x][y]
                r_total += r
                g_total += g
                b_total += b
                count += 1

            if count > 0:
                r_avg = r_total // count
                g_avg = g_total // count
                b_avg = b_total // count
                for dx, dy in neighbors:
                    x, y = i + dx, j + dy
                    pixel_matrix[x][y] = (r_avg, g_avg, b_avg)


def get_2d_array(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

    width, height = img.size
    pixel_data = list(img.getdata()) # Get a flat sequence of pixel values

    # Reshape the 1D sequence into a 2D list
    two_d_array = []
    for i in range(height):
        row = pixel_data[i * width : (i + 1) * width]
        two_d_array.append(row)

    return two_d_array


if __name__ == "__main__":
    main()