# Training a OpenCV Haar Cascade Classifier in CDSW

This is an example of how you can train a OpenCV Haar Cascade Classifier (model) using the Cloudera Data Science Workbench. The trained model can then be used to detect images.

1) Start a new session and open up a Termial (>_Terminal access)

2) Clone this repository

        git clone https://github.com/mrnugget/opencv-haar-classifier-training
        cd opencv-haar-classifier-training

3) Put your positive images in the `./positive_images` folder and create a list
of them:

Positive image contain the object.  
You need to crop them so that only our desired object is visible.  
The ratios (w x h) need to be the same for each.
I used 40 positive images. Each image was exactly 59w by 33h.  

        find ./positive_images -iname "*.jpg" > positives.txt

4) Put the negative images in the `./negative_images` folder and create a list of them:

Negative images are ones that do not contain the object.  
I used 800 negative images

        find ./negative_images -iname "*.jpg" > negatives.txt 
        
        
5) Convert the `bin/createsamples.pl` script from dos to unix

        perl -pe 's/\r\n|\n|\r/\n/g' bin/createsamples.pl > bin/createsamples_unix.pl
        

6) Create positive samples with the `bin/createsamples_unix.pl` script and save them
to the `./samples` folder:

        perl bin/createsamples_unix.pl positives.txt negatives.txt samples 1500\
          "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
          -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 59 -h 33"
          
7) Use `tools/mergevec.py` to merge the samples in `./samples` into one file:

        python ./tools/mergevec.py -v samples/ -o samples.vec
        
8) Start training the classifier with opencv_traincascade, which comes with OpenCV, and save the results to ./classifier

        opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
          -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
          -numNeg 800 -w 59 -h 33 -mode ALL -precalcValBufSize 1024\
          -precalcIdxBufSize 1024

    After starting the training program it will print back its parameters and then start training. Each stage will print out some analysis as it is trained:

      ```
      ===== TRAINING 0-stage =====
      <BEGIN
      POS count : consumed   1000 : 1000
      NEG count : acceptanceRatio    600 : 1
      Precalculation time: 11
      +----+---------+---------+
      |  N |    HR   |    FA   |
      +----+---------+---------+
      |   1|        1|        1|
      +----+---------+---------+
      |   2|        1|        1|
      +----+---------+---------+
      |   3|        1|        1|
      +----+---------+---------+
      |   4|        1|        1|
      +----+---------+---------+
      |   5|        1|        1|
      +----+---------+---------+
      |   6|        1|        1|
      +----+---------+---------+
      |   7|        1| 0.711667|
      +----+---------+---------+
      |   8|        1|     0.54|
      +----+---------+---------+
      |   9|        1|    0.305|
      +----+---------+---------+
      END>
      Training until now has taken 0 days 3 hours 19 minutes 16 seconds.
      ```

    Each row represents a feature that is being trained and contains some output about its HitRatio and FalseAlarm ratio. If a training stage only selects a few features (e.g. N = 2) then its possible something is wrong with your training data.

    At the end of each stage the classifier is saved to a file and the process can be stopped and restarted. This is useful if you are tweaking a machine/settings to optimize training speed.

9) Wait until the process is finished (which takes a long time — a couple of days probably, depending on the computer you have and how big your images are).

10) Use your finished classifier (model) in CDSW!

Run `detect_image.py`

## Acknowledgements

Modified the instructions found here (https://github.com/mrnugget/opencv-haar-classifier-training) to run on CDSW

## References & Links:

http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html  
https://github.com/mrnugget/opencv-haar-classifier-training  
