# Image_SR_and_Deblurring
Generation of De-blurred, Super resolved images in Sports and surveillance footage from blurry low quality resolution images using GANs


Project Abstract:

	The goal of the Project we have worked on is to create and develop a machine learning pipeline which is comprised of two components firstly a Deblur Generative Adversarial Networks (GAN) and secondly a SuperResolution Generative Adversarial Networks (GAN) which work in unison in order to convert and transform Low Quality Blurred images into a higher quality Super resolved unblurred image. In our solution we are aiming to tackle various types of blurs such as linear blurring, Gaussian Blurring and,Media Blurring. The main Machine Learning Concept we are using in both components of our pipeline is GAN or Generative Adversarial Networks. GAN’s are unsupervised learning algorithms and generate data similar to the real data, using this principle we are generating Unblurred and super-resolved images. The Trained Discriminator acts as an Accurate classifier and has the main functionality of distinguishing and differentiating between the real images and the multiple generated images, At the point in time when the discriminator is unable to differentiate between the real images and the generated Unblurred images, it is safe to say that we have generated the most unblurred and Super resolved image as possible.


Create the following folders in deblur-gan/ folder :

	input_images

	original

	output_all

	output_deblur

	results

	GOPRO_Large

	Download Deblur Gan’s Dataset at https://drive.google.com/file/d/1H0PIXvJH4c40pk7ou6nAwoxuR4Qh_Sa2/view?usp=sharing and extract the zip file into the deblur-gan/GOPRO_Large folder





Code Execution: 

	To run the SR-GAN code , just run the cells of the SRGAN.ipynb file 


	Execute the following commands in the order as follows:

		pip install -r requirements/requirements.txt
		pip install -e .
		cd into deblur-gan directory

	To create the training and testing set do the following:

		python scripts/organize_gopro_dataset.py --dir_in=GOPRO_Large --dir_out=images
	
	Training:
	
		python scripts/train.py --n_images=512 --batch_size=16 --log_dir /path/to/log/dir


	Testing from Test dataset:
	
		python scripts/test.py
	
	
	The outputs of the above will be the blurry image, the original image and the deburred image.
	
	
How to use the UI

	Open 2 Anaconda command prompts from deblur-gan directory:
		Run: python scripts/app.py 
		Run: python api.py

	Type localhost:3000 in your browser url
	Click on the upload button in the top right of the screen



Types of Input Scenarios: 

	Take your own image from webcam and apply blur

		Click on take a snap. 
		Save the image as original.png under the folder deblur-gan/original
		Click on any one of the buttons which apply a filter:
		Wait for response code 200 on the terminal which is running app.py.
		Click on “view imgs side by side” 
		Open the folder output_all and view output.png, 
		it will contain the 4 Images will be in the order:
		original image, blurry image, deblurred image, deblurred+super-resolved image. 
		Click on view deblurred image, view super-resolved image to see the psnr values (Viewing the images on each of the button presses only works on Internet explorer as the other browsers have some privacy issues).




	Upload an original image and pre-blurred image 

		Save the blurred image as input.png under deblur-gan/input_images. 
		Save the original image as original.png under deblur-gan/original.
		Click on process image.
		Wait for response code 200 on the terminal which is running app.py.
		Click on “view imgs side by side” 
		Open the folder output_all and view output.png,
		it will contain the 4 Images will be in the order:
		original image, blurry image, deblurred image, deblurred+super-resolved image. 
		Click on view deblurred image, view super-resolved image to see the psnr values (Viewing the images on each of the button presses only work on Internet explorer as the other browsers have some privacy issue).


