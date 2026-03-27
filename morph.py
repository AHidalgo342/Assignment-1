from PIL import Image



blended_images = []

for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    image1 = Image.open(f"./images/W0.t{i}.jpg")
    image2 = Image.open(f"./images/W1.t{i}.jpg")

    image2 = image2.resize(image1.size)
    image2 = image2.convert(image1.mode)

    blended_image = Image.blend(image1, image2, alpha=(i * 0.1))

    output = f"./output/blended_image_{i}.png"
    print(output)

    blended_images.append(output)
    blended_image.save(output)

blended_images.insert(0, "./images/I0.jpg")
blended_images.append("./images/I1.jpg")

frames = [Image.open(image) for image in blended_images]

frames[0].save(
	'./output/blended_output.gif',
	save_all=True,
	append_images=frames[1:],
	duration=300,
	loop=0
)
