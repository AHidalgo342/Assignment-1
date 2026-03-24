from PIL import Image

image1 = Image.open('./images/I0.jpg')
image2 = Image.open('./images/I1.jpg')

image2 = image2.resize(image1.size)
image2 = image2.convert(image1.mode)

blended_images = []

for i in [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0]:
	blended_image = Image.blend(image1, image2, alpha=i)

	output = f"./output/blended_image_{i}.png"
	print(output)
	blended_images.append(output)
	blended_image.save(output)

frames = [Image.open(image) for image in blended_images]

frames[0].save(
	'./output/blended_output.gif',
	save_all=True,
	append_images=frames[1:],
	duration=300,
	loop=0
)
